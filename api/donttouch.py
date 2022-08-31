import threading
import random
from rest_framework.response import Response
from rest_framework .decorators import api_view
from api.serializers import Myserializer
from rest_framework import views





k=0
num1=0
n=0
def _start():
    t = threading.Timer(3.0, _start)
    t.start()
    global k, num1
    k=k+0
    print(k)   
    num1 = random.randint(10, 20) #servers started
    k=k+num1
    print("{} servers running".format(k))
    
    
t = threading.Timer(3.0, _start)
t.start() 


def _stop():
    t = threading.Timer(4.0, _stop)
    t.start()
    global k,n
    k=k+0 
    n = random.randint(5, k)
    print ("4 sec stopped {} servers".format(n))
    k= k-n #servers running
    
    print("now {} 4 sec Servers running".format(k))
    

t = threading.Timer(4.0, _stop)
t.start() 


def _report():
    t = threading.Timer(5.0, _report)
    t.start()
    print ("{} servers running at sec 5".format(k))
    
 

t = threading.Timer(5.0, _report)
t.start() 

'''def check():
    z=hellooo()
    print ("{} servers...similar too 5".format(z))'''


    

class GetStart(views.APIView):
    
    def get(self, request):
        k
        num1
        n
        res= [{'_start':num1},{'_stop':k},{'_report':n}]
        results= Myserializer(res, many=True).data
        return Response(results)

@api_view()
def hello_world(request):

    return Response({"message": "Hello, world!"})

@api_view()
def aki(request):
    
    return Response({"message": "Hello, world!"})



  

