from wtforms import Form, validators, IntegerField


class AccountGetForm(Form):
    id = IntegerField("ID", [validators.DataRequired()])
