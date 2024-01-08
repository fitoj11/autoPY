import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# answer = math.log(int(time.time()))
# print(answer)
login = "" # ваш логин
password = "" # ваш пароль
text_values = []
link = "https://stepik.org/lesson/236895/step/1"

@pytest.mark.parametrize('links', ["236895", "236896","236897", "236898", "236899","236903","236904", "236905"])
def test_login(browser, links):
    global text1
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)

    wait = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']"))
    ) # presence_of_element_located - нахождение на странице + надо дополнительно импорнуть. Ждем загрузки элемента до 10с


    button0 = browser.find_element(By.CSS_SELECTOR, "a[class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']")
    button0.click() # переходим в попапе на страницу логина
    time.sleep(2)
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
    input3.send_keys(login)    
    time.sleep(2)
    input4 = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    input4.send_keys(password)
    time.sleep(2)
    button3 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button3.click()
    try:
        time.sleep(2)
        wait = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']"))
        )    
        answer = math.log(int(time.time()))
        input1 = browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']")
        input1.send_keys(answer)
        time.sleep(1)
        button1 = WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='submit-submission']"))
        )
        button1.click()  
        time.sleep(2)
    except:
        pass    
    time.sleep(3) # отладка
    wait = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p[class='smart-hints__hint']"))
    )
    time.sleep(2)
    input2 = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']")
    text = ""
    # correct = input2.text
    # input2.text == "Correct!"

    text_values.append(text + input2.text) if input2.text != "Correct!" else text_values

def test_cleanup():
    global text_values
    print("\nОбщий текст:")
    print("\n".join(text_values))