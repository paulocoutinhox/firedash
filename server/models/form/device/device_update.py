from models.domain.device import Device
from models.validators.unique_validator import Unique
from wtforms import validators, StringField, IntegerField
from wtforms_alchemy import ModelForm


class DeviceUpdateForm(ModelForm):
    id = IntegerField("ID", [validators.DataRequired()])

    name = StringField("Name", [validators.DataRequired(), validators.length(max=255)])

    token = StringField(
        "Token",
        [validators.DataRequired(), validators.length(max=255), Unique(Device.token)],
    )
