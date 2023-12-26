from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def before_scenario(context, scenario):
    print("Running scenario with tags:", scenario.tags)
    if 'firefox' in scenario.tags:
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        # service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(options=firefox_options)
    else:
        print("Initializing Chrome WebDriver")
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def after_scenario(context, scenario):
    context.driver.quit()
