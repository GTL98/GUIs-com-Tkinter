import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Scrolling')
tela.geometry('600x400')

# Texto
texto = tk.Text(master=tela)
for i in range(1, 200):
    texto.insert(f'{i}.0', f'Texto: {i}\n')
texto.pack(
    expand=True,
    fill='both'
)

# Scrollbar
navegacao = ttk.Scrollbar(
    master=tela,
    orient='vertical',
    command=texto.yview
)
texto.configure(yscrollcommand=navegacao.set)
navegacao.place(
    relx=1,
    rely=0,
    relheight=1,
    anchor='ne'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
