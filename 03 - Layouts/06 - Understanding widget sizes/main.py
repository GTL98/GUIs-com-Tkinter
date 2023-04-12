import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Tamanho dos widgets')
tela.geometry('400x300')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Label 1',
    background='green'
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='red',
    width=50  # a medida não é em pixels, mas sim no tamanho dos caracteres (é melhor usar o "fill" de pack())
)

# Layout pack()
label_1.pack()
label_2.pack()

# Layout grid()
tela.columnconfigure(
    index=(0, 1),
    weight=1,
    uniform='a'
)
tela.rowconfigure(
    index=(0, 1),
    weight=1,
    uniform='a'
)
label_1.grid(
    row=0,
    column=0
)
label_2.grid(
    row=1,
    column=0,
    sticky='news'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
