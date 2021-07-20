from django.db import models

# Create your models here.
class Kakaoshop(models.Model):
    rank = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)