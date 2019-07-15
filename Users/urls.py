from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('register', views.register, name = 'register'),
    url('reg_org', views.organisation_register, name='organisation_register'),
    url('admin_signin', views.admin_sigin, name='admin_signin'),
    url('login_success', views.login_success, name='login_success'),
    url('logout', views.logout, name='logout'),
]
