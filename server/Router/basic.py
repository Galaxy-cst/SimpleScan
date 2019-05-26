from flask import Blueprint, redirect, url_for

basic_api = Blueprint('basic_api', __name__)


@basic_api.route('/')
@basic_api.route('/api')
def index():
    return 'SimpleScan API Server !'


@basic_api.errorhandler(405)
@basic_api.errorhandler(404)
def page_not_found():
    return redirect(url_for('/'))
