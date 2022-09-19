import time

from pages.product_page import ProductPage


def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    productpage = ProductPage(browser, link)  # иниц. Page Object, передаем в конструктор экземпляр драйвера и url адрес
    productpage.open()                        # открываем страницу
    productpage.should_be_product_page()      # проверяем что это точно ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    productpage = ProductPage(browser, link)  # иниц. Page Object, передаем в конструктор экземпляр драйвера и url адрес
    productpage.open()                        # открываем страницу
    productpage.add_to_cart()                 # добавляем продукт в корзину
    productpage.solve_quiz_and_get_code()     # вызываем метод для рассчета кода
    productpage.check_product_is_added_message()  # проверяем сообщение о добавлении продукта в корзину
    productpage.check_cart_price()                # проверяем что цена в корзине совпадает с ценой продукта
    time.sleep(1200)

