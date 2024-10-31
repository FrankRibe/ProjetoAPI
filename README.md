
# ProjetoAPI - Gestão Escolar com Flask

Este é um sistema simples de gestão acadêmica desenvolvido com Flask e SQLAlchemy, focado no gerenciamento de Professores, Turmas e Alunos. O sistema permite realizar operações CRUD (Criar, Ler, Atualizar e Deletar) nas entidades com as devidas relações entre elas.

## Clonar o Projeto

Clone o repositório para sua máquina:

```bash
git clone https://github.com/FrankRibe/ProjetoAPI.git
cd ProjetoAPI
```

## Estrutura de Pastas

A estrutura do projeto está organizada da seguinte forma:

```
/PROJETOAPI
    ├── app/
    │   ├── __init__.py                   # Inicializa o app Flask e configurações gerais
    │   ├── models.py                     # Modelos gerais do banco de dados
    │   ├── routes.py                     # Rotas principais da aplicação
    │   ├── alunos/
    │   │   ├── __init__.py               # Inicializa o módulo de alunos
    │   │   ├── alunos_routes.py          # Rotas específicas para alunos
    │   │   └── alunos_models.py          # Modelos e funções relacionados aos alunos
    │   ├── professores/
    │   │   ├── __init__.py               # Inicializa o módulo de professores
    │   │   ├── professores_routes.py     # Rotas específicas para professores
    │   │   └── professores_models.py     # Modelos e funções relacionados aos professores
    │   ├── turmas/
    │   │   ├── __init__.py               # Inicializa o módulo de turmas
    │   │   ├── turmas_routes.py          # Rotas específicas para turmas
    │   │   └── turmas_models.py          # Modelos e funções relacionados às turmas
    │   ├── templates/                    # Pasta para os templates HTML
    │   │   ├── index.html                # Template principal
    │   │   ├── aluno/
    │   │   │   ├── aluno_id.html         # Template para visualização de um aluno específico
    │   │   │   ├── aluno_update.html     # Template para atualização de aluno
    │   │   │   ├── alunos.html           # Template para listar alunos
    │   │   │   └── criarAlunos.html      # Template para criação de alunos
    │   │   ├── professor/
    │   │   │   ├── professor_id.html     # Template para visualização de um professor específico
    │   │   │   ├── professor_update.html # Template para atualização de professor
    │   │   │   ├── professores.html      # Template para listar professores
    │   │   │   └── criarProfessores.html # Template para criação de professores
    │   │   ├── turmas/
    │   │       ├── turma_id.html         # Template para visualização de uma turma específica
    │   │       ├── turma_update.html     # Template para atualização de turma
    │   │       ├── turmas.html           # Template para listar turmas
    │   │       └── criarTurmas.html      # Template para criação de turmas
    ├── instance/
    │   └── escola.db                     # Banco de dados SQLite do projeto
    ├── .gitignore                        # Arquivo Gitignore para evitar o commit de arquivos desnecessários
    ├── README.md                         # Documentação do projeto
    └── run.py                            # Arquivo principal para iniciar o app Flask
```

## Requisitos para Instalação

- Python 3.x
- Flask
- SQLAlchemy

## Instalação e Configuração

1. **Crie um ambiente virtual (opcional):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Inicie a aplicação:**

    ```bash
    python run.py
    ```