import os
import pickle

CAMINHO_DADOS = "dados/usuarios.pkl"

class ControleUsuarios:
    @staticmethod
    def carregar_usuarios():
        if not os.path.exists(CAMINHO_DADOS):
            return {}
        try:
            with open(CAMINHO_DADOS, "rb") as f:
                return pickle.load(f)
        except EOFError:
            return {}  


    @staticmethod
    def salvar_usuarios(usuarios):
        with open(CAMINHO_DADOS, "wb") as f:
            pickle.dump(usuarios, f)

    @staticmethod
    def registrar_usuario(usuario, senha):
        usuarios = ControleUsuarios.carregar_usuarios()
        if usuario in usuarios:
            return False
        usuarios[usuario] = {"senha": senha, "progresso": {}}
        ControleUsuarios.salvar_usuarios(usuarios)
        return True

    @staticmethod
    def validar_login(usuario, senha):
        usuarios = ControleUsuarios.carregar_usuarios()
        return usuario in usuarios and usuarios[usuario]["senha"] == senha

    @staticmethod
    def salvar_progresso(usuario, linguagem, fase):
        usuarios = ControleUsuarios.carregar_usuarios()
        if usuario not in usuarios:
            return
        usuarios[usuario]["progresso"][linguagem] = fase
        ControleUsuarios.salvar_usuarios(usuarios)

    @staticmethod
    def obter_progresso(usuario, linguagem):
        usuarios = ControleUsuarios.carregar_usuarios()
        return usuarios.get(usuario, {}).get("progresso", {}).get(linguagem, 0)
