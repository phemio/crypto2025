from functools import partial
import pytest
from pytest_bdd import given, when, then, parsers
from base.DriverClass import Driver
from Utilities.customlogger import CustomLogger as Cl
import time
from tests.Pages.LandingPage import LandingPage
from Configuration.config import Config

log = Cl.loggen()
EXTRA_TYPES = {
    'String': str,
}

parse_str = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


device_os = ""
browser_os = ""
web_flag = False
app_flag = False

#Get OS
if Config.get_platform_info() == "app":
    device_os = Config.read_yml_file(Config.config_driver_path,
                                     Config.get_device_caps
                                     (Config.get_device_info())["platformName"])
    web_flag = False
    app_flag = True
elif Config.get_platform_info() == "web":
    browser_os = Config.read_yml_file(Config.config_driver_path,
                                      Config.get_device_caps
                                      (Config.get_device_info())["browserName"])
    web_flag = True
    app_flag = False
else:
    pass


# add fixture create_report_folder if run in terminal
@pytest.fixture(autouse=app_flag)
def launch_app():
    log.info("Launch APP")
    driver = Driver()
    if device_os == "Android":
        driver = driver.aos_driver()
    else:
        driver = driver.ios_driver()
    yield driver
    time.sleep(5)
    driver.quit()
    log.info("Close APP")


@pytest.fixture(params=browser_os, autouse=web_flag)
def launch_web(request):
    log.info("Launch Browser")
    driver = Driver()
    if request.param == "Chrome":
        driver = driver.get_chrome_browser()
    elif request.param == "Firefox":
        driver = driver.get_firefox_browser()
    elif request.param == "Edge":
        driver = driver.get_edge_browser()
    yield driver
    time.sleep(5)
    driver.quit()
    log.info("Close Browser")


def pytest_bdd_step_error(step, step_func, exception):
    print(f'Step Failed: {step} and the step function {step_func}')
    print(f'Reason: {exception}')

# --------------------------------------------------General Background step---------------------------------------------#
