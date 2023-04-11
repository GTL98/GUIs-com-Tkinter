# Colocar 2 botões e 1 entrada:
    # Um botão deve estar nas coordenadas 2,2 preenchendo a célula;
    # Um botão deve estar nas coordenadas 0,2 preenchendo a célula;
    # A entrada deve estar nas coordenadas 3,3 indo da direita para a esquerda e;
    # Utilizar o arquivo main.py como base

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Grid Layout')
tela.geometry('600x400')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Label 1',
    background='red'
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='blue'
)
label_3 = ttk.Label(
    master=tela,
    text='Label 3',
    background='green'
)
label_4 = ttk.Label(
    master=tela,
    text='Label 4',
    background='yellow'
)
botao_1 = ttk.Button(
    master=tela,
    text='Botão 1'
)
botao_2 = ttk.Button(
    master=tela,
    text='Botão 2'
)
entrada = ttk.Entry(master=tela)

# Definir a grade
tela.columnconfigure(
    index=(0, 1, 2),
    weight=1,
    uniform='a'
)
tela.columnconfigure(
    index=3,
    weight=2,
    uniform='a'
)
tela.rowconfigure(
    index=(0, 1, 2),
    weight=1,
    uniform='a'
)
tela.rowconfigure(
    index=3,
    weight=3,
    uniform='a'
)

# Colocar os widgets
label_1.grid(
    row=0,
    column=0,
    sticky='news'
)
label_2.grid(
    row=1,
    column=1,
    rowspan=3,
    sticky='news'
)
label_3.grid(
    row=1,
    column=0,
    columnspan=3,
    sticky='news',
    padx=20,
    pady=10
)
label_4.grid(
    row=3,
    column=3,
    sticky='se'
)
botao_1.grid(
    row=2,
    column=2,
    sticky='news'
)
botao_2.grid(
    row=0,
    column=3,
    sticky='news'
)
entrada.grid(
    row=3,
    column=3,
    sticky='we'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
