from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """"
    The user of the Donation System
    """
    ROLE_CHOICES = (('admin', 'admin'), ('user', 'user'))
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique = True, null = False)
    first_name = models.CharField(max_length=50, null = False)
    last_name = models.CharField(max_length=100, null = True)
    password = models.CharField(max_length=100, null = False)
    email = models.EmailField(max_length = 254, null =True)
    role = models.CharField(choices = ROLE_CHOICES, max_length=50 , null = False)

    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    
    REQUIRED_FIELDS = ['password']


    def __str__(self):
        return self.first_name


class Donation(models.Model):
    """
    Donation details API. 
    """
    # donationName = models.ForeignKey(DonationsManagement, on_delete=CASCADE)
    donationName = models.CharField(max_length=50, null= False)
    description = models.CharField(max_length=500, null= True)

    def donationId(self):
        return self.id

    def __str__(self):
        return self.donationName



class DonationsManagement(models.Model):
    """
    Donation Management API
    """
    donationType = models.ForeignKey(Donation, on_delete=CASCADE)
    amount = models.IntegerField(null = False, default = 0)
    date = models.DateTimeField(auto_now_add=True)
    userName = models.ForeignKey(User, on_delete=CASCADE)

    def user_name(self):
        return self.userName.username

    def donation_type(self):
        return self.donationType.donationName

    def __str__(self):
        return str(self.donationType)

