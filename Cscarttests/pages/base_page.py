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
    def open_second_tab(self):
        self.browser.execute_script("window.open('https://dev.demo.cs-cart.ru/admin.php')")
        self.tabs(1)
    def tabs(self, tab_number): # создает массив и нумерует вкладки, в функции надо указать "self, номер вкладки"
        link = self.browser.window_handles
        self.browser.switch_to.window(link[tab_number])
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    def is_not_element_present(self, driver, how, what, timeout=0): # ждем пока элемент пропадет - пропал - выдаем True
        self.browser.implicitly_wait(0)
        try:
            WebDriverWait(driver, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def is_element_present_zero_time(self, how, what): # если элемента нет в моменте, то сразу отдаем ошибку, время не ждем
        self.browser.implicitly_wait(0) # переопредели время ожидания от класса на 0
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True