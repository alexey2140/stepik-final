from selenium.webdriver.common.by import By
import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url) # вариант 2 реализации переходов между страницами
        login_page.should_be_login_page()


        # login_page = page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        # login_page.should_be_login_page()             # вариант 1 реализации переходов между страницами

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    pageB = BasketPage(browser, link)
    pageB.cart_should_be_empty()

