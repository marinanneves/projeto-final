import tkinter as tk
from tkinter import messagebox 
import sqlite3

class Floricultura:

    def __init__(self, tela):
        self.tela = tela
        titulo = "Sistema de Floricultura"
        self.titulo = titulo
        self.tela.title(self.titulo)
        self.tela.geometry("300x300")
        
        # Conectar ao banco de dados
        self.conn = sqlite3.connect("floricultura.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                            ID INTEGER PRIMARY KEY,
                            NOME TEXT,
                            EMAIL VARCHAR,
                            SENHA VARCHAR,
                            PRECO REAL,
                            QTD INTEGER,
                            TIPO TEXT)""")
        
        # Criar os campos de entrada
        self.nomelabel = tk.Label(tela, text="Nome")
        self.nomelabel.pack()
        self.nomeentry = tk.Entry(tela, width=30)
        self.nomeentry.pack()
        
        self.emaillabel = tk.Label(tela, text="Email")
        self.emaillabel.pack()
        self.emailentry = tk.Entry(tela, width=30)
        self.emailentry.pack()
        
        self.senhalabel = tk.Label(tela, text="Senha")
        self.senhalabel.pack()
        self.senhaentry = tk.Entry(tela, show="*", width=30)
        self.senhaentry.pack()

        self.precolabel = tk.Label(tela, text="Preço")
        self.precolabel.pack()
        self.precoentry = tk.Entry(tela, width=30)
        self.precoentry.pack()
        
        self.qtdlabel = tk.Label(tela, text="Quantidade")
        self.qtdlabel.pack()
        self.qtdentry = tk.Entry(tela, width=30)
        self.qtdentry.pack()
        
        self.tipolabel = tk.Label(tela, text="Tipo")
        self.tipolabel.pack()
        self.tipoentry = tk.Entry(tela, width=30)
        self.tipoentry.pack()
        
        self.cadastrarbutton = tk.Button(tela, text="Cadastrar", command=self.cadastrar)
        self.cadastrarbutton.pack()

    def cadastrar(self):
        nome = self.nomeentry.get()
        email = self.emailentry.get()
        senha = self.senhaentry.get()
        preco = self.precoentry.get()
        qtd = self.qtdentry.get()
        tipo = self.tipoentry.get()

        if len(nome.strip()) <= 0 or len(email.strip()) <= 0 or len(senha.strip()) <= 0 or len(preco.strip()) <= 0 or len(qtd.strip()) <= 0 or len(tipo.strip()) <= 0:
            messagebox.showinfo(self.titulo, "Campos obrigatórios")
        else:
            try:
                preco = float(preco)  # Convertendo para float
                qtd = int(qtd)        # Convertendo para int
                self.cursor.execute("INSERT INTO usuarios(NOME, EMAIL, SENHA, PRECO, QTD, TIPO) VALUES (?, ?, ?, ?, ?, ?)", (nome, email, senha, preco, qtd, tipo))
                self.conn.commit()
                messagebox.showinfo(self.titulo, "Cadastro realizado")
                self.tela.destroy()
            except ValueError:
                messagebox.showerror(self.titulo, "Preço e quantidade devem ser numéricos.")

if __name__ == "__main__":
    tela = tk.Tk()
    acesso = Floricultura(tela)
    tela.mainloop()
