from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


class ProductPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def add_to_card(self):
        add_to_card = self.browser.find_element(*MainPageLocators.add_to_card)
        add_to_card.click()
    def solve_quiz_and_get_code(self):
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


    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, "'Login' not in URL"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form dont found"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REG_FORM), "Reg form dont found"