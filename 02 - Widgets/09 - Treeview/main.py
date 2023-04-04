import tkinter as tk
from tkinter import ttk
from random import choice

# Tela
tela = tk.Tk()
tela.title('Treeview')
tela.geometry('600x400')

# Dados
nomes = [
    'Bob',
    'Maria',
    'Alex',
    'James',
    'Susan',
    'Henry',
    'Lisa',
    'Anna',
    'Lisa'
]
sobrenomes = [
    'Smith',
    'Brown',
    'Wilson',
    'Thomson',
    'Cook',
    'Taylor',
    'Walker',
    'Clark'
]

# Treeview
tabela = ttk.Treeview(
    master=tela,
    columns=(
        'nome',
        'sobrenome',
        'email'
    ),
    show='headings'  # coloca as colunas da esquerda para direita
)
tabela.heading(
    'nome',  # nome da coluna
    text='Nome'  # qual o nome mostrado na GUI
)
tabela.heading(
    'sobrenome',
    text='Sobrenome'
)
tabela.heading(
    'email',
    text='E-mail'
)
tabela.pack(
    fill='both',
    expand=True
)

# Colocar os dados na tabela
tabela.insert(
    parent='',  # indica qual tabela será adicionado os dados. String vazia indica a própria tabela
    index=0,  # informa em qual linha será adicionado os dados
    values=('John', 'Doe', 'jhon.doe@email.com')
)
for i in range(100):
    nome = choice(nomes)
    sobrenome = choice(sobrenomes)
    email = f'{nome.lower()[0]}.{sobrenome.lower()}@email.com'
    dados = (nome, sobrenome, email)
    tabela.insert(
        parent='',
        index=0,
        values=dados
    )

# Parâmetro "index"
tabela.insert(
    parent='',
    index=tk.END,  # isso permite colocar os dados na última linha da tabela
    values=('XXXXX', 'YYYYY', 'ZZZZZ')
)


# Eventos
def selecao_item(_):
    """Função responsável por informar qual é o item selecionado da tabela."""
    for i in tabela.selection():
        print(tabela.item(i)['values'])


def deletar_itens(_):
    """Função responsável por deletar as linhas selecionadas da tabela."""
    for i in tabela.selection():
        tabela.delete(i)


tabela.bind(
    '<<TreeviewSelect>>',
    selecao_item
)
tabela.bind(
    '<Delete>',  # tecla "Delete" ou "Del" do teclado
    deletar_itens
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
