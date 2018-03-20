from django.db import models

# Create your models here.
class RegistrationTable(models.Model):
    name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    email = models.EmailField(max_length=50 , unique = True)
    mobile = models.CharField(max_length = 15)
    def __str__(self):
        return self.name

class EventTable(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length = 15)
    event = models.CharField(max_length=200)

    def __str__(self):
        return self.event
