import threading
import random
from rest_framework.response import Response
from rest_framework .decorators import api_view
from .serializers import ApiSerializer #ApiStartSerializer, ApiStopSerializer, ApiReportSerializer
from .models import Api, ApiStart, ApiStop, ApiReport
import datetime



global k
k=0
def _start():
    global k, num1
    t = threading.Timer(3.0, _start)
    t.start() 
    num1 = random.randint(10, 20) #servers started
    k=k+num1
    time=ApiStart.objects.values_list('program_time')
    if time:
        time=ApiStart.objects.values_list('program_time').order_by('-id')[0]
        recorded_time=(time[0])
        prog_time= recorded_time + 30
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - start {} servers".format(p_time, num1))
        event=ApiStart(_start=num1, program_time=prog_time)
        event.save() #save to db
        start='start' + ' ' + str(num1) + ' ' + 'servers'
        api=Api(_start=start,program_time=p_time)
        api.save() #save to db
    else:
        prog_time= 43200
        prog_time= prog_time + 30
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - start {} servers".format(p_time, num1))
        event=ApiStart(_start=num1, program_time=prog_time)
        event.save() #save to db
        start='start'+ ' ' + str(num1) + ' ' + 'servers'
        api=Api(_start=start,program_time=p_time)
        api.save()
    
    
t = threading.Timer(3.0, _start)
t.start() 


def _stop():
    global k, n
    t = threading.Timer(4.0, _stop)
    t.start()
    n = random.randint(5, k)
    k = k-n #servers running
    time=ApiStop.objects.values_list('program_time')
    if time:
        time=ApiStop.objects.values_list('program_time').order_by('-id')[0]
        recorded_time=(time[0])
        prog_time= recorded_time + 40
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - stop {} servers".format(p_time, num1))
        event=ApiStop(_stop=k, program_time=prog_time)
        event.save()
        stop='stop' + ' ' + str(n)  + ' ' + 'servers'
        api=Api(_stop=stop,program_time=p_time)
        api.save()
    else:
        prog_time= 43200
        prog_time= prog_time + 40
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - stop {} servers".format(p_time, num1))
        event=ApiStop(_stop=n, program_time=prog_time)
        event.save() #save to db
        stop='stop' + ' ' + str(n)  + ' ' + 'servers'
        api=Api(_stop=stop,program_time=p_time)
        api.save()

    

t = threading.Timer(4.0, _stop)
t.start() 


def _report():
    global k, prog_time
    t = threading.Timer(5.0, _report)
    t.start()
    time=ApiReport.objects.values_list('program_time')
    if time:
        time=ApiReport.objects.values_list('program_time').order_by('-id')[0]
        recorded_time=(time[0])
        prog_time= recorded_time + 50
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - reported {} servers".format(p_time, num1))
        event=ApiReport(_report=k, program_time=prog_time)
        event.save()
        report='report' + ' ' + str(k)  + ' ' + 'servers running'
        api=Api(_report=report,program_time=p_time)
        api.save()
    else:
        prog_time= 43200
        prog_time= prog_time + 50
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - report {} servers running".format(p_time, num1))
        event=ApiReport(_report=k, program_time=prog_time)
        event.save() #save to db  
        report='report' + ' ' + str(k)  + ' ' + 'servers running'
        api=Api(_report=report,program_time=p_time)  
 

t = threading.Timer(5.0, _report)
t.start()




@api_view(['GET'])
def display(request):
    api=Api.objects.all().order_by('-id')[:1]
    serializer=ApiSerializer(api, many=True )
    return Response(serializer.data) 
    
 

'''
@api_view(['GET'])
def display(request):
strt=ApiStart.objects.all().order_by('-id')[:1]
    stp=ApiStop.objects.all().order_by('-id')[:1]
    rpt=ApiReport.objects.all().order_by('-id')[:1]
    strt_obj=ApiStartSerializer(strt, many=True)
    stp_obj=ApiStopSerializer(stp, many=True)
    rpt_obj=ApiReportSerializer(rpt, many=True)
    display=strt_obj.data + stp_obj.data + rpt_obj.data
    api=Api.objects.all().order_by('-id')[:1]
    serializer=ApiSerializer(api, many=True )
    return Response(serializer.data)'''








  


 