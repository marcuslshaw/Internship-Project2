from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Input your username and password here
username = ""
password = ""


@given('Open main page_f')
def open_main_page(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://soft.reelly.io/sign-in')


@then("Log into the page_f")
def log_into_page(context):
    WebDriverWait(context.browser, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'number-text-grid') and contains(text(), '9')]"))
    )
    email_button = context.browser.find_element(By.CSS_SELECTOR, "input#email-2")
    email_button.click()
    email_button.send_keys(username)

    WebDriverWait(context.browser, 15).until(
        EC.element_to_be_clickable((By.ID, "field"))
    )
    password_button = context.browser.find_element(By.ID, "field")
    password_button.click()
    password_button.send_keys(password)

    WebDriverWait(context.browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@wized='loginButton']"))
    )
    login_button = context.browser.find_element(By.XPATH, "//a[@wized='loginButton']")
    login_button.click()


@then("Click on settings_f")
def settings_page(context):
    WebDriverWait(context.browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'menu-button-block') and .//div[contains(text(), 'Settings')]]"))
    )
    settings_button = context.browser.find_element(By.XPATH, "//a[contains(@class, 'menu-button-block') and .//div[contains(text(), 'Settings')]]")
    settings_button.click()


@then("Click on community_f")
def community_page(context):
    WebDriverWait(context.browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'page-setting-block') and .//div[contains(text(), 'Community')]]"))
    )
    community_button = context.browser.find_element(By.XPATH, "//a[contains(@class, 'page-setting-block') and .//div[contains(text(), 'Community')]]")
    community_button.click()


@then("Verify pages_f")
def verify_pages(context):
    WebDriverWait(context.browser, 15).until(
        EC.visibility_of_element_located((By.ID, "w-node-_6e3bc4fc-1cba-e8aa-f064-7d9d7860967f-bfd82bee"))
    )
    community_verify = context.browser.find_element(By.ID, "w-node-_6e3bc4fc-1cba-e8aa-f064-7d9d7860967f-bfd82bee")
    assert community_verify.is_displayed(), "Community page is not displayed"


@then("Verify contact_f")
def open_target(context):
    WebDriverWait(context.browser, 15).until(
        EC.visibility_of_element_located((By.ID, "w-node-_7ef36cf0-cbfd-8dd9-8c6f-e78b7fb3af26-bfd82bee"))
    )
    contact_verify = context.browser.find_element(By.ID, "w-node-_7ef36cf0-cbfd-8dd9-8c6f-e78b7fb3af26-bfd82bee")
    assert contact_verify.is_displayed(), "Contact section is not displayed"
