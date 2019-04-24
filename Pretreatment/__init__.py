# from Pretreatment import pretreatment
from Pretreatment.toips import toips
from Pretreatment.scanner import scanner
from Pretreatment.portstoDB import store_data


def start(data):
    ip_list = toips(data)
    if 'in Err' in ip_list:
        return False
    report_file = scanner(ip_list)
    store_data(report_file)
    return True
