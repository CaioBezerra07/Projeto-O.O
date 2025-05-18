import tkinter as tk
from tkinter import font, messagebox
from package.controle.controle_fases import ControleFases
from package.controle.controle_usuarios import ControleUsuarios

class TelaFase(tk.Toplevel):
    def __init__(self, usuario, linguagem, fase, master):
        super().__init__(master)
        self.usuario = usuario
        self.linguagem = linguagem
        self.fase = fase
        self.master = master
        self.title(f"Fase {fase} - {linguagem}")
        self.geometry("600x400")
        self.resizable(True, True)
        self.configure(bg="#2c3e50")

        self.perguntas = ControleFases.obter_perguntas(linguagem, fase)
        self.indice = 0

        # Fontes
        self.title_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=12)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        # Frame branco principal
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True, padx=40, pady=40)

        # Título
        tk.Label(frame, text=f"{linguagem} - Fase {fase}", bg="white", fg="#34495e", font=self.title_font).pack(pady=(10, 20))

        # Enunciado
        self.label_enunciado = tk.Label(frame, text="", wraplength=500, justify="left", font=self.label_font, bg="white", fg="#2c3e50")
        self.label_enunciado.pack(pady=10, padx=20, anchor="w")

        # Alternativas
        self.var_escolha = tk.IntVar()
        self.botoes = []
        for i in range(4):
            btn = tk.Radiobutton(frame, text="", variable=self.var_escolha, value=i,
                                 font=self.label_font, bg="white", anchor="w", fg="#2c3e50",
                                 selectcolor="#ecf0f1", padx=10)
            btn.pack(fill="x", padx=20, pady=5)
            self.botoes.append(btn)

        # Botão responder
        self.btn_responder = tk.Button(frame, text="Responder", font=self.button_font,
                                       bg="#27ae60", fg="white", relief=tk.FLAT,
                                       command=self.verificar, cursor="hand2")
        self.btn_responder.pack(pady=20)

        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        if self.indice < len(self.perguntas):
            pergunta = self.perguntas[self.indice]
            self.label_enunciado.config(text=pergunta.enunciado)
            self.var_escolha.set(-1)
            for i, alt in enumerate(pergunta.alternativas):
                self.botoes[i].config(text=alt)
        else:
            ControleUsuarios.salvar_progresso(self.usuario, self.linguagem, self.fase)
            messagebox.showinfo("Fim", f"Você completou a fase {self.fase}!")
            self.fechar()

    def verificar(self):
        resposta = self.var_escolha.get()
        correta = self.perguntas[self.indice].correta

        if resposta == correta:
            self.indice += 1
            self.mostrar_pergunta()
        else:
            messagebox.showwarning("Incorreto", "Resposta errada. Tente novamente.")

    def fechar(self):
        self.destroy()
        self.master.deiconify()
