from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        addtocartbutton = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        addtocartbutton.click()

    def check_cart_price(self):
        pass

    def check_product_is_added_message(self):
        pass

    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), "Product gallery is not present"
