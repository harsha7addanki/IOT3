from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	path('', login),
	path('login/', LoginUsr.as_view(), name="login"),
	path('things/', things),
	path('thing/<int:thingid>',thing, name='thing'),
	path('logout/',logout, name='logout'),
	path('signup/',SignUp.as_view(), name='signup'),
	# Add Urls: Add an thing in that model
	path('thingadd/',ThingAdd.as_view(), name="thinga"),
	path('propadd/<int:thingid>',PropAdd.as_view(), name='propadd'),
	path('devadd/', DevAdd.as_view(), name='devadd'),
	# Delete Urls: Delete an thing in that model
	path('thingdel/<int:id>',ThingDel.as_view(), name="thingd"),
	path('propdel/<int:thingid>/<int:id>',PropDel.as_view(), name='propdel'),
	path('devdel/<int:id>', DevDel.as_view(), name='devdel')
]

urlpatterns += staticfiles_urlpatterns()
