from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[style='display:inline;float:right']"), text_='100')) # найти элемент, ждем до 12 секунд. Как только значение в элементе (текст) 
    # будет равен 100 - идем дальше
    
    input1 = browser.find_element(By.CSS_SELECTOR, "button[id='book']")
    input1.click()

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

