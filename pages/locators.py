from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "//form[@id='register_form']")
    LOGIN_FORM = (By.CSS_SELECTOR, "//form[@id='login_form']")


class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    PRODUCT_GALLERY = (By.XPATH, "//div[@id='product_gallery']")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    CART_SUM = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@id='messages']/div[1]//strong")
