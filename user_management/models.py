from django.db import models


class UserProfile(models.Model):
    """
    Model for storing users.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    iban = models.IntegerField()
