#coding: utf8

from tkinter import *

def bt_click():
	bt.place(x=50, y=50)
	lb["text"] = "Funcionou tinindo que ta tinindo"

janela = Tk()

lb = Label(janela, text="Fala ae galera!!!")
lb.place(x=100, y=130)
janela["bg"] = "#2196f3"
janela.geometry("300x300+400+100")

bt = (Button(janela, width=20, text="OK", command=bt_click))
bt.place(x=10, y=10)


janela.mainloop()