# from Pretreatment import pretreatment
from app.Pretreatment.toips import toips
from app.Pretreatment.toports import toports
from app.Pretreatment.scanner import scanner
from app.Pretreatment.portstoDB import store_data
from app.Pretreatment.addNewTasks import add_tasks


def start(data):
    ip_list = toips(data)
    if 'in Err' in ip_list:
        return False
    report_file = scanner(ip_list)
    store_data(report_file)
    return True


class Pretreatment:
    def __init__(self):
        pass

    def get_ip(self, ip, ip_type):
        return toips(ip, ip_type)

    def get_ports(self, ports):
        return toports(ports)

    def check_ip(self, ip, ip_type):
        if toips(ip, ip_type):
            return True
        else:
            return False

    def check_ports(self, ports):
        if toports(ports):
            return True
        else:
            return False

    def check_all(self, ip, ip_type, ports):
        if toips(ip, ip_type) and toports(ports):
            return True
        else:
            return False

    def add_task(self, ip, ip_type, ports):
        if self.check_all(ip, ip_type, ports):
            ip_list = self.get_ip(ip, ip_type)
            ports_list = self.get_ports(ports)
            add_tasks(ip_list, ports_list)
            return True
        else:
            return False
