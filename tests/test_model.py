import unittest
import mlflow
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle


class TestModelLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up dagshub credentials for mlflow tracking
        dagshub_token = os.getenv("CAPSTONE_PROJ")
        if not dagshub_token:
            raise EnvironmentError(
                "CAPSTONE_PROJ environment variable is not set")

        os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
        os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

        dagshub_url = "https://dagshub.com"
        repo_owner = "brij26"
        repo_name = "MLOPS-Capstone_Proj"

        # Setup mlflow tracking uri
        mlflow.set_tracking_uri(
            f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

        # load new model from mlflow model registery
        cls.new_model_name = "MyModel"
        cls.new_model_version = cls.get_latest_model_versions(
            cls.new_model_name)
        cls.new_model_uri = f'models:/{cls.new_model_name}/{cls.new_model_version}'
        cls.new_model = mlflow.pyfunc.load_model(cls.new_model_uri)

        # Load the vectorizer
        cls.vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

        # Load holdout test data
        cls.holdout_data = pd.read_csv("data/processed/test_bow.csv")

    @staticmethod
    def get_latest_model_versions(model_name, stage="Staging"):
        client = mlflow.MlflowClient()
        latest_version = client.get_latest_versions(model_name, stages=[stage])
        return latest_version[0].version if latest_version else None

    def test_model_loaded_properly(self):
        self.assertIsNotNone(self.new_model)

    def test_model_signature(self):
        # Create a dummy inpur for the model based on expected input shape
        input_text = "hi how are you"
        input_data = self.vectorizer.transform([input_text])
        input_df = pd.DataFrame(input_data.toarray(), columns=[
                                str(i) for i in range(input_data.shape[1])])

        # Predict using the new model to verify the input and output shapes
        predictions = self.new_model.predict(input_df)

        # Verify the input shape
        self.assertEqual(input_df.shape[1], len(
            self.vectorizer.get_feature_names_out()))

        # Verify the output shape (assuming binary classification with binary output)
        self.assertEqual(len(predictions), input_df.shape[0])
        # assuming a single output column for binary classification
        self.assertEqual(len(predictions.shape), 1)

    def test_model_preformance(self):
        # Extract features and labels from holdout test data
        X_holdout = self.holdout_data[:, :-1]
        y_holdout = self.holdout_data[:, -1]

        # Predict using the new model
        y_pred_new = self.new_model.predict(X_holdout)

        # Calculate preformance metrics for the new model
        accuracy_new = accuracy_score(y_holdout, y_pred_new)
        precision_new = precision_score(y_holdout, y_pred_new)
        recall_new = recall_score(y_holdout, y_pred_new)
        f1_new = f1_score(y_holdout, y_pred_new)

        # Define expected thresholds for the performance metrics
        expected_accuracy = 0.4
        expected_recall = 0.4
        expected_precision = 0.4
        expected_f1 = 0.4

        # Assure that the new model meets the performance thresholds
        self.assertGreaterEqual(accuracy_new, expected_accuracy,
                                f"Accuracy should be atleast {expected_accuracy}")
        self.assertGreaterEqual(precision_new, expected_precision,
                                f"Accuracy should be atleast {expected_precision}")
        self.assertGreaterEqual(
            recall_new, expected_recall, f"Accuracy should be atleast {expected_recall}")
        self.assertGreaterEqual(f1_new, expected_f1,
                                f"Accuracy should be atleast {expected_f1}")


if __name__ == '__main__':
    unittest.main()
