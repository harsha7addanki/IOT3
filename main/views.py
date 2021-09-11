from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from models.models import User, Thing, Device, Property
import  base64


# Create your views here.
def logout(request):
	del request.session["user"]
	return HttpResponseRedirect("/")


def login(request):
	try:
		request.session["user"]
	except KeyError:
		return render(request, "login.html")
	return HttpResponseRedirect("/things/")


class SignUp(View):
	def post(self, request):
		user = User(username=request.POST.get("username"), password=request.POST.get("pass"))
		user.save()
		request.session["user"] = request.POST.get("username")
		return HttpResponseRedirect("/things/")


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
	try:
		request.session["user"]
	except KeyError:
		return render(request, "login.html")
	context = {
		"things": User.objects.get(pk=request.session["user"]).things.all(),
		"devices": User.objects.get(pk=request.session["user"]).devices.all()
	}
	print(User.objects.get(pk=request.session["user"]).devices.all())
	return render(request, "things.html", context)


def thing(request, thingid):
	try:
		request.session["user"]
	except KeyError:
		return render(request, "login.html")
	context = {
		"thing": User.objects.get(pk=request.session["user"]).things.get(pk=thingid)
	}
	return render(request, "thing.html", context)


class ThingAdd(View):
	def post(self, request):
		try:
			request.session["user"]
		except KeyError:
			return render(request, "login.html")
		makething = Thing(name=request.POST.get("name"),
		                  device=User.objects.get(pk=request.session["user"]).devices.get(pk=request.POST.get("device")),
		                  thing_secret=request.POST.get("secret")
		                  )
		makething.save()
		User.objects.get(pk=request.session["user"]).things.add(makething)
		return HttpResponseRedirect("/things/")


class PropAdd(View):
	def post(self, request, thingid):
		try:
			request.session["user"]
		except KeyError:
			return render(request, "login.html")
		makeprop = Property(key=request.POST.get("key"), type=request.POST.get("type"))
		makeprop.save()
		User.objects.get(pk=request.session["user"]).things.get(pk=thingid).properties.add(makeprop)
		return HttpResponseRedirect("/thing/" + str(thingid))


class DevAdd(View):
	def post(self, request):
		try:
			request.session["user"]
		except KeyError:
			return render(request, "login.html")
		makedev = Device(name=request.POST.get("name"), dev_secret=request.POST.get("devsec"))
		makedev.save()
		User.objects.get(pk=request.session["user"]).devices.add(makedev)
		return HttpResponseRedirect("/things/")


class ThingDel(View):
	def get(self, request, id):
		try:
			request.session["user"]
		except KeyError:
			return render(request, "login.html")
		Thing.objects.filter(id=id).delete()
		return HttpResponseRedirect("/things/")


class PropDel(View):
	def get(self, request, thingid, id):
		try:
			request.session["user"]
		except KeyError:
			return render(request, "login.html")
		Property.objects.filter(id=id).delete()
		return HttpResponseRedirect("/thing/" + str(thingid))


class DevDel(View):
	def get(self, request, id):
		try:
			request.session["user"]
		except KeyError:
			return render(request, "login.html")
		Device.objects.filter(id=id).delete()
		return HttpResponseRedirect("/things/")
