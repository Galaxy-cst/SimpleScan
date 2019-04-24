# pretreatment input to ip or ip list
from IPy import IP
import dns.resolver
import json

def toips(data):
    input_data=json.loads(data)
    input_type=input_data['type']
    ip=input_data['content']
    if input_type == 'ip':
        ips=[]
        try:
            Ip = IP(ip)
        except KeyboardInterrupt:
            exit(0)
        except:
            return "in Err"
        for x in Ip:
            ips.append(str(x))
        return ips
    elif input_type == 'domain':
        A = dns.resolver.query(ip,'A')   # 指定查看类型为A记录
        domains=[]
        for i in A.response.answer:  # 通过response.answer方法获取查询回应信息
            for j in i.items:        # 遍历回应信息
                domains.append(j.address)
            return domains
