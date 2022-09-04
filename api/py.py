import threading
import random
from rest_framework.response import Response
from rest_framework .decorators import api_view
from .serializers import Myserializer
from rest_framework import views
from .models import Event
import datetime



global k
k=0
def _start():
    global k, num1
    t = threading.Timer(3.0, _start)
    t.start()
    # #print(k)   
    num1 = random.randint(10, 20) #servers started
    k=k+num1
    time=Event.objects.values_list('program_time').order_by('-id')[0]
    prog_time=(time[0])
    if prog_time==43200:
        prog_time=prog_time + 3
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - start {} servers".format(p_time, num1))
        event=Event(_start=num1, program_time=prog_time)
        event.save()
    else:
        #print(prog_time)
        if prog_time==43208:
            prog_time=prog_time + 1
            def convert(prog_time):
                return str(datetime.timedelta(seconds = prog_time))
            p_time=convert(prog_time)
            print("{} - start {} servers".format(p_time, num1))
            event=Event(_start=num1, program_time=prog_time)
            event.save()
            #print("{} servers started".format(num1))
        else:
            if prog_time==43209:
                prog_time=prog_time + 3
                def convert(prog_time):
                    return str(datetime.timedelta(seconds = prog_time))
                p_time=convert(prog_time)
                print("{} - stop {} servers".format(p_time, n))
                event=Event(_stop=n, program_time=prog_time)
                event.save() 
            else:
                if prog_time==43212:
                    prog_time=prog_time + 3
                    def convert(prog_time):
                        return str(datetime.timedelta(seconds = prog_time))
                    p_time=convert(prog_time)
                    print("{} - start {} servers".format(p_time, num1))
                    event=Event(_start=num1, program_time=prog_time)
                    event.save()
                else:
                    prog_time=prog_time + 2
                    def convert(prog_time):
                        return str(datetime.timedelta(seconds = prog_time))
                    p_time=convert(prog_time)
                    print("{} - start {} servers".format(p_time, num1))
                    event=Event(_start=num1, program_time=prog_time)
                    event.save()
            
    
    
t = threading.Timer(3.0, _start)
t.start() 


def _stop():
    global k, n
    t = threading.Timer(4.0, _stop)
    t.start()
    n = random.randint(5, k)
     #print ("4 sec stopped {} servers".format(n))
    k = k-n #servers running
    time=Event.objects.values_list('program_time').order_by('-id')[0]
    prog_time=(time[0])
    if prog_time==43203:
        prog_time=prog_time + 1
        def convert(prog_time):
            return str(datetime.timedelta(seconds = prog_time))
        p_time=convert(prog_time)
        print("{} - stop {} servers".format(p_time, n))
        event=Event(_stop=n, program_time=prog_time)
        event.save()
    else:
        if prog_time==43209:
            prog_time=prog_time + 3
            def convert(prog_time):
                return str(datetime.timedelta(seconds = prog_time))
            p_time=convert(prog_time)
            print("{} - stop {} servers".format(p_time, n))
            event=Event(_stop=n, program_time=prog_time)
            event.save()
        else:
            prog_time=prog_time + 2
            def convert(prog_time):
                return str(datetime.timedelta(seconds = prog_time))
            p_time=convert(prog_time)
            print("{} - stop {} servers".format(p_time, n))
            event=Event(_stop=n, program_time=prog_time)
            event.save()
     #print("now {} Servers running after 4  secs".format(s))
    

t = threading.Timer(4.0, _stop)
t.start() 


'''def _report():
    global k
    #r=k+r
    t = threading.Timer(5.0, _report)
    t.start()
    time=Event.objects.values_list('program_time').order_by('-id')[0]
    prog_time=(time[0])
    prog_time=prog_time + (5-4)
    def convert(prog_time):
        return str(datetime.timedelta(seconds = prog_time))
    p_time=convert(prog_time)
    print("{} - report {} servers running".format(p_time, k))
    event=Event(_report=k, program_time=prog_time)
    event.save()
     #print ("{} servers running at sec 5".format(r))
    
 

t = threading.Timer(5.0, _report)
t.start()'''



'''class GetStart(views.APIView):
    def get(self, request):
        r
        num1
        n
        res= [{'_start':num1},{'_stop':r},{'_report':n}]
        results= Myserializer(res, many=True).data
        return Response(results)'''



@api_view(['GET'])
def display(request):
    events=Event.objects.all()
    serializer=Myserializer(events, many=True)

    return Response(serializer.data)







  

