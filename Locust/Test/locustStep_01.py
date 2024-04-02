from locust import HttpUser, task, between
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
    # @task(1)
    # def test_home_page(self):
    #     response = self.client.get("")
    #     next_url = response.headers.get("Location")
    #     if next_url:
    #         self.client.get(next_url)
    #         print(next_url)
    #     print(next_url)
        # self.client.post("/login", {"имя пользователя": "admin", "пароль": "admin"}) # post запрос
    @task(2)
    def hello_world(self):
        self.client.get("reward-points/")
    # @task(3)
    # def index(self):
    #     self.client.get("http://localhost:5000/index")