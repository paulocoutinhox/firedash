from wtforms import Form, PasswordField, validators


class AuthUpdatePasswordForm(Form):
    old_password = PasswordField(
        "Old password", [validators.DataRequired(), validators.length(max=255)]
    )

    password = PasswordField(
        "New password",
        [
            validators.DataRequired(),
            validators.length(max=255),
            validators.EqualTo("repeat_password", message="Passwords must match"),
        ],
    )

    repeat_password = PasswordField("Repeat password", [validators.length(max=255)])
