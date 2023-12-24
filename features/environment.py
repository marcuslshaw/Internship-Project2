from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def before_scenario(context, scenario):
    print("Running scenario with tags:", scenario.tags)
    if 'firefox' in scenario.tags:
        # service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox()
    else:
        print("Initializing Chrome WebDriver")
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def after_scenario(context, scenario):
    context.driver.quit()
