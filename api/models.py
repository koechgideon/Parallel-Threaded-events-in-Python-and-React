from datetime import datetime
from django.db import models


class Api(models.Model):
    actual_time=models.TimeField(auto_now_add=True)
    _start=models.TextField(max_length=200,null=True, blank=True)
    _stop=models.TextField(max_length=200,null=True, blank=True)
    _report=models.TextField(max_length=200,null=True, blank=True)
    program_time=models.CharField(max_length=200, null=False, blank=False)

class ApiStart(models.Model):
    actual_time=models.DateTimeField(auto_now_add=True)
    _start=models.IntegerField(null=True, blank=True)
    program_time=models.IntegerField(null=False, blank=False)

class ApiStop(models.Model):
    actual_time=models.DateTimeField(auto_now_add=True)
    _stop=models.IntegerField(null=True, blank=True)
    program_time=models.IntegerField(null=True, blank=True)

class ApiReport(models.Model):
    actual_time=models.DateTimeField(auto_now_add=True)
    _report=models.IntegerField(null=True, blank=True)
    program_time=models.IntegerField(null=True, blank=True)
    



