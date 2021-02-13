from .base_page import BasePage
from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.NAME)
        return name.text

    def get_success_product_name(self):
        success_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME)
        return success_product_name.text

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        return price.text

    def solve_quiz_and_get_code(self):
        self.browser.implicitly_wait(3)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message must be disappeared! "
