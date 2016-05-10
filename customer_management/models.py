from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from localflavor.generic.models import IBANField


class CustomerAdmin(AbstractBaseUser):
    user = models.OneToOneField(User)


class Customer(models.Model):
    """
    Model for storing users.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    owner = models.ForeignKey(CustomerAdmin)
    iban = IBANField(unique=True)

