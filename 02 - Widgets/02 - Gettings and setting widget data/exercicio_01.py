# Criar um botão que muda o texto da label pela entrada e desabilita a entrada
# Criar um botão que habilita a entrada e escreve na label

import tkinter as tk
from tkinter import ttk


def desabilitar():
    """Função responsável por mudar a label conforme o que tem na entrada
    e desabilitar a entrada."""
    texto_entrada = entrada.get()  # obter a entrada
    label['text'] = texto_entrada  # mudar o texto da label
    entrada['state'] = 'disabled'  # desabilitar a entrada


def habilitar():
    """Função responsável por mudar a label e habilitar a entrada."""
    label['text'] = 'Algum texto'  # mudar o texto da label
    entrada['state'] = 'enabled'  # habilitar a entrada


# Tela
tela = tk.Tk()
tela.title('Exercício 01')

# Label
label = ttk.Label(master=tela)
label.pack()

# Entrada
entrada = ttk.Entry(master=tela)
entrada.pack()

# Botão que desabilita a entrada
botao_desabilitar = ttk.Button(
    master=tela,
    text='Desabilitar',
    command=desabilitar
)
botao_desabilitar.pack()

# Botão que habilita a entrada
botao_habilitar = ttk.Button(
    master=tela,
    text='Habilitar',
    command=habilitar
)
botao_habilitar.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
