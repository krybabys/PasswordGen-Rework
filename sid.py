import os
import tkinter as tk
from tkinter import font
from urllib import response
from PIL import Image,ImageTk
import random
import secrets
import string


h = 400
w = 600

root = tk.Tk ()
root.minsize(w, h)
root.maxsize(w, h)
canvas = tk.Canvas(root, height= h , width = w,  bg = 'grey')
canvas.pack()


background_Image = ImageTk.PhotoImage(Image.open('/Users/nicolasmorgan/coding/test.jpeg'))
background_Lable = tk.Label(root, image= background_Image)
background_Lable.place(relheight= 1, relwidth= 1)

frame = tk.Frame(root, bg = 'black', bd=3)
frame.place(relheight= 0.1, relwidth= 0.5, relx= 0.5, rely= 0.2, anchor= 'n')

e = tk.Entry(frame, font= 25, bg = 'grey', fg = 'white')
e.place(relheight= 1 , relwidth= .75)

# Password Generator


def pas(value):
    value = int(value) -1
    p ="".join(secrets.choice(string.punctuation + string.digits + string.ascii_letters) for x in range (value))
    password_output['text'] = 'test'






button1 = tk.Button(frame , font = 40, text = 'test', bg = 'white', command=lambda: pas(e.get()))
button1.place(relheight= 1 , relx = .78)

lower_frame = tk.Frame(root, bg = 'black', bd = 4)
lower_frame.place(relheight= .5 , relwidth=.8, rely = .9 ,relx =.5,anchor = 's')
frame2= tk.Frame(lower_frame, bg='grey')
frame2.place(relheight=1,relwidth=1)


password_output_frame = tk.Frame(lower_frame,bg = 'black', bd = 5)
password_output_frame.place(relheight=.3,relwidth=.8 ,relx = .1, rely = .15)
password_output = tk.Label(password_output_frame, bg='white', text='')
password_output.place(relheight=1, relwidth= 1)


root.mainloop()

