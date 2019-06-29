from wtforms import Form, PasswordField, validators, BooleanField, IntegerField


class AccountUpdateForm(Form):
    id = IntegerField('ID', [validators.DataRequired()])

    name = PasswordField('Name', [validators.DataRequired()])

    email = PasswordField('Email', [validators.DataRequired(), validators.Email()])

    photo_url = PasswordField('Photo url')

    password = PasswordField('New password', [
        validators.EqualTo('repeat_password', message='Passwords must match')
    ])

    repeat_password = PasswordField('Repeat password')

    is_admin = BooleanField('Is admin')
