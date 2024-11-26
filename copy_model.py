import os
import shutil
from src.kidney_cnn_classifier import logging


source_file = 'artifacts/training/model.h5'
destination_file = 'model/model.h5'

def copy_model_file():
    """
    Copies the trained model file from the training stage to the model directory.
    """
    if os.path.exists(source_file):
        print('Model file found.')

        os.makedirs('model', exist_ok=True)
        logging.info(f"Creating directory: {destination_file} for the file: {source_file}")
        shutil.copy(source_file, destination_file)
        logging.info(f"Model file copied to: {destination_file}")
    else:
        logging.error(f"Model file not found at: {source_file}")

    return destination_file


if __name__ == "__main__":
    try:
        print(os.getcwd())
        copy_model_file()
    except Exception as e:
        logging.exception(e)
        raise e