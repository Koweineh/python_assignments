from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from . import views

def index(request):
    return HttpResponse("hello")

