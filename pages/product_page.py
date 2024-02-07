from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        btn.click()
    
    def should_be_succsess_msg(self):
        assert self.is_element_present(*ProductPageLocators.MSG), "There's no message about the added item "
    
    def shoul_be_item_name_in_msg(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_check = self.browser.find_element(*ProductPageLocators.ITEM_NAME_CHECK).text
        assert item_name == item_name_check, "There's no such name"
        
    def shoul_be_item_price_msg(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE_MSG), "There's no price in a message "
    
    def should_be_item_price_equal_in_msg(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        item_price_check = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_MSG_CHECK).text
        assert item_price == item_price_check, "Prices not equal"
    

        