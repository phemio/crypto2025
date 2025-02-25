from base.BasePage import BasePage
from Utilities.customlogger import CustomLogger
from tests.elements.Element_Repository_EN import ElementRepositoryEN as LangEN
from Configuration.config import Config as Cf
cl = CustomLogger()


class HomePage(BasePage):

    _home_title_text = "MyObservatory"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_in_home_page(self):
        actual_text = self.get_element_text(LangEN.HOME_TITLE.value, "xpath")
        expect_text = self._home_title_text
        self.element_text_comparison(expect_text, actual_text)
        cl.allure_logs(f"{self.verify_in_home_page.__name__}")

    def click_menu_button(self):
        self.click_element(LangEN.HOME_MENU_BUTTON.value, "aid")
        cl.allure_logs(f"{self.click_menu_button.__name__} in {self.__class__.__name__}")





