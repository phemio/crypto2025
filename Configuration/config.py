import json
import os
from datetime import datetime
import yaml
import platform
import re


class Config:
    os_flag = platform.system()  # "Windows" or "Mac"
    window_folder_dir = os.getcwd().replace("\\", "\\\\")
    mac_folder_dir = os.getcwd()
    config_yml_path = os.getcwd() + "\\Configuration\\os_path_config.yaml" \
        if os_flag == "Windows" else os.getcwd() + "/Configuration/os_path_config.yaml"
    config_config_path = os.getcwd() + "\\base\\config.yaml" \
        if os_flag == "Windows" else os.getcwd() + "/base/config.yaml"
    config_driver_path = os.getcwd() + "\\base\\driverConfig.yaml" \
        if os_flag == "Windows" else os.getcwd() + "/base/driverConfig.yaml"
    execution_script_path = window_folder_dir + "\\\\execution_script.bat" \
        if os_flag == "Windows" else mac_folder_dir + "/execution_script.sh"
    report_path = window_folder_dir + "\\\\Reports\\\\allurereports\\\\" \
        if os_flag == "Windows" else mac_folder_dir + "/Reports/allurereports/"
    generate_allure_report_path = window_folder_dir + "\\\\generate_allure.bat" \
        if os_flag == "Windows" else mac_folder_dir + "/generate_allure.sh"

    @staticmethod
    def read_yml_file(filename, key):
        try:
            with open(filename, "r") as file:
                yaml_map = yaml.safe_load(file)
            yml_nodes = key.split('.')
            for i in range(len(yml_nodes) - 1):
                yaml_map = yaml_map[yml_nodes[i]]
            return yaml_map[yml_nodes[-1]]
        except Exception as e:
            raise e

    @staticmethod
    def get_test_data(test_data):
        if test_data.startsWith("$"):
            test_data = test_data[1:]
            return Config.read_yml_file("", test_data)
        return test_data

    @staticmethod
    def get_device_info():
        return Config.read_yml_file(Config.config_config_path, "executionConfig.device")

    @staticmethod
    def get_platform_info():
        return Config.read_yml_file(Config.config_config_path, "executionConfig.platform")

    @staticmethod
    def get_env_info():
        env = Config.read_yml_file(Config.config_config_path, "executionConfig.environment")
        if env == "UAT":
            return Config.read_yml_file(Config.config_config_path, "environmentConfig.UAT")

    @staticmethod
    def get_device_caps(device):
        caps = {
            "platformName": device + ".DesiredCapabilities.platformName",
            "deviceName": device + ".DesiredCapabilities.deviceName",
            "browserName": device + ".DesiredCapabilities.browserName"
        }
        return caps

    @staticmethod
    def get_execute_tags():
        return Config.read_yml_file(Config.config_config_path, "executionConfig.tags")

    @staticmethod
    def get_parallel_number():
        return Config.read_yml_file(Config.config_config_path, "executionConfig.parallelNumber")

    @staticmethod
    def get_reset_flag():
        return Config.read_yml_file(Config.config_config_path, "executionConfig.resetFlag")

    def get_dir_path(self):
        if self.os_flag == "Windows":
            return Config.window_folder_dir
        else:
            return Config.mac_folder_dir

    def get_screenshot_folder_path(self):
        path = self.get_dir_path()
        with open(path) as config_file:
            config = json.load(config_file)
        if "screen_path" not in config:
            raise Exception('The config file does not contain "screen_path"')
        screenshot_path = config["screen_path"]
        return screenshot_path

    @staticmethod
    def get_log_folder_path(_os):
        if _os == "Windows":
            return Config.window_folder_dir + Config.read_yml_file(Config.config_yml_path, "Windows.log_path")
        else:
            return Config.mac_folder_dir + Config.read_yml_file(Config.config_yml_path, "Mac.log_path")

    @staticmethod
    def create_new_report_folder(parent_dir, new_report_dir):
        path = os.path.join(parent_dir, new_report_dir)
        try:
            os.mkdir(path)
            return path
        except OSError as e:
            error_msg = "failed to create directory"
            print(error_msg)
            raise Exception(error_msg) from e

    @staticmethod
    def get_current_time():
        now = datetime.now()
        date_time_value = now.strftime("%d%m%Y_%H%M%S")
        return date_time_value

