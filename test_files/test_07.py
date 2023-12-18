from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# def calc(b):
#   return str(int(y)+int(x))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='num1']")
    x = x_element.text

    y_element = browser.find_element(By.CSS_SELECTOR, "span[id='num2']")
    y = y_element.text

    c = str(int(y)+int(x))
    print(c)


    input1 = browser.find_element(By.CSS_SELECTOR, "select[id='dropdown']")
    input1.click()

    input2 = browser.find_element(By.CSS_SELECTOR, "option[value='" + c + "']")
    input2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()