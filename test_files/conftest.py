import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By # не влияет на запускаемые тесты, в каждом необходимо импортировать отдельно

# @pytest.fixture(scope="function") # создали общую функцию для запуска браузера
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', 
                     help="Choose browser: chrome or firefox") # описываем аргумент, если оставим default=none - то при не заполнении аргумента browser_name будет падать с ошибкой


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome": # условие и значение переменной для браузера в запросе "pytest -s -v --browser_name=firefox test_fixture8.py"
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox") # обработчик, если значение будет иным
    yield browser
    print("\nquit browser..")
    browser.quit()