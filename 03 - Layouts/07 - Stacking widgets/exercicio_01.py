# Usar o arquivo main.py como base e adicionar mais uma label e mais
# um botão para sobrepor os widgets

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Sobreposição de widgets')
tela.geometry('400x400')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Label 1',
    background='green'
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='red'
)
label_3 = ttk.Label(
    master=tela,
    text='Label 3',
    background='blue'
)

botao_1 = ttk.Button(
    master=tela,
    text='Botão Label 1',
    command=lambda: label_1.tkraise()
)
botao_2 = ttk.Button(
    master=tela,
    text='Botão Label 2',
    command=lambda: label_2.tkraise()
)
botao_3 = ttk.Button(
    master=tela,
    text='Botão Label 3',
    command=lambda: label_3.tkraise()
)

# Layout
label_1.place(
    x=50,
    y=100,
    width=200,
    height=150
)
label_2.place(
    x=150,
    y=60,
    width=140,
    height=100
)
label_3.place(
    x=75,
    y=80,
    width=100,
    height=70
)

botao_1.place(
    relx=0.6,
    rely=1,
    anchor='se'
)
botao_2.place(
    relx=0.8,
    rely=1,
    anchor='se'
)
botao_3.place(
    relx=1,
    rely=1,
    anchor='se'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
