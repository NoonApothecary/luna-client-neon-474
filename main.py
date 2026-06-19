import requests
import json

class LunarClient:
    def __init__(self, base_url='https://api.luna.com'):
        self.base_url = base_url
        self.session = requests.Session()

    def get_lunar_data(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def post_lunar_data(self, endpoint, data):
        url = f'{self.base_url}/{endpoint}'
        response = self.session.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None

if __name__ == '__main__':
    client = LunarClient()
    print(client.get_lunar_data('info'))
    data = {'key': 'value'}
    print(client.post_lunar_data('data', data))