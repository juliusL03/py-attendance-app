import datetime

from django.db import models
from django.utils import timezone


class Users(models.Model):
    userID = models.CharField(max_length=6)
    userName = models.CharField(max_length=200)

    def __str__(self):
        return self.userID

class Attendance_log (models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    timeInOut = models.DateTimeField()
    typeInOut = models.CharField(max_length=2)


