import os
import mlflow


def promote_model():
    """Promoting model to production stage"""
    dagshub_token = os.getenv("CAPSTONE_PROJ")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_PROJ environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "brij26"
    repo_name = "MLOPS-Capstone-Proj"

    # Set up mlflow tracking uri
    mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

    client = mlflow.MlflowClient()

    model_name = "MyModel"
    # get the latest version in staging
    latest_version_staging = client.get_latest_versions(
        model_name, stages=["Staging"])[0].version

    # Archive the current production model
    prod_versions = client.get_latest_versions(
        model_name, stages=["Production"])
    for version in prod_versions:
        client.transition_model_version_stage(
            name=model_name,
            version=version.version,
            stage="Archived"
        )

    # Promote the new model to production
    client.transition_model_version_stage(
        name=model_name,
        version=latest_version_staging,
        stage="Production"
    )
    print(f"Model version {latest_version_staging} promoted to production")


if __name__ == "__main__":
    promote_model()
