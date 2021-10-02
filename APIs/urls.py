from django.contrib import admin
from django.urls import path, include
from .views import Users_list, DonationsManagement_list, Donation_list, UserViewSet
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('Users/', Users_list),
    path('Donation/', Donation_list),
    path('DonationsManagement/', DonationsManagement_list),

    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view())

]
 