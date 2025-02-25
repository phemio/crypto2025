from base.BasePage import BasePage
from Utilities.customlogger import CustomLogger
from tests.elements.Element_Repository_EN import ElementRepositoryEN as LangEN
from Configuration.config import Config as Cf
cl = CustomLogger()


class HomeMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_forecast_menu(self):
        self.click_element(LangEN.FORECAST_MENU_BUTTON.value, "xpath")
        cl.allure_logs(f"{self.click_forecast_menu.__name__} in {self.__class__.__name__}")

    def click_nine_day_forecast_menu(self):
        self.click_element(LangEN.NINE_DAY_MENU_BUTTON.value, "xpath")
        cl.allure_logs(f"{self.click_nine_day_forecast_menu.__name__} in {self.__class__.__name__}")





