from locust import HttpUser, task, between
import random
import re
class MainFunction(HttpUser):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.wait_time = between(1, 1)
    def get_request(self, endpoint):
        response = self.client.get(f"{self.url}/{endpoint}", headers=self.headers)
        return response
    def post_request(self, endpoint, form_data):
        response = self.client.post(f"{self.url}/{endpoint}", data=form_data, headers=self.headers)
        return response