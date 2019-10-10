from wtforms import Form, PasswordField, validators


class AuthUpdatePasswordForm(Form):
    old_password = PasswordField("Old password", [validators.DataRequired()])

    password = PasswordField(
        "New password",
        [
            validators.DataRequired(),
            validators.EqualTo("repeat_password", message="Passwords must match"),
        ],
    )

    repeat_password = PasswordField("Repeat password")
