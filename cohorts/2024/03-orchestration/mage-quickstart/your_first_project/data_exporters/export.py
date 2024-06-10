import mlflow
import mlflow.sklearn
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(training_artifacts, *args, **kwargs):
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("test_experiment_now")

    model, vectorizer = training_artifacts

    with open('/tmp/vectorizer.bin', 'wb') as f_out:
        pickle.dump(vectorizer, f_out)

    with mlflow.start_run():
        mlflow.sklearn.log_model(model, artifact_path="models")
        mlflow.log_artifact(local_path='/tmp/vectorizer.bin', artifact_path="models_pickle")


