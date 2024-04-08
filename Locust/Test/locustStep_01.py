from locust import HttpUser, task, between
import random
import re
class WebsiteTestUser(HttpUser):
    wait_time = between(1, 1)
    def on_start(self): # запускает до старта locust
        # response = self.client.post("", {"_csrf": "fOKf7GAaekjslZ2_fbMfakKaDHpEg3Y2GIqk3TuKxPQLz-iDGHdDHJ7X-MYN63hbDM9OES_ANA9fxP2IC9uIuQ==", "edition": "ult", "type": "online"})
        # next_url = response.headers.get("Content-Type")
        # if next_url:
        #     self.client.get(next_url)
        #     print(next_url)
        # print(next_url)
        # response = self.client.get("")
        # headers = response.headers
        # for key, value in headers.items():
        #     print(f"{key}: {value}")
        # response = self.client.get("")
        # csrf_token = response.text.find('meta[name="csrf-token"]', first=True).attrs.get("content")
        # self.client.post("/", data={"_csrf": csrf_token, "edition": "ult", "type": "online"})

        global url
        global security_hash
        global headers
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
        response = self.client.get("", headers=headers)
        html_content = response.text
        csrf_token = re.search(r'<meta name="csrf-token" content="(.+?)">', html_content).group(1)
        form_data = {
            "_csrf": csrf_token,
            "edition": "ult",
            "type": "online"
        }
        response = self.client.post("", data=form_data, headers=headers)
        print(response.url)
        url = response.url
        # response2 = self.client.get("", headers=headers)
        # html_content2 = response2.text
        # security_hash_storefront = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"',html_content2).group(1)
        # print(security_hash_storefront)
        response2 = self.client.get(f"{url}admin.php?dispatch=auth.login_form&return_url=admin.php", headers=headers)
        html_content2 = response2.text
        security_hash = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        print(security_hash)
        form_data = {
            "return_url": "admin.php?dispatch=index.index",
            "user_login": "admin@example.com",
            "password": "admin",
            "dispatch[auth.login]": "Войти",
            "security_hash": security_hash
        }
        print(f"{url}admin.php")
        self.client.post(f"{url}admin.php", data=form_data, headers=headers)
        # response_test = self.client.post(f"{url}admin.php", data=form_data, headers=headers)
        # print(response_test.text)
        form_data2 = {
            "full_render": "true",
            "security_hash": security_hash,
            "result_ids": "addons_list, top_bar, header_navbar, header_subnav, addons_counter, elm_developer_pages, elm_all_dev_pages",
            "is_ajax": "1"
        }
        self.client.post(f"{url}admin.php?dispatch=addons.update_status&id=recaptcha&status=D&redirect_url=admin.php%3Fdispatch%3Daddons.manage", data=form_data2, headers=headers)
        print(f"{url}admin.php?dispatch=addons.update_status&id=recaptcha&status=D&redirect_url=admin.php%3Fdispatch%3Daddons.manage")

        # Необходимо добавить User-Agent с реального запроса, тогда get запрос будет удачным. Также, необходимо обработать
        # JavaScript из тела ответа. Так создается демка и мы сможем получить ID демки.
        #
        # response = self.client.get("", headers=headers)
        # cookie_header = response.headers.get("Set-Cookie")
        # if cookie_header:
        #     csrf = cookie_header.split(";")[0]
        #     print(csrf)
        # html_content = response.text
        # csrf_token = re.search(r'<meta name="csrf-token" content="(.+?)">', html_content).group(1)
        # print(csrf_token)
        # # self.client.post("", {"_csrf": csrf_token, "edition": "ult", "type": "online"})
        # self.client.post("", data={"_csrf": csrf_token, "edition": "ult", "type": "online"}, headers=headers)

        # headers = response.headers
        # for key, value in headers.items():
        #     print(f"{key}: {value}")
        # print(self.client.post("", {"_csrf": csrf_token, "edition": "ult", "type": "online"}).request.body)
        # for key, value in body.items():
        #     print(f"{key}: {value}")
        pass
    def on_stop(self): # запускается после остановки locust

        pass
    @task(1) # Запросы главной страницы
    def home_page(self):
        self.client.get(url)
    @task(2) # Регистрация
    def registration(self):
        # response_test = self.client.get(f"{url}index.php?dispatch=auth.logout") ## logout
        self.client.get(f"{url}index.php?dispatch=auth.logout", headers=headers)  ## logout
        # print(response_test.url, 1)
        # response_test2 = self.client.get(url)
        self.client.get(url)
        # print(response_test2.url, 1.1)
        number = random.randint(0, 100)
        response2 = self.client.get(f"{url}profiles-add", headers=headers)
        # print(response2.url, 2)
        html_content2 = response2.text
        security_hash_storefront1 = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        # print(security_hash_storefront1)
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
            "security_hash": security_hash_storefront1
        }
        response = self.client.post(url, data=form_data, headers=headers)
        # url_test = response.url

        # self.client.post(url, data=form_data, headers=headers)

        try:
            html_content2 = response.text # выводит email если залогинены
            # test = re.search(r'"ty-account-info__item ty-dropdown-box__item ty-account-info__name">(.*?)</li>', html_content2)
            test = re.search(r'"ty-account-info__item  ty-account-info__name ty-dropdown-box__item">(.*?)</li>', html_content2).group(1)
            print(test)
        except:
            print("none")
        #
        # print(url_test, 3)
        print("random number: ", number)
    # @task(3)
    # def registration_test(self):
    #     number = random.randint(0, 100)
    #     response2 = self.client.get(f"{url}profiles-add", headers=headers)
    #     html_content2 = response2.text
    #     security_hash_storefront1 = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"',
    #                                           html_content2).group(1)
    #     # print(security_hash_storefront1)
    #     form_data = {
    #         "ship_to_another": "",
    #         "user_data[firstname]": "",
    #         "user_data[lastname]": "",
    #         "user_data[phone]": "",
    #         "user_data[email]": f"test{number}@mail.ru",
    #         "user_data[password1]": f"test{number}",
    #         "user_data[password2]": f"test{number}",
    #         "user_data[birthday]": "",
    #         "all_mailing_lists[]": "1",
    #         "dispatch[profiles.update]": "",
    #         "security_hash": security_hash_storefront1
    #     }
    #     response = self.client.post(url, data=form_data, headers=headers)
    #     url_test = response.url
    #     print(url_test, 2)
    #     print(number)

    # @task(3) # Запрос каталога товаров
    # def home_page(self):
    #     self.client.get(url)
    # @task(4) # Оформить заказ
    # def home_page(self):
    #     self.client.get(url)