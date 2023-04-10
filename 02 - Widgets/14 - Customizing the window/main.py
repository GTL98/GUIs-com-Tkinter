import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Mais do que uma simples tela')

# String de geometry(): 'LARGURAxALTURA+POSIÇÃO HORIZONTAL+POSIÇÃO VERTICAL'
tela.geometry('600x400+100+200')

# Colocar um .ico na tela
tela.iconbitmap('python.ico')

# Tamanho da tela
tela.minsize(200, 100)  # limita o tamanho mínimo da tela
tela.maxsize(800, 600)  # limita o tamanho máximo da tela
tela.resizable(True, True)  # permite redimenzionar em apenas em um dos eixos

# Atributos do monitor
print(tela.winfo_screenwidth())  # informa a largura do monitor, não do app
print(tela.winfo_screenheight())  # informa a altura do monitor, não do app

# Atributos da tela
tela.attributes('-alpha', 1)  # transparência da tela
tela.attributes('-topmost', True)  # a tela do app fica sobre todas as outras

# Evento de segurança
tela.bind(
    '<Escape>',
    lambda evento: tela.quit()
)

tela.attributes('-fullscreen', True)  # a tela fica em tela cheia

# Barra de título
tela.overrideredirect(True)  # a barra de título some, junto com os botões de minimizar, maximizar e fechar
grip = ttk.Sizegrip(master=tela)  # permite redimensionar a tela do app quando não há a barra de título
grip.place(
    relx=1,  # vai de 0 até 1, do começo da tela até o fim do eixo X
    rely=1,  # vai de 0 até 1, do começo da tela até o fim do eixo Y
    anchor='se'  # as siglas são da Rosa dos ventos
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
