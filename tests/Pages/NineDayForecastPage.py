from base.BasePage import BasePage
from Utilities.customlogger import CustomLogger
from tests.elements.Element_Repository_EN import ElementRepositoryEN as LangEN
from Configuration.config import Config as Cf
from datetime import datetime, timedelta

cl = CustomLogger()


class NineDayForecastPage(BasePage):

    current_date = datetime.now()
    tomorrow_date = current_date + timedelta(days=1)
    formatted_date = tomorrow_date.strftime("%d %B")
    expect_date = tomorrow_date.strftime("%d %b")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_the_first_date_forecast_page(self):
        actual_text = self.get_element_text(LangEN.FIRST_DAY_IN_NINE_DAY_FORECAST.value + '"' + self.formatted_date + '"]', "xpath")
        expect_text = self.expect_date
        self.element_text_comparison(expect_text, actual_text)
        print(f'Get actual text from application: {actual_text} ; expect text for tmr date: {expect_text}')
        cl.allure_logs(f"{self.verify_the_first_date_forecast_page.__name__}")





