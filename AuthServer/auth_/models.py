from django.db import models


class User(models.Model):
    created_at = models.DateTimeField()
    account_expired = models.BooleanField()
    authority = models.CharField(max_length=255)
    sns_at = models.BooleanField()
    enable = models.BooleanField()


class SNS(models.Model):
    provider = models.CharField(max_length=255)
    prov_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Non_SNS(models.Model):
    _id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    last_pwd_updated = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
