from tkinter import *
# funções
def escreve():
	lb["text"] = ed.get()


# configuração da janela
janela = Tk()
janela.title("Tkinter - Entry")
janela["bg"] = "#616161"
janela.geometry("500x300+400+200")

#### Área de trabalho da janela
# caixa de entrada
ed = Entry(janela) 
ed.place(x=10, y=50)

# botão
btn = Button(janela, width = 10, text="Buscar", command=escreve)
btn.place(x=10, y=10)

# Label
lb = Label(janela,width=30, text="oi")
lb.place(x=10, y=80)



janela.mainloop()