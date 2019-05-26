from app.Call.ports import ports


def scanner(ip_list=[None]):
    report_file = ports(ip_list)
    return report_file
