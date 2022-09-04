import threading
import random
from rest_framework.response import Response
from rest_framework .decorators import api_view
from .serializers import ApiStartSerializer, ApiStopSerializer, ApiReportSerializer
from .models import ApiStart, ApiStop, ApiReport
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
        prog_time= recorded_time + 3
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - start {} servers".format(p_time, num1))
        event=ApiStart(_start=num1, program_time=prog_time)
        event.save() #save to db
    else:
        prog_time= 43200
        prog_time= prog_time + 3
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - start {} servers".format(p_time, num1))
        event=ApiStart(_start=num1, program_time=prog_time)
        event.save() #save to db
    
    
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
        prog_time= recorded_time + 4
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - stop {} servers".format(p_time, num1))
        event=ApiStop(_stop=num1, program_time=prog_time)
        event.save()
    else:
        prog_time= 43200
        prog_time= prog_time + 4
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - stop {} servers".format(p_time, num1))
        event=ApiStop(_stop=num1, program_time=prog_time)
        event.save() #save to db
    

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
        prog_time= recorded_time + 5
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - reported {} servers".format(p_time, num1))
        event=ApiReport(_report=num1, program_time=prog_time)
        event.save()
    else:
        prog_time= 43200
        prog_time= prog_time + 5
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - report {} servers".format(p_time, num1))
        event=ApiReport(_report=num1, program_time=prog_time)
        event.save() #save to db      
 

t = threading.Timer(5.0, _report)
t.start()




@api_view(['GET'])
def display(request):
    strt=ApiStart.objects.values('actual_time','_start', 'program_time')
    stp=ApiStop.objects.values('actual_time','_stop', 'program_time')
    rpt=ApiReport.objects.values('actual_time','_report', 'program_time')
    strt_obj=ApiStartSerializer(strt, many=True)
    stp_obj=ApiStopSerializer(stp, many=True)
    rpt_obj=ApiReportSerializer(rpt, many=True)
    display=strt_obj.data + stp_obj.data + rpt_obj.data
    return Response(display)    








  


 