import tkinter as tk
from tkinter import font
from package.controle.controle_usuarios import ControleUsuarios
from package.interface.tela_fase import TelaFase

class TelaLinguagem(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.title("Escolha de Linguagem - Aprenda Programação")
        self.geometry("400x500")
        self.resizable(True, True)
        self._centralizar_janela(400, 500)
        self.configure(bg="#2c3e50")

        # Fontes
        self.title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=12)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        # Frame principal - agora expansível
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True, padx=40, pady=40)

        tk.Label(frame, text=f"Olá, {usuario}!", bg="white", fg="#34495e", font=self.title_font).pack(pady=(30, 10))
        tk.Label(frame, text="Escolha uma linguagem:", bg="white", fg="#34495e", font=self.label_font).pack(pady=5)

        self.linguagens = ["C", "Java", "Python"]
        for linguagem in self.linguagens:
            tk.Button(frame, text=linguagem, bg="#2980b9", fg="white", font=self.button_font,
                      relief=tk.FLAT, cursor="hand2", width=20,
                      command=lambda l=linguagem: self.mostrar_fases(l)).pack(pady=8)

    def _centralizar_janela(self, largura, altura):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (largura / 2))
        y = int((screen_height / 2) - (altura / 2))
        self.geometry(f"{largura}x{altura}+{x}+{y}")

    def mostrar_fases(self, linguagem):
        self.withdraw()
        self.fase_selector = FaseSelector(self.usuario, linguagem, self)
        self.fase_selector.grab_set()
        self.fase_selector.focus()
        self.fase_selector.protocol("WM_DELETE_WINDOW", self.fechar_fase_selector)

    def fechar_fase_selector(self):
        self.fase_selector.destroy()
        self.deiconify()

class FaseSelector(tk.Toplevel):
    def __init__(self, usuario, linguagem, master):
        super().__init__(master)
        self.usuario = usuario
        self.linguagem = linguagem
        self.master = master
        self.title(f"Fases de {linguagem}")
        self.geometry("400x500")
        self.resizable(True, True)  # Agora pode esticar
        self._centralizar_janela(400, 500)
        self.configure(bg="#2c3e50")

        # Fontes
        self.title_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        progresso = ControleUsuarios.obter_progresso(usuario, linguagem)

        # Frame principal
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True, padx=40, pady=40)

        tk.Label(frame, text=f"{linguagem} - Escolha a fase", bg="white", fg="#34495e", font=self.title_font).pack(pady=(30, 20))

        for fase in range(1, 4):
            estado = tk.NORMAL if progresso >= fase - 1 else tk.DISABLED
            tk.Button(frame, text=f"Fase {fase}", bg="#27ae60", fg="white", font=self.button_font,
                      relief=tk.FLAT, cursor="hand2", width=20, state=estado,
                      command=lambda f=fase: self.abrir_fase(f)).pack(pady=8)

        # Botão voltar
        tk.Button(frame, text="Voltar para Linguagens", bg="#e74c3c", fg="white", font=self.button_font,
                  relief=tk.FLAT, cursor="hand2", width=20,
                  command=self.voltar_para_linguagens).pack(pady=20)

    def _centralizar_janela(self, largura, altura):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (largura / 2))
        y = int((screen_height / 2) - (altura / 2))
        self.geometry(f"{largura}x{altura}+{x}+{y}")

    def abrir_fase(self, fase):
        self.withdraw()
        self.tela_fase = TelaFase(self.usuario, self.linguagem, fase, self)
        self.tela_fase.grab_set()
        self.tela_fase.focus()
        self.tela_fase.protocol("WM_DELETE_WINDOW", self.fechar_tela_fase)

    def fechar_tela_fase(self):
        self.tela_fase.destroy()
        self.deiconify()

    def voltar_para_linguagens(self):
        self.destroy()
        self.master.deiconify()
