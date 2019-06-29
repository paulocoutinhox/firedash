from wtforms import Form, validators, IntegerField


class DeviceGetForm(Form):
    id = IntegerField('ID', [validators.DataRequired()])
