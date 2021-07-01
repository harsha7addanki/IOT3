from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from models.models import User, Thing, Device


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


class ThingAdd(View):
	def post(self, request):
		makething = Thing(name=request.POST.get("name"),
		                  device=User.objects.get(pk=request.session["user"]).devices.get(pk=request.POST.get("device")))
		makething.save()
		User.objects.get(pk=request.session["user"]).things.add(makething)
		return HttpResponseRedirect("/things/")