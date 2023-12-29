from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Use your own name and password
username = "marcuslshaw+test@gmail.com"
password = "IocXTZ845MNEPhP"


@given('Open main page_v2')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@then("Log into the page_v2")
def log_into_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'number-text-grid') and contains(text(), '9')]"))
    )
    email_button = context.driver.find_element(By.CSS_SELECTOR, "input#email-2")
    email_button.click()
    email_button.send_keys(username)

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "field"))
    )
    password_button = context.driver.find_element(By.ID, "field")
    password_button.click()
    password_button.send_keys(password)

    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@wized='loginButton']"))
    )
    login_button = context.driver.find_element(By.CSS_SELECTOR, "a[wized='loginButton'][class='login-button w-button']")

    # login_button = context.driver.find_element(By.XPATH, "//a[@wized='loginButton']")
    login_button.click()
    print("Button clicked")


@then("Click on settings_v2")
def settings_page(context):
    context.driver.save_screenshot("screenshot.png")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'menu-button-block') and .//div[contains(text(), 'Settings')]]"))
    )
    settings_button = context.driver.find_element(By.XPATH, "//a[contains(@class, 'menu-button-block') and .//div[contains(text(), 'Settings')]]")
    settings_button.click()


@then("Click on community_v2")
def community_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'page-setting-block') and .//div[contains(text(), 'Community')]]"))
    )
    community_button = context.driver.find_element(By.XPATH, "//a[contains(@class, 'page-setting-block') and .//div[contains(text(), 'Community')]]")
    community_button.click()


@then("Verify pages_v2")
def verify_pages(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "w-node-_6e3bc4fc-1cba-e8aa-f064-7d9d7860967f-bfd82bee"))
    )
    community_verify = context.driver.find_element(By.ID, "w-node-_6e3bc4fc-1cba-e8aa-f064-7d9d7860967f-bfd82bee")
    assert community_verify.is_displayed(), "Community page is not displayed"


@then("Verify contact_v2")
def open_target(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "w-node-_7ef36cf0-cbfd-8dd9-8c6f-e78b7fb3af26-bfd82bee"))
    )
    contact_verify = context.driver.find_element(By.ID, "w-node-_7ef36cf0-cbfd-8dd9-8c6f-e78b7fb3af26-bfd82bee")
    assert contact_verify.is_displayed(), "Contact section is not displayed"
