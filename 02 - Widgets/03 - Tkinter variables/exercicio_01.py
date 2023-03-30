# Criar 2 entradas e 1 label que devem ser conectados por StringVar
# e devem começar com a palavra "Teste"

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 01')

# StringVar
string_var = tk.StringVar(value='Teste')

# Entrada 1
entrada_1 = ttk.Entry(
    master=tela,
    textvariable=string_var
)
entrada_1.pack()

# Entrada 2
entrada_2 = ttk.Entry(
    master=tela,
    textvariable=string_var
)
entrada_2.pack()

# Label
label = ttk.Label(
    master=tela,
    textvariable=string_var
)
label.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
