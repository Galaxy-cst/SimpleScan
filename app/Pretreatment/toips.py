# pretreatment input to ip or ip list
from IPy import IP
import dns.resolver


def toips(ip, ip_type):
    if ip_type == 'ip':
        ips = []
        try:
            Ip = IP(ip)
        except KeyboardInterrupt:
            exit(0)
        except:
            return False
        for x in Ip:
            ips.append(str(x))
        return ips
    elif ip_type == 'domain':
        try:
            A = dns.resolver.query(ip, 'A')  # 指定查看类型为A记录
            domains = []
            for i in A.response.answer:  # 通过response.answer方法获取查询回应信息
                for j in i.items:  # 遍历回应信息
                    domains.append(j.address)
                return domains
        except:
            return False
