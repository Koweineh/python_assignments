from django.shortcuts import render,redirect

# Create your views here.
def display_form(request):
    return render(request,"form.html")

def handle_form(request):
 
    request.session['x']= request.POST['fname']
    request.session['y']= request.POST['lname']
    request.session['z']= request.POST['favorite']
    
    return redirect('/show_results')

def result_form(request):
    # request.session.flush()
    del request.session['x']
    return render(request,"show.html")