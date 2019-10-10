import firebase_admin
import wtforms_json
from elasticsearch import Elasticsearch
from firebase_admin import credentials
from flask import Flask
from flask_json import FlaskJSON
from flask_sqlalchemy import SQLAlchemy

from config.data import config_data

flask = Flask(
    __name__,
    template_folder="../../web-cli/dist",
    static_folder="../../web-cli/dist/static",
)

flask.config["SQLALCHEMY_DATABASE_URI"] = config_data["database_uri"]
flask.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config_data[
    "database_track_modifications"
]
flask.config["TEMPLATES_AUTO_RELOAD"] = config_data["templates_auto_reload"]
flask.config["SESSION_TYPE"] = config_data["server_session_type"]
flask.config["JSON_ADD_STATUS"] = False
flask.config["DEBUG"] = config_data["debug"]

flask.secret_key = config_data["secret_key"]

# flask plugins
json = FlaskJSON(flask)
wtforms_json.init()

# database
db = SQLAlchemy(flask)

# firebase
if config_data["firebase_enabled"]:
    cred = credentials.Certificate(config_data["firebase_credential_path"])

    firebase_admin.initialize_app(
        cred, {"databaseURL": config_data["firebase_database_url"]}
    )

# elasticsearch
es: Elasticsearch

if config_data["elasticsearch_enabled"]:
    es = Elasticsearch(config_data["elasticsearch_config"])

# routes
from routes.routes_home import routes_home
from routes.routes_api_data import routes_api_data
from routes.routes_api_account import routes_api_account
from routes.routes_api_device import routes_api_device
from routes.routes_api_auth import routes_api_auth

flask.register_blueprint(routes_home)
flask.register_blueprint(routes_api_auth)
flask.register_blueprint(routes_api_account)
flask.register_blueprint(routes_api_device)
flask.register_blueprint(routes_api_data)
