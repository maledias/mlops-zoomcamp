import mlflow
import mlflow.sklearn
import os 
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(model_artifacts, *args, **kwargs):
    mlflow.set_tracking_uri("dsalkjfsa")
    
    print(mlflow)
    print(vars(mlflow))
    raise Exception("Parar")

    model, vectorizer = model_artifacts

    with mlflow.start_run():

        with open('/tmp/vectorizer.bin', 'wb') as f_out:
            pickle.dump(vectorizer, f_out)

        mlflow.sklearn.log_model(model, artifact_path="models")

        mlflow.log_artifact(local_path='/tmp/vectorizer.bin', artifact_path="vectorizer_pickle")
    
    # Specify your data exporting logic here


