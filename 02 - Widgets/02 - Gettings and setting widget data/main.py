import tkinter as tk
from tkinter import ttk


def funcao_botao():
    """Função responsável por dar uma função ao botão."""
    # Obter o valor da entrada
    texto_entrada = entrada.get()

    # Atualizar a label
    # label.configure(text='Uma outra label')
    label['text'] = texto_entrada  # funciona da mesma forma que a linha de cima
    entrada['state'] = 'disabled'


# Tela
tela = tk.Tk()
tela.title('Obter e configurar os widgets')

# Widgets
label = ttk.Label(
    master=tela,
    text='Uma Label'
)
label.pack()

entrada = ttk.Entry(master=tela)
entrada.pack()

botao = ttk.Button(
    master=tela,
    text='Botão',
    command=funcao_botao
)
botao.pack()

if __name__ == '__main__':
    tela.mainloop()
