class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.progresso = {}

    def validar_senha(self, senha_informada):
        return self.senha == senha_informada

    def atualizar_progresso(self, linguagem, fase):
        self.progresso[linguagem] = max(fase, self.progresso.get(linguagem, 0))

    def obter_progresso(self, linguagem):
        return self.progresso.get(linguagem, 0)
