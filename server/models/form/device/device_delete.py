from wtforms import Form, validators, IntegerField


class DeviceDeleteForm(Form):
    id = IntegerField('ID', [validators.DataRequired()])
