import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ResultsPage(BasePage):

    STREAM_TILES = (By.XPATH, '//a[@data-a-target="preview-card-image-link"]')
    RESULT_URL = "//www.twitch.tv/directory/category/"

    def __init__(self, browser):
        self.browser = browser

    def assert_page_url(self, url_part, timeout=10):
        self.assert_on_page(f"{self.RESULT_URL}{url_part}", timeout)

    def scroll_to_item(self, num_scrolls):
        self.scroll_down(num_scrolls)

    def select_streamer(self, item_name):
        streamer = self.browser.find_element(By.CSS_SELECTOR, f"a[href*='/{item_name}']")
        streamer.click()
        
    def wait_for_results_to_load(self, wait_time=1):
        # self.wait_for_element(self.STREAM_TILES, timeout)
        self.wait_for_page_to_load(wait_time)
