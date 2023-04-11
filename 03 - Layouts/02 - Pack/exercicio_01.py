# Criar um layout

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('400x600')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Primeira Label',
    background='red'
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='blue'
)
label_3 = ttk.Label(
    master=tela,
    text='Última Label das Labels',
    background='green'
)
botao = ttk.Button(
    master=tela,
    text='Botão'
)

# Layout
label_1.pack(
    side='top',
    fill='x'
)
label_2.pack(
    side='top',
    expand=True
)
label_3.pack(
    side='top',
    expand=True,
    fill='both'
)
botao.pack(
    side='top',
    fill='x'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
