import tkinter as tk
from tkinter import ttk


def funcao_botao(parametro):
    """Função do botão quando usado o lambda."""
    print('O botão foi pressionado')
    print(parametro.get())


def outra_funcao(parametro):
    """Função para evitar a utilização do lambda."""
    def funcao_interna():
        print('O botão foi pressionado')
        print(parametro.get())
    return funcao_interna


# Tela
tela = tk.Tk()
tela.title('Botões, funções e argumentos')

# Widgets
entrada_string = tk.StringVar(value='Teste')
entrada = ttk.Entry(
    master=tela,
    textvariable=entrada_string
)
entrada.pack()

botao = ttk.Button(
    master=tela,
    text='Botão',
    command=outra_funcao(entrada_string)
)
botao.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
