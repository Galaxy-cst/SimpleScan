import requests
from bs4 import BeautifulSoup
def find_all_links():
    links=[]
    r = requests.get('https://www.baidu.com')
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('a'):
        links.append(link.get('href'))
        # print(link.get('href'))
    print(links)

def find_all_forms():
    forms=[]
    r = requests.get('https://www.gltlab.cn')
    soup = BeautifulSoup(r.text)
    for form in soup.find_all('form'):
        action = form.action
        method = form.method
        if hasattr(form, 'method'):
            forms.append([action,method])
        else:
            form.append([action])
    print(forms)
# find_all_links()
find_all_forms()

