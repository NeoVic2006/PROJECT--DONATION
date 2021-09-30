from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import User, Donation, DonationsManagement


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'role']
    

class DonationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'


class DonationsManagementSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DonationsManagement
        fields = '__all__'