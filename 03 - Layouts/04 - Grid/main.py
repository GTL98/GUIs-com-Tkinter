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

# Definir a grade
tela.columnconfigure(
    index=(0, 1, 2),  # escrever assim indica que essas colunas terão o mesmo tamanho
    weight=1,
    uniform='a'  # todas as colunas terão o mesmo tamanho, mesmo que vazias
)
tela.columnconfigure(
    index=3,
    weight=2,
    uniform='a'
)
tela.rowconfigure(
    index=(0, 1, 2),  # escrever assim indica que essas linhas terão o mesmo tamanho
    weight=1,
    uniform='a'  # todas as linhas terão o mesmo tamanho, mesmo que vazias
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
    rowspan=3,  # quantas linhas o widget ocupará do layout
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

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
