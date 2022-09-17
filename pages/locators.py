from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "//form[@id='register_form']")
    LOGIN_FORM = (By.CSS_SELECTOR, "//form[@id='login_form']")