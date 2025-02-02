from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.Exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.Entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
from networksecurity.components.data_validation import DataValidation
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
        

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    