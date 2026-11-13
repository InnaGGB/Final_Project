from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_NAME_CHECK = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    MSG = (By.CSS_SELECTOR, ".alertinner>strong:nth-child(1)")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ITEM_PRICE_MSG = (By.CSS_SELECTOR, ".alertinner>p>strong")
    ITEM_PRICE_MSG_CHECK = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")