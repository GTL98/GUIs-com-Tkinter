import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Canvas')
tela.geometry('600x400')

# Canvas
canvas = tk.Canvas(
    master=tela,
    bg='white'
)
canvas.pack()

# Retângulo
canvas.create_rectangle(
    (50, 20, 100, 200),  # coordenadas do retângulo
    fill='red',  # cor do retângulo
    width=10,  # largura da linha do retângulo
    dash=(1, 2, 1, 1),  # padrão da linha do retângulo
    outline='green'  # cor da linha do retângulo
)

# Polígono
canvas.create_polygon(
    (0, 0, 100, 200, 300, 50, 150, -50),  # coordenadas dos pontos
    fill='gray'  # cor do polígono
)

# Círculo
canvas.create_oval(
    (200, 50, 300, 150),  # dimensões do círculo
    fill='green'  # cor do círculo
)

# Arco
canvas.create_arc(
    (200, 50, 300, 150),  # coordenadas do arco
    fill='red',  # cor do arco
    start=45,  # ângulo inicial do arco
    extent=140,  # ângulo final do arco
    style=tk.CHORD,  # estilo da linha do arco
    outline='blue',  # cor da linha que representa o arco
    width=5  # espessura da linha do arco
)

# Linha
canvas.create_line(
    (0, 0, 100, 150),  # pontos de começo e fim da linha
    fill='blue'  # cor da linha
)

# Texto
canvas.create_text(
    (100, 200),  # posição do texto
    text='Isso é um texto!',  # texto a ser escrito
    fill='green',  # cor do texto
    width=10
)

# Widgets com canvas
canvas.create_window(
    (150, 100),
    window=ttk.Button(
        master=tela,
        text='Isso é um texto!'
    )
)


if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
