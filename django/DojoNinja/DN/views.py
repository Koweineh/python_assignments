from django.shortcuts import render,HttpResponse,redirect
from .models import Dojo,Ninja

# Create your views here.
def method1(request):
    context = { 
               'xxx' : Dojo.objects.all() ,
        
    }
    return render(request, 'form.html', context)

def method2(request):
    Dojo.objects.create(name=request.POST['dname'],city=request.POST['city'],state=request.POST['state'])
    return redirect("/")

def method3(request):
   Ninja.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],dojos=Dojo.objects.get(id=request.POST['dojosss']))
   return redirect("/")