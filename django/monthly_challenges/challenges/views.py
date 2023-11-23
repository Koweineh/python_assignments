from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from . import views
from django.urls import reverse



monthly_challenges = {
    "january": "Eat no meant for the entire month",
    "february": "Walk for a  least 20 minutes every day !",
    "march": "Learn Django for a least 20 minutes every day",
    "april": "Learn Django for a least 20 minutes every day",
    "may": "Learn Django for a 40 minutes every day",
    "june": "Learn Django for a 44 minutes every day",
    "july": "Learn Django for a 21",
    "august": "Learn Django for a 1231 minutes every day",
    "september": "Learn Django for a 123 minutes every day",
    "october": "Learn Django for a 12 31 minutes every day",
    "november": "Learn Django for a 213 123 minutes every day",
    "december": "Learn Django for a 123 1545 minutes every day",
}


def view_month(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        list_items += f"<li><a href='{" "}'</a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("NOT FOUND")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        x = "<h1>this month is not Supported!!!!!</h1>"
        return HttpResponseNotFound(x)
