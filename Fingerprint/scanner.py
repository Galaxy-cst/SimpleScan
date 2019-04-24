from call.service_detail import service_detail


def scanner(port_list, task_id):
    report_file = service_detail(port_list, task_id)
    return report_file
