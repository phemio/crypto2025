import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException, NoSuchElementException)
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customlogger import CustomLogger as Cl
from Configuration.config import Config

import time

cf = Config()


class BasePage:
    log = Cl.loggen()
    _timeout = 20

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_value, locator_type):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, self._timeout, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locator_type == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locator_value))
            return element
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locator_value))
            return element
        elif locator_type == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UiSelector().description("%s")' % locator_value))
            return element
        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locator_value)))
            return element
        elif locator_type == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locator_value))
            return element
        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locator_value))
            return element
        elif locator_type == "aid":
            element = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, locator_value))
            return element
        else:
            self.log.info("Locator value " + locator_value + "not found")
        return element

    def get_element(self, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            self.log.info(
                "Element found with LocatorType :" + locator_type + " with the locatorValue :" + locator_value)
            return element
        except Exception as e:
            self.log.info(
                "Element not found with LocatorType :" + locator_type + " with the locatorValue :" + locator_value)
            self.take_screenshot(locator_type)
            raise Exception(f"Unable to find the " + locator_value + " element") from e

    def get_element_text(self, locator_value, locator_type="id"):
        try:
            text = self.get_element(locator_value, locator_type).get_attribute("text")
            self.log.info(
                "Element found and text is :" + text)
            return text
        except Exception as e:
            raise Exception(f"Unable to find the text attribute of " + locator_value + " element") from e

    def element_text_comparison(self, expect_text, actual_text):
        try:
            self.log.info(f"expect_text: {expect_text}; actual_text: {actual_text}")
            if expect_text.strip() == actual_text.strip():
                self.log.info(f"expect_text: {expect_text} is equals to actual_text: {actual_text}")
            else:
                self.log.info(f"expect_text: {expect_text} is not equals to actual_text: {actual_text}")
                raise Exception(f"expect_text: {expect_text} is not equals to actual_text: {actual_text}")
        except Exception as e:
            raise e

    def click_element(self, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType :" + locator_type + " and with the locatorValue :" + locator_value)
            return element
        except Exception as e:
            self.log.info(
                "Unable to click on Element not found with LocatorType :"
                + locator_type + " with the locatorValue :" + locator_value)
            self.take_screenshot(locator_type)
            raise Exception(f"Unable to click the " + locator_value + " element") from e

    def click_if_exist_element(self, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType :" + locator_type + " and with the locatorValue :" + locator_value)
            return element
        except Exception as e:
            self.log.info(
                "Unable to click on Element not found with LocatorType :"
                + locator_type + " with the locatorValue :" + locator_value)
            self.take_screenshot(locator_type)

    def send_text(self, text, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.send_keys(text)
            self.log.info(
                "Send text on Element with LocatorType :"
                + locator_type + " and with the locatorValue :" + locator_value)
        except Exception as e:
            self.log.info(
                "Unable to send text on Element not found with LocatorType :"
                + locator_type + " with the locatorValue :" + locator_value)
            self.take_screenshot(locator_type)
            raise Exception(f"Unable to send text on the " + locator_value + " text field") from e

    def is_displayed(self, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.is_displayed()
            self.log.info(
                "Element with LocatorType :" + locator_type + " and with the locatorValue :" + locator_value)
        except Exception as e:
            self.log.info(
                " Element not found with LocatorType :" + locator_type + " with the locatorValue :" + locator_value)
            self.take_screenshot(locator_type)
            raise Exception("Unable to find the display of " + locator_value) from e

    def is_enabled(self, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.is_enabled()
            self.log.info(
                "Element is enabled with LocatorType :" + locator_type + " and with the locatorValue :" + locator_value)
        except Exception as e:
            self.log.info(
                "Element is not enabled with LocatorType :" + locator_type + " with the locatorValue :" + locator_value)
            self.take_screenshot(locator_type)
            raise Exception("Element is not enabled for " + locator_value) from e

    def screen_shot(self, screenshot_name):
        file_name = screenshot_name + "_" + time.strftime("%d_%m_%y_%H_%M_%S") + ".png"
        screenshot_directory = cf.get_screenshot_folder_path()
        screenshot_path = screenshot_directory + file_name
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot save successfully to path : " + screenshot_path)
        except Exception as e:
            self.log.info("Unable to take screenshot")
            raise Exception("Unable to take screenshot") from e

    def take_screenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def get_url(self, url):
        self.driver.get(url)
