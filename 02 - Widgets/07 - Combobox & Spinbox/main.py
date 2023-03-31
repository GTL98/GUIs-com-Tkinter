import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Combobox & Spinbox')
tela.geometry('600x400')

# Combobox
itens = ['Sorvete', 'Pizza', 'Refri']  # criar uma lista com os itens
comida_string = tk.StringVar(value=itens[0])
combo = ttk.Combobox(
    master=tela,
    textvariable=comida_string
)
combo['values'] = itens  # o parâmetro "values" pode ser usado na própria classe "Combobox(values=)"
combo.pack()

# Eventos
combo.bind(
    '<<ComboboxSelected>>',
    lambda evento: combo_label.configure(text=f'A comida selecionada foi: {comida_string.get()}')
)

# Label
combo_label = ttk.Label(
    master=tela,
    text='label',
)
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
    master=tela,
    from_=3,
    to=20,
    increment=3,
    textvariable=spin_int,
    command=lambda: print('uma seta foi pressionada')
)
spin.bind('<<Increment>>', lambda evento: print('Aumenta'))
spin.bind('<<Decrement>>', lambda evento: print('Diminui'))
spin.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
