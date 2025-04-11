from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class TwitchHomePage(BasePage):

    BASE_URL = BasePage.get_config_value("base_url", "https://www.twitch.tv/")  
  
    SEARCH_ICON = (By.CSS_SELECTOR, "a[href='/directory']")
    SEARCH_INPUT = (By.XPATH, '//input[@data-a-target="tw-input"]')
    BROWSE_LINK = (By.XPATH, '//a[@data-a-target="browse-link"]')
    ACCEPT_BUTTON = (By.XPATH, '//button[@data-a-target="consent-banner-accept"]')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.BASE_URL)

    def perform_search(self, phrase):
        try:
            search_icon_element = self.browser.find_element(*self.SEARCH_ICON)
            if search_icon_element.is_displayed():
                search_icon_element.click()
            else:
                print("Search icon is not displayed.")
        except NoSuchElementException:
            print("Search icon not found.")

        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
