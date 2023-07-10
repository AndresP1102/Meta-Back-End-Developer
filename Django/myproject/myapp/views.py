from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from myapp.models import DrinksCategory, Drinks, Booking, Employees, Menu

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

def about(request):
    return HttpResponse("About us")

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {"menu": menu_items}
    return render(request, "menu.html", items_dict)

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