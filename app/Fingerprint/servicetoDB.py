# decode service and system info to store in DB
from lib.DBHelper.DB import DBConnect
from bs4 import BeautifulSoup


def store_servicedetail(port_list, task_id, report_file):
    service = ''
    sysinfo = ''
    with open(report_file, 'r')as f:
        soup = BeautifulSoup(f, 'html.parser')
        for link in soup.find_all('service'):
            service = link.get('name')
            del link['name']
            link = soup.service
            link.clear()
            details = str(link)
        for link in soup.find_all('osmatch'):
            sysinfo = link.get('name')
    result = {'service': service, 'sysinfo': sysinfo, 'details': details, 'task_id': task_id, 'port': port_list[1]}
    with DBConnect() as conn:
        conn.insert_serviceandinfo(result)
    return result
