from django.shortcuts import render,HttpResponse,redirect
from .models import User

# Create your views here.
def method1(request):
    return render(request,"form.html")


def method2(request):
    User.objects.create(name=request.POST["name"],email=request.POST["email"],age=request.POST["age"])
    
    return redirect("/xxx")



def method3 (request):
    context ={
    'allusers':User.objects.all(),
    }
    return render(request,"form.html",context)