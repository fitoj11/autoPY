import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
# def test_solve_quiz_and_get_code(browser):
#
