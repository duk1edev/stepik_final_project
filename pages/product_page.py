from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        time.sleep(4)
        button.click()
        self.solve_quiz_and_get_code()

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
            time.sleep(3)
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
