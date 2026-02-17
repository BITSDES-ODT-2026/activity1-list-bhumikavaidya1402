#Create any from machine import Pin
from machine import Pin
import time
#18,19,33,32
y1= Pin(18,Pin.OUT)
b1=Pin(19,Pin.OUT)
y2=Pin(33,Pin.OUT)
b2= Pin(32,Pin.OUT)


led= [[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]]

for i in led:
    y1.value(i[0])
    b1.value(i[1])
    y2.value(i[2])
    b2.value(i[3])
    time.sleep(0.3)

Code 2- 

from machine import Pin
import time
#5,14,15,19
c1= Pin(5,Pin.OUT)
c2=Pin(14,Pin.OUT)
c3=Pin(15,Pin.OUT)
c4= Pin(19,Pin.OUT)

while True:
    
    #1
    c1.value(1)
    c2.value(0)
    c3.value(0)
    c4.value(0)
    time.sleep_ms(5)

    #2
    c1.value(0)
    c2.value(1)
    c3.value(0)
    c4.value(0)
    time.sleep_ms(5)

    #3
    c1.value(0)
    c2.value(0)
    c3.value(1)
    c4.value(0)
    time.sleep_ms(5)
    
    #4
    c1.value(0)
    c2.value(0)
    c3.value(0)
    c4.value(1)
    time.sleep_ms(5)
