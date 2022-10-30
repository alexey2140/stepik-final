import time

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_new_user(self, email, password):  # метод для регистрации нового пользователя
        self.fill_in_email_registration(email)
        self.fill_in_password_registration(password)
        self.fill_in_confirm_password_registration(password)
        self.browser.find_element(*LoginPageLocators.REGISTRAION_SUBMIT).click()

    def fill_in_email_registration(self, email): # метод для ввода емейла для регистрации
        email_registration_input = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        email_registration_input.send_keys(email)

    def fill_in_password_registration(self, password):  # метод для ввода пароля для регистрации
        password_registration_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REG)
        password_registration_input.send_keys(password)

    def fill_in_confirm_password_registration(self, password):  # метод для ввода подтверждения пароля
        password_confirm_registration_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONF_REG)
        password_confirm_registration_input.send_keys(password)