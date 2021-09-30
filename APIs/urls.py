from django.contrib import admin
from django.urls import path
from .views import Users_list, DonationsManagement_list, Donation_list


urlpatterns = [
    path('Users/', Users_list),
    path('Donation/', Donation_list),
    path('DonationsManagement/', DonationsManagement_list),
]
