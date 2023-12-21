from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#  Start Chrome Browser
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

#Input your user name and password here
username = ""
password = ""


@given('Open main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@then("Log into the page")
def log_into_page(context):
    sleep(5)
    email_button = context.driver.find_element(By.CSS_SELECTOR, "input#email-2")
    email_button.click()
    email_button.send_keys(username)
    password_button = context.driver.find_element(By.ID, "field")
    password_button.click()
    password_button.send_keys(password)
    login_button = context.driver.find_element(By.XPATH, "//a[@wized='loginButton']")
    login_button.click()
    sleep(8)


@then("Click on settings")
def settings_page(context):
    settings_button = context.driver.find_element(By.XPATH, "//a[contains(@class, 'menu-button-block') and .//div[contains(text(), 'Settings')]]")
    settings_button.click()


@then("Click on community")
def community_page(context):
    community_button = context.driver.find_element(By.XPATH, "//a[contains(@class, 'page-setting-block') and .//div[contains(text(), 'Community')]]")
    community_button.click()


@then("Verify pages")
def verify_pages(context):
    community_verify = context.driver.find_element(By.ID, "w-node-_6e3bc4fc-1cba-e8aa-f064-7d9d7860967f-bfd82bee")


@then("Verify contact")
def open_target(context):
    contact_verify = context.driver.find_element(By.ID, "w-node-_7ef36cf0-cbfd-8dd9-8c6f-e78b7fb3af26-bfd82bee")


driver.quit()
