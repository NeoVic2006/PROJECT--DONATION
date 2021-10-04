from django.contrib import admin
from django.urls import path, include
from .views import Users_list, DonationsManagement_list, Donation_list, UserViewSet, user_details
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/', Users_list),
    path('users/<int:pk>', Users_list),
    path('Donation/', Donation_list),
    path('DonationsManagement/', DonationsManagement_list),
    path('user_details/<str:pk>/', user_details , name='user_details'),

    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view())

]
 

 