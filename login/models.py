from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    school_region=models.CharField(max_length=300)
    school_name=models.CharField(max_length=300)

    def __str__(self):
        return self.school_name

class Groups(models.Model):
    group_number=models.CharField(max_length=300)
    group_teacher=models.ForeignKey(User, on_delete=models.SET_NULL,null=True ,limit_choices_to={'is_staff': True},related_name='teacher_groups')
    group_school=models.ForeignKey(School,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.group_number


class Pupils(models.Model):
    pupil_username=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,limit_choices_to={'is_staff':False},related_name='pupil_profiles')
    pupil_fullname=models.CharField(max_length=300)
    pupil_group=models.ForeignKey(Groups,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.pupil_fullname