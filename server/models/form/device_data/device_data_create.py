from wtforms import Form, validators, StringField, FloatField


class DeviceDataCreateForm(Form):
    device_token = StringField(
        "Device Token", [validators.DataRequired(), validators.length(max=255)]
    )

    type = StringField("Type", [validators.DataRequired(), validators.length(max=255)])

    value = FloatField("Value", [validators.DataRequired()])
