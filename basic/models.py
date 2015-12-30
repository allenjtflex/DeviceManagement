from django.db import models

# Create your models here.
class Vender(models.Model):
	title = models.CharField(max_length=60, blank=False)
	create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_at = models.DateTimeField(auto_now_add=False, auto_now=True)


class Category(models.Model):
	description = models.CharField(max_length=60, blank=False)
	effictive = models.BooleanField()
	create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.description


class Equipment(models.Model):
	category = models.ForeignKey(Category)
	description = models.CharField(max_length=60, blank=False)
	brand = models.CharField(max_length=30, blank=False)
	spec = models.CharField(max_length=200)
	create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __str__(self):
		return self.description

"""
class EquipmentSpec(models.Model):
	equipment = models.ForeignKey(Equipment)
	spec = models.CharField(max_length=60, blank=False)
	effictive = models.Boolean()
	create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
"""