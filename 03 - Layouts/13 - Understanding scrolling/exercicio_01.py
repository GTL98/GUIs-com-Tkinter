# Usando o arquivo main_1.py como base:
    # Criar a scrollbar no eixo X;
    # Essa scrollbar deve estar na base do App;
    # Para movimentar no eixo X, usar a tecla "Ctrl" e a roda do mouse

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
    scrollregion=(0, 0, 2000, 5000)
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

# Rodinha do mouse eixo Y
canvas.bind(
    '<MouseWheel>',
    lambda evento: canvas.yview_scroll(
        -evento.delta // 60,
        'units'
    )
)

# Rodinha do mouse eixo X
canvas.bind(
    '<Control MouseWheel>',
    lambda evento: canvas.xview_scroll(
        -evento.delta // 60,
        'units'
    )
)

# Scrollbar eixo Y
navegacao_y = ttk.Scrollbar(
    master=tela,
    orient='vertical',
    command=canvas.yview
)
canvas.configure(yscrollcommand=navegacao_y.set)
navegacao_y.place(
    relx=1,
    rely=0,
    relheight=1,
    anchor='ne'
)

# Scrollbar eixo X
navegacao_x = ttk.Scrollbar(
    master=tela,
    orient='horizontal',
    command=canvas.xview
)
canvas.configure(xscrollcommand=navegacao_x.set)
navegacao_x.place(
    relx=0,
    rely=1,
    relwidth=1,
    anchor='sw'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
