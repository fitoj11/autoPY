from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.support.ui import WebDriverWait
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    add_to_card = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    correct_name = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main']>h1")
    correct_value = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main']>p")
    correct_name_01 = (By.CSS_SELECTOR, "div[class='alertinner ']>strong")
    correct_value_01 = (By.CSS_SELECTOR, "div[class='alertinner ']>p>strong")
class LoginPageLocators():
    LOGIN_LINK_LOGINPAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REG_FORM = (By.CSS_SELECTOR, "#register_form")
class CsCartLocators():
    LC = (By.CSS_SELECTOR, "a[class='ty-account-info__title']")
    PRODUCT_LINK = (By.CSS_SELECTOR, "div[class='ty-grid-list__image']>a>img")
    Add_to_cart_button = (By.CSS_SELECTOR, "div>div>button[class='ty-btn__primary ty-btn__big ty-btn__add-to-cart cm-form-dialog-closer ty-btn']")
    ADD_NOTIFICATION = (By.CSS_SELECTOR, "div[class='cm-notification-content cm-notification-content-extended notification-content-extended  cm-auto-hide'")
    cart_button = (By.CSS_SELECTOR, "span[class='ty-icon ty-icon-moon-commerce ty-minicart__icon filled']")
    cart_name = (By.CSS_SELECTOR, "h1[class='ty-mainbox-title']")
    cart_popup_button = (By.CSS_SELECTOR, "div[class='ty-float-left']")
    close = (By.CSS_SELECTOR, "span[class='cm-notification-close close']")
    quantity = (By.CSS_SELECTOR, "div[class='ty-product-notification__price']>span:nth-child(1)")
    price_product = (By.CSS_SELECTOR, "div[class='ty-product-block__price-actual']>span>span>span:nth-child(1)")
    quantity_cart = (By.CSS_SELECTOR, "td>span[class='price']:nth-child(1)")
    quantity_cart2 = (By.CSS_SELECTOR, "td>span[class='ty-sub-price']:nth-child(1)")
    price_cart = (By.CSS_SELECTOR, "p>span[id]")
    CHECKOUT_LINK = (By.CSS_SELECTOR, "div[class='ty-float-right ty-cart-content__right-buttons']>a[class='ty-btn ty-btn__primary ']")
    checkout_price = (By.CSS_SELECTOR, "div[class='ty-order-products__price']>span:nth-child(3)")
