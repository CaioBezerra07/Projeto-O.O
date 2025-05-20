import tkinter as tk
from tkinter import font, messagebox
from package.controle.controle_usuarios import ControleUsuarios
import subprocess
import sys

class TelaRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro - BITLINGO")
        self.geometry("400x500")
        self.resizable(True, True)
        self._centralizar_janela(400, 500)
        self.configure(bg="#2c3e50")

        # Fontes
        self.title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=12)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        # Frame central branco
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True, padx=40, pady=40)

        # Título
        tk.Label(frame, text="Crie sua conta", font=self.title_font, bg="white", fg="#34495e").pack(pady=(20, 30))

        # Campos de entrada
        self._criar_campo(frame, "Usuário:", "usuario")
        self._criar_campo(frame, "Senha:", "senha", show="*")
        self._criar_campo(frame, "Confirmar Senha:", "confirma", show="*")

        # Botão confirmar
        btn_confirmar = tk.Button(frame, text="Confirmar Cadastro", bg="#27ae60", fg="white",
                                  font=self.button_font, command=self.cadastrar, relief=tk.FLAT, cursor="hand2")
        btn_confirmar.pack(fill="x", padx=20, pady=(25, 10))

        # Botão voltar
        btn_voltar = tk.Button(frame, text="Voltar", bg="#2980b9", fg="white",
                               font=self.button_font, command=self.voltar, relief=tk.FLAT, cursor="hand2")
        btn_voltar.pack(fill="x", padx=20)

    def _centralizar_janela(self, largura, altura):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (largura / 2))
        y = int((screen_height / 2) - (altura / 2))
        self.geometry(f"{largura}x{altura}+{x}+{y}")

    def _criar_campo(self, parent, texto, atributo, show=None):
        tk.Label(parent, text=texto, font=self.label_font, bg="white", fg="#34495e").pack(anchor="w", padx=30)
        entry = tk.Entry(parent, font=self.label_font, show=show if show else "")
        entry.pack(padx=30, fill="x", pady=(3, 15))
        setattr(self, f"entry_{atributo}", entry)

    def cadastrar(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        confirma = self.entry_confirma.get()

        if senha != confirma:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        if ControleUsuarios.registrar_usuario(usuario, senha):
            messagebox.showinfo("Sucesso", "Cadastro realizado!")
            self.destroy()
            subprocess.Popen([sys.executable, "main.py"])
        else:
            messagebox.showerror("Erro", "Usuário já existe.")

    def voltar(self):
        self.destroy()
        subprocess.Popen([sys.executable, "main.py"])
