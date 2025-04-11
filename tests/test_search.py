import time
import pytest
from selenium.webdriver.common.by import By
from pages.results_page import ResultsPage
from pages.twitch_home import TwitchHomePage
from utils.popup_handler import handle_pop_up, handle_cookie_banner

@pytest.mark.parametrize("browser", [
    {"mode": "desktop"},
    # {"mode": "mobile", "device": "iPhone XR"},
], indirect=True)
def test_twitch_search_desktop(browser):
    twitch_home = TwitchHomePage(browser)
    results_page = ResultsPage(browser)

    # Load the Twitch homepage
    twitch_home.load()
    
    # Handle potential pop-ups on the homepage
    handle_cookie_banner(browser)

    # Enter the search term "StarCraft II"
    twitch_home.perform_search("StarCraft II")

    # Wait for the results page to load
    results_page.wait_for_results_to_load(3)

    # Scroll down twice
    results_page.scroll_to_item(2)  # Scroll down twice
    
    # Select a streamer
    handle_pop_up(browser)
    results_page.select_streamer("starcraft")
    results_page.wait_for_results_to_load(5)
    
    # Save a screenshot of the streamer page.
    browser.save_screenshot("screenshots/streamer_web_page.png")

@pytest.mark.parametrize("browser", [
    {"mode": "mobile", "device": "Pixel 7"},
], indirect=True)
def test_twitch_search_mobile(browser):
    twitch_home = TwitchHomePage(browser)
    results_page = ResultsPage(browser)

    # Load the Twitch homepage
    twitch_home.load()
    
    # Handle potential pop-ups on the homepage
    handle_cookie_banner(browser)

    # Enter the search term "StarCraft II"
    twitch_home.perform_search("StarCraft II")

    # Wait for the results page to load
    results_page.wait_for_results_to_load(3)

    # Scroll down twice
    results_page.scroll_to_item(2)  # Scroll down twice
    
    # Select a streamer
    handle_pop_up(browser)
    results_page.select_streamer("starcraft")
    results_page.wait_for_results_to_load(5)
    
    # Save a screenshot of the streamer page.
    browser.save_screenshot("screenshots/streamer_mobile_page.png")