from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm

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

def aboutus(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)