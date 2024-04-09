from .base_page import BasePage
from .product_page import *
from selenium.webdriver.common.by import By
from .locators import CsCartCatalogLocators
class CatalogPage(BasePage):
    def go_to_catalog(self):
        link = self.browser.find_element(*CsCartCatalogLocators.CATALOG_LINK)
        link.click()
    def should_be_catalog(self):
        url = self.browser.current_url
        assert 'dispatch=products.search' in url, "'dispatch=products.search' not in URL"
    def should_be_all_same_products_in_displays(self):
        name1 = ProductDisplayType1(self.browser).go_to_display_type1_and_get_products()
        name2 = ProductDisplayType2(self.browser).go_to_display_type2_and_get_products()
        name3 = ProductDisplayType3(self.browser).go_to_display_type3_and_get_products()
        assert name1 == name2, "product default display type not equal 2 type"
        assert name1 == name3, "product default display type not equal 3 type"
        assert name2 == name3, "product 2 display type not equal 3 type"
    def
class ProductDisplayType1(BasePage):
    def __init__(self, browser):
        self.browser = browser
    def found_products_default_display_type(self):
        elements = self.browser.find_elements(*CsCartCatalogLocators.find_products)
        names = []
        for element in elements:
            name_value = element.get_attribute("title")
            if name_value:
                names.append(name_value)
        return names
    def display_type1(self):
        link = self.browser.find_element(*CsCartCatalogLocators.display_type1)
        link.click()
        ProductPage.loader_wait(self)
    def go_to_display_type1_and_get_products(self):
        self.display_type1()
        names = self.found_products_default_display_type()
        return names
class ProductDisplayType2(BasePage):
    def __init__(self, browser):
        self.browser = browser
    def found_products_2_display_type(self):
        elements = self.browser.find_elements(*CsCartCatalogLocators.find_products_type2)
        names = []
        for element in elements:
            name_value = element.get_attribute("title")
            if name_value:
                names.append(name_value)
        return names
    def display_type2(self):
        link = self.browser.find_element(*CsCartCatalogLocators.display_type2)
        link.click()
        ProductPage.loader_wait(self)
    def go_to_display_type2_and_get_products(self):
        self.display_type2()
        names = self.found_products_2_display_type()
        return names
class ProductDisplayType3(BasePage):
    def __init__(self, browser):
        self.browser = browser
    def found_products_3_display_type(self):
        elements = self.browser.find_elements(*CsCartCatalogLocators.find_products_type3)
        names = []
        for element in elements:
            name_value = element.get_attribute("title")
            if name_value:
                names.append(name_value)
        return names
    def display_type3(self):
        link = self.browser.find_element(*CsCartCatalogLocators.display_type3)
        link.click()
        ProductPage.loader_wait(self)
    def go_to_display_type3_and_get_products(self):
        self.display_type3()
        names = self.found_products_3_display_type()
        return names