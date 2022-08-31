from rest_framework import serializers
from .models import Event


class Myserializer(serializers.Serializer):
    class Meta:
        model=Event
        fields=('_start','_stop','_report')

class Myserializer(serializers.Serializer):
    _start=serializers.IntegerField(required=False)
    _stop=serializers.IntegerField(required=False)
    _report=serializers.IntegerField(required=False)
    class Meta:
        extra_kwargs = {'_start': {"required": False}}
        extra_kwargs = {'_stop': {"required": False}}
        extra_kwargs = {'_stop': {"required": False}}