from tortoise import fields, models

from app.utils import now


class Client(models.Model):
    """Settings for authorization through our app"""
    client_id = fields.CharField(max_length=32, unique=True, pk=True)
    client_secret = fields.BinaryField(max_length=1024)

    name = fields.CharField(max_length=255)
    homepage = fields.CharField(max_length=255)
    callback_url = fields.CharField(max_length=255)

    created_at = fields.DatetimeField(default=now)
    owner = fields.ForeignKeyField("account.User")
