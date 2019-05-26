from flask import Blueprint, jsonify
from app.System.systemInfoModel import system_info

system_api = Blueprint('system_api', __name__)


@system_api.route('/api/system/cpu')
def system_cpu():
    return jsonify({'cpu': system_info.get_cpu_rate()})


@system_api.route('/api/system/mem')
def system_mem():
    return jsonify({'mem': system_info.get_mem_rate()})


@system_api.route('/api/system/ip')
def system_ip():
    return jsonify({'intranet_ip': system_info.intranet_ip, 'extranet_ip': system_info.extranet_ip})


@system_api.route('/api/system/pps')
def system_pps():
    return jsonify(system_info.pps)


@system_api.route('/api/system/all')
def system_all():
    return jsonify({
        'cpu': system_info.get_cpu_rate(),
        'mem': system_info.get_mem_rate(),
        'ip': {
            'intranet_ip': system_info.intranet_ip,
            'extranet_ip': system_info.extranet_ip
        },
        'pps': system_info.pps
    })
