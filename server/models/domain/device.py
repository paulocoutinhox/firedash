import datetime

import jwt

from app.app_data import db
from config.data import config_data


class Device(db.Model):
    __tablename__ = "device"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def get_id(self):
        return self.id

    def get_jwt_encoded(self):
        encode_data = {"iat": datetime.datetime.utcnow(), "device_id": self.id}

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
            keys = ["id", "name", "created_at", "updated_at"]
        elif scenario == "update":
            keys = ["id", "name", "created_at", "updated_at"]
        elif scenario == "list":
            keys = ["id", "name", "created_at", "updated_at"]
        elif scenario == "get":
            keys = ["id", "name", "created_at", "updated_at"]

        return dict([(k, getattr(self, k)) for k in keys])
