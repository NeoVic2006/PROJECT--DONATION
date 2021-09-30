import re
from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import User, Donation, DonationsManagement
from .serializers import UserSerialiser, DonationSerialiser, DonationsManagementSerialiser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Users_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerialiser(users, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerialiser(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Donation_list(request):
    if request.method == "GET":
        donation = Donation.objects.all()
        serializer = DonationSerialiser(donation, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = DonationSerialiser(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def DonationsManagement_list(request):
    if request.method == "GET":
        donation_management = DonationsManagement.objects.all()
        serializer = DonationsManagementSerialiser(donation_management, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = DonationsManagementSerialiser(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)