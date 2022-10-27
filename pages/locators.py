from selenium.webdriver.common.by import By


class LoginPageLocators():
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")


class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    PRODUCT_GALLERY = (By.XPATH, "//div[@id='product_gallery']")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    CART_SUM = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner') and contains(text(),'basket now')]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.XPATH, "//a[contains(text(),'View basket')]")


class BasketPageLocators():
    CART_IS_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")
    CONTINUE_LINK = (By.XPATH, "// a[.='Continue shopping']")
    PRODUCTS_FORM = (By.XPATH, "//form[@id='basket_formset']")
