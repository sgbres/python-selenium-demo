import datetime
import pytest
import os
import json

from utils.browser_setup import setup_browser


@pytest.fixture(scope="session")
def config():
    # Adjust the path so that we go one level up from tests/ to the project root.
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    with open(config_path) as f:
        return json.load(f)

@pytest.fixture(scope="function")
def browser(request, config):
    # Default mode is 'desktop'
    mode = "desktop"
    # If parameters are passed, fetch 'mode' and an optional 'device' name.
    if hasattr(request, "param"):
        params = request.param
        mode = params.get("mode", "desktop")
    
    if mode == "mobile":
        # Get the desired device, defaulting to "iPhone XR" if not specified.
        device = request.param.get("device", "iPhone XR")
        device_config = config["devices"].get(device)
        if not device_config:
            raise ValueError(f"Device '{device}' not found in the configuration.")
        
        # Build the mobile_emulation dictionary using device metrics
        mobile_emulation = {
            "deviceMetrics": {
                "width": device_config["width"],
                "height": device_config["height"],
                # "pixelRatio": 3.0  # Adjust if needed.
            },
            # "userAgent": None  # Optionally, set a mobile user agent here.
        }
        
        driver = setup_browser(
            mobile_emulation=mobile_emulation,
            browser_type=config.get("browser", "Chrome"),
            implicit_wait=config.get("implicit_wait", 10)
        )
    else:
        # For desktop mode, simply do not enable mobile emulation.
        driver = setup_browser(
            mobile_emulation=None,
            browser_type=config.get("browser", "Chrome"),
            implicit_wait=config.get("implicit_wait", 10)
        )
    
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # We only want to act after the actual test call and if it failed
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\n🖼  Screenshot saved to: {file_path}")
