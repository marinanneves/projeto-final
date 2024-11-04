import tkinter as tk
from tkinter import ttk
import sqlite3

class Liste:
       def __init__(self, tela):
        self.tela = tela
        titulo = "Banco de Dados TechStore"
        self.tela.title(titulo)
        self.tela.geometry("600x200")

        # Conexão com o banco de dados
        self.conn = sqlite3.connect("techstore.db")
        self.cursor = self.conn.cursor()

        # Buscando os dados
        self.cursor.execute("SELECT * FROM usuarios")
        tot_usuarios = self.cursor.fetchall()
        self.conn.close()

        # Configurando a Treeview
        self.tree = ttk.Treeview(self.tela, columns=("ID", "Nome", "Email", "Senha"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Senha", text="Senha")

        # Inserindo os dados na Treeview
        for usuarios in tot_usuarios:
            self.tree.insert("", tk.END, values=usuarios)

        self.tree.pack()

if __name__ == "__main__":
    tela = tk.Tk()
    lista = Liste(tela)
    tela.mainloop()
