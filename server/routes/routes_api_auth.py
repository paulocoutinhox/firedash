from datetime import datetime

from flask import Blueprint, request
from flask_json import as_json

from app.app_data import db
from models.domain.account import Account
from models.form.auth.auth_update import AuthUpdateForm
from models.form.auth.auth_update_password import AuthUpdatePasswordForm
from utils import response
from utils.auth import account_token_required

routes_api_auth = Blueprint('api_auth', __name__)


@routes_api_auth.route('/api/auth/login', methods=['POST'])
@as_json
def action_login():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    email = content.get('email')
    password = content.get('password')

    account = Account.query.filter_by(email=email).first()

    if account and account.check_password(password):
        encoded_jwt = account.get_jwt_encoded()

        return response.success(data={
            'account': account.to_dict('login'),
            'token': encoded_jwt
        })
    else:
        return response.not_success('validate')


@routes_api_auth.route('/api/auth/update-password', methods=['POST'])
@account_token_required
@as_json
def action_update_password(account):
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AuthUpdatePasswordForm.from_json(content)

    if form.validate():
        if account.check_password(form.old_password.data):
            account.set_password(form.password.data)
            account.updated_at = datetime.utcnow()

            db.session.flush()
            db.session.commit()

            return response.success()
        else:
            return response.with_validate_error('password', ['The old password is wrong'])
    else:
        return response.from_form(form)


@routes_api_auth.route('/api/auth/update', methods=['POST'])
@account_token_required
@as_json
def action_update(account):
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AuthUpdateForm.from_json(content)

    if form.validate():
        account.name = form.name.data
        account.email = form.email.data
        account.photo_url = form.photo_url.data
        account.updated_at = datetime.utcnow()

        db.session.flush()
        db.session.commit()

        account = Account.query.get(account.id)

        return response.success(data={
            'account': account.to_dict('update')
        })
    else:
        return response.from_form(form)


@routes_api_auth.route('/api/auth/get', methods=['POST'])
@account_token_required
@as_json
def action_get(account):
    return response.success(data={
        'account': account.to_dict('update')
    })
