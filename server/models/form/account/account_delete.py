from wtforms import Form, validators, IntegerField


class AccountDeleteForm(Form):
    id = IntegerField('ID', [validators.DataRequired()])
