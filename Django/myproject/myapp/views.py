from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from myapp.models import DrinksCategory, Drinks, Booking, Employees, Menu

# Create your views here.
def home(request):
    return render(request, "home.html")

def drinks(request, drink_name):
    drink = {
        "mocha": "Coffee",
        "tea":"Bevarage",
        "lemonade":"Refreshment",
    }
    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2> {drink_name} <h2>" + choice_of_drink)

def about(request):
    return render(request, "about.html")

def menu(request):
    return render(request, "menu.html")

def book(request):
    return render(request, "book.html")

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)