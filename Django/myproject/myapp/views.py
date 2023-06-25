from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def drinks(request, drink_name):
    drink = {
        "mocha": "Coffee",
        "tea":"Bevarage",
        "lemonade":"Refreshment",
    }
    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2> {drink_name} <h2>" + choice_of_drink)