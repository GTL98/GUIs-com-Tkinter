# Criar 2 Radibutton e 1 Checkbutton
# Radiobutton:
    # Os valores devem ser "A" e "B";
    # Selecionar qualquer um dos 2 deve mostrar o valor do Checkbutton;
    # Selecionar um Radiobutton desmarca o Checkbutton
# Checkbutton:
    # Selecionar o Checkbutton mostra os valores dos Radiobutton
    # Usar BooleanVar do Tkinter

import tkinter as tk
from tkinter import ttk


def funcao_radio():
    """Função responsável por dar uma função ao Radiobutton."""
    print(check_var.get())
    check_var.set(False)


# Tela
tela = tk.Tk()
tela.title('Exercício 01')

# Vars
check_var = tk.BooleanVar()
radio_var = tk.StringVar()

# Radiobutton
radio_1 = ttk.Radiobutton(
    master=tela,
    text='Radiobutton 1',
    value='A',
    variable=radio_var,
    command=funcao_radio
)
radio_1.pack()

radio_2 = ttk.Radiobutton(
    master=tela,
    text='Radiobutton 2',
    value='B',
    variable=radio_var,
    command=funcao_radio
)
radio_2.pack()

# Checkbutton
check = ttk.Checkbutton(
    master=tela,
    text='Checkbutton',
    variable=check_var,
    command=lambda: print(radio_var.get())
)
check.pack()

if __name__ == '__main__':
    # Mostar a tela
    tela.mainloop()
