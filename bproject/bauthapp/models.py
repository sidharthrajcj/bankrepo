
# Create your models here.
from django.db import models
from django.urls import reverse


class user(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Materials(models.Model):
    name=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    age = models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone_number = models.CharField(max_length=10)
    mail_id = models.EmailField(null=True, blank=True)
    address = models.TextField()
    account = models.CharField(max_length=1, choices=[('S', 'Savings_Account'), ('C', 'Current_Account'), ('O', 'Other_Account')])
    materials=models.ManyToManyField(Materials,blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branches = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name