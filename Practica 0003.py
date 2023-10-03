#from tkinter import*

import tkinter as tk

App = tk.Tk()
App.title("Conversor de Temperatura")

labell = tk.Label(App,text ="Fahrenheit:")
labell.grid(row=0, column=0)

entry1 = tk.Entry(App)
entry1.grid(row=0, column=1)

button1 = tk.Button(App,text="Convertir a Celsius")
button1.grid(row=0, column=2)

label2 = tk.Label(App, text="Celsius")
label2.grid(row=1, column=0)

entry2 =tk.Entry(App)
entry2.grid(row=1, column= 1)

button2 =tk.Button(App, text="Convertir a Fahrenheit")
button2.grid(row=1, column=2)

button3 = tk.Button(App, text= "Restablecer")
button3.grid(row=2, column=1)

App.mainloop()