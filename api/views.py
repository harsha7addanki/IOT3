from django.http import JsonResponse
from models import models


# Create your views here.

def get(request, user, thing, dev_secret, key):
	user = models.User.objects.filter(username=user)[0]
	thing = user.things.filter(name=thing)[0]
	device = thing.device
	if device.dev_secret == dev_secret:
		property = thing.properties.filter(key=key)[0]
		return JsonResponse({"type": property.type, "value": property.value})
	else:
		return JsonResponse({"Err": "invalid credentials"})


def set(request, user, thing, dev_secret, key, value):
	user = models.User.objects.filter(username=user)[0]
	thing = user.things.filter(name=thing)[0]
	device = thing.device
	if device.dev_secret == dev_secret:
		property = thing.properties.filter(key=key)[0]
		property.value = value
		property.save()
		return JsonResponse({"type": property.type, "value": property.value})
	else:
		return JsonResponse({"Err": "invalid credentials"})
