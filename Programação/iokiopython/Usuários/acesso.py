import tkinter as tk
from tkinter import messagebox, Frame, Radiobutton, IntVar
import sqlite3
import hashlib

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Acesso")
        self.root.geometry("300x300")

        # Configuração da conexão com o banco de dados
        self.conn = sqlite3.connect("techstore.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                email TEXT UNIQUE,
                senha TEXT
            )
        """)


        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root, width=30)
        self.nome_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.pack()

        self.senha_label = tk.Label(root, text="Senha:")
        self.senha_label.pack()
        self.senha_entry = tk.Entry(root, width=30, show="*")
        self.senha_entry.pack()


        self.frame_cima = Frame(root)
        self.frame_cima.pack()

        # Botões de rádio para seleção de cliente ativo
        self.radio_valor = IntVar()
        self.radio_valor.set(1)  # Definir seleção padrão

        self.label = tk.Label(self.frame_cima, text='Cliente está ativo?')
        self.label.pack(anchor='w')
        self.sim = Radiobutton(self.frame_cima, text='Sim', variable=self.radio_valor, value=1)
        self.sim.pack(anchor='w')
        self.nao = Radiobutton(self.frame_cima, text='Não', variable=self.radio_valor, value=2)
        self.nao.pack(anchor='w')


        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=5)
        self.cadastro_button = tk.Button(root, text="Cadastrar", command=self.cadastro)
        self.cadastro_button.pack(pady=5)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        email = self.email_entry.get()
        senha = self.hash_password(self.senha_entry.get())
        self.cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
        usuario = self.cursor.fetchone()
        if usuario:
            messagebox.showinfo("Login", f"Bem-vindo, {usuario[1]}!")  # usuario[1] é o nome
            self.root.destroy()  # Fecha a janela de login
        else:
            messagebox.showerror("Login", "Email ou senha incorretos")

    def cadastro(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messagebox.showinfo("Sistema de Login", "Todos os campos são obrigatórios")
            return

        hashed_senha = self.hash_password(senha)
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, hashed_senha)
            )
            self.conn.commit()
            messagebox.showinfo("Sistema de Login", "Cadastro realizado com sucesso!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Sistema de Login", "Email já cadastrado.")

if __name__ == "__main__":
    root = tk.Tk()
    loginsystem = LoginSystem(root)
    root.mainloop()
