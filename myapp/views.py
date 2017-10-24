# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.views import generic
def dashboard(request):
	return render(request,"myapp/index.html")

def details(request):
	return render(request,"myapp/details.html")

def contacts(request):
	return render(request,"myapp/contacts.html")

