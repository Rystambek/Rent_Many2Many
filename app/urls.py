from django.contrib import admin
from django.urls import path

from app.views.car import CarView
from app.views.customer import CustomerView


urlpatterns = [
    path('car/<int:id>',CarView.as_view()),
    path('car/',CarView.as_view()),
    path('customer/',CustomerView.as_view()),
    path('customer/<int:id>',CustomerView.as_view())
]
