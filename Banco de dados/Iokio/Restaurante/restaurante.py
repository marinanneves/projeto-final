import tkinter as tk
from tkinter import messagebox
import sqlite3

class Cliente:
    def __init__(self, tela):
        self.tela = tela
        titulo = "Restaurante Popular"
        self.titulo = titulo
        self.tela.title(titulo)
        self.tela.geometry("300x400")
        
        self.conn = sqlite3.connect("respopular.bd")
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                                COD INTEGER PRIMARY KEY,
                                NOME TEXT,
                                DATANASC DATE,
                                ATIVO TEXT,
                                CPF VARCHAR,
                                CODPROF INT,
                                CAD INT,
                                CODDEFICIENCIA INT,
                                CODDOENCA INT,
                                ABONADO TEXT
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

        self.codproflabel = tk.Label(tela, text="Código Profissão")
        self.codproflabel.pack()
        self.codprofentry = tk.Entry(tela, width=30)
        self.codprofentry.pack()

        self.cadlabel = tk.Label(tela, text="CAD Único")
        self.cadlabel.pack()
        self.cadentry = tk.Entry(tela, width=30)
        self.cadentry.pack()

        self.coddeficiencialabel = tk.Label(tela, text="Deficiência")
        self.coddeficiencialabel.pack()
        self.coddeficienciaentry = tk.Entry(tela, width=30)
        self.coddeficienciaentry.pack()

        self.coddoencalabel = tk.Label(tela, text="Doença")
        self.coddoencalabel.pack()
        self.coddoencaentry = tk.Entry(tela, width=30)
        self.coddoencaentry.pack()

        self.abonadolabel = tk.Label(tela, text="Abonado")
        self.abonadolabel.pack()
        self.abonadoentry = tk.Entry(tela, width=30)
        self.abonadoentry.pack()

        self.cadastrarbutton = tk.Button(tela, text="Cadastrar", command=self.cadastrar)
        self.cadastrarbutton.pack()

    def cadastrar(self):
        nome = self.nomeentry.get()
        datanasc = self.datanascentry.get()
        ativo = self.ativoentry.get()
        cpf = self.cpfentry.get()
        codprof = self.codprofentry.get()
        cad = self.cadentry.get()
        coddeficiencia = self.coddeficienciaentry.get()
        coddoenca = self.coddoencaentry.get()
        abonado = self.abonadoentry.get()

        if len(nome.strip()) <= 0 or len(cpf.strip()) <= 0 or len(codprof.strip()) <= 0:
            messagebox.showinfo(self.titulo, "Campos Obrigatórios")
        else:
            self.cursor.execute("""INSERT INTO usuarios (NOME, DATANASC, ATIVO, CPF, CODPROF, CAD, CODDEFICIENCIA, CODDOENCA, ABONADO) 
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                (nome, datanasc, ativo, cpf, codprof, cad, coddeficiencia, coddoenca, abonado))
            self.conn.commit()
            messagebox.showinfo(self.titulo, "Cadastro Realizado")
            self.tela.destroy()

if __name__ == "__main__":
    tela = tk.Tk()
    cliente = Cliente(tela)
    tela.mainloop()