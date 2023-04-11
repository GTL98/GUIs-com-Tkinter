import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Pack')
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
    text='Última Label',
    background='green'
)
botao = ttk.Button(
    master=tela,
    text='Botão'
)

# Layout
label_1.pack(side='left', expand=True, fill='both')
label_2.pack(side='top', expand=True, fill='both')
label_3.pack(side='top', expand=True, fill='both')
botao.pack(side='top', expand=True, fill='both')

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
