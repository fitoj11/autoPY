from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.support.ui import WebDriverWait
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    add_to_card = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    correct_name = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main']>h1")
    correct_value = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main']>p")
    correct_name_01 = (By.CSS_SELECTOR, "div[class='alertinner ']>strong")
    correct_value_01 = (By.CSS_SELECTOR, "div[class='alertinner ']>p>strong")
class LoginPageLocators():
    LOGIN_LINK_LOGINPAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REG_FORM = (By.CSS_SELECTOR, "#register_form")
class CsCartLocators():
    LC = (By.CSS_SELECTOR, "a[class='ty-account-info__title']")
    PRODUCT_LINK = (By.CSS_SELECTOR, "div[class='ty-grid-list__image']>a>img")
    Add_to_cart_button = (By.CSS_SELECTOR, "div>div>button[class='ty-btn__primary ty-btn__big ty-btn__add-to-cart cm-form-dialog-closer ty-btn']")
    ADD_NOTIFICATION = (By.CSS_SELECTOR, "div[class='cm-notification-content cm-notification-content-extended notification-content-extended  cm-auto-hide'")
    cart_button = (By.CSS_SELECTOR, "span[class='ty-icon ty-icon-moon-commerce ty-minicart__icon filled']")
    cart_name = (By.CSS_SELECTOR, "h1[class='ty-mainbox-title']")
    cart_popup_button = (By.CSS_SELECTOR, "div[class='ty-float-left']")
    close = (By.CSS_SELECTOR, "span[class='cm-notification-close close']")
    quantity = (By.CSS_SELECTOR, "div[class='ty-product-notification__price']>span:nth-child(1)")
    price_product = (By.CSS_SELECTOR, "div[class='ty-product-block__price-actual']>span>span>span:nth-child(1)")
    quantity_cart = (By.CSS_SELECTOR, "td>span[class='price']:nth-child(1)")
    quantity_cart2 = (By.CSS_SELECTOR, "td>span[class='ty-sub-price']:nth-child(1)")
    price_cart = (By.CSS_SELECTOR, "p>span[id]")
    CHECKOUT_LINK = (By.CSS_SELECTOR, "div[class='ty-float-right ty-cart-content__right-buttons']>a[class='ty-btn ty-btn__primary ']")
    checkout_price = (By.CSS_SELECTOR, "div[class='ty-order-products__price']>span:nth-child(3)")
    checkout_quantity = (By.CSS_SELECTOR, "div[class='ty-order-products__price']>span:nth-child(1)")
    required_inputs = (By.CSS_SELECTOR, "div[class*='field--input']:has(>label[class*='required']) input")
    shipping = (By.CSS_SELECTOR, "[class*='pickup--map-list']")
    shipping_block = (By.CSS_SELECTOR, "div[data-ca-shipping*='pickup_offices']>div[class*='--list']>label:nth-child(2)")
    shipping_block_click = (By.CSS_SELECTOR, "[class='litecheckout__group litecheckout__step']")
    # loader = (By.CSS_SELECTOR , "div[data-ca-shipping*='pickup_offices']>div[class*='--list']>label:nth-child(2)")
    loader = (By.CSS_SELECTOR, "div[id='ajax_overlay'][style='display: block;']")
    payment_link = (By.CSS_SELECTOR, "[data-ca-toggling='payments_form_wrapper_18']")
    required_terms = (By.CSS_SELECTOR, "[id*='id_accept_terms']")
    place_order_button = (By.CSS_SELECTOR, "[name='dispatch[checkout.place_order]']")
    admin_entry = (By.CSS_SELECTOR, "[name='dispatch[auth.login]']")
    moduls_entry = (By.CSS_SELECTOR, "[href*='addons.manage'][class*='icon']")
    found_recaptcha = (By.CSS_SELECTOR, "tr[id*='recaptcha']")
    # off_recaptcha = (By.CSS_SELECTOR, "tr[id*='recaptcha']")
    found_recaptcha_tool = (By.CSS_SELECTOR, "tr[id*='recaptcha']>td[class*='nowrap']>div>[class*='tools']")
    off_recaptcha = (By.CSS_SELECTOR, "tr[id*='recaptcha']>td[class*='nowrap']>div>[class*='tools']>div>ul>li>[class*='render']")
    captcha = (By.CSS_SELECTOR, "div[id*='captcha']")
    order_succes_link = (By.CSS_SELECTOR, "div[class='ty-checkout-complete__order-success']>p>a[href*='order_id=']")
    "https://dev.demo.cs-cart.ru/admin.php"
    "div>label[class*='required']"
    "div[class*='field--input']>label[class*='required']"
    "div[class*='field--input']:has(>label[class*='required'])" # оператор :has() выбирает родительский элемент по характеристикам дочернего.
    "div[class*='field--input']:has(>label[class*='required']) input" # находим родителя, потом смещаемся на дочерний элемент "input"
class CsCartCatalogLocators():
    CATALOG_LINK = (By.CSS_SELECTOR, "button[class='ty-search-magnifier']")
    find_products = (By.CSS_SELECTOR, "bdi>a")
    display_type1 = (By.CSS_SELECTOR, "div[class='ty-sort-container__views-icons']>a:nth-child(1)")
    display_type2 = (By.CSS_SELECTOR, "div[class='ty-sort-container__views-icons']>a:nth-child(2)")
    display_type3 = (By.CSS_SELECTOR, "div[class='ty-sort-container__views-icons']>a:nth-child(3)")
    lower_price = (By.CSS_SELECTOR, "[class='sort-by-price-asc ty-sort-dropdown__content-item']")
    high_price = (By.CSS_SELECTOR, "[class='sort-by-price-desc ty-sort-dropdown__content-item']")
    find_products_price = (By.CSS_SELECTOR, "[class='ty-price']>span:nth-child(1)")
    find_sort_dropbox = (By.CSS_SELECTOR, "[id='sw_elm_sort_fields']")