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
_feature = "\\tests\\features\\HKO.feature"
_os = platform.system()
_new_feature_path = config.get_dir_path() + _feature if _os == "Windows" else _feature.replace("\\", "/")
scenarios(_new_feature_path)


def test_scenario_hko():
    pass


@given("user go to the homepage")
def user_go_to_homepage(launch_app):
    log.info("given - user go to the homepage")
    print("given - user go to the homepage")
    landing_page = LandingPage(launch_app)
    landing_page.bypass_to_homepage_flow()
    home_page = HomePage(launch_app)
    home_page.verify_in_home_page()
    log.info("user navigated to the homepage")
    print("user navigated to the homepage")


@when("user click menu and select forecast submenu to choose nine day forecast")
def user_click_menu_and_select_forecast_submenu_to_choose_nine_day_forecast(launch_app):
    log.info("when - user click menu and select forecast submenu to choose nine day forecast")
    print("when - user click menu and select forecast submenu to choose nine day forecast")
    home_page = HomePage(launch_app)
    home_page.click_menu_button()
    home_menu = HomeMenu(launch_app)
    home_menu.click_forecast_menu()
    home_menu.click_nine_day_forecast_menu()


@then("verify the first date is correct in nine day forecast page")
def verify_the_first_date_is_correct_in_nine_day_forecast_page(launch_app):
    log.info("then - verify the first date is correct in nine day forecast page")
    print("then - verify the first date is correct in nine day forecast page")
    nine_day_page = NineDayForecastPage(launch_app)
    nine_day_page.verify_the_first_date_forecast_page()
    log.info("Verified the first date is correct in nine day forecast page")
    print("Verified the first date is correct in nine day forecast page")

