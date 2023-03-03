from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    age = models.IntegerField(max_length=50, blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    phone = models.IntegerField(max_length=50, blank=True, null=False)
    country = models.CharField(max_length=50, blank=True)


def __str__(self):
    return self.name
