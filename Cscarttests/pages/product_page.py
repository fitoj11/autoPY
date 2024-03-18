from .base_page import BasePage
# from .main_page import *
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import MainPageLocators
from .locators import CsCartLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

quantity = None
price = None
class ProductPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # def add_to_card(self):
    #     add_to_card = self.browser.find_element(*MainPageLocators.add_to_card)
    #     add_to_card.click()
    def correct_name(self):
        correct_name = self.browser.find_element(*MainPageLocators.correct_name).text
        correct_name_01 = self.browser.find_element(*MainPageLocators.correct_name_01).text
        assert correct_name == correct_name_01, "name is diff"
    def correct_value(self):
        correct_value = self.browser.find_element(*MainPageLocators.correct_value).text
        correct_value_01 = self.browser.find_element(*MainPageLocators.correct_value_01).text
        assert correct_value == correct_value_01, "price is diff"
    def should_be_product_page(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, "'Login' not in URL"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form dont found"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REG_FORM), "Reg form dont found"
    def should_be_have_addTOcart_button(self):
        assert self.is_element_present(*CsCartLocators.Add_to_cart_button), "Not have add to cart button"
    def add_to_cart(self):
        global price
        link = self.browser.find_element(*CsCartLocators.Add_to_cart_button)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        price = self.browser.find_element(*CsCartLocators.price_product).text
        link.click()
    def should_be_have_notification(self):
        assert self.browser.find_element(*CsCartLocators.ADD_NOTIFICATION), "Not have notification after add to cart"
    def go_to_cart(self):
        global quantity
        link = self.browser.find_element(*CsCartLocators.cart_button)
        close = self.is_element_present(*CsCartLocators.close)
        if close != None:
            close = self.browser.find_element(*CsCartLocators.close)
            quantity = self.browser.find_element(*CsCartLocators.quantity).text
            close.click()
            link.click()
            link2 = self.browser.find_element(*CsCartLocators.cart_popup_button)
            link2.click()
        else:
            link.click()
            link2 = self.browser.find_element(*CsCartLocators.cart_popup_button)
            link2.click()
    def should_be_in_cart(self):
        assert self.is_element_present(*CsCartLocators.cart_name), "Not in cart"
    def should_be_quantity_equal(self):
        abs = (float(self.browser.find_element(*CsCartLocators.quantity_cart).text)
               / float(self.browser.find_element(*CsCartLocators.quantity_cart2).text))
        assert (int(abs) == int(quantity)
                and self.browser.find_element(*CsCartLocators.quantity_cart2).text == price), "Not same quantity"
    def click_product_from_main_page(self):
        link = self.browser.find_element(*CsCartLocators.PRODUCT_LINK)
        link.click()
    def go_to_checkout(self):
        link = self.browser.find_element(*CsCartLocators.CHECKOUT_LINK)
        link.click()
    def should_be_quantity_equal_checkout(self):
        assert (int(quantity) == int(self.browser.find_element(*CsCartLocators.checkout_quantity).text)
                and self.browser.find_element(*CsCartLocators.checkout_price).text == price), "Not same quantity"
    def pass_required(self):
        link = self.browser.find_elements(*CsCartLocators.required_inputs)
        for x in range(len(link)):
            link[x].send_keys('test@test.test')

    def change_shipping(self):
        try:
            link = self.browser.find_element(*CsCartLocators.shipping_block_click)
            if link != None:
                self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
                link.click()
        except:
            return True
        if self.is_not_element_present(self.browser, *CsCartLocators.loader) == True:
            link2 = self.browser.find_element(*CsCartLocators.shipping_block)
            link2.click()
    def loader_wait(self):
        try:
            self.is_not_element_present(self.browser, *CsCartLocators.loader)
        finally:
            return True
    def tabs(self, tab_number): # создает массив и нумерует вкладки, в функции надо указать "self, номер вкладки"
        link = self.browser.window_handles
        self.browser.switch_to.window(link[tab_number])
    def move_to_elemnt(self, element):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    def change_payment(self):
        ProductPage.loader_wait(self)
        link = self.browser.find_element(*CsCartLocators.payment_link)
        link.click()
    def click_required_terms(self):
        ProductPage.loader_wait(self)
        link = self.browser.find_element(*CsCartLocators.required_terms)
        ProductPage.move_to_elemnt(self, link)
        link.click()
    def click_place_order_button(self):
        link = self.browser.find_element(*CsCartLocators.place_order_button)
        ProductPage.move_to_elemnt(self, link)
        link.click()
    def enter_admin(self):
        ProductPage.tabs(self, 1)
        # self.is_element_here(self.browser, *CsCartLocators.admin_entry)
        link = self.browser.find_element(*CsCartLocators.admin_entry)
        link.click()
class BeforeMethod(BasePage):
    def main_product_add_in_cart_checkout(self): # с главной, в товар, в карточку, в корзину, в чекаут
        BasePage.open(self)
        ProductPage.click_product_from_main_page(self)
        ProductPage.add_to_cart(self)
        ProductPage.go_to_cart(self)
        ProductPage.go_to_checkout(self)
    def pass_required_checkout_for_order(self): # ввести в чекауте все обязательные поля, изменить шиппинг, изменить способ доставки (по тел)
        ProductPage.pass_required(self)
        ProductPage.change_shipping(self)
        ProductPage.change_payment(self)
        ProductPage.click_required_terms(self)
        ProductPage.click_place_order_button(self)
    def kill_recaptcha(self):
        BasePage.open_second_tab(self)
        ProductPage.enter_admin(self)



    def main_add_checout_success_order(self): # главная - товар - добавить в корзину - чекаут - заполнить все поля - нажать плейс ордер
        BeforeMethod.main_product_add_in_cart_checkout(self)
        BeforeMethod.pass_required_checkout_for_order(self)