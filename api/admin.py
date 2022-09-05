import imp
from django.contrib import admin
from .models import Api, ApiStart, ApiReport, ApiStop


admin.site.register(Api)
admin.site.register(ApiStart)
admin.site.register(ApiStop)
admin.site.register(ApiReport)
