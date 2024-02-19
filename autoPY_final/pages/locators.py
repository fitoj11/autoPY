from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
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
