import tkinter as tk
import ttkbootstrap as ttk


def conversor():
    """Função responsável por converter milhas para km."""
    entrada_milha = entrada_int.get()
    saida_km = entrada_milha * 1.609
    saida_string.set(f'{saida_km} Km')


# Tela
tela = ttk.Window(themename='darkly')
tela.title('Demo')  # nome da tela
tela.geometry('300x150')  # dimensões da tela

# Label
label_titulo = ttk.Label(
    master=tela,  # onde será colocado a label
    text='Milhas para Km',  # texto da label
    font='Calibri 24 bold'  # características da fonte
)
label_titulo.pack()  # colocar a label na tela

# Campo de entrada
frame_entrada = ttk.Frame(master=tela)  # colocar outros widgets juntos
entrada_int = tk.IntVar()
entrada = ttk.Entry(
    master=frame_entrada,
    textvariable=entrada_int
)
botao = ttk.Button(
    master=frame_entrada,
    text='Converter',
    command=conversor
)
entrada.pack(
    side='left',
    padx=10
)
botao.pack(side='right')
frame_entrada.pack(pady=10)

# Saída
saida_string = tk.StringVar()
label_saida = ttk.Label(
    master=tela,
    text='Saída',
    font='Calibri 24',
    textvariable=saida_string
)
label_saida.pack(pady=5)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
