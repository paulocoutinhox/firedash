from wtforms import Form, validators, StringField, IntegerField, FloatField


class DeviceDataCreateForm(Form):
    device_id = IntegerField('Device ID', [validators.DataRequired()])

    type = StringField('Type', [validators.DataRequired()])

    value = FloatField('Value', [validators.DataRequired()])
