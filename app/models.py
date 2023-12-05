from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Car(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField(unique=True)
    description = models.TextField(default="",blank=True)
    price = models.FloatField()
    color = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    years = models.IntegerField()
    motors = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"
    

class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=62,null=True,blank=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.TextField(default='',blank=True)
    birtday_day = models.DateField()
    gender = models.CharField(
        max_length=1,
        choices=[
            ("F","Female"),
            ("M","Male")
        ]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(limit_value=18),MaxValueValidator(limit_value=35)]
        )
    username = models.CharField(max_length=64,unique=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name}"