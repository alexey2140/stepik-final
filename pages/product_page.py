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
