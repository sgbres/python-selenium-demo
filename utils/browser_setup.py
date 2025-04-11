from selenium import webdriver

def setup_browser(mobile_emulation=None, browser_type="chrome", implicit_wait=10):
    options = webdriver.ChromeOptions()
    
    if mobile_emulation:
        options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Unsupported browser type. Currently, only 'chrome' is supported.")
    
    driver.implicitly_wait(implicit_wait)
    
    # If a custom deviceMetrics is provided, adjust the browser window size
    if mobile_emulation and "deviceMetrics" in mobile_emulation:
        metrics = mobile_emulation["deviceMetrics"]
        width = metrics.get("width")
        height = metrics.get("height")
        if width and height:
            driver.set_window_size(width, height)
    
    return driver
