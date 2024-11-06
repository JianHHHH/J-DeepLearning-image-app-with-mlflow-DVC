# now load the constant to the experimental file
from ImageClassifier.constants import *
# we also need to import the two function in utils folder to help us read yaml file
from ImageClassifier.utils.common import read_yaml, create_directories
# add the missing class
from ImageClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    # this init function is used to created the root directory artifacts for the entire project
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    # this function is used to created the artifacts directories of data_ingestion component within the 
    # root directory of artifacts
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        # here config being assinged as the value of the key of data_ingestion in config.yaml file
        # it has four sub key: 
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config