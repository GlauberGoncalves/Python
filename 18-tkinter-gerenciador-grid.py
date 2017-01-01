from tkinter import *

#configuração da janela
janela = Tk()
janela.geometry("300x300+400+200")
janela["bg"] = "#2196f3"


btn1 = Button(janela, text="Access point", bg="white")
btn2 = Button(janela, text="Rádio Frequencia", bg="white")
btn3 = Button(janela, text="Terminal de consulta", bg="white")


btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)




janela.mainloop()