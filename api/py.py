
import random

import threading


k=0
def hello():
    t = threading.Timer(3.0, hello)
    t.start()
    global k
    print(k)   
    num1 = random.randint(10, 20) #servers started
    k=k+num1
    print("{} servers running".format(k))
    x=k
    return x

t = threading.Timer(3.0, hello)
t.start() 

def helloo():
    t = threading.Timer(4.0, helloo)
    t.start()
    global k 
    n = random.randint(5, k)
    print ("4 sec stopped {} servers".format(n))
    k= k-n #servers running
    y=k
    print("now {} 4 sec Servers running".format(k))
    return y


t = threading.Timer(4.0, helloo)
t.start() 

def hellooo():
    t = threading.Timer(5.0, hellooo)
    t.start()
    print ("{} servers running at sec 5".format(k))
    z=k
    return z 

t = threading.Timer(5.0, hellooo)
t.start() 

def check():
    z=hellooo()
    print ("{} servers...similar too 5".format(z))

check()





