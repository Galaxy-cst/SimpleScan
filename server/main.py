from flask import Flask
from server.config import server_init
from server.Router import router_init

app = Flask(__name__)
server_init(app)
router_init(app)
