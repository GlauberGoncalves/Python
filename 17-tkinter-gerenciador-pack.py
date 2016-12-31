from tkinter import *

# configuração da janela
janela = Tk()
janela.geometry("300x300+450+200")
janela["bg"] = "#99d"

# labels 
lb1 = Label(janela, text="label 1", bg="blue")
lb2 = Label(janela, text="label 2", bg="white")
lb3 = Label(janela, text="label 3", bg="green")
lb4 = Label(janela, text="label 4", bg="yellow")

lb1.pack(side=BOTTOM)
lb2.pack(side=LEFT)
lb3.pack(side=TOP)
lb4.pack(side=RIGHT)



janela.mainloop()