from django.db import models

class REG(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100)
    address = models.TextField(default='null')
    password = models.CharField(max_length=100)


class ROC(models.Model):
    username = models.CharField(max_length=100)
    incident_details = models.TextField(default='null')
    area_details = models.TextField(default='null')
    mobile = models.CharField(max_length=100)
    time = models.TextField(default='null')
    type=models.CharField(max_length=100,default="roc")
    PSNumber = models.CharField(max_length=100,default="000")
    victim_details = models.TextField(default='null')
    status = models.TextField(default='delivered')
    
class RAC(models.Model):
    username = models.CharField(max_length=100)
    incident_details = models.TextField(default='null')
    area_details = models.TextField(default='null')
    mobile = models.CharField(max_length=100)
    time = models.TextField(default='null')
    type=models.CharField(max_length=100,default="rac")
    victim_details = models.TextField(default='null')
    PSNumber = models.CharField(max_length=100,default="000")
    image=models.ImageField(upload_to='racpics/')
    status = models.TextField(default='delivered')

class RMC(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    attributes = models.TextField(default='null')
    native_place = models.TextField(default='null')
    applicant_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    time = models.TextField(default='null')
    place_missed = models.TextField(default='null')
    type=models.CharField(max_length=100,default="rmc")
    PSNumber = models.CharField(max_length=100,default="000")
    image=models.ImageField(upload_to='rmcpics/')
    status = models.TextField(default='delivered')

class COP(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    PSNumber = models.CharField(max_length=100)
    

