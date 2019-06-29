from wtforms import Form, PasswordField, validators, BooleanField


class AccountCreateForm(Form):
    name = PasswordField('Name', [validators.DataRequired()])

    email = PasswordField('Email', [validators.DataRequired(), validators.Email()])

    photo_url = PasswordField('Photo url')

    password = PasswordField('New password', [
        validators.DataRequired(),
        validators.EqualTo('repeat_password', message='Passwords must match')
    ])

    repeat_password = PasswordField('Repeat password')

    is_admin = BooleanField('Is admin')
