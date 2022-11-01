#!/usr/bin/env python3 
from tkinter import *
import time

root = Tk()
root.title("Clock")
root.attributes('-fullscreen', True)
time1 = ''
clock = Label(root, font=('Arial 170'), bg='#000', fg='#FFF', cursor='none')
clock.pack(fill=BOTH, expand=1)


def tick():
    global time1
    # узнаем время 
    time2 = time.strftime('%H:%M:%S') 
    # фрейм обновляется как только время меняется
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # вызовы идут каждые 200 милисекунд
    clock.after(200, tick)


tick()
root.mainloop()
