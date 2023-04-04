import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Frames & Parenting')
tela.geometry('600x400')

# Frame
frame = ttk.Frame(
    master=tela,
    width=200,
    height=200,
    borderwidth=1,  # espessura da borda
    relief=tk.GROOVE  # tipo da borda
)
frame.pack_propagate(False)  # isso permite que o tamanho do frame seja do tamanho original, não dos widgets internos
frame.pack(side='left')

# Configurações master
label = ttk.Label(
    master=frame,
    text='Label no frame'
)
label.pack()

botao = ttk.Button(
    master=frame,
    text='Botão no frame'
)
botao.pack()

# Exemplo
label_2 = ttk.Label(
    master=tela,
    text='Label fora do frame'
)
label_2.pack(side='right')

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
