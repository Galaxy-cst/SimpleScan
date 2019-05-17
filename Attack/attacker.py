import requests
from requests import Request


class attacher():
    def __init__(self):
        self.s = requests.Session()

    def send(self, url, params=None, method="GET", data=None, header=None):
        req = Request(method=method, url=url, params=params, data=data, headers=header)
        prepped = self.s.prepare_request(req)
        resp = self.s.send(prepped)
        return resp

    def sends(self, ip, urls, params=None, method="GET", data=None, header=None, name=None):
        results = []
        for url in urls:
            url = "http://{}/{}".format(ip, url)
            try:
                results.append(self.send(url, params, method, data, header))
            except:
                pass
        return results
