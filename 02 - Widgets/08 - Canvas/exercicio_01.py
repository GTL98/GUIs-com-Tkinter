# Usar os eventos "bind" para criar um paint básico

import tkinter as tk


def desenhar_canvas(evento):
    """Função responsável por desenhar no canvas."""
    x = evento.x
    y = evento.y
    canvas.create_oval(
        (
            x-tamanho_pincel/2,
            y-tamanho_pincel/2,
            x+tamanho_pincel/2,
            y+tamanho_pincel/2
        ),
        fill='black'
    )


def ajuste_pincel(evento):
    """Função responsável por ajustar o tamanho do pincel."""
    global tamanho_pincel
    if evento.delta > 0:
        tamanho_pincel += 4
    else:
        tamanho_pincel -= 4

    # Limitar o tamanho do pincel
    tamanho_pincel = max(0, min(tamanho_pincel, 50))


# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('600x400')

# Canvas
canvas = tk.Canvas(
    master=tela,
    bg='white'
)
canvas.pack()

# Desenhar no canvas
tamanho_pincel = 2
canvas.bind(
    '<Motion>',
    desenhar_canvas
)
canvas.bind(
    '<MouseWheel>',
    ajuste_pincel
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()