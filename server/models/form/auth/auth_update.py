from wtforms import Form, PasswordField, validators


class AuthUpdateForm(Form):
    name = PasswordField('Name', [validators.DataRequired()])

    email = PasswordField('Email', [validators.DataRequired(), validators.Email()])

    photo_url = PasswordField('Photo url')
