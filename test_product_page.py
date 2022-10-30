import time

import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        Rpage = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakemail.org" + "12#"
        Rpage.open()
        Rpage.register_new_user(email, password)
        Rpage.should_be_authorized_user()

    @pytest.mark.smokee
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        productpage = ProductPage(browser, link)  # иниц. Page Object, передаем в конструктор экземпляр драйвера и url адрес
        productpage.open()                        # открываем страницу
        productpage.should_not_be_success_message()  # проверяем что сообщение об успехе не отображается и оно не отображ.

    @pytest.mark.smokee
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        #link = f"{linkp}"
        productpage = ProductPage(browser, link)  # иниц. Page Object, передаем в конструктор экземпляр драйвера и url адрес
        productpage.open()                        # открываем страницу
        productpage.add_to_cart()                 # добавляем продукт в корзину
        #productpage.solve_quiz_and_get_code()     # вызываем метод для рассчета кода
        productpage.check_product_is_added_message()  # проверяем сообщение о добавлении продукта в корзину
        productpage.check_cart_price()                # проверяем что цена в корзине совпадает с ценой продукта
        time.sleep(3)


def test_guest_can_go_to_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    productpage = ProductPage(browser, link)  # иниц. Page Object, передаем в конструктор экземпляр драйвера и url адрес
    productpage.open()                        # открываем страницу
    productpage.should_be_product_page()      # проверяем что это точно ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    productpage = ProductPage(browser, link)     # иниц. Page Object, передаем в конструктор экземпляр драйвера и url
    productpage.open()                           # открываем страницу
    productpage.add_to_cart()                    # добавляем продукт в корзину
    productpage.should_not_be_success_message()  # проверяем что сообщение об успехе не отображается НО оно отображается


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    productpage = ProductPage(browser, link)  # иниц. Page Object, передаем в конструктор экземпляр драйвера и url адрес
    productpage.open()                        # открываем страницу
    productpage.add_to_cart()                 # добавляем продукт в корзину
    productpage.should_be_disappeared_success_message()  # проверяем что нет сообщения об успехе


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


#@pytest.mark.smoke
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # иниц. Product Page Page Object
    page.open()  # переходим на Product Page
    page.go_to_login_page()  # переходим на Login Page кликая на ссылку в хедере
    pageL = LoginPage(browser, link)  # иниц. Login Page Page Object
    pageL.should_be_login_page()  # проверка что мы перешли на Login Page


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # иниц. Product Page Page Object
    page.open()  # переходим на Product Page
    page.go_to_cart_page()  # переходим на Cart Page по клику на ссылку в хедере
    pageC = BasketPage(browser, link)
    pageC.cart_should_be_empty()


