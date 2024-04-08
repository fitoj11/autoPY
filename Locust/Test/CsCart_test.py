from locust import HttpUser, task, between
import random
import re
# from function import MainFunction
class WebsiteTestUser(HttpUser):
    def on_start(self):
        global url
        url = 'https://dev.demo.cs-cart.ru/stores/924c539f0eb37b1d/'
        pass
    def on_stop(self):

        pass
    def get_request(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
        response = self.client.get(url, headers=headers)
        return response
    @task(1)
    def home_page(self):
        response = self.get_request(f"{url}/123")
        print(response.text)