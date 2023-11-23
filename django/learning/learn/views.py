from django.shortcuts import render, redirect

# Create your views here.
def display_form(request):
    return render(request,'form.html')

def handle_form(request):
    request.session['x'] = request.POST['First_Name']
    request.session['y'] = request.POST['Last_Name']
    request.session['z'] = request.POST['Favorite']
    
    return redirect('/show_results')



def show (request):
    # request.session.flush()
    # del request.session['x']
    return render(request, "show.html")
