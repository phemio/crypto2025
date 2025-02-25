import logging
from datetime import datetime
import os
from Configuration.config import Config
import allure
import platform

cf = Config()
_os = platform.system()


class CustomLogger:
    @staticmethod
    def loggen():
        now = datetime.now()
        date = now.strftime("%d%m%Y")
        time = now.strftime("%H%M%S")
        today_folder_name = date
        path = os.path.join(cf.get_log_folder_path(_os),
                            today_folder_name)
        if not os.path.isdir(path):
            os.mkdir(path)

        logging.basicConfig(filename=f'Logs\\{today_folder_name}\\mobile_log_{time}.log' if _os == "Windows" else f'Logs/{today_folder_name}/mobile_log_{time}.log', level=logging.INFO,
                            force=True,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def allure_logs(text):
        with allure.step(text):
            pass
