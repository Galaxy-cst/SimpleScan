# decode hydra results to store in DB
from DBHelper.DB import DBConnect
import json
import re

# def bruteforce_store(name):
name = 'temp.json'
task_id =
with open(name, 'r') as f:
    a = f.read()
    b = json.loads(a)
    remarks = b['results']
    print(remarks)
    ip = remarks[0]['host']
    port = remarks[0]['port']
    result = {'vulns': 'bruteforce', 'remarks': remarks, 'ip': ip, 'port': port, 'task_id': task_id, }
    # with DBConnect() as conn:
    #     conn.insert_vulns_remarks()
    # return result
