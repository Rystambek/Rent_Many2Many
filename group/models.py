from django.db import models

# Create your models here.
from app.models import Customer

class Group(models.Model):
    name = models.CharField(max_length=20,unique=True)
    student = models.ManyToManyField(Customer)

    def __str__(self) -> str:
        return self.name