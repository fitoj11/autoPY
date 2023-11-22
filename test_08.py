from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)
    
    input0 = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input0) # скролл страницы до элемента, при "true" элемент в начале страницы
    # browser.execute_script("window.scrollBy(0, 100);") # скролл на 100 пикселей

    input1 = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
