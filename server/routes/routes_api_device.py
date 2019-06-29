from datetime import datetime

from flask import Blueprint, request
from flask_json import as_json

from app.app_data import db
from models.domain.device import Device
from models.form.device.device_create import DeviceCreateForm
from models.form.device.device_delete import DeviceDeleteForm
from models.form.device.device_get import DeviceGetForm
from models.form.device.device_update import DeviceUpdateForm
from utils import response
from utils.auth import account_token_required

routes_api_device = Blueprint('api_device', __name__)


@routes_api_device.route('/api/device/create', methods=['POST'])
@account_token_required(export=False)
@as_json
def action_create():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceCreateForm.from_json(content)

    if form.validate():
        new_device = Device()

        new_device.name = form.name.data
        new_device.created_at = datetime.utcnow()

        db.session.add(new_device)
        db.session.flush()
        db.session.commit()

        new_device = Device.query.get(new_device.id)

        return response.success(data={
            'device': new_device.to_dict('create')
        })
    else:
        return response.from_form(form)


@routes_api_device.route('/api/device/update', methods=['POST'])
@account_token_required(export=False)
@as_json
def action_update():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceUpdateForm.from_json(content)

    if form.validate():
        device = Device.query.get(form.id.data)

        if device:
            device.name = form.name.data
            device.updated_at = datetime.utcnow()

            db.session.flush()
            db.session.commit()

            device = Device.query.get(device.id)

            return response.success(data={
                'device': device.to_dict('update')
            })
        else:
            return response.not_success('not-found')
    else:
        return response.from_form(form)


@routes_api_device.route('/api/device/delete', methods=['POST'])
@account_token_required(export=False)
@as_json
def action_delete():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceDeleteForm.from_json(content)

    if form.validate():
        device = Device.query.get(form.id.data)

        if device:
            db.session.delete(device)
            db.session.flush()
            db.session.commit()

            return response.success()
        else:
            return response.not_success('not-found')
    else:
        return response.from_form(form)


@routes_api_device.route('/api/device/list', methods=['POST'])
@account_token_required(export=False)
@as_json
def action_list():
    devices = Device.query.order_by(Device.created_at.desc()).all()
    devices = [r.to_dict('list') for r in devices]

    return response.success(data={
        'list': devices,
    })


@routes_api_device.route('/api/device/get', methods=['POST'])
@account_token_required(export=False)
@as_json
def action_get():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceGetForm.from_json(content)

    if form.validate():
        device = Device.query.get(form.id.data)

        if device:
            return response.success(data={
                'device': device.to_dict('get')
            })
        else:
            return response.not_success('not-found')
    else:
        return response.from_form(form)


@routes_api_device.route('/api/device/token', methods=['POST'])
@account_token_required(export=False)
@as_json
def action_token():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceGetForm.from_json(content)

    if form.validate():
        device = Device.query.get(form.id.data)

        if device:
            return response.success(data={
                'token': device.get_jwt_encoded()
            })
        else:
            return response.not_success('not-found')
    else:
        return response.from_form(form)
