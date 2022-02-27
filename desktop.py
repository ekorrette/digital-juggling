import serial
from time import time
from tkinter import *
from tkinter.ttk import *
from tkinter import font

root = Tk()
root.title('Ball.')
root.geometry("700x500")
root.configure(bg='green')
lbl = Label(root, font = ('TeX Gyre Termes Math', 200, 'bold'),
        background = 'green',
        foreground = 'red'
        )
lbl.place(relx=0.5, rely=0.5, anchor='center')
lblm = Label(root, font = ('TeX Gyre Termes Math', 50, 'bold'),
        background = 'green',
        foreground = 'red'
        )
lblm.place(relx=0.1, rely=0., anchor='nw')
lbl.pack()

serialPort = serial.Serial(port='/dev/rfcomm0', baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)
last = 0
max_count = 0
DELTA = 1.5

def print(thing, other_thing):
    lbl.config(text = str(thing))
    lblm.config(text = 'max: ' + str(other_thing))

throw_count = 0
print(throw_count, max_count)



def loop():
    global last, throw_count
    data = serialPort.read()
    t = time()
    if t - last > DELTA:
        throw_count = 0

    if data:
        throw_count += 1
        max_count = max(max_count, throw_count)
        print(throw_count, max_count)
        last = t
    lbl.after(1, loop)

loop()
root.mainloop()
