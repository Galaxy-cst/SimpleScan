import requests
from requests import Request, Session


class attacher():
    def __init__(self):
        self.s = requests.Session()

    def send(self, url, params=None, method="GET", data=None, header=None):
        req = Request(method=method, url=url, params=params, data=data)
        prepped = self.s.prepare_request(req)
        resp = self.s.send(prepped, header=header)
        return resp

    def sends(self, urls, params=None, method="GET", data=None, header=None, name=None):
        results = []
        for url in urls:
            results.append(self.send(url, params, method, data, header))
        return results
