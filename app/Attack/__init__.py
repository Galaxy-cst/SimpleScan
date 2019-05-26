from app.Attack.payloads_lister import payloads_iter
from app.Attack.attacker import attacher


def make_attack(ip, port):
    a = attacher()
    for payload in payloads_iter():
        payload['ip'] = '{}:{}'.format(ip, port)
        print(a.sends(**payload))
