import re
import os
import string
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import dagshub
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import warnings
warnings.simplefilter('ignore', UserWarning)
warnings.filterwarnings("ignore")

# Set mlflow tracking uri and dagshub integration
MLFLOW_TRACKING_URI = ""
dagshub.init(repo_name="MLOPS-Capstone-proj", repo_owner="brij", mlflow=True)
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("Logistic Regression Hyperparameter Tuning")

# ================ Text PreProcessing Functions =======================


def preprocess_text(text):
    """ Applies multiple text preprocessing steps. """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    text = text.lower()  # Convert to lowercase
    text = re.sub("r\d+", '', text)  # Remove Numbers
    text = re.sub(f"{re.escape(string.punctuation)}",
                  " ", text)  # Remove punctuations
    text = re.sub(r'http?://\S+|www\.\S+', '', text)  # Remove URLs
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split(
    ) if word not in stop_words])  # Lemmatizer and stop word removal

    return text.strip()


# ======================== Load And Prepare Data ======================
def load_and_prepare_data(file_path):
    """Load , preprocess and vectorize the dataset."""

    df = pd.read_csv(file_path)

    # Apply text preprocessing
    df['review'] = df["review"].astype(str).apply(preprocess_text)

    # Filter binary classification
    df = df[df["sentiment"].isin(['positive', 'negative'])]
    df["sentiment"] = df["sentiment"].map({"negative": 0, "positive": 1})

    # Convert text data to tfidf vector
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["review"])
    y = df["sentiment"]

    return train_test_split(X, y, test_size=0.2, random_state=42), vectorizer


# ================== Train and Log Model ===========================
def train_and_log_model(X_train, X_test, y_train, y_test, vectorizer):
    """Train a Logistic Regression Model with GridSearch and logs results to mlflow."""

    param_grid = {
        "C": [0.1, 1, 10],
        "penalty": ["l1", "l2"],
        "solver": ["liblinear"]
    }

    with mlflow.start_run() as parent_run:
        grid_search = GridSearchCV(
            LogisticRegression(), param_grid, cv=5, scoring="f1", n_jobs=-1)
        grid_search.fit(X_train, y_train)

        # Log all Hyperparameter tuning runs
        for params, mean_score, std_score in zip(grid_search.cv_results_["params"],
                                                 grid_search.cv_results_[
                                                     "mean_test_score"],
                                                 grid_search.cv_results_["std_test_score"]):
            with mlflow.start_run(run_name=f"LR with params: {params}", nested=True) as child_run:
                model = LogisticRegression(**params)
                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                metrics = {
                    "accuracy": accuracy_score(y_test, y_pred),
                    "precision": precision_score(y_test, y_pred),
                    "recall": recall_score(y_test, y_pred),
                    "f1_socre": f1_score(y_test, y_pred),
                    "mean_cv_score": mean_score,
                    "std_cv_score": std_score
                }

                # Log parameters and Metrics
                mlflow.log_params(params)
                mlflow.log_metrics(metrics)

                print(
                    f"Params : {params} | Accuracy : {metrics['accuracy']:.4f} | F1 : {metrics['f1_socre']:.4f}")

        # Log the best Model
        best_params = grid_search.best_params_
        best_model = grid_search.best_estimator_
        best_f1 = grid_search.best_score_

        mlflow.log_params(best_params)
        mlflow.log_metric("best_f1_score", best_f1)
        mlflow.sklearn.log_model(best_model, "model")

        print(
            f"\nBest Params : {best_params} | Best F1 Score : {best_f1:.4f}")


# ================= Main Execution ==================
if __name__ == "__main__":
    (X_train, X_test, y_train, y_test), vectorizer = load_and_prepare_data(
        "notebooks/data.csv")
    train_and_log_model(X_train, X_test, y_train, y_test, vectorizer)
