import json
import logging
import random
import numpy as np
from typing import Any, Dict, List, Union

def load_json(file_path: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Load and parse a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        Union[Dict[str, Any], List[Dict[str, Any]]]: Parsed JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        logging.info(f"Successfully loaded JSON data from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in file {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error loading JSON from {file_path}: {e}")
        raise

def save_file(file_path: str, content: str) -> None:
    """
    Save content to a file.

    Args:
        file_path (str): Path to the file where content will be saved.
        content (str): Content to be written to the file.

    Raises:
        IOError: If there's an error writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        logging.info(f"Successfully saved content to {file_path}")
    except IOError as e:
        logging.error(f"Error writing to file {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error saving file {file_path}: {e}")
        raise
def set_seed(seed_value=42):
    random.seed(seed_value)
    np.random.seed(seed_value)