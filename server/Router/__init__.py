from server.Router.basic import basic_api
from server.Router.user import user_api
from server.Router.system import system_api
from server.Router.task import task_api
from server.Router.payloads import payloads_api


def router_init(app):
    blueprint_list = [basic_api, user_api, system_api, task_api, payloads_api]
    for blueprint in blueprint_list:
        app.register_blueprint(blueprint)
