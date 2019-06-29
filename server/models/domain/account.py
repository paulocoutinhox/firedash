import datetime

import jwt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.app_data import db
from config.data import config_data


class Account(UserMixin, db.Model):
    __tablename__ = 'account'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_jwt_encoded(self):
        encode_data = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=config_data['jwt_login_expiration_amount']),
            'iat': datetime.datetime.utcnow(),
            'account_id': self.id
        }

        encoded_jwt = jwt.encode(
            encode_data,
            config_data['jwt_key'],
            algorithm=config_data['jwt_algorithm']
        )

        return encoded_jwt.decode('UTF-8')

    def to_dict(self, scenario):
        if not scenario:
            return {}

        keys = []

        if scenario == 'create':
            keys = ['id', 'name', 'email', 'photo_url', 'is_admin', 'created_at', 'updated_at']
        elif scenario == 'update':
            keys = ['id', 'name', 'email', 'photo_url', 'is_admin', 'created_at', 'updated_at']
        elif scenario == 'list':
            keys = ['id', 'name', 'email', 'photo_url', 'is_admin', 'created_at', 'updated_at']
        elif scenario == 'get':
            keys = ['id', 'name', 'email', 'photo_url', 'is_admin', 'created_at', 'updated_at']
        elif scenario == 'login':
            keys = ['id', 'name', 'email', 'photo_url', 'is_admin', 'created_at', 'updated_at']

        return dict([(k, getattr(self, k)) for k in keys])
