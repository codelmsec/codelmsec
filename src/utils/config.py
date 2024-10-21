import os
import yaml
import logging
from typing import Any, Dict

class ConfigError(Exception):
    """Custom exception for configuration-related errors."""
    pass

class Config:
    """
    Configuration manager that loads settings from a YAML file and provides
    access to configuration parameters throughout the project.
    """

    def __init__(self, config_file: str = "config/config.yaml"):
        """
        Initialize the Config object by loading the configuration file.

        Args:
            config_file (str): Path to the YAML configuration file.
                               Defaults to 'config/config.yaml'.
        """
        self.config_file = config_file
        self.config_data = self.load_config()
        logging.info(f"Configuration loaded from {self.config_file}")

    def load_config(self) -> Dict[str, Any]:
        """
        Load the YAML configuration file.

        Returns:
            Dict[str, Any]: Parsed configuration data.

        Raises:
            ConfigError: If the configuration file is not found or invalid.
        """
        if not os.path.exists(self.config_file):
            logging.error(f"Configuration file {self.config_file} does not exist.")
            raise ConfigError(f"Configuration file {self.config_file} does not exist.")

        try:
            with open(self.config_file, 'r') as file:
                config = yaml.safe_load(file)
                logging.debug(f"Configuration data: {config}")
                return config
        except yaml.YAMLError as e:
            logging.error(f"Error parsing the configuration file: {e}")
            raise ConfigError(f"Error parsing the configuration file: {e}")
        except Exception as e:
            logging.error(f"Unexpected error loading configuration: {e}")
            raise ConfigError(f"Unexpected error loading configuration: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a configuration value using a dot-separated key.

        Args:
            key (str): Dot-separated key string (e.g., 'paths.outputs').
            default (Any): Default value to return if the key is not found.

        Returns:
            Any: The value associated with the key, or the default value.
        """
        keys = key.split('.')
        value = self.config_data
        try:
            for k in keys:
                value = value[k]
            logging.debug(f"Retrieved config value for '{key}': {value}")
            return value
        except KeyError:
            logging.warning(f"Configuration key '{key}' not found. Using default: {default}")
            return default

    @property
    def data_path(self) -> str:
        """Path to the data directory."""
        return self.get('data.prompt_code_pairs', 'data/prompt_code_pairs.json')

    @property
    def list_of_cwes_path(self) -> str:
        """Path to the list of CWEs."""
        return self.get('data.list_of_cwes', 'data/list_of_cwes.json')

    @property
    def codeql_mapping_path(self) -> str:
        """Path to the CodeQL message to CWE mapping file."""
        return self.get('data.codeqlmsg_to_cwe', 'data/codeqlmsg_to_cwe.json')

    @property
    def outputs_path(self) -> str:
        """Base path for output directories."""
        return self.get('paths.outputs', 'outputs')

    @property
    def few_shot_prompts_path(self) -> str:
        """Path for storing few-shot prompt files."""
        return os.path.join(self.outputs_path, self.get('paths.few_shot_prompts', 'few_shot_prompts'))

    @property
    def non_secure_prompts_path(self) -> str:
        """Path for storing non-secure prompt files."""
        return os.path.join(self.outputs_path, self.get('paths.non_secure_prompts', 'non_secure_prompts'))

    @property
    def generated_code_path(self) -> str:
        """Path for storing generated code files."""
        return os.path.join(self.outputs_path, self.get('paths.generated_code', 'generated_code'))

    @property
    def vulnerability_reports_path(self) -> str:
        """Path for storing vulnerability reports."""
        return os.path.join(self.outputs_path, self.get('paths.vulnerability_reports', 'vulnerability_reports'))

    @property
    def final_reports_path(self) -> str:
        """Path for storing final summary reports."""
        return os.path.join(self.outputs_path, self.get('paths.final_reports', 'final_reports'))
    @property
    def number_of_fs_prompts(self) -> int:
        """Number of few-shot prompts to generate."""
        return self.get('prompt_generation.number_of_fs_prompts', 'number_of_fs_prompts')

    @property
    def number_of_examples_per_cwe(self) -> int:
        """Number of examples per CWE."""
        return self.get('prompt_generation.number_of_examples_per_cwe', 'number_of_examples_per_cwe')


def load_config(config_file: str = "config/config.yaml") -> Config:
    """
    Convenience function to create and return a Config instance.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        Config: An instance of the Config class.
    """
    return Config(config_file)
