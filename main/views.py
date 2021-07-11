from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from models.models import User, Thing, Device, Property


# Create your views here.

def login(request):
	return render(request, "login.html")


class LoginUsr(View):
	def post(self, request):
		try:
			user = User.objects.get(pk=request.POST.get("user"))
		except:
			return HttpResponseRedirect("/")

		if user.password == request.POST.get("password"):
			request.session["user"] = request.POST.get("user")
			return HttpResponseRedirect("/things/")
		else:
			return HttpResponseRedirect("/")


def things(request):
	if request.session["user"]:
		context = {
			"things": User.objects.get(pk=request.session["user"]).things.all(),
			"devices": User.objects.get(pk=request.session["user"]).devices.all()
		}
		print(User.objects.get(pk=request.session["user"]).devices.all())
		return render(request, "things.html", context)


def thing(request, thingid):
	if request.session["user"]:
		context = {
			"thing": User.objects.get(pk=request.session["user"]).things.get(pk=thingid)
		}
		return render(request, "thing.html", context)


class ThingAdd(View):
	def post(self, request):
		if request.session["user"]:
			makething = Thing(name=request.POST.get("name"),
			                  device=User.objects.get(pk=request.session["user"]).devices.get(
				                  pk=request.POST.get("device")))
			makething.save()
			User.objects.get(pk=request.session["user"]).things.add(makething)
			return HttpResponseRedirect("/things/")


class PropAdd(View):
	def post(self, request, thingid):
		if request.session["user"]:
			makeprop = Property(key=request.POST.get("key"), type=request.POST.get("type"))
			makeprop.save()
			User.objects.get(pk=request.session["user"]).things.get(pk=thingid).properties.add(makeprop)
			return HttpResponseRedirect("/thing/" + str(thingid))


class DevAdd(View):
	def post(self, request):
		if request.session["user"]:
			makedev = Device(name=request.POST.get("name"), dev_secret=request.POST.get("devsec"))
			makedev.save()
			User.objects.get(pk=request.session["user"]).devices.add(makedev)
			return HttpResponseRedirect("/things/")


class ThingDel(View):
	def post(self, request):
		if request.session["user"]:
			Thing.objects.filter(id=request.POST.get("id")).delete()
			return HttpResponseRedirect("/things/")


class PropDel(View):
	def post(self, request, thingid):
		if request.session["user"]:
			Property.objects.filter(id=request.POST.get("id")).delete()
			return HttpResponseRedirect("/thing/" + str(thingid))


class DevDel(View):
	def post(self, request):
		if request.session["user"]:
			Device.objects.filter(id=request.POST.get("id")).delete()
			return HttpResponseRedirect("/things/")
