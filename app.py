from flask import Flask, jsonify, request
from lib.DBHelper.DB import DBConnect
import json
from concurrent.futures import ThreadPoolExecutor
from app.Fingerprint import get_fingerprint
from app.Attack.Hydra import bruteforce
from app.System.userModel import login, change_password

executor = ThreadPoolExecutor(10)
app = Flask(__name__)


@app.route('/')
def index():
    return 'SimpleScan API Server !'


@app.route('/results/read_all_ip_port')
def read_all_ip_port():
    with DBConnect() as conn:
        results = conn.read_all_ip_port()
    return jsonify(results)


@app.route('/fingerprint/new_task', methods=['POST'])
def new_task():
    data = request.form['data']
    data_obj = json.loads(data)
    executor.submit(get_fingerprint, data_obj['port_list'], data_obj['task_id'])
    return 'OK'


@app.route('/scanner')
def scanner():
    ip = '120.79.214.167'
    executor.submit(bruteforce, ip)
    return 'sucess!'


@app.route('/api/user/login', methods=['POST'])
def router_login():
    print(request.json)
    user = request.json['userName']
    password = request.json['password']
    return login(password) and (user == 'admin')


@app.route('/api/user/changePassword', methods=['POST'])
def router_change_password():
    new_password = request.form['newPassword']
    change_password(new_password)
    return 'sucess!'