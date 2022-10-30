from selenium.webdriver.common.by import By
from pages.locators import BasePageLocators
from pages.login_page import LoginPage

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)