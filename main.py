from src.kidney_cnn_classifier import logger
from src.kidney_cnn_classifier.pipeline.stage_01_data_ingestion import Data_ingestion_training_pipeline
from src.kidney_cnn_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.kidney_cnn_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.kidney_cnn_classifier.pipeline.stage_04_model_evaluation_with_mlflow import EvaluationPipeline
import os

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = Data_ingestion_training_pipeline()
    data_ingestion.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<< \n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"*****************")
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Training'
try:
    logger.info(f"*****************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Evaluation with MLflow stage'

os.environ['MLFLOW_TRACKING_USERNAME'] = "kvamsi7"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "d6b1c8cf96f5b7cc6f735f6e0c8d127e5ad9c82d"

try:
    logger.info(f'****************')
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e

