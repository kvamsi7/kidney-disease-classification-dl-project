from src.kidney_cnn_classifier import logger

from src.kidney_cnn_classifier.pipeline.stage_01_data_ingestion import Data_ingestion_training_pipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = Data_ingestion_training_pipeline()
    data_ingestion.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<< \n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e