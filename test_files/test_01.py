import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link1 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link1.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='last_name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname'][class='form-control city']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname'][id='country']")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()