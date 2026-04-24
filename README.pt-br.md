[Inglês](README.md) | [Português](README.pt-br.md)

# Documentação Técnica do Projeto - Movie API

Esta documentação fornece uma visão detalhada da Movie API, um sistema de gerenciamento de filmes desenvolvido como parte de um desafio técnico para a Wattio. O sistema permite realizar operações de CRUD (Create, Read, Update, Delete) em uma base de dados de filmes.

---

## 1. Visão Geral do Projeto
A **Movie API** é uma aplicação backend projetada para gerenciar um catálogo de filmes. O objetivo principal é fornecer uma interface RESTful para que usuários possam cadastrar, listar e remover filmes, garantindo a persistência dos dados e uma arquitetura escalável e organizada.

### Principais Funcionalidades:
- Listagem de todos os filmes cadastrados.
- Busca detalhada de um filme por ID.
- Cadastro de novos filmes (Nome, Gênero, Duração e Avaliação).
- Exclusão de filmes existentes.
- Tratamento de erros centralizado.

---

## 2. Arquitetura e Estrutura
O projeto adota uma **Arquitetura em Camadas (Layered Architecture)**, o que facilita a manutenção, testes e a separação de responsabilidades.

### Organização de Pastas:
```text
C:\Users\User\Documents\Mateus\Programação\projetos\Github\python\backend\
├── main.py                # Ponto de entrada da aplicação
├── controller/            # Camada de controle (orquestração de requisições)
├── service/               # Camada de lógica de negócio
├── repository/            # Camada de acesso a dados (Persistência)
├── model/                 # Modelos de banco de dados e esquemas de validação (Pydantic)
├── database/              # Configurações de conexão com o banco de dados
├── router/                # Definição das rotas e endpoints
└── docker-compose.yml     # Configuração de containers
```

### Papel de cada diretório:
- **`router/`**: Define os caminhos da API e direciona as requisições para os controllers.
- **`controller/`**: Recebe os dados da rota, valida a existência de recursos e chama os serviços necessários.
- **`service/`**: Contém a lógica de negócio principal, filtrando ou processando dados antes de passá-los ao repositório.
- **`repository/`**: Abstrai as operações de banco de dados (SQLAlchemy), isolando a lógica de persistência.
- **`model/`**: Define a estrutura dos dados tanto para o banco (`movie_model.py`) quanto para entrada/saída via API (`movie_schema.py`).
- **`database/`**: Configura o motor do SQLite e a sessão do SQLAlchemy.

---

## 3. Fluxo da Aplicação
O fluxo de dados segue uma linha unidirecional para garantir consistência:

1. **Requisição**: O cliente faz uma chamada HTTP (ex: `GET /filmes/`).
2. **Router**: O `movie_router.py` identifica o endpoint e injeta a dependência do `MovieController`.
3. **Controller**: O `MovieController` aciona o `MovieService`.
4. **Service**: O `MovieService` solicita os dados ao `MovieRepository`.
5. **Repository**: O `MovieRepository` executa a consulta via SQLAlchemy no banco `movies.db`.
6. **Resposta**: O dado retorna pelo mesmo caminho, sendo validado pelo `MovieSchema` antes de chegar ao cliente.

---

## 4. Tecnologias Utilizadas
- **Linguagem**: Python 3.11.
- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) (Performance e documentação automática).
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Mapeamento objeto-relacional).
- **Validação de Dados**: [Pydantic](https://docs.pydantic.dev/) (Schemas e tipagem).
- **Banco de Dados**: SQLite (Leve e sem necessidade de servidor externo).
- **Servidor ASGI**: Uvicorn.
- **Containerização**: Docker e Docker Compose.

---

## 5. Pré-requisitos
Antes de iniciar, certifique-se de ter instalado:
- **Python 3.11** ou superior.
- **Pip** (Gerenciador de pacotes do Python).
- **Docker** e **Docker Compose** (Opcional, para execução via container).

---

## 6. Instalação e Execução (Python puro)

### Passo 1: Clonar o Repositório
```bash
git clone <url-do-repositorio>
cd backend
```

### Passo 2: Criar Ambiente Virtual
```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### Passo 3: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Executar a Aplicação
```bash
uvicorn main:app --reload
```
A API estará disponível em `http://127.0.0.1:8000`.

---

## 7. Instalação e Execução (Docker)

O projeto está configurado para subir rapidamente utilizando Docker Compose.

### Comandos:
```bash
# Para subir o container
docker-compose up --build

# Para rodar em segundo plano
docker-compose up -d
```

- **Porta**: A API será exposta na porta `8000`.
- **Volumes**: O código local está mapeado para dentro do container, permitindo atualizações em tempo real (hot reload).

---

## 8. Configuração do Projeto
- **Banco de Dados**: O arquivo `movies.db` é criado automaticamente na raiz do projeto na primeira execução.
- **CORS**: A aplicação está configurada para aceitar requisições de `localhost` e `localhost:8080` (ajustável em `main.py`).
- **Variáveis de Ambiente**: Utiliza `PYTHONUNBUFFERED=1` para garantir que os logs sejam exibidos imediatamente no console.

---

## 9. Detalhamento dos Módulos

### `repository/movie_repository.py`
Gerencia a conexão ativa com o banco. Um detalhe importante é que as funções `create` e `delete` retornam a lista atualizada de todos os filmes, facilitando a atualização de estados no frontend.

### `controller/movie_controller.py`
Implementa o tratamento de erros HTTP. Caso um filme solicitado por ID não exista, o controller lança uma `HTTPException` com status 404.

### `main.py`
Possui um `exception_handler` global que captura qualquer erro inesperado do sistema e retorna uma mensagem amigável de "Erro interno customizado", evitando vazamento de stacktraces para o usuário final.

---

## 10. API Endpoints

### Filmes
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **GET** | `/filmes/` | Retorna a lista de todos os filmes. |
| **GET** | `/filmes/{id}/` | Retorna os detalhes de um filme específico. |
| **POST** | `/filmes/` | Cadastra um novo filme. |
| **DELETE** | `/filmes/{id}/` | Remove um filme do sistema. |

#### Exemplo de Payload (POST):
```json
{
  "name": "Interestelar",
  "genre": "Ficção Científica",
  "duration": 169,
  "rate": 8.7
}
```

---

## 11. Boas Práticas e Convenções
- **Dependency Injection**: Uso extensivo do `Depends` do FastAPI para gerenciar instâncias de classes.
- **Type Hinting**: Todo o projeto utiliza tipagem estática do Python para maior clareza e redução de bugs.
- **DRY (Don't Repeat Yourself)**: Lógicas de banco isoladas em repositórios.
- **Surgical Updates**: O banco de dados é inicializado automaticamente via `Base.metadata.create_all` no repositório.

---

## 12. Possíveis Melhorias
1. **Paginação**: Adicionar paginação no endpoint `GET /filmes/` para lidar com grandes volumes de dados.
2. **Testes Automatizados**: Implementar testes unitários com `pytest` e testes de integração para as rotas.
3. **Logs**: Implementar um sistema de log estruturado para monitoramento em produção.
4. **Migrations**: Utilizar `Alembic` para gerenciar mudanças no esquema do banco de dados em vez do `create_all`.
5. **Autenticação**: Adicionar proteção às rotas de escrita (POST/DELETE) usando JWT.

---
Documentação gerada para suporte ao desenvolvimento e onboarding.
