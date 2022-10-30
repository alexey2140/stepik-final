from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY_MESSAGE), \
            "Cart empty message is not presented, but should be"
        assert self.is_element_present(*BasketPageLocators.CONTINUE_LINK), \
            "Continue link is not presented, but should be"
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_FORM), \
            "Product element is presented, but should not be"
