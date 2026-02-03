---
stepsCompleted: ['step-01-validate-prerequisites', 'step-02-design-epics', 'step-03-create-stories', 'step-04-final-validation']
inputDocuments: ['_bmad-output/planning-artifacts/prd.md', '_bmad-output/planning-artifacts/architecture.md']
---

# hyper-bmad - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for hyper-bmad, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

FR1: Administrador pode criar produtos com nome, descrição e preço
FR2: Administrador pode editar produtos existentes
FR3: Cliente pode listar todos os produtos disponíveis
FR4: Sistema valida que nome do produto é obrigatório
FR5: Sistema valida que preço do produto é maior que zero
FR6: Cliente pode adicionar produtos ao carrinho especificando quantidade
FR7: Cliente pode remover items do carrinho
FR8: Cliente pode visualizar carrinho com todos os items
FR9: Sistema calcula total do carrinho automaticamente
FR10: Sistema mantém carrinho por sessão anônima
FR11: Sistema persiste produtos no banco de dados
FR12: Sistema persiste carrinho no banco de dados
FR13: Sistema retorna dados em formato JSON

### NonFunctional Requirements

NFR1: API responde a requisições em menos de 500ms
NFR2: Operações de leitura (GET) completam em menos de 200ms
NFR3: Operações de escrita (POST/PUT/DELETE) completam em menos de 500ms

### Additional Requirements

- **Starter template (Epic 1 Story 1):** Inicialização manual com FastAPI; comando `pip install fastapi uvicorn sqlalchemy`; estrutura de pastas criada manualmente durante implementação (sem cookiecutter).
- **Infrastructure:** Execução 100% local; SQLite como banco; sem Alembic no MVP (criação manual de tabelas no código de inicialização).
- **Session management:** Session ID gerado pela API (UUID v4); cliente envia via header `X-Session-ID` ou cookie; se não fornecido, API cria nova sessão; session_id armazenado em `carts.session_id`.
- **Error handling:** Exception handlers customizados no FastAPI; respostas JSON consistentes com códigos HTTP 200, 201, 400, 404, 500; formato de erro FastAPI padrão `{"detail": "..."}`.
- **Project structure:** Arquitetura em camadas: `app/api/`, `app/services/`, `app/models/`, `app/schemas/`, `app/utils/`; `tests/` espelhando estrutura do código.
- **Naming conventions:** Banco em snake_case (tabelas: `products`, `carts`, `cart_items`; colunas snake_case); API REST plural; código: arquivos/funções/variáveis snake_case, classes PascalCase.
- **Request/Response:** JSON, Content-Type application/json, UTF-8; resposta direta sem wrapper; listas como array direto; campos JSON em snake_case; datas ISO 8601.
- **Data layer:** SQLAlchemy 2.x como ORM; Pydantic para validação de request/response; tabelas `products`, `carts`, `cart_items` com FK `product_id`, `cart_id`.
- **API documentation:** Swagger UI em `/docs` e ReDoc em `/redoc` (automático FastAPI).
- **Logging:** Logging básico Python com níveis (DEBUG, INFO, WARNING, ERROR) e contexto estruturado via `extra`.
- **Custom exceptions:** ProductNotFoundError, CartNotFoundError, ValidationError em `app/utils/exceptions.py`; handlers globais em `app/main.py`.
- **Validation:** Pydantic schemas para validação automática na API; regras de negócio (nome obrigatório, preço > 0) também na camada de serviços.

### FR Coverage Map

FR1: Epic 1 - Criar produtos (nome, descrição, preço)
FR2: Epic 1 - Editar produtos existentes
FR3: Epic 1 - Listar produtos disponíveis
FR4: Epic 1 - Validação: nome obrigatório
FR5: Epic 1 - Validação: preço maior que zero
FR6: Epic 2 - Adicionar itens ao carrinho com quantidade
FR7: Epic 2 - Remover itens do carrinho
FR8: Epic 2 - Visualizar carrinho com todos os itens
FR9: Epic 2 - Cálculo automático do total do carrinho
FR10: Epic 2 - Carrinho por sessão anônima
FR11: Epic 1 - Persistência de produtos no banco
FR12: Epic 2 - Persistência de carrinho no banco
FR13: Epic 1 e 2 - Respostas em JSON (aplicado em ambos os épicos)

## Epic List

### Epic 1: Catálogo de Produtos
Administrador pode cadastrar e editar produtos; cliente pode listar o catálogo. API expõe produtos com validações e persistência.
**FRs covered:** FR1, FR2, FR3, FR4, FR5, FR11, FR13

### Epic 2: Carrinho de Compras
Cliente pode adicionar e remover itens do carrinho, visualizar carrinho e total, com sessão anônima persistida.
**FRs covered:** FR6, FR7, FR8, FR9, FR10, FR12, FR13

---

## Epic 1: Catálogo de Produtos

Administrador pode cadastrar e editar produtos; cliente pode listar o catálogo. API expõe produtos com validações e persistência.

### Story 1.1: Project Setup and API Foundation

As a developer,
I want a runnable FastAPI project with the agreed folder structure and dependencies,
So that I can implement features on a solid base.

**Acceptance Criteria:**

