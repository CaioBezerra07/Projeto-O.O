#  Projeto BITLINGO

Este projeto e uma aplicacao educacional gamificada, inspirada no estilo do Duolingo, mas voltada para o **aprendizado de linguagens de programacao**. O sistema permite que usuarios escolham uma linguagem (C, Java ou Python) e avancem por fases com perguntas de multipla escolha. O progresso e salvo, e as fases sao desbloqueadas conforme o usuario avanca.

---

##  Definicao do Problema

Muitos estudantes enfrentam dificuldade para aprender linguagens de programacao de forma pratica, divertida e progressiva. Este projeto resolve esse problema ao propor um ambiente interativo, com fases de perguntas que reforcam conceitos fundamentais, desbloqueio progressivo e salvamento do progresso individual de cada usuario.

A aplicacao tambem atende aos criterios de um projeto de Orientacao a Objetos, incluindo heranca, polimorfismo, composicao forte, mixins, encapsulamento, associacao fraca e serializacao de objetos.

---

##  Casos de Uso

### 1. Cadastrar Usuario
- O usuario informa nome e senha para criar sua conta.
- O sistema salva os dados serializados.

### 2. Login
- Usuario acessa o sistema com nome e senha.
- Validacao contra dados salvos.

### 3. Escolher Linguagem
- Apos o login, o usuario escolhe uma linguagem (C, Java ou Python).

### 4. Visualizar e Acessar Fases
- O usuario visualiza quais fases estao desbloqueadas.
- Ao concluir uma fase, a proxima e desbloqueada.

### 5. Responder Perguntas
- Cada fase contem perguntas de maltipla escolha.
- Ao acertar todas, o usuario avanca.

### 6. Salvar Progresso
- O progresso e salvo por linguagem.
- Ao reentrar, o sistema retoma o progresso salvo.

---

## Como Rodar o Projeto

### Requisitos

- Python 3.8 ou superior
- Tkinter (ja incluso na maioria das instalacoes do Python)

### Estrutura do Projeto

```
projeto_duolingo_programacao/
├── main.py
├── README.md
├── dados/                      
│   └── usuarios.pkl
│   └── perguntas.json
├── package/
│   ├── controle/
│   │   ├── controle_usuarios.py
│   │   └── controle_fases.py
│   ├── interface/
│   │   ├── tela_login.py
│   │   ├── tela_registro.py
│   │   ├── tela_linguagem.py
│   │   └── tela_fase.py
│   └── modelo/
│       └── pergunta.py
│       └── usuario.py
```

### Executar o projeto

Abra o terminal na pasta raiz do projeto e execute:

```bash

python main.py

```

### Problemas comuns

- Se `tkinter` nao funcionar, certifique-se de que esta usando se a versao usado do Python ja contem o tkinter, caso contrario, instale:

Para Windows:
```
pip install tk
```

Para Linux (Debian/Ubuntu):
```
sudo apt-get install python3-tk

```
---

## Tecnologias Utilizadas

- Python 3
- Tkinter (interface grafica)
- Pickle (serializacao de dados)

---

## Orientacao a Objetos Aplicada

- **Heranca**: Fase - subclasses para organizacao futura
- **Polimorfismo**: metodo `verificar_resposta` e logica de fase
- **Composicao forte**: Fase contem perguntas
- **Associacao fraca**: Usuario associado a progresso por linguagem
- **Mixin**: comportamento de resposta
- **Encapsulamento**: atributos e metodos bem definidos
- **Serializacao**: dados salvos com `pickle`

---

## Autor

Projeto desenvolvido por Caio Breno como atividade pratica da disciplina **Orientacao a Objetos - UnB Gama .
