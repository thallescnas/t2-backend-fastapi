# 🚗 Car API

Este projeto é um sistema de gerenciamento de carros desenvolvido como parte de um trabalho para a matéria de **Backend**. A API permite realizar as operações básicas de CRUD (Create, Read, Update, Delete) para o cadastro de veículos.

## 📝 Descrição
A aplicação foi construída utilizando **FastAPI**, **SQLAlchemy** e **PostgreSQL**, seguindo uma arquitetura organizada em modelos, esquemas e rotas.

### Funcionalidades:
- Listagem de todos os carros.
- Consulta de um carro específico por ID.
- Cadastro de novos carros.
- Atualização de dados de carros existentes.
- Remoção de carros.
- Consulta do carro mais recentemente cadastrado.
- Endpoint de health check para verificação de status da API.

## 🛣️ Endpoints

### Saúde do Sistema
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/health` | Verifica se a API está online |

### Gerenciamento de Carros
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/cars/` | Lista todos os carros cadastrados |
| `GET` | `/cars/{id}` | Obtém os detalhes de um carro específico pelo ID |
| `POST` | `/cars/` | Cadastra um novo veículo |
| `PATCH` | `/cars/{id}` | Atualiza parcialmente os dados de um carro |
| `DELETE` | `/cars/{id}` | Remove um veículo do sistema |
| `GET` | `/cars/latest` | Retorna o carro cadastrado mais recentemente |

## 🚀 Instruções para Execução

### Pré-requisitos
- Docker e Docker Compose instalados

### Instalação e Execução
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd p2-t2-fastapi
   ```

2. Configure as variáveis de ambiente copiando e editando o arquivo `.env.EXAMPLE`:
   ```bash
   cp .env.EXAMPLE .env
   ```
   Abra o arquivo `.env` e preencha as informações do seu banco de dados.
   *Nota: No `DB_URL`, utilize `db` como hostname, pois é o nome do serviço definido no `compose.yml`.*

3. Suba a aplicação utilizando o Docker Compose:
   ```bash
   docker compose up --build
   ```

A API estará disponível em `http://127.0.0.1:8000`. A documentação interativa (Swagger) pode ser acessada em `http://127.0.0.1:8000/docs`.

---

## 🧪 Instruções para Execução dos Testes

O projeto utiliza o framework `pytest` para a realização de testes automatizados.

Para executar os testes dentro do container da aplicação, utilize o comando:
```bash
docker compose exec backend pytest
```

---

## 👤 Autor
**Thalles C. Nascimento**
