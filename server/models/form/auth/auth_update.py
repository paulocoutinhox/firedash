from wtforms import Form, validators, StringField


class AuthUpdateForm(Form):
    name = StringField("Name", [validators.DataRequired(), validators.length(max=255)])

    email = StringField(
        "Email",
        [validators.DataRequired(), validators.length(max=255), validators.Email()],
    )

    photo_url = StringField("Photo url", [validators.length(max=255)])
