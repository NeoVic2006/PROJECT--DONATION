from django.contrib import admin
from .models import User, DonationsManagement, Donation
# Register your models here.


admin.site.register(User)
admin.site.register(DonationsManagement)
admin.site.register(Donation)