from django.urls import path
from .views import get, set

urlpatterns = [
    path("get/<str:user>/<str:thing>/<str:dev_secret>/<str:key>",get),
    path("set/<str:user>/<str:thing>/<str:dev_secret>/<str:key>/<str:value>",set),
]