import tkinter as tk
from tkinter import ttk


def funcao_botao():
    """Função responsável por dar função ao botão."""
    print('O botão foi pressionado!')


# Criar a tela
tela = tk.Tk()
tela.title('Tela e 02 - Widgets')
tela.geometry('800x500')

# ttk.Label
label = ttk.Label(
    master=tela,
    text='Isso é um teste'
)
label.pack()

# tk.Text
texto = tk.Text(master=tela)
texto.pack()

# ttk.Entry
entrada = ttk.Entry(master=tela)
entrada.pack()

# ttk.Button
botao = ttk.Button(
    master=tela,
    text='Botão',
    command=funcao_botao
)
botao.pack()


if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
