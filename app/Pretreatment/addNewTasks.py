from lib.DBHelper import DBConnect
import json


def add_tasks(ip_list, ports_list):
    with DBConnect() as conn:
        payloads = []
        for ip in ip_list:
            payloads.append(
                {'ip': ip, 'current_task': 'SCAN_STATUS_PORTSCAN', 'config': json.dumps({'ports': ports_list})})
        conn.insert_ip_port(payloads)
