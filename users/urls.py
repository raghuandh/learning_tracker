from django.urls import re_path as url3
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # login page
    url3(r'^login/$', LoginView.as_view(template_name='users/login.html'),\
        name='login'),
    # logout page
    url3(r'^logout/$', views.logout_view, name='logout'),
    # registration
    url3(r'^register/$', views.register, name='register'),
]