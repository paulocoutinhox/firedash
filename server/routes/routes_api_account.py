from datetime import datetime

from flask import Blueprint, request
from flask_json import as_json

from app.app_data import db
from models.domain.account import Account
from models.form.account.account_create import AccountCreateForm
from models.form.account.account_delete import AccountDeleteForm
from models.form.account.account_get import AccountGetForm
from models.form.account.account_update import AccountUpdateForm
from utils import response
from utils.auth import account_auth_token_required

routes_api_account = Blueprint("api_account", __name__)


@routes_api_account.route("/api/account/create", methods=["POST"])
@account_auth_token_required
@as_json
def action_create(account):
    if not account.is_admin:
        return response.unauthorized()

    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AccountCreateForm.from_json(content)

    if form.validate():
        new_account = Account()

        new_account.name = form.name.data
        new_account.token = form.token.data
        new_account.email = form.email.data
        new_account.photo_url = form.photo_url.data
        new_account.is_admin = form.is_admin.data
        new_account.created_at = datetime.utcnow()

        new_account.set_password(form.password.data)

        db.session.add(new_account)
        db.session.flush()
        db.session.commit()

        new_account = Account.query.get(new_account.id)

        return response.success(data={"account": new_account.to_dict("create")})
    else:
        return response.from_form(form)


@routes_api_account.route("/api/account/update", methods=["POST"])
@account_auth_token_required
@as_json
def action_update(account):
    if not account.is_admin:
        return response.unauthorized()

    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AccountUpdateForm.from_json(content)

    if form.validate():
        found_account = Account.query.get(form.id.data)

        if found_account:
            found_account.name = form.name.data
            found_account.token = form.token.data
            found_account.email = form.email.data
            found_account.photo_url = form.photo_url.data
            found_account.is_admin = form.is_admin.data
            found_account.updated_at = datetime.utcnow()

            if form.password.data:
                found_account.set_password(form.password.data)

            db.session.flush()
            db.session.commit()

            found_account = Account.query.get(found_account.id)

            return response.success(data={"account": found_account.to_dict("update")})
        else:
            return response.not_success("not-found")
    else:
        return response.from_form(form)


@routes_api_account.route("/api/account/delete", methods=["POST"])
@account_auth_token_required
@as_json
def action_delete(account):
    if not account.is_admin:
        return response.unauthorized()

    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AccountDeleteForm.from_json(content)

    if form.validate():
        if form.id.data > 1:
            found_account = Account.query.get(form.id.data)

            if found_account:
                db.session.delete(found_account)
                db.session.flush()
                db.session.commit()

                return response.success()
            else:
                return response.not_success("not-found")
        else:
            return response.with_validate_error("id", ["Cannot delete this account."])
    else:
        return response.from_form(form)


@routes_api_account.route("/api/account/list", methods=["POST"])
@account_auth_token_required
@as_json
def action_list(account):
    if not account.is_admin:
        return response.unauthorized()

    accounts = Account.query.order_by(Account.created_at.desc()).all()
    accounts = [r.to_dict("list") for r in accounts]

    return response.success(data={"list": accounts})


@routes_api_account.route("/api/account/get", methods=["POST"])
@account_auth_token_required
@as_json
def action_get(account):
    if not account.is_admin:
        return response.unauthorized()

    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AccountGetForm.from_json(content)

    if form.validate():
        found_account = Account.query.get(form.id.data)

        if found_account:
            return response.success(data={"account": found_account.to_dict("get")})
        else:
            return response.not_success("not-found")
    else:
        return response.from_form(form)


@routes_api_account.route("/api/account/token", methods=["POST"])
@account_auth_token_required
@as_json
def action_token(account):
    if not account.is_admin:
        return response.unauthorized()

    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = AccountGetForm.from_json(content)

    if form.validate():
        found_account = Account.query.get(form.id.data)

        if found_account:
            return response.success(data={"token": found_account.get_jwt_encoded()})
        else:
            return response.not_success("not-found")
    else:
        return response.from_form(form)
