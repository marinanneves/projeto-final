import tkinter as tk
from tkinter import messagebox
import sqlite3

class Cadastro_Profissional:
    def __init__(self, tela):
        self.tela = tela
        titulo = "Cadastro de Profissional"
        self.titulo = titulo
        self.tela.title(titulo)
        self.tela.geometry("300x250")

        self.conn = sqlite3.connect("restaurante.bd")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS profissionais (
                                COD INTEGER PRIMARY KEY,
                                NOME TEXT,
                                DATANASC DATE,
                                ATIVO TEXT,
                                CPF VARCHAR,
                                SENHA VARCHAR                       
                              )""")

        self.nomelabel = tk.Label(tela, text="Nome")
        self.nomelabel.pack()
        self.nomeentry = tk.Entry(tela, width=30)
        self.nomeentry.pack()

        self.datanasclabel = tk.Label(tela, text="Data Nascimento")
        self.datanasclabel.pack()
        self.datanascentry = tk.Entry(tela, width=30)
        self.datanascentry.pack()

        self.ativolabel = tk.Label(tela, text="Ativo")
        self.ativolabel.pack()
        self.ativoentry = tk.Entry(tela, width=30)
        self.ativoentry.pack()

        self.cpflabel = tk.Label(tela, text="CPF")
        self.cpflabel.pack()
        self.cpfentry = tk.Entry(tela, width=30)
        self.cpfentry.pack()

        self.codproflabel = tk.Label(tela, text="Senha de Acesso")
        self.codproflabel.pack()
        self.codprofentry = tk.Entry(tela, width=30)
        self.codprofentry.pack()

        self.cadastrarbutton = tk.Button(tela, text="Cadastrar", command=self.cadastrar)
        self.cadastrarbutton.pack()

    def cadastrar(self):
        nome = self.nomeentry.get()
        datanasc = self.datanascentry.get()
        ativo = self.ativoentry.get()
        cpf = self.cpfentry.get()
        senha = self.codprofentry.get()

        if len(nome.strip()) <= 0 or len(cpf.strip()) <= 0 or len(senha.strip()) <= 0:
            messagebox.showinfo(self.titulo, "Campos Obrigatórios")
        else:
            self.cursor.execute("INSERT INTO profissionais (NOME, DATANASC, ATIVO, CPF, SENHA) VALUES (?, ?, ?, ?, ?)", (nome, datanasc, ativo, cpf, senha))
            self.conn.commit()
            messagebox.showinfo(self.titulo, "Cadastro Realizado")
            self.tela.destroy()

if __name__ == "__main__":
    tela = tk.Tk()
    Cadastro_Profissional = Cadastro_Profissional(tela)
    tela.mainloop()
