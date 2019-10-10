import time
from datetime import datetime, timedelta

from app.app_data import db
from flask import Blueprint, request
from flask_json import as_json
from models.domain.device import Device
from models.domain.device_data import DeviceData
from models.form.device_data.device_data_create import DeviceDataCreateForm
from models.form.device_data.device_data_out_device import DeviceDataOutByDeviceForm
from models.form.device_data.device_data_out_random import DeviceDataOutByRandomForm
from utils import response
from utils.auth import account_auth_token_required, device_auth_token_required
from utils.random import random_int_values, random_datetime_range

routes_api_data = Blueprint("api_data", __name__)


@routes_api_data.route("/api/data/out/random", methods=["POST"])
@account_auth_token_required(export=False)
@as_json
def action_data_out_by_random():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceDataOutByRandomForm.from_json(content)

    if form.validate():
        datasets = form.datasets.data
        dataset_list = []

        for _ in range(datasets):
            items = random_int_values(
                form.amount.data, form.min_value.data, form.max_value.data
            )

            dataset_list.append({"items": items})

        labels = random_datetime_range(
            datetime.now() - timedelta(seconds=form.amount.data - 1),
            datetime.now(),
            dt_format=form.format_dt.data,
        )

        return response.success(data={"labels": labels, "datasets": dataset_list})
    else:
        return response.from_form(form)


@routes_api_data.route("/api/data/out/device", methods=["POST"])
@account_auth_token_required(export=False)
@as_json
def action_data_out_by_device():
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceDataOutByDeviceForm.from_json(content)

    if form.validate():
        device = Device.query.filter(Device.token == form.device_token.data).first()

        if device:
            items = DeviceData.query.filter(
                DeviceData.device_id == device.id,
                DeviceData.type == form.type.data,
                DeviceData.created_at >= form.start_dt.data,
                DeviceData.created_at <= form.end_dt.data,
            ).all()

            if items:
                if form.format_dt.data:
                    labels = map(
                        lambda item: item.created_at.strftime(form.format_dt.data),
                        items,
                    )
                else:
                    labels = map(
                        lambda item: time.mktime(item.created_at.timetuple()), items
                    )

                items = map(lambda item: item.value, items)

                return response.success(
                    data={"labels": labels, "datasets": [{"items": items}]}
                )
            else:
                return response.not_success("empty")
        else:
            return response.not_success("not-found")
    else:
        return response.from_form(form)


@routes_api_data.route("/api/data/in", methods=["POST"])
@device_auth_token_required
@as_json
def action_data_in(device):
    content = request.get_json(silent=True)
    content = content if content is not None else {}

    form = DeviceDataCreateForm.from_json(content)
    form.device_token.data = device.token

    if form.validate():
        new_device_data = DeviceData()

        new_device_data.device_id = device.id
        new_device_data.type = form.type.data
        new_device_data.value = form.value.data
        new_device_data.created_at = datetime.utcnow()

        db.session.add(new_device_data)
        db.session.flush()
        db.session.commit()

        return response.success()
    else:
        return response.from_form(form)
