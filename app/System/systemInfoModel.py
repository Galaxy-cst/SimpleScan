from time import sleep
from threading import Timer
from os import listdir
from os.path import join as fjoin
import socket
import requests
import json
import psutil


class SystemInfo:
    def __init__(self):
        self.pps = {'rx_pps': 0, 'tx_pps': 0}
        self.intranet_ip = self.get_intranet_ip()
        self.extranet_ip = self.get_extranet_ip()
        self.pps_timer_starter()

    def pps_timer_starter(self):
        pps_timer = Timer(0, self.pps_calculator)
        pps_timer.start()

    def get_pps_file_path(self):
        basepath = '/sys/class/net'
        for flist in listdir(basepath):
            if flist[0] == 'e':
                return fjoin(basepath, flist, 'statistics')

    def pps_calculator(self):
        pps_file_path = self.get_pps_file_path()
        with open(fjoin(pps_file_path, 'rx_packets')) as f:
            rx_origin = int(f.read())
        with open(fjoin(pps_file_path, 'tx_packets')) as f:
            tx_origin = int(f.read())
        sleep(5)
        with open(fjoin(pps_file_path, 'rx_packets')) as f:
            rx_now = int(f.read())
        with open(fjoin(pps_file_path, 'tx_packets')) as f:
            tx_now = int(f.read())
        rx_pps = (rx_now - rx_origin) / 5
        tx_pps = (tx_now - tx_origin) / 5
        self.pps = {'rx_pps': rx_pps, 'tx_pps': tx_pps}
        self.pps_timer_starter()

    def get_intranet_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('1.1.1.1', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def get_extranet_ip(self):
        r = requests.get('https://httpbin.org/ip')
        return json.loads(r.text)['origin'].split(',')[0]

    def get_cpu_rate(self):
        return psutil.cpu_percent()

    def get_mem_rate(self):
        return psutil.virtual_memory().percent


system_info = SystemInfo()
