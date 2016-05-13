from django.db import models
from django.contrib.auth.models import User
from localflavor.generic.models import IBANField


class Customer(models.Model):
    """
    Model for storing users.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    owner = models.ForeignKey(User)
    iban = IBANField(unique=True)
    avatar = models.ImageField(blank=True, null=True)
