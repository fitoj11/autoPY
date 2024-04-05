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
        response2 = self.client.get(f"{url}admin.php?dispatch=auth.login_form&return_url=admin.php", headers=headers)
        html_content2 = response2.text
        security_hash = re.search(r'name="security_hash" class="cm-no-hide-input" value="([^"]+)"', html_content2).group(1)
        # print(security_hash)
        form_data = {
            "return_url": "admin.php?dispatch=index.index",
            "user_login": "admin@example.com",
            "password": "admin",
            "dispatch[auth.login]": "Войти",
            "security_hash": security_hash
        }
        # print(f"{url}admin.php")
        form_data2 = {
            "full_render": "true",
            "security_hash": security_hash,
            "result_ids": "addons_list, top_bar, header_navbar, header_subnav, addons_counter, elm_developer_pages, elm_all_dev_pages",
            "is_ajax": "1"
        }
        self.client.post(f"{url}admin.php?dispatch=addons.update_status&id=recaptcha&status=D&redirect_url=admin.php%3Fdispatch%3Daddons.manage", data=form_data2, headers=headers)
        # print(f"{url}admin.php?dispatch=addons.update_status&id=recaptcha&status=D&redirect_url=admin.php%3Fdispatch%3Daddons.manage")

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
        number = random.randint(0, 100)
        form_data = {
            "ship_to_another": "",
            "user_data[firstname]": "",
            "user_data[lastname]": "",
            "user_data[phone]": "",
            "user_data[email]": f"test{ number }@mail.ru",
            "user_data[password1]": f"test{ number }",
            "user_data[password2]": f"test{ number }",
            "user_data[birthday]": "",
            "all_mailing_lists[]": "1",
            "dispatch[profiles.update]": "",
            "security_hash": "8b2913d8094a15a693a50efb5c82c279"
        }
        self.client.post(url, data=form_data)

    # @task(3) # Запрос каталога товаров
    # def home_page(self):
    #     self.client.get(url)
    # @task(4) # Оформить заказ
    # def home_page(self):
    #     self.client.get(url)