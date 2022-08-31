import threading
import random
from rest_framework.response import Response
from rest_framework .decorators import api_view
from .serializers import Myserializer
from rest_framework import views
from .models import Event



global k
k=0
def _start():
    global k, num1
    t = threading.Timer(30.0, _start)
    t.start()
    # #print(k)   
    num1 = random.randint(10, 20) #servers started
    k=k+num1
    event=Event(_start=num1)
    event.save()
    # #print("{} servers started".format(num1))
    
    
t = threading.Timer(30.0, _start)
t.start() 


def _stop():
    global k, n
    t = threading.Timer(40.0, _stop)
    t.start()
    n = random.randint(5, k)
     #print ("4 sec stopped {} servers".format(n))
    k = k-n #servers running
    s=k
    event=Event(_stop=n)
    event.save()
    
     #print("now {} Servers running after 4  secs".format(s))
    

t = threading.Timer(40.0, _stop)
t.start() 


def _report():
    global k,r
    r=k+r
    t = threading.Timer(50.0, _report)
    t.start()
    event=Event(_report=k)
    event.save()
     #print ("{} servers running at sec 5".format(r))
    
 

t = threading.Timer(50.0, _report)
t.start()



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







  

