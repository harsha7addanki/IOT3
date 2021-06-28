from django.db import models


# Create your models here
class Property(models.Model):
	TYPES = (
		("I", "Integer"),
		("S", "String"),
		("B", "Boolean"),
		("D", "Decimal")
	)
	type = models.CharField(max_length=64, choices=TYPES)
	key = models.CharField(max_length=64, primary_key=True)
	value = models.CharField(max_length=64)


class Device(models.Model):
	name = models.CharField(max_length=64)
	dev_secret = models.CharField(max_length=64)


class Thing(models.Model):
	name = models.CharField(max_length=64)
	properties = models.ManyToManyField(Property, blank=True)
	device = models.ForeignKey("Device", on_delete=models.CASCADE)


class User(models.Model):
	username = models.CharField(max_length=64, primary_key=True)
	password = models.CharField(max_length=64)
	things = models.ManyToManyField(Thing, blank=True)
	devices = models.ManyToManyField(Device, blank=True)
