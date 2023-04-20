import tkinter as tk
from tkinter import ttk
from random import randint, choice

# Tela
tela = tk.Tk()
tela.title('Scrolling')
tela.geometry('600x400')

# Canvas
canvas = tk.Canvas(
    master=tela,
    bg='white',
    scrollregion=(0, 0, 2000, 5000)  # isso permite que o Canvas tenha mais espaço, pode scrolar por ele
)
canvas.create_line(0,
                   0,
                   2000,
                   5000,
                   fill='green',
                   width=10)
for i in range(100):
    esquerda = randint(0, 2000)
    topo = randint(0, 5000)
    direita = esquerda + randint(10, 500)
    baixo = topo + randint(10, 500)
    cor = choice(('red', 'green', 'blue', 'yellow', 'orange'))
    canvas.create_rectangle(
        esquerda,
        topo,
        direita,
        baixo,
        fill=cor
    )
canvas.pack(
    expand=True,
    fill='both'
)

# Rodinha do mouse
canvas.bind(
    '<MouseWheel>',
    lambda evento: canvas.yview_scroll(
        -evento.delta // 60,  # de quanto em quanto será feito o scroll
        'units'  # a unidade: pode ser "units" ou "pages"
    )
)

# Scrollbar
navegacao = ttk.Scrollbar(
    master=tela,
    orient='vertical',
    command=canvas.yview  # permite scrollar para baixo da tela
)
canvas.configure(yscrollcommand=navegacao.set)  # isso permite que a barra de navegação tenha o tamanho correto
navegacao.place(
    relx=1,
    rely=0,
    relheight=1,
    anchor='ne'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
