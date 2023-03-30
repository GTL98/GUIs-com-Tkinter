# Adicionar uma label escrito "Minha Label" e um botão com a função que printa "olá"
import tkinter as tk
from tkinter import ttk

# Criar a tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('300x150')

# Adicionar a label
label = ttk.Label(
    master=tela,
    text='Minha Label'
)
label.pack()

# Adicionar o botão
botao = ttk.Button(
    master=tela,
    text='Me aperte!',
    command=lambda: print('Olá')
)
botao.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
