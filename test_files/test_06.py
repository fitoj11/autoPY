from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img[id='treasure']")
    x = x_element.get_attribute("valuex") # берет значение из "valuex"
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()