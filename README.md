# ProjetoAPI - Focado em Gestão escolar com FLASK

Esse é um sistema de gestão academica simples, desenvolvido com Flask e SQLAlchermy. O sistemas gerencia Professores, Turma, Aluno com relaçoes necessárias sobre as entidades.


# Clonar projeto:

"Git clone https://github.com/FrankRibe/ProjetoAPI.git"

# Pastas 

/PROJETOAPI
    app/
    │
    ├── __init__.py           # Inicializa a aplicação Flask
    ├── models.py             # Define os modelos de dados (Turma, Aluno, etc.)
    ├── routes.py             # Rotas gerais da aplicação (opcional)
    ├── alunos/
    │   ├── __init__.py       # Inicializa o módulo de alunos
    │   ├── alunos_routes.py   # Rotas para os alunos
    │   └── alunos_model.py    # Modelos e funções para os alunos
    └── turmas/
        ├── __init__.py       # Inicializa o módulo de turmas
        ├── turmas_routes.py   # Rotas para as turmas
        └── turmas_model.py    # Modelos e funções para as turmas/app
            __init__.py     # Inicia o app Flask e configura o banco de dados
            models.py       # Define os modelos do Banco de dados (Professor,Turma,Aluno)
            routes.py       # Define as rotas da aplicação
            config.py       # Confirgurar o app (como banco de dados)
    run.py                  # Arquivo que inicia a aplicação do Flask    
    README.md               # Documentação do projeto
    requeriments.txt        # Arquivo com as dependências do projeto    

# Requisitos para instalação

- Python
- Flask
- SQLAlchemy