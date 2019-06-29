from wtforms import Form, PasswordField, validators


class DeviceCreateForm(Form):
    name = PasswordField('Name', [validators.DataRequired()])
