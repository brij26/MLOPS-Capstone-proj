import json
import mlflow
import logging
from src.logger import logging
import os
import dagshub

import warnings
warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings('ignore')

# Below code block is for production use
# -----------------------------------------------------------------------------------------------------
# set up dagshub credentials for mlflow tracking

dagshub_token = os.getenv("CAPSTONE_PROJ")
if not dagshub_token:
    raise EnvironmentError("CAPSTONE_PROJ environment variable is not set")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

dagshub_url = "https://dagshub.com"
repo_owner = "brij26"
repo_name = "MLOPS-Capstone-Proj"

# Setup mlflow tracking uri
mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')
# -----------------------------------------------------------------------------------------------------


# Below code block is for local use
# -----------------------------------------------------------------------------------------------------
# mlflow.set_tracking_uri(
#     "https://dagshub.com/brij26/MLOPS-Capstone-proj.mlflow")
# dagshub.init(repo_name="MLOPS-Capstone-proj", repo_owner="brij26", mlflow=True)
# -----------------------------------------------------------------------------------------------------


def load_model_info(file_path: str) -> dict:
    """Load the model from the json file"""
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logging.debug("Model info loaded from %s", file_path)
        return model_info
    except FileNotFoundError:
        logging.error("File not found: %s", e)
        raise
    except Exception as e:
        logging.error(
            "Unexpected error occurred while loading the model info: %s", e)
        raise


def register_model(model_name: str, model_info: dict) -> None:
    """
    Register the model to mlflow model registery
    """
    try:
        model_uri = f"runs:/{model_info['run_id']}/{model_info['model_path']}"

        # Register the model
        model_version = mlflow.register_model(model_uri, model_name)

        # Transition the model to "Staging" stage
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            name=model_name,
            version=model_version.version,
            stage="Staging"
        )

        logging.debug(
            f'Model {model_name} version {model_version} registered and transitioned to Staging')
    except Exception as e:
        logging.error("error during model registration: %s", e)
        raise


def main():
    try:
        model_info_path = 'reports/experiment_info.json'
        model_info = load_model_info(model_info_path)

        model_name = "MyModel"
        register_model(model_name, model_info)

    except Exception as e:
        logging.error("Failed to complete model registration process : %s", e)
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
