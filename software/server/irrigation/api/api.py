import logging

from flask import Flask, Blueprint
from flask_cors import CORS

from utils import Log
from api.settings import API_PREFIX
from api.endpoints import init
from api.endpoints import areas
from api.endpoints import area_types
from repositories.database.init_db import init_db


_LOGGER = Log(logger=logging.getLogger('irrigation'))


# init flask app
app = Flask(__name__)


# iniciamos base de datos
init_db()


# blueprints
bp = Blueprint('api', __name__, url_prefix=API_PREFIX)  # api's blueprint
bp.register_blueprint(init.blueprint)
bp.register_blueprint(area_types.blueprint)
bp.register_blueprint(areas.blueprint)
app.register_blueprint(bp)

# cors
CORS(app)
