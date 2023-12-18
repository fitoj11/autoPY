from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

welcome_text2 = 1

try: 
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control third']")
    input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.CSS_SELECTOR, "input[class='form-control first'][placeholder='Input your phone:']")
    # input4.send_keys("Russia")
    # input5 = browser.find_element(By.CSS_SELECTOR, "input[class='form-control second'][placeholder='Input your address:']")
    # input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text1 = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text1

    class TestAbs(unittest.TestCase):
        def test_abs1(self):
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text1, "Should be absolute value of a number")

    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control third']")
    input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.CSS_SELECTOR, "input[class='form-control first'][placeholder='Input your phone:']")
    # input4.send_keys("Russia")
    # input5 = browser.find_element(By.CSS_SELECTOR, "input[class='form-control second'][placeholder='Input your address:']")
    # input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text2 = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text2

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    class TestAbs2(unittest.TestCase):
         def test_abs2(self):
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text2, "Should be absolute value of a number")
        
    if __name__ == "__main__":
        unittest.main()
    