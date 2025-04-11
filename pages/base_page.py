import json
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, browser):
        self.driver = driver
        self.browser = browser

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def input_text(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    def scroll_down(self, num_scrolls):
        # self.driver.execute_script("window.scrollBy(0, 1000);")
        for _ in range(num_scrolls):
            self.browser.execute_script("window.scrollBy(0, 800)")
            time.sleep(1)

    def assert_on_page(self, expected_url, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.url_to_be(expected_url),
            message=f"Expected URL to be {expected_url}, but got {self.browser.current_url}"
        )

    def wait_for_page_to_load(self, wait_time=1):
        time.sleep(wait_time)

    @staticmethod
    def get_config_value(key, default=None):
        config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
        try:
            with open(config_path, "r") as config_file:
                config = json.load(config_file)
            return config.get(key, default)
        except FileNotFoundError:
            print(f"⚠️ Config file not found at {config_path}. Using default value.")
            return default