import json

from tests.api.session import RequestTypes as Rt
from Utilities.customlogger import CustomLogger
from datetime import datetime, timedelta

cl = CustomLogger()


class SZSEAPI:

    URL = "https://www.szse.cn/api/market/ssjjhq/getTimeData?marketId=1&code=000001&language=EN"

    @staticmethod
    def get_instrument_data():
        body = Rt.GET(SZSEAPI.URL).text
        return body

    @staticmethod
    def response_code(lang):
        response = Rt.GET(SZSEAPI.URL.replace("language=EN", f"language={lang}"))
        if response.status_code == 200:
            print("Request successful!")
            market_data = response.json()
            print("Market Data for 000001.SHE:")
            print(market_data)

    @staticmethod
    def verify_high_bigger_than_low():
        response = Rt.GET(SZSEAPI.URL)
        market_data = response.json()
        if market_data['data']["high"] > market_data['data']["low"]:
            print("High bigger than low!")
        else:
            print("High smaller than low!")

    # @staticmethod
    # def get_relative_humidity():
    #     body = Rt.GET(f'{NineDayForeCastAPI.URL}?dataType={NineDayForeCastAPI.get_nine_day_data()}'
    #                   f'&lang={NineDayForeCastAPI.get_nine_day_lang()}').text
    #     today = datetime.now()
    #     day_after_tomorrow = today + timedelta(days=2)
    #     formatted_date = day_after_tomorrow.strftime("%Y%m%d")
    #     json_data = json.loads(body)
    #     for data in json_data["weatherForecast"]:
    #         if data["forecastDate"] == formatted_date:
    #             return (f"The day after tomorrow is: {data['forecastDate']} and the Relative Humidity is:"
    #                     f" {data['forecastMinrh']['value']}-{data['forecastMaxrh']['value']}%")

    # @staticmethod
    # def get_nine_day_lang():
    #     return nine_day.lang
    #
    # @staticmethod
    # def get_nine_day_data():
    #     return nine_day.data


