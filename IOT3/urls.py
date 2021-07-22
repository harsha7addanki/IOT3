"""IOT3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include("main.urls")),
	path('api/', include("api.urls"))
]


def error_404(request, exception):
	data = {}
	return render(request, 'err/404.html', data, status=404)


def error_500(request):
	data = {}
	return render(request, 'err/500.html', data ,status=500)


def error_400(request, exception):
	data = {}
	return render(request, 'err/400.html', data, status=400)


def error_403(request, exception):
	data = {}
	return render(request, 'err/403.html', data, status=403)


handler404 = error_404
handler500 = error_500
handler403 = error_403
handler400 = error_400
