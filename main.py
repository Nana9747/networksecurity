from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.Exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.Entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,ModelTrainerConfig
from networksecurity.Entity.config_entity import DataTransformationConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_tranformation import DataTransFormation
from networksecurity.components.modal_trainer import ModelTrainer
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact =dataingestion.initiate_data_ingestion()
        logging.info("Data initiation Completed")
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation =DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransFormation(data_validation_artifact,data_transformation_config)
        logging.info("Initiate the Data tranformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
        

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    