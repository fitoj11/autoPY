from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import CsCartLocators
from .product_page import ProductPage
from .login_page import LoginPage
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def should_be_have_LC(self):
        assert self.is_element_present(*CsCartLocators.LC), "not have LC"
    def click_product_from_main_page(self):
        link = self.browser.find_element(*CsCartLocators.PRODUCT_LINK)
        link.click()
    def should_be_have_addTOcart_button(self):
        assert self.is_element_present(*CsCartLocators.Add_to_cart_button), "Not have add to card button"