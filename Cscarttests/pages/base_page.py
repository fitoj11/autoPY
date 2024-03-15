from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def is_not_element_present(self, driver, how, what, timeout=0): # ждем пока элемент пропадет - пропал - выдаем True
        try:
            WebDriverWait(driver, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False