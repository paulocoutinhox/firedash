import datetime

import jwt

from app.app_data import db
from config.data import config_data


class Device(db.Model):
    __tablename__ = "device"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    token = db.Column(db.Text, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)

    def get_id(self):
        return self.id

    def get_jwt_encoded(self):
        encode_data = {"iat": datetime.datetime.utcnow(), "device_token": self.token}

        expiration_amount = config_data["jwt_device_expiration_amount"]

        if expiration_amount:
            encode_data["exp"] = datetime.datetime.utcnow() + datetime.timedelta(
                days=expiration_amount
            )

        encoded_jwt = jwt.encode(
            encode_data, config_data["jwt_key"], algorithm=config_data["jwt_algorithm"]
        )

        return encoded_jwt.decode("UTF-8")

    def to_dict(self, scenario):
        if not scenario:
            return {}

        keys = []

        if scenario == "create":
            keys = ["id", "name", "token", "created_at", "updated_at"]
        elif scenario == "update":
            keys = ["id", "name", "token", "created_at", "updated_at"]
        elif scenario == "list":
            keys = ["id", "name", "token", "created_at", "updated_at"]
        elif scenario == "get":
            keys = ["id", "name", "token", "created_at", "updated_at"]

        return dict([(k, getattr(self, k)) for k in keys])
