import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://reqres.in"
    
    def post(self, endpoint, data):
        return requests.post(f"{self.base_url}{endpoint}", json=data)

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}")

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}")