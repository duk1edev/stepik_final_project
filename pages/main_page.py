from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        # login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        # assert self.browser.find_element(By.CSS_SELECTOR, "#login_link999"), 'Login link is not present'
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link333"), 'Login link is not present'

