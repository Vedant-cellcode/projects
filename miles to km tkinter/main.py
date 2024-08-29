from tkinter import *

window=Tk()
window.minsize(width=220,height=110)
window.title('Miles to Km Converter')
window.config(padx=20,pady=20)
window.config(background='yellow')

label1=Label(text='is equal to',font=('ariel',10))
label1.grid(row=1,column=0)

label6 = Label(text=0, font=('ariel',10))
label6.grid(row=1, column=1)

def conversion():
    miles1=float(miles.get())
    km=miles1*1.609
    label5 = Label(text=round(km,3), font=('ariel', 10))
    label5.grid(row=1, column=1)

miles=Entry(width=8)
miles.grid(row=0,column=1)

button =Button(text='Calculate',command=conversion)
button.grid(row=2,column=1)

label2=Label(text='Miles',font=('courier',8))
label2.grid(row=0,column=2)

label3=Label(text='Km',font=('courier',8))
label3.grid(row=1,column=2)

window.mainloop()