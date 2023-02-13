from machine import Pin
import time

farol1=[Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT), Pin(12, Pin.IN, Pin.PULL_UP)] # Green, Yellow, Red, Button
farol2=[Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), farol1[3]] # Green, Yellow, Red, Button

def wait(t:int,farol:list[Pin]):
    ini=time.time()
    while time.time() - ini <= t and farol[3].value():
        pass

def seFarol(farol:list[Pin], vals:list[int]):
    b=Pin(13, Pin.OUT)
    for i in range(0,3): farol[i].value(vals[i])

while True:
    print('Green/Red')
    seFarol(farol1,[1,0,0])
    seFarol(farol2,[0,0,1])
    wait(5,farol1)
    
    print('Yellow/Red')
    seFarol(farol1,[0,1,0])
    time.sleep(2)
    
    print('Red/Green')
    seFarol(farol1,[0,0,1])
    seFarol(farol2,[1,0,0])
    wait(5,farol2)

    print('Red/Yellow')
    seFarol(farol2,[0,1,0])
    time.sleep(2)
 