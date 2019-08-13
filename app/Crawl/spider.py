import requests
from bs4 import BeautifulSoup


def find_all_links():
    links = []
    r = requests.get('https://www.baidu.com')
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links


def find_all_forms():
    forms = []
    r = requests.get('https://www.gltlab.cn')
    soup = BeautifulSoup(r.text, "html.parser")
    for form in soup.find_all('form'):
        action = form.action
        if hasattr(form, 'method'):
            forms.append([form.get('action'), form.get('method')])
        else:
            forms.append([action])
    return forms
