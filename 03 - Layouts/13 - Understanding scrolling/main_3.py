import tkinter as tk
from tkinter import ttk
from random import choice

# Tela
tela = tk.Tk()
tela.title('Scrolling')
tela.geometry('600x400')

# Treeview
tabela = ttk.Treeview(
    master=tela,
    columns=(1, 2),
    show='headings'
)
tabela.heading(
    1,
    text='Nome'
)
tabela.heading(
    2,
    text='Sobrenome'
)
nomes = ['Bob', 'Alex', 'James', 'Susan',
         'Henry', 'Lisa', 'Anna', 'Harry']
sobrenomes = ['Smith', 'Brown', 'Wilson', 'Thomson',
              'Cook', 'Taylor', 'Walker', 'Clark']
for i in range(100):
    tabela.insert(
        parent='',
        index=tk.END,
        values=(choice(nomes), choice(sobrenomes))
    )
    tabela.pack(
        expand=True,
        fill='both'
    )

# Scrollbar
navegacao = ttk.Scrollbar(
    master=tela,
    orient='vertical',
    command=tabela.yview
)
tabela.configure(yscrollcommand=navegacao.set)
navegacao.place(
    relx=1,
    rely=0,
    relheight=1,
    anchor='ne'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
