from locust import HttpUser, task, between
import random
import re
class FlowException(Exception):
   pass
class WebsiteTestUser(HttpUser):
    # wait_time = between(0, 0.01)
    def on_start(self): # запускает до старта locust
        global url
        global security_hash
        global headers
        global security_hash_storefront2
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
        response = self.client.get("", headers=headers, name = 'Инициализация. Запрос на получение токена')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        html_content = response.text
        csrf_token = re.search(r'<meta name="csrf-token" content="(.+?)">', html_content).group(1)
        if csrf_token is None or csrf_token == "NoneType":
            raise FlowException('None have object')
        form_data = {
            "_csrf": csrf_token,
            "edition": "ult",
            "type": "online"
        }
        response = self.client.post("", data=form_data, headers=headers, name = 'Инициализация. Создание демо магазина')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        url = response.url
        html_content2 = response.text
        security_hash_storefront2 = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        if security_hash_storefront2 is None or security_hash_storefront2 == "NoneType":
            raise FlowException('None have object')
        response2 = self.client.get(f"{url}admin.php?dispatch=auth.login_form&return_url=admin.php", headers=headers, name = 'Инициализация. Получение security_hash')
        if response2.status_code != 200:
            raise FlowException('Not 200 status code')
        html_content2 = response2.text
        security_hash = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        if security_hash is None or security_hash == "NoneType":
            raise FlowException('None have object')
        form_data = {
            "return_url": "admin.php?dispatch=index.index",
            "user_login": "admin@example.com",
            "password": "admin",
            "dispatch[auth.login]": "Войти",
            "security_hash": security_hash
        }
        print(f"{url}admin.php")
        response = self.client.post(f"{url}admin.php", data=form_data, headers=headers, name = 'Инициализация. Авторизация в админку')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        form_data2 = {
            "full_render": "true",
            "security_hash": security_hash,
            "result_ids": "addons_list, top_bar, header_navbar, header_subnav, addons_counter, elm_developer_pages, elm_all_dev_pages",
            "is_ajax": "1"
        }
        self.client.post(f"{url}admin.php?dispatch=addons.update_status&id=recaptcha&status=D&redirect_url=admin.php%3Fdispatch%3Daddons.manage", data=form_data2, headers=headers, name = 'Инициализация. Рекапча килл')
        pass
    def on_stop(self): # запускается после остановки locust
        pass
    @task(1) # Запросы главной страницы
    def home_page(self):
        response = self.client.get(url, name = 'Главная страница. Запрос главной страницы')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
    @task(2) # Регистрация
    def registration(self):
        response = self.client.get(f"{url}index.php?dispatch=auth.logout", headers=headers, name = 'Регистрация. Выход из аккаунта (перед регистрацией)')  ## logout
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        number = random.randint(0, 100000)
        response2 = self.client.get(f"{url}profiles-add", headers=headers, name = 'Регистрация. Получение security_hash_storefront')
        html_content2 = response2.text
        security_hash_storefront1 = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        if security_hash_storefront1 is None or security_hash_storefront1 == "NoneType":
            raise FlowException('None have object')
        form_data = {
            "ship_to_another": "",
            "user_data[firstname]": f"{number}",
            "user_data[lastname]": "",
            "user_data[phone]": "",
            "user_data[email]": f"test{number}@mail.ru",
            "user_data[password1]": f"test{number}",
            "user_data[password2]": f"test{number}",
            "user_data[birthday]": "",
            "all_mailing_lists[]": "1",
            "dispatch[profiles.update]": "",
            "security_hash": security_hash_storefront1}
        response = self.client.post(url, data=form_data, headers=headers, name = 'Регистрация. Регистрация')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        try:
            html_content2 = response.text # выводит email если залогинены
            account_number = re.search(r'"ty-account-info__item  ty-account-info__name ty-dropdown-box__item">(.*?)</li>', html_content2).group(1)
            if account_number == None or account_number == "NoneType":
                raise FlowException('None have object')
            if int(account_number) == number:
                print("Account name: ", number)
        except:
            raise FlowException('Account not registred')
        pass
    @task(3) # запрос всего каталога
    def catalog(self):
        params = {
              "match": "all",
              "subcats": "Y",
              "pcode_from_q": "Y",
              "pshort": "Y",
              "pfull": "Y",
              "pname": "Y",
              "pkeywords": "Y",
              "search_performed": "Y",
              "hint_q": "Искать товары",
              "dispatch": "products.search",
              "security_hash": f"{security_hash_storefront2}"}
        response = self.client.get(url, headers=headers, params=params, name='Запрос каталога. Запрос всех товаров')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        pass
    @task(4) # Добавить товар в корзину, оформить заказ
    def home_page(self):
        response2 = self.client.get(f"{url}index.php?dispatch=auth.logout", headers=headers, name = 'Оформление заказа. Выход из аккаунта (перед оформлением заказа)')
        if response2.status_code != 200:
            raise FlowException('Not 200 status code')
        html_content2 = response2.text
        security_hash_storefront1 = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        if security_hash_storefront1 is None or security_hash_storefront1 == "NoneType":
            raise FlowException('None have object')
        form_data = {
            "result_ids": "cart_status *, wish_list *, checkout *, account_info *",
            "redirect_url": "index.php?dispatch = products.view & product_id = 278",
            "product_data[278][product_id]": "278",
            "appearance[show_price_values]": "1",
            "appearance[show_price]": "1",
            "appearance[show_list_discount]": "1",
            "appearance[show_product_options]": "1",
            "feature_548": "1195",
            "appearance[details_page]": "1",
            "additional_info[info_type]": "D",
            "additional_info[is_preview]": "",
            "additional_info[get_icon]": "1",
            "additional_info[get_detailed]": "1",
            "additional_info[get_additional]": "",
            "additional_info[get_options]": "1",
            "additional_info[get_discounts]": "1",
            "additional_info[get_features]": "",
            "additional_info[get_extra]": "",
            "additional_info[get_taxed_prices]": "1",
            "additional_info[get_for_one_product]": "1",
            "additional_info[detailed_params]": "1",
            "additional_info[features_display_on]": "C",
            "additional_info[get_active_options]": "",
            "additional_info[get_only_selectable_options]": "",
            "additional_info[get_variation_features_variants]": "1",
            "additional_info[get_variation_info]": "1",
            "additional_info[get_variation_name]": "1",
            "additional_info[get_product_type]": "",
            "appearance[dont_show_points]": "",
            "appearance[show_sku]": "1",
            "appearance[show_product_amount]": "1",
            "appearance[show_qty]": "1",
            "appearance[capture_options_vs_qty]": "",
            "product_data[278][amount]": "1",
            "appearance[show_add_to_cart]": "1",
            "appearance[show_list_buttons]": "1",
            "appearance[but_role]": "big",
            "appearance[quick_view]": "",
            "security_hash": security_hash_storefront1,
            "full_render": "Y",
            "is_ajax": "1",
            "dispatch[checkout.add..278]": ""}
        response = self.client.post(url, data=form_data, headers=headers, name = 'Оформление заказа. Добавить товар в корзину')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        number = random.randint(0, 100000)
        form_data = {
            "ship_to_another": "1",
            "additional_result_ids[]": "litecheckout_final_section, litecheckout_step_payment, checkout *",
            "shipping_ids[0]": "6",
            "user_data[s_address]": f"test{number}",
            "user_data[s_zipcode]": "101000",
            "user_data[fullname]": "",
            "user_data[phone]": "",
            "user_data[email]": f"test{number}@test.test",
            "selected_payment_method": "18",
            "payment_id": "18",
            "result_ids": "",
            "dispatch": "checkout.place_order",
            "customer_notes": "",
            "payment_id": "18",
            "payment_info[address]": "",
            "payment_info[zip_postal_code]": "",
            "payment_info[phone]": "",
            "payment_info[organization_customer]": "",
            "payment_info[inn_customer]": "",
            "payment_info[bank_details]": "",
            "ship_to_another": "0",
            "user_data[ship_to_another]": "0",
            "accept_terms": "N",
            "accept_terms": "Y",
            "all_mailing_lists[]": "1",
            "update_steps": "1",
            "security_hash": security_hash_storefront1
        }
        response = self.client.post(url, data=form_data, headers=headers, name = 'Оформление заказа. Оформить заказ')
        if response.status_code != 200:
            raise FlowException('Not 200 status code')
        html_content2 = response.text
        try:
            order_id_match = re.search(r'dispatch=checkout.complete&amp;([^"]+)"', html_content2)
            if order_id_match is None:
                raise FlowException('None have object')

            order_id = order_id_match.group(1)
            if order_id == "NoneType":
                raise FlowException('Order not success')
        except FlowException as e:
            raise e
        except Exception as ex:
            raise FlowException('Unexpected error occurred: {}'.format(ex))
        print("Order, account name: ", number)
        print(order_id)
        pass