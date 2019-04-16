import Pretreatment.toips
import Fingerprint
from DBHelper.DB import DBConnect

print(Pretreatment.start('{"type":"ip","content":"192.168.0.1/30"}'))
# print(Fingerprint.start('12.11.1.4,ip'))
ilist = ({'ip': '121.121.121.121', 'port': 80}, {'ip': '121.121.121.121', 'port': 443})
# with DBConnect() as conn:
#     ip_list = conn.write_ip_port(ilist)
with DBConnect() as conn:
    ip_list = conn.read_all_ip_port()
print(ip_list)
