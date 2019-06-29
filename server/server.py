from app.app_data import flask
from config.data import config_data

if __name__ == '__main__':
    flask.run(
        host=config_data['server_host'],
        port=config_data['server_port'],
        debug=config_data['debug']
    )
