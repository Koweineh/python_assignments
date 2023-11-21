from django.shortcuts import render, redirect
import random


def index(request):
    if "gold" not in request.session:
        request.session["gold"]= 0
        request.session["activity"]=[]
    return render(request,"index.html")    

def process_money(request):
    category = request.POST["category"]
    x=0
    y=0
    if category == "farm":
        x= 10
        y= 20
    elif category == "cave":
        x= 20
        y= 30    
    elif category == "house":
        x= 30
        y= 40        
    else:
        x = -50
        y = 50    
        
    gold = random.randint(x, y)
    request.session["gold"] += gold
    request.session["activity"].append("You have earned"+ str(gold)+" from "+category+" .")
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')




