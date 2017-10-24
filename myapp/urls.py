from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (password_change,password_change_done,)
from django.contrib.auth.decorators import login_required
from myapp.views import dashboard,details,contacts

urlpatterns =[
 	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_change/$', password_change, {
        'template_name': 'registration/change_password.html'}, 
        name='password_change'),
    url(r'^password_change_done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^account/$',login_required(dashboard)),
    url(r'^about/$',login_required(details)),
    url(r'^contact/$',login_required(contacts)),
]