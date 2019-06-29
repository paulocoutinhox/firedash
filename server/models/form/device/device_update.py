from wtforms import Form, validators, StringField, IntegerField


class DeviceUpdateForm(Form):
    id = IntegerField('ID', [validators.DataRequired()])

    name = StringField('Name', [validators.DataRequired()])
