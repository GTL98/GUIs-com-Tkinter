import tkinter as tk
from tkinter import ttk


def funcao_botao():
    """Função responsável por dar uma função ao botão."""
    print('Um botão básico')
    print(radio_var.get())


# Tela
tela = tk.Tk()
tela.title('Botões')
tela.geometry('600x400')

# Botão
botao_string = tk.StringVar(value='Um botão com StringVar')  # o valor retornado é um str
botao = ttk.Button(
    master=tela,
    text='Botão',
    command=funcao_botao,
    textvariable=botao_string
)
botao.pack()

# Checkbutton
check_var = tk.IntVar(value=10)  # o valor retornado é um int
check_1 = ttk.Checkbutton(
    master=tela,
    text='Checkbutton 1',
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5
)
check_1.pack()

check_2 = ttk.Checkbutton(
    master=tela,
    text='Checkbutton 2',
    command=lambda: check_var.set(5)
)
check_2.pack()

# Radiobutton
radio_var = tk.StringVar()  # melhor saída, pois transforma tudo em string
radio_1 = ttk.Radiobutton(
    master=tela,
    text='Radiobutton 1',
    value='radio_1',  # qualquer coisa para deixar o ID único
    variable=radio_var,
    command=lambda: print(radio_var.get())
)
radio_1.pack()

radio_2 = ttk.Radiobutton(
    master=tela,
    text='Radiobutton 2',
    value=2,  # qualquer coisa para deixa o ID único
    variable=radio_var
)
radio_2.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
