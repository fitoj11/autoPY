from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button0 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button0.click()

    first_window = browser.window_handles[0] # запомнить первую вкладку
    new_window = browser.window_handles[1] # запомнить вторую вкладку
    browser.switch_to.window(new_window) # переключится на вторую вкладку
    
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
