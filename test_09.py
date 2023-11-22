from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file.txt') 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
