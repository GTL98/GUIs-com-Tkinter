# Criar uma Spinbox que contenha as letras A, B, C, D, E
# e mostre o valor sempre que decrescer

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')

# Spinbox
itens = ('A', 'B', 'C', 'D', 'E')
spin_str = tk.StringVar(value=itens[0])
spin = ttk.Spinbox(
    master=tela,
    values=itens,
    textvariable=spin_str
)
spin.bind(
    '<<Decrement>>',
    lambda evento: print(spin_str.get())
)
spin.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
