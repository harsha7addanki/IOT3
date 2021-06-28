from django.urls import path
from .views import *

urlpatterns = [
	path('', login),
	path('login/', LoginUsr.as_view(), name="login"),
	path('things/', things)
]
