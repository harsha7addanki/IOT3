from django.urls import path
from .views import *

urlpatterns = [
	path('', login),
	path('login/', LoginUsr.as_view(), name="login"),
	path('things/', things),
	path('thing/<int:thingid>',thing, name='thing'),
	# Add Urls: Add an thing in that model
	path('thingadd/',ThingAdd.as_view(), name="thinga"),
	path('propadd/<int:thingid>',PropAdd.as_view(), name='propadd'),
	path('devadd/', DevAdd.as_view(), name='devadd'),
	# Delete Urls: Delete an thing in that model
	path('thingdel/',ThingDel.as_view(), name="thingd"),
	path('propdel/<int:thingid>',PropDel.as_view(), name='propdel'),
	path('devdel/', DevDel.as_view(), name='devdel')
]
