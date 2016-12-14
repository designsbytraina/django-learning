from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
	""""""
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()

############################
# More types - https://docs.djangoproject.com/en/1.10/ref/models/fields/
	# IntegerField
	# DecimalField

	# CharField(max_length=200, null=True, blank=True, default='x', choices='Small, Medium, Large')
	# TextField
	# EmailField - includes validation
	# URLField - includes validation

	# FileField
	# ImageField

	# BooleanField
	# DateTimeField
############################

