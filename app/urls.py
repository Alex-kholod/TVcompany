from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="main"),
    path('/models', views.models_tv, name="models"),
    path('/shipments', views.shipments, name="shipments"),
    path('/supply', views.supply, name="supply"),
    path('/stocks', views.stocks, name="stocks"),
]