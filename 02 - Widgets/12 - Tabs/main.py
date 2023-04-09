import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Tabs')
tela.geometry('600x400')

# Notebook widget
notebook = ttk.Notebook(master=tela)

# Criar as abas
tab_1 = ttk.Frame(master=notebook)
label_1 = ttk.Label(
    master=tab_1,
    text='Texto no Tab 1'
)
botao_1 = ttk.Button(
    master=tab_1,
    text='Botão no Tab 1'
)
label_1.pack()
botao_1.pack()

tab_2 = ttk.Frame(master=notebook)
label_2 = ttk.Label(
    master=tab_2,
    text='Texto no Tab 2'
)
entrada = ttk.Entry(master=tab_2)
label_2.pack()
entrada.pack()

# Adiciona a aba no widget
notebook.add(
    tab_1,
    text='Tab 1'
)
notebook.add(
    tab_2,
    text='Tab 2'
)
notebook.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
