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
