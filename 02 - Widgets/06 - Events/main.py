import tkinter as tk
from tkinter import ttk


def obter_posicao(evento):
    """Função responsável por obter a posição XY do mouse."""
    print(f'x: {evento.x} y:{evento.y}')


# Tela
tela = tk.Tk()
tela.title('Eventos')
tela.geometry('600x500')

# Widgets
texto = tk.Text(master=tela)
texto.pack()

entrada = ttk.Entry(master=tela)
entrada.pack()

botao = ttk.Button(
    master=tela,
    text='Botão'
)
botao.pack()

# Eventos (uma string: '<modificador-tipo-detalhe>')
# botao.bind('<Alt-KeyPress-a>', lambda evento: print(evento))
# tela.bind('<KeyPress>', lambda evento: print(f'A tecla {evento.char} foi pressionada'))
#
# texto.bind('<Motion>', obter_posicao)

entrada.bind('<FocusIn>', lambda evento: print('O campo de entrada foi selecionado'))
entrada.bind('<FocusOut>', lambda evento: print('O camp de entrada foi deselecionado'))

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
