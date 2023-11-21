# formapp/views.py
from django.shortcuts import render, redirect ,HttpResponse

def welcome(request):
    return HttpResponse ("Welcome :)")


def form_view(request):
    return render(request, 'form.html')

def result_view(request):
# session 
    request.session['name']= request.POST['fname'],
    request.session['Dojo']= request.POST['Dojo_Location'],
    request.session['Favorite']= request.POST['Favorite_language'],
    request.session['text']= request.POST['comment']
    
    return redirect("/show_results")
    
def show(request):
    return render (request, 'show.html')