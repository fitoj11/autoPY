from .pages.catalog_page import *
import time
link = "https://dev.demo.cs-cart.ru/"
def test_should_be_in_catalog(browser): # с главной в каталог, проверка, что в каталоге
    page = CatalogPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.should_be_catalog()
def test_remember_products_switch_display_type(browser): # в каталоге, товары на разных сортировках одинаковые, сортировки работают
    page = CatalogPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.should_be_all_same_products_in_displays()
def test_switch_sort_low(browser): # в каталог, сортировка по низкой цене, товары отсортированы
    page = CatalogPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.sort_lower_price()
    page.should_be_sort_is_lower()
def test_switch_sort_high(browser): # в каталог, сортировка по высокой цене, товары отсортированы
    page = CatalogPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.sort_high_price()
    page.should_be_sort_is_high()
def test_switch_pagination_steps(browser): # изменение количества отображаемых элементов на странице
    page = CatalogPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.found_products_default_display_type()
