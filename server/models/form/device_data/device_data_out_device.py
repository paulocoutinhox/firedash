from wtforms import Form, validators, StringField, IntegerField


class DeviceDataOutByDeviceForm(Form):
    device_id = IntegerField("Device ID", [validators.DataRequired()])

    type = StringField("Type", [validators.DataRequired()])

    start_dt = StringField("Start period", [validators.DataRequired()])

    end_dt = StringField("End period", [validators.DataRequired()])

    format_dt = StringField("Period format", [validators.DataRequired()])
