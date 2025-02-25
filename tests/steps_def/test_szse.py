import time
import pytest
from functools import partial
from pytest_bdd import scenarios, given, when, then, scenario, parsers
from Configuration.config import Config
import platform
from allure import severity, severity_level
from tests.Pages.LandingPage import LandingPage
from tests.Pages.HomePage import HomePage
from tests.Pages.HomeMenu import HomeMenu
from tests.api.modules.SZSEAPI import SZSEAPI
from tests.Pages.NineDayForecastPage import NineDayForecastPage
from tests.Pages.SZSEPage import SZSEPage
from Utilities.customlogger import CustomLogger as Cl

EXTRA_TYPES = {
    'String': str,
}
parse_str = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

config = Config()
log = Cl.loggen()
_feature = "\\tests\\features\\SZSE.feature"
_os = platform.system()
_new_feature_path = config.get_dir_path() + _feature if _os == "Windows" else _feature.replace("\\", "/")
scenarios(_new_feature_path)


def test_scenario_szse():
    pass

@given("user go to szse page")
def user_go_to_szse_page(launch_web):
    log.info("given - user go to szce page")
    print("given - user go to szce page")
    szse_page = SZSEPage(launch_web)
    szse_page.go_to_szse_page()
    log.info("user navigated to szse homepage")
    print("user navigated to szse homepage")

@when(parse_str("send the API request endpoint with pref {lang} language"))
def send_the_API_request_endpoint_with_pref(lang):
    log.info(f"when - send the API request endpoint with pref {lang} language")
    print(f"when - send the API request endpoint with pref {lang} language")
    szse_api = SZSEAPI
    szse_api.response_code(lang)

@then("verify high bigger than low")
def verify_high_bigger_than_low():
    log.info(f"then - verify high bigger than low")
    print(f"then - verify high bigger than low")
    szse_api = SZSEAPI
    szse_api.verify_high_bigger_than_low()
