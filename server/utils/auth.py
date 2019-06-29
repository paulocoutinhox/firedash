import re
from functools import wraps, partial

import jwt
from flask import request, jsonify

from config.data import config_data
from models.domain.account import Account
from models.domain.device import Device


def account_token_required(func=None, *, export=True):
    if func is None:
        return partial(account_token_required, export=export)

    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()

        account_id = claims.get('account_id', 0)

        if account_id > 0:
            account = Account.query.get(account_id)

            if account:
                if export:
                    return func(*args, **kwargs, account=account)
                else:
                    return func(*args, **kwargs)
            else:
                return jsonify({'success': False, 'message': 'unauthorized'}), 401
        else:
            return jsonify({'success': False, 'message': 'unauthorized'}), 401

    return wrapper


def device_token_required(func=None, *, export=True):
    if func is None:
        return partial(device_token_required, export=export)

    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()

        device_id = claims.get('device_id', 0)

        if device_id > 0:
            device = Device.query.get(device_id)

            if device:
                if export:
                    return func(*args, **kwargs, device=device)
                else:
                    return func(*args, **kwargs)
            else:
                return jsonify({'success': False, 'message': 'unauthorized'}), 401
        else:
            return jsonify({'success': False, 'message': 'unauthorized'}), 401

    return wrapper


def verify_jwt_in_request():
    jwt_token = get_jwt_from_request()

    if not jwt_token:
        return jsonify({'success': False, 'message': 'unauthorized'}), 401


def get_jwt_claims():
    jwt_token = get_jwt_from_request()

    try:
        jwt_decoded = decode_auth_token(jwt_token)

        if jwt_decoded and isinstance(jwt_decoded, dict):
            return jwt_decoded
    except:
        pass

    return {}


def get_jwt_from_request():
    if request.headers:
        auth_header = request.headers.get('Authorization')

        if auth_header and len(auth_header) > 0:
            auth_header = auth_header.split(" ")[1]
            expr = "^[A-Za-z0-9-_=]+\\.[A-Za-z0-9-_=]+\\.?[A-Za-z0-9-_.+/=]*$"

            try:
                token = re.search(expr, auth_header).group(0)
                token = token.strip()
            except:
                token = None
                pass

            if token and len(token) > 0:
                return token

    return None


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(
            auth_token,
            config_data['jwt_key'],
            algorithms=[config_data['jwt_algorithm']]
        )

        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
