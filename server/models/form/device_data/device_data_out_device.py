from wtforms import Form, validators, StringField


class DeviceDataOutByDeviceForm(Form):
    device_token = StringField(
        "Device Token", [validators.DataRequired(), validators.length(max=255)]
    )

    type = StringField("Type", [validators.DataRequired(), validators.length(max=255)])

    start_dt = StringField("Start period", [validators.DataRequired()])

    end_dt = StringField("End period", [validators.DataRequired()])

    format_dt = StringField(
        "Period format", [validators.Optional(), validators.length(max=255)]
    )
