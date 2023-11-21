from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    if request.method == 'POST':
        # Handle the form submission
        user_guess = int(request.POST.get('user_guess'))
        correct_number = request.session['correct_number']
        
        if user_guess == correct_number:
            result = "Correct! You guessed the right number."
        elif user_guess < correct_number:
            result = "Too low! Try again."
        else:
            result = "Too high! Try again."
    else:
        # Generate a random number between 1 and 100 and store it in the session
        request.session['correct_number'] = random.randint(1, 100)
        result = None

    return render(request,'home.html', {'result': result})

