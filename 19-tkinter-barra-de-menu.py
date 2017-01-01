from tkinter import filedialog
from tkinter import *

# configuração da janela
janela = Tk()
menubar = Menu(janela)
janela.config(menu=menubar)
janela.title('Tk Menu')
janela.geometry('300x150+400+200')

# criação das colunas do menu
filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)

# Nomeando cada coluna
menubar.add_cascade(label='Arquivo', menu=filemenu)
menubar.add_cascade(label='Cores', menu=filemenu2)
menubar.add_cascade(label='Ajuda', menu=filemenu3)

# Atribuindo as funções do sistema operacional aos botões
def Open(): filedialog.askopenfilename()
def Save(): filedialog.asksaveasfilename()
def Quit(): janela.destroy()
def ColorBlue(): Text(background='blue').pack()
def ColorRed(): Text(background='red').pack()
def ColorBlack(): Text(background='#000').pack()

filemenu.add_command(label='Abrir...', command=Open)
filemenu.add_command(label='Salvar como...', command=Save)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=Quit)
filemenu2.add_command(label='Meu', command=ColorBlue)
filemenu2.add_command(label='programa', command=ColorRed)
filemenu2.add_command(label='Tá bonito', command=ColorBlack)
janela.mainloop()