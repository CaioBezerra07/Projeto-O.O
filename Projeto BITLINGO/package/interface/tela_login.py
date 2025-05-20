import tkinter as tk
from tkinter import font, messagebox
from package.controle.controle_usuarios import ControleUsuarios
from package.interface.tela_registro import TelaRegistro
from package.interface.tela_linguagem import TelaLinguagem

class TelaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Faça o login - BITLINGO")
        self.geometry("400x500")
        self.resizable(True, True)
        self._centralizar_janela(400, 500)
        self.configure(bg="#2c3e50")

        # Fontes
        self.title_font = font.Font(family="Segoe UI", size=24, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=11)
        self.entry_font = font.Font(family="Segoe UI", size=12)
        self.button_font = font.Font(family="Segoe UI", size=14, weight="bold")
        self.message_font = font.Font(family="Segoe UI", size=10, slant="italic")

        # Frame branco central 
        self.frame = tk.Frame(self, bg="white", bd=0)
        self.frame.pack(fill="both", expand=True, padx=40, pady=40)

        # Cabeçalho
        tk.Label(self.frame, text="Bem-vindo!", bg="white", fg="#34495e", font=self.title_font).pack(pady=(10, 20))

        # Campo usuário
        tk.Label(self.frame, text="Usuário", bg="white", fg="#34495e", font=self.label_font).pack(anchor="w", padx=20)
        self.entry_usuario = tk.Entry(self.frame, font=self.entry_font, bd=2, relief=tk.GROOVE)
        self.entry_usuario.pack(padx=20, fill="x", pady=(3, 10))

        # Campo senha com botão de mostrar
        tk.Label(self.frame, text="Senha", bg="white", fg="#34495e", font=self.label_font).pack(anchor="w", padx=20)
        pass_frame = tk.Frame(self.frame, bg="white")
        pass_frame.pack(padx=20, fill="x", pady=(3, 10))

        self.pass_var = tk.StringVar()
        self.entry_senha = tk.Entry(pass_frame, font=self.entry_font, bd=2, relief=tk.GROOVE,
                                    show="*", textvariable=self.pass_var)
        self.entry_senha.pack(side="left", fill="x", expand=True)

        self.show_password = False
        self.toggle_button = tk.Button(pass_frame, text="Mostrar", bg="#ecf0f1", fg="#34495e",
                                       font=("Segoe UI", 9, "bold"), relief=tk.FLAT,
                                       command=self.toggle_password, cursor="hand2")
        self.toggle_button.pack(side="left", padx=(5, 0))

        # Botão entrar
        btn_entrar = tk.Button(self.frame, text="Entrar", bg="#3498db", fg="white", font=self.button_font,
                               relief=tk.FLAT, cursor="hand2", command=self.login)
        btn_entrar.pack(fill="x", padx=20, pady=(20, 10))

        # Botão cadastrar
        btn_cadastrar = tk.Button(self.frame, text="Cadastrar", bg="#2ecc71", fg="white", font=self.button_font,
                                  relief=tk.FLAT, cursor="hand2", command=self.abrir_cadastro)
        btn_cadastrar.pack(fill="x", padx=20)

        # Mensagem de erro
        self.message = tk.Label(self.frame, text="", bg="white", fg="#e74c3c", font=self.message_font)
        self.message.pack(pady=(10, 0))

        self.bind("<Return>", lambda e: self.login())

    def _centralizar_janela(self, largura, altura):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (largura / 2))
        y = int((screen_height / 2) - (altura / 2))
        self.geometry(f"{largura}x{altura}+{x}+{y}")

    def toggle_password(self):
        if self.show_password:
            self.entry_senha.config(show="*")
            self.toggle_button.config(text="Mostrar")
        else:
            self.entry_senha.config(show="")
            self.toggle_button.config(text="Ocultar")
        self.show_password = not self.show_password

    def login(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.pass_var.get().strip()

        if ControleUsuarios.validar_login(usuario, senha):
            self.destroy()
            TelaLinguagem(usuario)
        else:
            self.message.config(text="Usuário ou senha inválidos.")

    def abrir_cadastro(self):
        self.destroy()
        TelaRegistro()
