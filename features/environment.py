from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def before_scenario(context, scenario):
    print("Running scenario with tags:", scenario.tags)
    if 'firefox' in scenario.tags:
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--headless")
        # service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(options=firefox_options)

    elif 'browserstack' in scenario.tags:
        bs_user = 'marcusshaw_kLfDar'
        bs_key = 'SpoVeuBzxDJRLqBWFGAm'
        url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

        options = FirefoxOptions()
        bstack_options = {
            'os': "Windows",
            'osVersion': "10",
            'browserName': 'Firefox',
            'sessionName': 'scenario_name'
        }

        options.set_capability('bstack:options', bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)
    else:
        print("Initializing Chrome WebDriver")
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def after_scenario(context, scenario):
    context.driver.quit()
