from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class Object(Model):
    name = models.TextField(
        unique = True,
        blank = False,
        max_length = 30,
    )
    description = models.TextField(
        unique = False,
        blank = True,
        max_length = 120
    )
    quantiy = models.PositiveIntegerField(
        unique = False,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
    )

