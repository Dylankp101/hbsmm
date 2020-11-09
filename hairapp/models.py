from django.db import models
import re
from datetime import datetime

class ClientManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Please Enter a valid Email"
        if len(postData['name']) < 3:
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['phone']) < 7:
            errors["phone"] = "Please Enter a valid Phone Number"
        if postData['date']<str(datetime.now()):
            errors["date"] = "Please enter a Valid Date"
        if len(postData['time']) < 0:
            errors["time"] = "Please Enter a valid Time"
        if len(postData['notes']) < 0:
            errors["notes"] = "notes"
        return errors

class Client(models.Model):
    name = models.CharField(max_length=45)
    email = models.TextField(max_length=45)
    phone = models.IntegerField()
    date = models.DateField(null=True, blank=True) 
    time = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    objects = ClientManager()

class AdminManager(models.Manager):
    def l_validator(self,postData):
        errors={}
        stored_username=['sadiemaelogan']
        stored_password=['darwindog123']
        if postData['username'] not in stored_username:
            errors['username'] = "Invalid Username/Password"
        if postData['password'] not in stored_password:
            errors['password'] = ""
        return errors

class Admin(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    objects = AdminManager()









