from selenium.webdriver.common.by import By
from selenium import webdriver
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    add_to_card = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
class LoginPageLocators():
    LOGIN_LINK_LOGINPAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REG_FORM = (By.CSS_SELECTOR, "#register_form")
