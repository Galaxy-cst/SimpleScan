def toports(ports):
    port_list = []
    if ports == 'all':
        ports = '1-65535'
    try:
        for port in ports.split(','):
            if '-' in port:
                port_num = num_range(port)
            else:
                port_num = [int(port)]
            for i in port_num:
                if 0 < i <= 65535:
                    port_list.append(i)
                else:
                    raise Exception("Invalid Ports")
    except:
        return False
    return port_list


def num_range(ports):
    ports_list = ports.split('-')
    first = int(ports_list[0])
    last = int(ports_list[1]) + 1
    if first - last >= 0:
        raise Exception("Invalid Range")
    return list(range(first, last))
