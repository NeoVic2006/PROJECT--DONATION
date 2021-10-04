from django.http import HttpResponse, JsonResponse
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User, Donation, DonationsManagement
from .serializers import UserSerialiser, DonationSerialiser, DonationsManagementSerialiser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.reverse import reverse
# Create your views here.


@csrf_exempt
def Users_list(request, id=0):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerialiser(users, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerialiser(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=user_data['id'])
        serializer = UserSerialiser(user, data=user_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == "DELETE":
        user = User.objects.get(id = id)
        user.delete()
        return JsonResponse("Delete Succesfully!", safe = False)





@api_view(['GET'])
def user_details(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerialiser(user, many=False)
    return Response(serializer.data)    


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



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    #authentication_classes = {TokenAuthentication, }
    #permission_classes = {IsAuthenticated, }
