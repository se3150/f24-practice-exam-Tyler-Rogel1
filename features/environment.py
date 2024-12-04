import behave_webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")  # Optional: ensure full-page rendering

    # Initialize behave_webdriver with the configured options
    context.behave_driver = behave_webdriver.Chrome(options=chrome_options)

def after_all(context):
    context.behave_driver.quit()
