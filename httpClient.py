import http.client
import urllib.parse

class HttpClient():
    def __init__(self, base_url):
        self.base_url = base_url
        self.conn = http.client.HTTPSConnection(base_url)

    def fetch(self, path):
        self.conn.request("GET", path or "/")
        response = self.conn.getresponse()
        if response.status != 200:
            raise Exception(f"Fail: {response.status}")
        content = response.read()
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            return content.decode('ISO-8859-1')
