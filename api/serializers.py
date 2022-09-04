from rest_framework import serializers
from .models import ApiStart, ApiStop, ApiReport


class ApiStartSerializer(serializers.Serializer):
    actual_time=serializers.DateTimeField()
    _start=serializers.IntegerField()
    program_time= serializers.IntegerField()
    class Meta:
        model=ApiStart
        fields=('actual_time', '_start', 'program_time')

class ApiStopSerializer(serializers.Serializer):
    actual_time=serializers.DateTimeField()
    _stop=serializers.IntegerField()
    program_time= serializers.IntegerField()
    class Meta:
        model=ApiStop
        fields=('__all__')

class ApiReportSerializer(serializers.Serializer):
    actual_time=serializers.DateTimeField()
    _report=serializers.IntegerField()
    program_time= serializers.IntegerField()
    class Meta:
        model=ApiReport
        fields=('__all__')


'''class ApiSerializer(serializers.Serializer):
    strtSerializer=ApiStartSerializer(read_only=True, many=True)
    stpSerializer=ApiStopSerializer(read_only=True, many=True)
    rptSerializer=ApiReportSerializer(read_only=True, many=True)
    class Meta:
        model=Api
        fields = ('__all__')'''




'''class Myserializer(serializers.Serializer):
    _start=serializers.IntegerField(required=False)
    _stop=serializers.IntegerField(required=False)
    _report=serializers.IntegerField(required=False)
    class Meta:
        extra_kwargs = {'_start': {"required": False}}
        extra_kwargs = {'_stop': {"required": False}}
        extra_kwargs = {'_stop': {"required": False}}'''

