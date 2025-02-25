from appium import webdriver as appdriver
from Configuration.config import Config
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


class Driver:

    @staticmethod
    def aos_driver():
        desired_caps = {}
        desired_caps['platformName'] = Config.read_yml_file(Config.config_driver_path,
                                                            Config.get_device_caps
                                                            (Config.get_device_info())["platformName"])
        desired_caps['automationName'] = 'UiAutomator2'
        # desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = Config.read_yml_file(Config.config_driver_path,
                                                          Config.get_device_caps
                                                          (Config.get_device_info())["deviceName"])
        desired_caps['appPackage'] = Config.get_env_info()["appPackage"]
        desired_caps['appActivity'] = Config.get_env_info()["appActivity"]
        desired_caps['noReset'] = Config.get_reset_flag()
        driver = appdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        return driver

    @staticmethod
    def ios_driver():
        desired_caps = {}
        desired_caps['platformName'] = Config.read_yml_file(Config.config_driver_path,
                                                            Config.get_device_caps
                                                            (Config.get_device_info())["platformName"])
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '15'
        desired_caps['deviceName'] = Config.read_yml_file(Config.config_driver_path,
                                                          Config.get_device_caps
                                                          (Config.get_device_info())["deviceName"])
        desired_caps['app'] = '/Users/pamung/Documents/HKDL.app'
        desired_caps['noReset'] = Config.get_reset_flag()
        driver = appdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        return driver

    @staticmethod
    def get_ios_simulator_safari_browser():
        """
        This function aims to define the iOS Simulator Safari Web Browser setting to be used for automation
        no parameters
        :return:
        """
        # Set up the web driver and launch the webview app. DesiredCapabilities
        capabilities = {
            'platformName': 'iOS',
            'platformVersion': '15.2',
            'automationName': 'XCUITest',
            'browserName': 'Safari',
            'deviceName': 'iPhone 13',
            'autoAcceptAlerts': 'true',
            'noReset': Config.get_reset_flag()

        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver

    @staticmethod
    def get_android_simulator_chrome_browser():
        """
        This function aims to define the Android Simulator Chrome Web Browser setting to be used for automation
        no parameters
        :return:
        """
        options = webdriver.ChromeOptions()
        options.set_capability('platformName', Config.read_yml_file(Config.config_driver_path,
                                                                    Config.get_device_caps
                                                                    (Config.get_device_info())["platformName"]))
        options.set_capability('chromedriverExecutable', '/usr/local/bin/chromedriver')
        # options.set_capability('deviceName', '26288d01bc1c7ece')
        options.set_capability('deviceName', Config.read_yml_file(Config.config_driver_path,
                                                                  Config.get_device_caps
                                                                  (Config.get_device_info())["deviceName"]))
        options.set_capability('noReset', Config.get_reset_flag())

        # capabilities = {
        #    'platformName': 'Android',
        #    'browserName': 'Chrome',
        #    'deviceName': '26288d01bc1c7ece',  # for real device
        #    # 'deviceName': 'emulator-5554',
        #    'chromeOptions': {
        #        'androidPackage': 'com.android.chrome',
        #    }
        # }

        # driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=options.to_capabilities())
        return driver

    @staticmethod
    def get_chrome_browser():
        """
        This function aims to define the Chrome Web Browser setting to be used for automation
        :no parameters
        :return: webdriver
        """
        _exec_path = Config.window_folder_dir + r"\\package\\chromedriver.exe" \
            if Config.os_flag == "Windows" else Config.mac_folder_dir + "/package/chromedriver.exe"
        s = Service(executable_path=_exec_path)
        opt = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=s, options=opt)
        driver.maximize_window()
        return driver

    @staticmethod
    def get_firefox_browser():
        """
        This function aims to define the Firefox Web Browser setting to be used for automation
        :no parameters
        :return:
        """
        _exec_path = Config.window_folder_dir + r"\\package\\geckodriver.exe" \
            if Config.os_flag == "Windows" else Config.mac_folder_dir + "/package/geckodriver.exe"
        s = Service(executable_path=_exec_path)
        opt = webdriver.FirefoxOptions()
        opt.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'\
            if Config.os_flag == "Windows" else r'/Mozilla Firefox/firefox.exe'
        driver = webdriver.Firefox(service=s, options=opt)
        driver.maximize_window()
        return driver

    @staticmethod
    def get_edge_browser():
        """
        This function aims to define the Edge Web Browser setting to be used for automation
        no parameters
        :return:
        """
        _exec_path = Config.window_folder_dir + r"\\package\\msedgedriver.exe" \
            if Config.os_flag == "Windows" else Config.mac_folder_dir + "/package/msedgedriver.exe"
        s = Service(executable_path=_exec_path)
        opt = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=s, options=opt)
        driver.maximize_window()
        return driver

    # def get_safari_browser(self):
    #     """
    #     This function aims to define the Safari Web Browser setting to be used for automation
    #     no parameters
    #     :return:
    #     """
    #     s = Service(executable_path=f"{Content.safari_path}safaridriver")
    #     driver = Safari(service=s)
    #     # driver = Safari()
    #     return driver
