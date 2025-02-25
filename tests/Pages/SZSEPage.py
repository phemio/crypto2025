from base.BasePage import BasePage
from Utilities.customlogger import CustomLogger
from tests.elements.Element_Repository_EN import ElementRepositoryEN as LangEN
from Configuration.config import Config as Cf
from datetime import datetime, timedelta

cl = CustomLogger()


class SZSEPage(BasePage):

    _url = "https://www.szse.cn/English/siteMarketData/siteMarketDatas/lookup/index.html?code=000001"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_szse_page(self):
        self.get_url(self._url)
        cl.allure_logs(f"{self.go_to_szse_page.__name__}")





