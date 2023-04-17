# Tendo como base o arquivo main.py, criar uma classe que armazena as configurações
# dos widgets para a classe Principal()
# e os argumentos como cor, texto da label e texto deo botão devem
# ser fornecidos como argumentos.

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """Classe responsável por executar o App."""
    def __init__(self, titulo, dimensao):
        super().__init__()

        # Configurações da tela
        self.title(titulo)
        self.geometry(f'{dimensao[0]}x{dimensao[1]}')
        self.minsize(dimensao[0], dimensao[1])

        # Widgets
        self.menu = Menu(self)
        self.principal = Principal(self)

        # Mostrar a tela
        self.mainloop()


class Menu(ttk.Frame):
    """Classe responsável por configurar os widgets do menu."""
    def __init__(self, master):
        super().__init__(master)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.criar_widgets()

    def criar_widgets(self):
        """Função responsável por criar os widgets do menu."""
        # Criar os widgets
        botao_menu_1 = ttk.Button(
            self,
            text='Botão 1'
        )
        botao_menu_2 = ttk.Button(
            self,
            text='Botão 2'
        )
        botao_menu_3 = ttk.Button(
            self,
            text='Botão 3'
        )

        slider_menu_1 = ttk.Scale(
            self,
            orient='vertical'
        )
        slider_menu_2 = ttk.Scale(
            self,
            orient='vertical'
        )

        frame_toggle = ttk.Frame(self)
        toggle_menu_1 = ttk.Checkbutton(
            frame_toggle,
            text='Check 1'
        )
        toggle_menu_2 = ttk.Checkbutton(
            frame_toggle,
            text='Check 2'
        )

        entrada = ttk.Entry(self)

        # Criar a grade
        self.columnconfigure(
            index=(0, 1, 2),
            weight=1,
            uniform='a'
        )
        self.rowconfigure(
            index=(0, 1, 2, 3, 4),
            weight=1,
            uniform='a'
        )

        # Colocar os widgets
        botao_menu_1.grid(
            column=0,
            row=0,
            sticky='news',
            columnspan=2
        )
        botao_menu_2.grid(
            column=2,
            row=0,
            sticky='news'
        )
        botao_menu_3.grid(
            column=0,
            row=1,
            sticky='news',
            columnspan=3
        )

        slider_menu_1.grid(
            column=0,
            row=2,
            sticky='news',
            rowspan=2,
            pady=20
        )
        slider_menu_2.grid(
            column=2,
            row=2,
            sticky='news',
            rowspan=2,
            pady=20
        )

        frame_toggle.grid(
            column=0,
            row=4,
            columnspan=3,
            sticky='news'
        )
        toggle_menu_1.pack(
            side='left',
            expand=True
        )
        toggle_menu_2.pack(
            side='left',
            expand=True
        )

        entrada.place(
            relx=0.5,
            rely=0.95,
            relwidth=0.9,
            anchor='center'
        )


class Principal(ttk.Frame):
    """Classe responsável por armazenar as configurações do menu principal."""
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entrada(self, 'Label 1', 'green', 'Botão 1')
        Entrada(self, 'Label 2', 'blue', 'Botão 2')


class Entrada(ttk.Frame):
    """Classe responsável por armazenar os widgets da classe Principal()."""
    def __init__(self, master, label_texto, label_cor, botao_texto):
        super().__init__(master)

        label = ttk.Label(
            self,
            text=label_texto,
            background=label_cor
        )
        botao = ttk.Button(
            self,
            text=botao_texto
        )

        label.pack(
            expand=True,
            fill='both'
        )
        botao.pack(
            expand=True,
            fill='both',
            pady=10
        )

        self.pack(
            side='left',
            expand=True,
            fill='both',
            padx=20,
            pady=20
        )


if __name__ == '__main__':
    # Executar o App
    App('Classe base do App', (600, 600))
