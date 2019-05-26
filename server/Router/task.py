from flask import Blueprint, request, jsonify, Response
from app.Pretreatment import Pretreatment
from lib.DBHelper import DBConnect

task_api = Blueprint('task_api', __name__)
pretreatment = Pretreatment()


def get_task_list(limit, current_page, offset):
    with DBConnect() as conn:
        payload = {'limit': limit, 'offset': offset}
        task_list = conn.select_task_list(payload)
        total = conn.select_task_count()
    return {'list': task_list, 'pagination': {
        'total': total,
        'pageSize': limit,
        'current': current_page
    }}


def get_task_detail(taskid):
    with DBConnect() as conn:
        payload = {'taskid': taskid}
        detail = conn.select_task_detail(payload)
        detail_vuln = conn.select_task_detail_vuln(payload)
    return {**detail, 'vuln': detail_vuln, 'taskid': taskid}


def get_task_detail_services(taskid):
    with DBConnect() as conn:
        payload = {'taskid': taskid}
        detail = conn.select_task_services(payload)
    return detail


def get_task_detail_vulnerabilities(taskid):
    with DBConnect() as conn:
        payload = {'taskid': taskid}
        detail = conn.select_task_vulnerabilities(payload)
    return detail


@task_api.route('/api/task/pre_check', methods=['POST'])
def pre_check():
    ip = request.json['ip']
    ports = request.json['ports']
    ip_type = request.json['type']
    ip_check = pretreatment.check_ip(ip, ip_type)
    ports_check = pretreatment.check_ports(ports)
    if ip_check and ports_check:
        return jsonify({'status': 'ok'})
    elif not ip_check:
        return jsonify({'status': 'error', 'description': 'IP格式错误' if ip_type == 'ip' else '域名格式错误'})
    elif not ports_check:
        return jsonify({'status': 'error', 'description': '端口格式错误'})


@task_api.route('/api/task/add', methods=['POST'])
def add():
    ip = request.json['ip']
    ports = request.json['ports']
    ip_type = request.json['type']
    if pretreatment.add_task(ip, ip_type, ports):
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error', 'description': '格式错误'})


@task_api.route('/api/task/list')
def task_list():
    limit = request.args.get('pageSize')
    current_page = request.args.get('currentPage')
    limit = 10 if not limit else int(limit)
    current_page = 1 if not current_page else int(current_page)
    offset = (current_page - 1) * limit
    return jsonify(get_task_list(limit, current_page, offset))


@task_api.route('/api/task/detail')
def task_detail():
    taskid = request.args.get('taskid')
    if taskid.isdigit():
        detail = get_task_detail(taskid)
        service = get_task_detail_services(taskid)
        vulnerabilities = get_task_detail_vulnerabilities(taskid)
        return jsonify(
            {'taskDetail': detail, 'taskDetailServices': service, 'taskDetailVulnerabilities': vulnerabilities})
    else:
        return Response(404)


@task_api.route('/api/task/detail/services')
def task_detail_services():
    taskid = request.args.get('taskid')
    if taskid.isdigit():
        return jsonify(get_task_detail_services(taskid))
    else:
        return Response(404)


@task_api.route('/api/task/detail/vulnerabilities')
def task_detail_vulnerabilities():
    taskid = request.args.get('taskid')
    if taskid.isdigit():
        return jsonify(get_task_detail_vulnerabilities(taskid))
    else:
        return Response(404)
