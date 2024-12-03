from pathlib import Path
import mlflow
import mlflow.keras
import tensorflow as tf
from urllib.parse import urlparse
from src.kidney_cnn_classifier.entity.config_entity import EvaluationConfig
from src.kidney_cnn_classifier.utils.common import read_yaml,create_directories,save_json

class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config = config
    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy":self.score[1]}
        save_json(path = Path("scores.json"), data = scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_experiment("kidney_disease_classification_tracking")
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run(run_name='Run2'):
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            # Model registry does not work file store
            if tracking_url_type_store != "file":
                # Register the model
                try:
                    mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
                except Exception as log_exception:
                    logger.info(f"Failed to register model: {log_exception}")
            else:
                mlflow.keras.log_model(self.model,"model")