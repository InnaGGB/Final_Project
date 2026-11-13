from encodings.punycode import selective_find

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.xfail(reason="Success message appears after adding, so the negative check fails by design")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Success message appears after adding, so the negative check fails by design")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()

def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "Qa!test12345")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_to_basket()
        page.should_be_item_name_in_msg()
        page.should_be_item_price_equal_in_msg()