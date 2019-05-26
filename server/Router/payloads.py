from flask import Blueprint, jsonify
from app.Attack import payloads_iter

payloads_api = Blueprint('payloads_api', __name__)


@payloads_api.route('/api/payloads/all')
def all_payloads():
    payloads = []
    for payload in payloads_iter():
        payloads.append(payload)
    return jsonify(payloads)
