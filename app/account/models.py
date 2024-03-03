import datetime

from tortoise import models, fields

from app.utils import now


class User(models.Model):
    """Main user model"""
    id = fields.BigIntField(pk=True)
    email = fields.CharField(unique=True, index=True, max_length=255)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    hashed_password: bytes = fields.BinaryField(description="User hashed password")
    last_login = fields.DatetimeField(default=now())


class Session(models.Model):
    """Session model to handle UI authorization"""
    session_key = fields.CharField(unique=True, max_length=1024, index=True)

    expire_at = fields.DatetimeField(description="Session expire timestamp")
    user = fields.ForeignKeyField("account.User",
                                  on_delete=fields.CASCADE)  # TODO support anonymous sessions

    additional_data = fields.JSONField(default=dict)

    # encrypted_data = fields.BinaryField() # TODO ENCRYPT SESSION user and expire date
