import os
from src.kidney_cnn_classifier.config.configuration import ConfigurationManager
from src.kidney_cnn_classifier.compnents.data_ingestion import DataIngestion
from src.kidney_cnn_classifier import logger

STAGE_NAME = 'Data Ingestion Stage'

class Data_ingestion_training_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        print(data_ingestion_config)
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME}' started <<<<<<<<")
        
        obj = Data_ingestion_training_pipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<.")
    except Exception as e:
        logger.exception(e)