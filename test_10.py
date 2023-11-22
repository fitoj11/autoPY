from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button0 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button0.click()

    prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    prompt.accept()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)

    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[class='form-control']")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
