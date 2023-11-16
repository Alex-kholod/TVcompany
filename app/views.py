from django.http import HttpResponse
from django.shortcuts import render, redirect
import MySQLdb
from . import services


# Create your views here.
def models_tv(request):
    data = services.get_models_tv()
    return render(request=request, template_name="app/models_tv.html", context=data)


def index(request):
    return render(request=request, template_name="app/index.html")


def shipments(request):
    data = services.get_shipments()
    return render(request=request, template_name="app/shipments.html", context=data)


def supply(request):
    data = services.get_supplies()
    return render(request=request, template_name="app/supply.html", context=data)


def stocks(request):
    data = services.get_stocks()
    return render(request=request, template_name="app/stocks.html", context=data)


def add_supply_form(request):
    if request.method == "POST":
        text = request.POST.get("test_text")
        return redirect('supply')
    return render(request=request, template_name="app/form_add_supply.html")
