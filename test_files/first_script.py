import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options # окно браузера не закрывается, после завершения скрипта
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)

time.sleep(2)

driver.get("https://google.com")
time.sleep(2)

textarea = driver.find_element(By.CSS_SELECTOR, "textarea")

textarea.send_keys("0000")
time.sleep(2)

submit_button = driver.find_element(By.CLASS_NAME, "gNO89b")

submit_button.click()
time.sleep(5)

submit_button1 = driver.find_element(By.CLASS_NAME, "MjjYud")

submit_button1.click()

time.sleep(3)

submit_button2 = driver.find_element(By.CSS_SELECTOR, "img[alt='Кинопоиск']")

submit_button2.click()

submit_button3 = driver.find_element(By.CSS_SELECTOR, "a[data-tid='de7c6530']")
time.sleep(3)
submit_button3.click()

time.sleep(5)
browser.quit()