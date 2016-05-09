from django.db import models
from localflavor.generic.models import IBANField


class Customer(models.Model):
    """
    Model for storing users.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # owner = models.Foreign
    iban = IBANField(unique=True)
