from flask import Blueprint, request, abort, jsonify
from app.System.userModel import User

user_api = Blueprint('user_api', __name__)
userModel = User()


@user_api.route('/api/user/login', methods=['POST'])
def login():
    username = request.json['userName']
    password = request.json['password']
    cookie = userModel.login(username, password)
    if cookie:
        res = jsonify({'status': 'ok', 'currentAuthority': username})
        res.set_cookie(key='simplescan-token', value=cookie)
        return res
    else:
        abort(401)


@user_api.route('/api/user/change_password', methods=['POST'])
def change_password():
    new_password = request.form['newPassword']
    userModel.change_password(new_password)
    return jsonify({'status': 'ok'})


@user_api.route('/api/user/current_user')
def current_user():
    cookie = request.cookies.get('simplescan-token')
    username = userModel.current_user(cookie)
    if username:
        user = {
            'name': username,
            'userid': '1',
        }
        return jsonify(user)
    else:
        abort(401)
