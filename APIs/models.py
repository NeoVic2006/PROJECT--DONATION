from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class User(models.Model):
    """"
    The user of the Donation System
    """
    firstName = models.CharField(max_length=50, null = False)
    lastName = models.CharField(max_length=100, null = False)
    email = models.EmailField(max_length = 254, null =True)
    role = models.CharField(max_length=50 , null = False)  # this should be True
    
    def __str__(self):
        return self.firstName


class Donation(models.Model):
    """
    Donation details API. 
    """
    # donationName = models.ForeignKey(DonationsManagement, on_delete=CASCADE)
    donationName = models.CharField(max_length=50, null= False)
    description = models.CharField(max_length=500, null= True)

    def __str__(self):
        return self.donationName    



class DonationsManagement(models.Model):
    """
    Donation Mangement API
    """
    donationType = models.ForeignKey(Donation, on_delete=CASCADE)
    amount = models.IntegerField(null = False, default = 0)
    date = models.DateTimeField(auto_now_add=True)
    userName = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return str(self.donationType)
