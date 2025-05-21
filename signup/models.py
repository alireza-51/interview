from django.db import models
from django.core.validators import MinLengthValidator

from signup.validators import phone_regex

class User(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    national_id = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
