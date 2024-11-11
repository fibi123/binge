import json
import os
import logging
from models.env_data import EnvData  # Replace with your actual model imports
from models.user_data import UserData
from models.data_table_data import DataTableData
from models.file_data import FileData
from utils.json_settings_file import JsonSettingsFile  # Assuming this is similar to ISettingsFile in Python

# Define constants for paths
RESOURCES_PATH = "src/test/resources/"
TEST_DATA_PATH = os.path.join(RESOURCES_PATH, "testdata/")
ENVIRONMENT_PATH = os.path.join(RESOURCES_PATH, "environment/")
USER_FILE_PATH = os.path.join(TEST_DATA_PATH, "userData.json")
DATA_TABLE_FILE_PATH = os.path.join(TEST_DATA_PATH, "dataTableData.json")
FILE_DATA_PATH = os.path.join(TEST_DATA_PATH, "fileData.json")

# Logger configuration
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Load environment configuration
ENVIRONMENT_CONFIG = JsonSettingsFile("env.json")


def get_env_data():
    env_config_path = os.path.join(ENVIRONMENT_PATH, f"{get_current_environment()}.json")
    return deserialize_json(env_config_path, EnvData)


def get_user_data():
    return deserialize_json(USER_FILE_PATH, UserData)


def get_data_table_data():
    return deserialize_json(DATA_TABLE_FILE_PATH, DataTableData)


def get_file_data():
    return deserialize_json(FILE_DATA_PATH, FileData)


def get_current_environment():
    return ENVIRONMENT_CONFIG.get_value("/env")


def deserialize_json(file_path, cls):
    """
    Deserialize JSON data from a file into an instance of the specified class.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return cls(**data)  # Assuming your classes accept **kwargs for deserialization
    except FileNotFoundError as e:
        logger.error(f"Settings file {file_path} not found or incorrect. Error msg: {str(e)}")
        raise RuntimeError(f"Could not load file: {file_path}") from e
