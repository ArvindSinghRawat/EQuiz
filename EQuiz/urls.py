from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^/adas', views.main, name = 'main'),
    url(r'^', views.signup, name = 'signup'),
]