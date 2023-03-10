from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length = 15, null = True)
    address = models.CharField(max_length = 255, null = True, blank=True)
    designation = models.CharField(max_length = 50, null = True)
    # avatar
    REQUIRED_FIELDS = []


# class Device(models.Model):
#     dev_options = [
#         ('PHONE', 'Phone'),
#         ('TABLET', 'Tablet'),
#         ('LAPTOP', 'Laptop'),
#     ]
#     available_options = [
#         ('AVAILABLE', 'Available'),
#         ('NOT_AVALIABLE', 'Not Available'),
#     ]
#     category = models.CharField(max_length=6, choices=dev_options, default='PHONE')
#     name = models.CharField(max_length=200)
#     available_status = models.CharField(max_length=13, choices=available_options, default='AVAILABLE')
#     # image =
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Log(models.Model):
#     device = models.ForeignKey(Device, on_delete = models.SET_NULL, null=True)
#     employee = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
#     pre_condition = models.CharField(max_length=500, null=True)
#     post_condition = models.CharField(max_length=500, null=True, blank=True)
#     checkout_date = models.DateTimeField(auto_now_add=True)
#     return_date = models.DateTimeField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.employee.username +' -> '+self.device.name