import tkinter as tk
from tkinter import ttk


def funcao_botao():
    """Função responsável por dar uma função ao botão."""
    print(string_var.get())
    string_var.set('Botão apertado')


# Tela
tela = tk.Tk()
tela.title('Variáveis Tkinter')

# Variável Tkinter
string_var = tk.StringVar()

# Widgets
label = ttk.Label(
    master=tela,
    text='label',
    textvariable=string_var
)
label.pack()

entrada = ttk.Entry(
    master=tela,
    textvariable=string_var
)
entrada.pack()

botao = ttk.Button(
    master=tela,
    text='Botão',
    command=funcao_botao
)
botao.pack()

if __name__ == '__main__':
    tela.mainloop()
