# decode ip file to store in DB
import json
import time
from DBHelper.DB import DBConnect


def store_data(name):
    ip_list = []
    task_id = time.time()
    with open(name, 'r')as f:
        a = json.load(f)
        for i in a:
            ip = i['ip']
            port = i['ports'][0]['port']
            ip_list.append({'ip': ip, 'port': port, 'task_id': task_id})
    with DBConnect() as conn:
        conn.write_ip_port(ip_list)
    return True
