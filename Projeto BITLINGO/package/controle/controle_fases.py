import json
import os
from package.modelo.pergunta import Pergunta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.join(BASE_DIR, "..", "..", "dados", "perguntas.json")

class ControleFases:
    @staticmethod
    def obter_perguntas(linguagem, fase):
        try:
            with open(CAMINHO, encoding='utf-8') as f:
                dados = json.load(f)

            perguntas_json = dados.get(linguagem, {}).get(str(fase), [])
            perguntas = []
            for p in perguntas_json:
                perguntas.append(Pergunta(p["enunciado"], p["alternativas"], p["correta"]))

            return perguntas
        except Exception as e:
            print("Erro ao carregar perguntas:", e)
            return []
