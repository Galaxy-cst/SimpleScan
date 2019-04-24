# call for nmap to get service and system info
from subprocess import Popen
import os


def service_detail(port_list, task_id):
    ip = port_list[0]
    port = port_list[1]
    p = Popen('nmap {} -p{} -A -oX ./scanner_results/{}.xml'.format(ip, port, task_id), shell=True)

    print(p.communicate())
    return os.path.abspath('./scanner_results/{}.xml'.format(task_id))