**Given** the project root with no existing app structure,
**When** I run `pip install fastapi uvicorn sqlalchemy` (or equivalent requirements.txt) and `uvicorn app.main:app --reload`,
**Then** the API starts and `/docs` returns Swagger UI.
**And** the project has folders `app/`, `app/api/`, `app/services/`, `app/models/`, `app/schemas/`, `app/utils/`, and `tests/` with `__init__.py` where needed.
**And** `app/main.py` initializes the FastAPI app and is the entry point.

### Story 1.2: Product Model and Database

As a developer,
I want the Product entity and SQLite table with custom exceptions for product errors,
So that products can be persisted and API can return consistent errors.

**Acceptance Criteria:**

**Given** the app is running,
**When** the application starts,
**Then** the `products` table exists with columns `id`, `name`, `description`, `price`, `created_at` (snake_case).
**And** the `Product` model is defined in `app/models/product.py` using SQLAlchemy with table name `products`.
**And** table creation is performed during database initialization (no Alembic).
**And** `app/utils/exceptions.py` defines `ProductNotFoundError` and it is registered in `app/main.py` so that raising it returns 404 with `{"detail": "..."}`.

### Story 1.3: Create Product

As an administrator,
I want to create a product with name, description and price,
So that the product is available in the catalog.

**Acceptance Criteria:**

**Given** the API is running and the database has the `products` table,
**When** I send `POST /products` with JSON body `{"name": "<string>", "description": "<string or null>", "price": <number>}` with name present and price > 0,
**Then** the product is saved to the database and the API returns 201 with the created product (id, name, description, price) in JSON.
**And** when name is missing or price is less than or equal to 0, the API returns 400 with a JSON body like `{"detail": "..."}`.
**And** response Content-Type is application/json; field names in JSON use snake_case.

### Story 1.4: List Products

As a client,
I want to list all products,
So that I can see the catalog.

**Acceptance Criteria:**

**Given** the API is running,
**When** I send `GET /products`,
**Then** the API returns 200 with a JSON array of products, each with id, name, description, price (and created_at if applicable).
**And** when there are no products, the API returns 200 with an empty array `[]`.
**And** response is direct array (no wrapper object).

### Story 1.5: Edit Product

As an administrator,
I want to edit an existing product by id,
So that catalog information stays correct.

**Acceptance Criteria:**

**Given** at least one product exists in the database,
**When** I send `PUT /products/{id}` with valid JSON (name, description optional, price > 0),
**Then** the product with that id is updated and the API returns 200 with the updated product in JSON.
**And** when the id does not exist, the API returns 404 with `{"detail": "..."}`.
**And** when the payload is invalid (e.g. missing name or price <= 0), the API returns 400 with `{"detail": "..."}`.

---

## Epic 2: Carrinho de Compras

Cliente pode adicionar e remover itens do carrinho, visualizar carrinho e total, com sessão anônima persistida.

### Story 2.1: Cart and CartItem Models

As a developer,
I want Cart and CartItem entities and SQLite tables, plus cart-related exception,
So that the cart and its items can be persisted and the API can return consistent errors.

**Acceptance Criteria:**

**Given** the app is running and the `products` table exists,
**When** the application starts,
**Then** the tables `carts` and `cart_items` exist: `carts` with `id`, `session_id`, `created_at`; `cart_items` with `id`, `cart_id`, `product_id`, `quantity`, and any timestamps (snake_case).
**And** foreign keys use naming `cart_id`, `product_id`.
**And** `app/utils/exceptions.py` defines `CartNotFoundError` (if not already present) and it is registered so that raising it returns 404 with `{"detail": "..."}`.

### Story 2.2: Get Cart and Session Management

As a client,
I want to get my cart (by session) with items and total,
So that I can see what I have added and the total amount.

**Acceptance Criteria:**

**Given** the API is running and cart tables exist,
**When** I send `GET /cart` without a session identifier,
**Then** the API creates a new session (UUID v4), creates an empty cart for it, and returns 200 with a cart representation including `items` (empty array) and `total` (e.g. 0 or 0.00).
**And** when I send `GET /cart` with header `X-Session-ID: <session_id>` (or equivalent session mechanism), the API returns 200 with that cart’s items and total.
**And** session_id is stored in the `carts` table; total is calculated from cart items (quantity × product price).
**And** response is JSON with snake_case fields (e.g. items, total, session_id if exposed).

### Story 2.3: Add Item to Cart

As a client,
I want to add a product to my cart with a quantity,
So that I can build my order.

**Acceptance Criteria:**

**Given** the API is running, products exist, and I have a cart (session),
**When** I send `POST /cart/items` with JSON e.g. `{"product_id": <id>, "quantity": <positive integer>}` and valid session (e.g. X-Session-ID),
**Then** the item is added to my cart (or quantity updated if the product is already in the cart, per product behavior) and the API returns 201 or 200 with the cart or item representation.
**And** when product_id does not exist, the API returns 404.
**And** when quantity is invalid (e.g. not positive), the API returns 400 with `{"detail": "..."}`.
**And** the cart total is consistent with the sum of (quantity × product price) for all items (FR9).

### Story 2.4: Remove Item from Cart

As a client,
I want to remove an item from my cart by item id,
So that I can correct my selection.

**Acceptance Criteria:**

**Given** my cart has at least one item,
**When** I send `DELETE /cart/items/{id}` with the cart item id and valid session,
**Then** that item is removed from the cart and the API returns 200 (or 204), and the cart total is recalculated.
**And** when the item id does not exist or does not belong to my cart, the API returns 404 with `{"detail": "..."}`.
**And** after removal, `GET /cart` shows the updated items and total.
