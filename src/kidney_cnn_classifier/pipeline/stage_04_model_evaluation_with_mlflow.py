from kidney_cnn_classifier.config.configuration import ConfigurationManager
from kidney_cnn_classifier.compnents.model_evaluation_mlflow import Evaluation
from kidney_cnn_classifier import logger



STAGE_NAME = 'Evaluation stage'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            # evaluation.log_into_mlflow()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f"*************************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e