import imp
from django.urls import path
from . views import display,ReportBtn

urlpatterns=[
#path('', GetStart.as_view(), name="start"),
path('display/', display, name="display"),
path('report/', ReportBtn, name="report")
]