from app import *

# from Fingerprint import get_fingerprint

# ip_list = Pretreatment.start('{"type":"ip","content":"120.79.214.167"}')
# print(ip_list)

# store_servicedetail

# ilist = ({'ip': '121.121.121.121', 'port': 80}, {'ip': '121.121.121.121', 'port': 443})


# task_id = '1555663034.6932669'
# port_list = ['120.79.214.167', 80]
# get_fingerprint(port_list, task_id)
from Attack import make_attack

make_attack('127.0.0.1', 80)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
