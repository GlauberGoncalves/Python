# processamento de dados simples
from tkinter import *

# funções
def somar():
	if(ed1.get().isnumeric() and ed2.get().isnumeric()):
		visor["text"] = float(ed1.get()) + float(ed2.get())
	else: visor["text"] = "Valores não são numericos"


# configuração da janela
janela = Tk()
janela.title("Processamento de dados")
janela.geometry("500x300+400+200")
janela["bg"] = "#cacaca"

# entrada de dados
ed1 = Entry(janela, width=10)
ed1.place(x=10, y=10)

ed2 = Entry(janela, width=10)
ed2.place(x=10, y=30)

# botão
btn =  Button(janela, width=5, text="Somar", command= somar)
btn.place(x=10, y=60)

# visor
visor = Label(janela, width=30)
visor.place(x=10, y=100)

janela.mainloop()