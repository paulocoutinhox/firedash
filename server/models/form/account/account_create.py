from models.domain.account import Account
from models.validators.unique_validator import Unique
from wtforms import PasswordField, validators, BooleanField, StringField
from wtforms_alchemy import ModelForm


class AccountCreateForm(ModelForm):
    name = StringField("Name", [validators.DataRequired(), validators.length(max=255)])

    email = StringField(
        "Email",
        [
            validators.DataRequired(),
            validators.length(max=255),
            validators.Email(),
            Unique(Account.email),
        ],
    )

    photo_url = StringField("Photo url", [validators.length(max=255)])

    password = PasswordField(
        "New password",
        [
            validators.DataRequired(),
            validators.length(max=255),
            validators.EqualTo("repeat_password", message="Passwords must match"),
        ],
    )

    repeat_password = PasswordField("Repeat password", [validators.length(max=255)])

    is_admin = BooleanField("Is admin")
