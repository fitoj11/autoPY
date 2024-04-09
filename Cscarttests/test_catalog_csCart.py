from .pages.catalog_page import CatalogPage
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