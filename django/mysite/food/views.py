from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context={
        'x': item_list,
    }
    return render(request,'food/index.html',context)


def item (request):
    return HttpResponse("<h1>Hello World!</h1>")