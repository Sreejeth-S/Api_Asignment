import requests
from utils.config import BASE_URL


#Added all the Request here
class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    def patch(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.patch(url, json=data, headers=headers)
        return response

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
