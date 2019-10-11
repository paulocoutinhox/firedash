import os
from collections import OrderedDict

config_data = OrderedDict()

config_data["debug"] = False
config_data["web_cli_enabled"] = True

config_data["secret_key"] = "[CHANGE-HERE]"
config_data["database_uri"] = "sqlite:///../../db/app.db"
config_data["database_track_modifications"] = False

config_data["server_host"] = None
config_data["server_port"] = 5000
config_data["server_session_type"] = "filesystem"

config_data["templates_auto_reload"] = False

config_data["jwt_key"] = "[CHANGE-HERE]"
config_data["jwt_algorithm"] = "HS256"
config_data["jwt_login_expiration_amount"] = 365 * 1
config_data["jwt_device_expiration_amount"] = False

config_data["firebase_enabled"] = False
config_data["firebase_database_url"] = ""
config_data["firebase_credential_path"] = ""

config_data["elasticsearch_enabled"] = False
config_data["elasticsearch_config"] = [{"host": "localhost", "port": 9200}]
