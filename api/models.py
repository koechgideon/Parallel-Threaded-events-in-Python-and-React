from datetime import datetime
from django.db import models


class Event(models.Model):
    _start=models.IntegerField(null=True, blank=True)
    _stop=models.IntegerField(null=True, blank=True)
    _report=models.IntegerField(null=True, blank=True)
    actual_time=models.DateField(default=datetime.now)
    program_time=models.DateField(auto_now_add=False)

    

