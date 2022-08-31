import imp
from django.urls import path
from . views import display

urlpatterns=[
#path('', GetStart.as_view(), name="start"),
path('display/', display, name="display")
]