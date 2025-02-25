from base.BasePage import BasePage
from Utilities.customlogger import CustomLogger
from tests.elements.Element_Repository_EN import ElementRepositoryEN as LangEN
# from Configuration.config import Config as Cf
cl = CustomLogger()


class LandingPage(BasePage):

    _disclaimer_title_text = "Disclaimer"
    _privacy_title_text = "Privacy Policy Statements"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def verify_in_landing_page(self):
    #     actual_text = self.get_element_text(LangEN.LANDING_TITLE_TEXT.value)
    #     expect_text = self._landing_title_text
    #     self.element_text_comparison(expect_text, actual_text)
    #     cl.allure_logs(f"{self.verify_in_landing_page.__name__}")
    #
    # def click_login_remote_button(self):
    #     self.click_element(LangEN.LOGIN_REMOTE_BUTTON.value)
    #     cl.allure_logs(f"{self.click_login_remote_button.__name__} in {self.__class__.__name__}")
    #
    # def send_id_textfield(self):
    #     username = Cf.read_yml_file(Cf.config_config_path, Cf.get_env_info()["loginAccount"]["username"])
    #     self.send_text(LangEN.ID_TEXT_FIELD.value, username)
    #     cl.allure_logs(f"Send {username} on {self.send_id_textfield.__name__} in {self.__class__.__name__}")
    #
    # def click_id_continue_button(self):
    #     self.click_element(LangEN.ID_CONTINUE_BUTTON.value)
    #     cl.allure_logs(f"{self.click_id_continue_button.__name__} in {self.__class__.__name__}")
    #
    # def go_to_url(self, url):
    #     self.get_url(url)
    #     cl.allure_logs(f"{self.go_to_url.__name__} in {self.__class__.__name__}")

# HKO_Project

    def bypass_to_homepage_flow(self):
        self.verify_in_disclaimer_page()
        self.click_agree_button()
        self.verify_in_privacy_page()
        self.click_agree_button()
        self.click_allow_notification_permission_button()
        self.click_android_ok_button()
        self.click_allow_permission_button()
        self.click_android_back_button()
        self.click_next_till_close_banner()
        cl.allure_logs(f"{self.bypass_to_homepage_flow.__name__}")

    def verify_in_disclaimer_page(self):
        actual_text = self.get_element_text(LangEN.DISCLAIMER_TITLE.value)
        expect_text = self._disclaimer_title_text
        self.element_text_comparison(expect_text, actual_text)
        cl.allure_logs(f"{self.verify_in_disclaimer_page.__name__}")

    def verify_in_privacy_page(self):
        actual_text = self.get_element_text(LangEN.DISCLAIMER_TITLE.value)
        expect_text = self._privacy_title_text
        self.element_text_comparison(expect_text, actual_text)
        cl.allure_logs(f"{self.verify_in_privacy_page.__name__}")

    def click_agree_button(self):
        self.click_element(LangEN.AGREE_BUTTON.value)
        cl.allure_logs(f"{self.click_agree_button.__name__} in {self.__class__.__name__}")

    def click_android_ok_button(self):
        self.click_element(LangEN.ANDROID_OK_BUTTON.value)
        cl.allure_logs(f"{self.click_android_ok_button.__name__} in {self.__class__.__name__}")

    def click_allow_permission_button(self):
        self.click_element(LangEN.LOCATION_ALLOW_PERMISSION_BUTTON.value)
        cl.allure_logs(f"{self.click_allow_permission_button.__name__} in {self.__class__.__name__}")

    def click_allow_notification_permission_button(self):
        self.click_element(LangEN.NOTIFICATION_ALLOW_BUTTON.value)
        cl.allure_logs(f"{self.click_allow_notification_permission_button.__name__} in {self.__class__.__name__}")

    def click_android_back_button(self):
        self.click_if_exist_element(LangEN.ANDROID_BACK_BUTTON.value, "xpath")
        cl.allure_logs(f"{self.click_android_back_button.__name__} in {self.__class__.__name__}")

    def click_banner_next_button(self):
        self.click_element(LangEN.BANNER_NEXT_PAGE_BUTTON.value)
        cl.allure_logs(f"{self.click_banner_next_button.__name__} in {self.__class__.__name__}")

    def click_next_till_close_banner(self):
        while self.get_element(LangEN.BANNER_NEXT_PAGE_BUTTON.value).get_attribute("content-desc") != "Close":
            self.click_banner_next_button()
        self.click_banner_next_button()
        cl.allure_logs(f"{self.click_next_till_close_banner.__name__} in {self.__class__.__name__}")
