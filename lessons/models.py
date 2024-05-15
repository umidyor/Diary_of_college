import datetime

from django.db import models
from login.models import *
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class SubjectGroupSchedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Dushanba'),
        ('Tuesday', 'Seshanba'),
        ('Wednesday', 'Chorshanba'),
        ('Thursday', 'Payshanba'),
        ('Friday', 'Juma'),
        ('Saturday', 'Shanba'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher=models.ForeignKey(User,limit_choices_to={'is_staff': True},on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10,choices=DAY_CHOICES)
    date_of_week=models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return f"{self.subject} - {self.group} - {self.day_of_week}"