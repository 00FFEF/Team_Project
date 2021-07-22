from django.db import models

# Create your models here.
class Kakaoshop(models.Model):
    rank = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)

class Navershop(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)

class Admachine(models.Model):
    UserID = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Age = models.DecimalField(max_digits=20,decimal_places=5)
    EstimatedSalary = models.DecimalField(max_digits=20,decimal_places=5)
    Purchased = models.DecimalField(max_digits=20,decimal_places=5)