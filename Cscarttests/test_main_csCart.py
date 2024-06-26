from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.product_page import BeforeMethod
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
link = "https://dev.demo.cs-cart.ru/"
def test_should_be_have_LC(browser): # на странице есть кнопка ЛК
    page = MainPage(browser, link)
    page.open()
    page.should_be_have_LC()
def test_product_cart_checkout_order(browser): # с главной можно перейти в карточку товара, есть кнопка "Добавить в корзину"
    page = MainPage(browser, link)
    page.open()
    page.click_product_from_main_page()
    page.should_be_have_addTOcart_button()
def test_add_to_cart(browser): # с главной в карточку товара, кнопка "Добавить в корзину", появляется нотификация о добавлении
    page = MainPage(browser, link)
    page.open()
    page.click_product_from_main_page()
    page = ProductPage(browser, link)
    page.add_to_cart()
    page.should_be_have_notification()
def test_product_in_cart(browser): # с главной, в карточку товара, добавить в корзину, перейти в корзину, тест на нахождение в корзине
    page = MainPage(browser, link)
    page.open()
    page.click_product_from_main_page()
    page = ProductPage(browser, link)
    page.add_to_cart()
    page.go_to_cart()
    page.should_be_in_cart()
    # time.sleep(10)
    page.should_be_quantity_equal()
def test_in_cart(browser): # в корзине тот товар, что мы добавили в корзину, тест что в чекауте столько же товара и по той же цене
    page = BeforeMethod(browser, link)
    page.main_product_add_in_cart_checkout()
    page = ProductPage(browser, link)
    page.should_be_quantity_equal_checkout()
    # time.sleep(2)
def test_main_add_checout_success_order(browser): # оформить заказ, тест что есть текст о удачном заказе + линк на заказ
    page = BeforeMethod(browser, link)
    page.main_add_checout_success_order()
    page = ProductPage(browser, link)
    page.should_be_have_order_details()
