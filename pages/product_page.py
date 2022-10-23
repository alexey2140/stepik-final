from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        addtocartbutton = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        addtocartbutton.click()

    def check_cart_price(self):
        productprice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(productprice)
        cartprice = self.browser.find_element(*ProductPageLocators.CART_SUM).text
        print(cartprice)
        assert productprice in cartprice

    def check_product_is_added_message(self):
        productname = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        addedproduct = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert productname == addedproduct

    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), "Product gallery is not present"

    def should_not_be_success_message(self):  # возможно этот метод не пригодится
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):  # метод на то что сообщение пропадет
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

