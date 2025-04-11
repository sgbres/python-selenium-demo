from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def handle_pop_up(driver):
    try:
        # Example: look for a 'Close' button on a modal
        close_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]")
        close_button.click()
    except NoSuchElementException:
        pass  # No modal found; continue with the test.

def handle_cookie_banner(driver):
    try:
        # Example: look for a 'Accept' button on a cookie banner
        accept_button = driver.find_element(By.XPATH, "//button[@data-a-target='consent-banner-accept']")
        accept_button.click()
    except NoSuchElementException:
        pass  # No cookie banner found; continue with the test.
