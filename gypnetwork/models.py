from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50)

class Sale(models.Model):
	name = models.CharField(max_length=50)

class Purchase(models.Model):
	name = models.CharField(max_length=50)