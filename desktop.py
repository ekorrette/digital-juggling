import serial
from time import time
from tkinter import *
from tkinter.ttk import *
from tkinter import font

root = Tk()
root.title('Ball.')
lbl = Label(root, font = ('TeX Gyre Termes Math', 100, 'bold'),
        background = 'green',
        foreground = 'red')
lbl.pack(anchor = 'center')

print(font.families())

serialPort = serial.Serial(port='/dev/rfcomm0', baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)
last = 0
DELTA = 1.5

def print(thing):
    lbl.config(text = 'count: ' + str(thing))

throw_count = 0
print(throw_count)



def loop():
    global last, throw_count
    data = serialPort.read()
    t = time()
    if t - last > DELTA:
        throw_count = 0

    if data:
        throw_count += 1
        #print(data)
        #print(int.from_bytes(data, 'little', signed=True))
        
        #count += 1
        print(throw_count//2)
        last = t
    lbl.after(1, loop)

loop()
root.mainloop()
