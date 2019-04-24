# call for masscan and return filepath
from subprocess import Popen
import os
import time


def ports(ip=[None]):
    file_id = time.time()
    ip_list = ','.join(ip)
    masscan_path = os.path.join(os.path.dirname(__file__), 'bin/masscan')
    print(masscan_path)
    p1 = Popen('{} -p80,443 {} --rate=500 -oJ ./scanner_results/{}.ss'.format(masscan_path, ip_list, file_id), shell=True)

    print(p1.communicate())
    return os.path.abspath('./scanner_results/{}.ss'.format(file_id))
