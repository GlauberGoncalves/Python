#coding: utf8

from tkinter import *

def click():
	lb1.place(x=0, y=0)
	


#configuração
janela = Tk()
janela["bg"] = "#000"
janela.geometry("400x400+400+100")

# Buttons
btn1 = Button(width=10, text="botão 1", command=click)
btn1.place(x=100, y=100)

btn2 = Button(width=10, text="botão 2", command=click)
btn2.place(x=200, y=100)

lb1 = Label(janela, text="Oi, é nois")
lb1.place(x=100, y=130)



# fim da janela
janela.mainloop()