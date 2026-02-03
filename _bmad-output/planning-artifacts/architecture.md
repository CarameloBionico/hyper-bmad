---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]
workflowType: 'architecture'
lastStep: 8
status: 'complete'
completedAt: '2026-02-03 16:57:46'
inputDocuments: ['_bmad-output/planning-artifacts/prd.md', '_bmad-output/planning-artifacts/product-brief-hyper-bmad-2026-02-03-144132.md']
workflowType: 'architecture'
project_name: 'hyper-bmad'
user_name: 'Pena'
date: '2026-02-03'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

---

## Project Context Analysis

### Requirements Overview

**Functional Requirements:**
- 13 FRs organizados em 3 áreas: Product Management (5), Cart Management (5), Data Persistence (3)
- CRUD completo de produtos com validações básicas
- Gerenciamento de carrinho com sessão anônima
- Persistência em SQLite e comunicação via JSON

**Non-Functional Requirements:**
- Performance: API < 500ms, GET < 200ms, POST/PUT/DELETE < 500ms
- Sem requisitos de segurança complexos (sem autenticação)
- Sem requisitos de escalabilidade (MVP local)

**Scale & Complexity:**
- Primary domain: API Backend
- Complexity level: Baixa
- Estimated architectural components: 3-4 (API, Service, Data, Validation)

### Technical Constraints & Dependencies

- Stack definido: Python + SQLite
- Sem autenticação/autorização
- Sem integrações externas
- Execução 100% local
- Sem versionamento de API no MVP

### Cross-Cutting Concerns Identified

- Validação de dados (nome obrigatório, preço > 0)
- Tratamento de erros (códigos HTTP padrão)
- Serialização JSON (request/response)
- Gerenciamento de sessão (carrinho anônimo)

---

## Starter Template Evaluation

### Primary Technology Domain

API Backend baseado na análise de requisitos do projeto.

### Starter Options Considered

Para este MVP simples, foram avaliadas duas abordagens:

1. **Criar do zero** (recomendado)
   - Estrutura mínima e controle total
   - Ideal para demonstrar desenvolvimento com IA
   - Menos overhead desnecessário

2. **Usar starter template** (não recomendado para MVP)
   - Templates como `fastapi-cookiecutter` ou `full-stack-fastapi-template`
   - Mais estrutura pré-configurada do que necessário
   - Pode adicionar complexidade desnecessária

### Selected Starter: Estrutura Manual com FastAPI

**Rationale for Selection:**
- MVP muito simples (6 endpoints apenas)
- Permite demonstrar cada decisão arquitetural explicitamente
- Estrutura mínima e clara para aprendizado
- SQLite já definido, não precisa de configuração complexa
- Ideal para contexto educacional (curso de Hyper Coding)

**Initialization Command:**

```bash
# Instalação de dependências básicas
pip install fastapi uvicorn sqlalchemy

# Estrutura será criada manualmente durante implementação
```

**Architectural Decisions Provided by FastAPI:**

**Language & Runtime:**
- Python 3.8+ com FastAPI framework
- Async/await support nativo
- Type hints para validação automática

**Data Validation:**
- Pydantic models para validação automática
- Validação de tipos e constraints
- Serialização/deserialização JSON automática

**API Documentation:**
- Swagger UI automático em `/docs`
- OpenAPI schema automático
- ReDoc em `/redoc`

**Build Tooling:**
- Uvicorn como ASGI server
- Hot reload em desenvolvimento
- Sem build step necessário (Python interpretado)

**Code Organization:**
- Estrutura será definida durante decisões arquiteturais
- Padrão recomendado: separação por camadas (API, Service, Data)

**Development Experience:**
- Hot reload automático
- Validação em tempo de desenvolvimento
- Documentação interativa durante desenvolvimento

**Note:** Inicialização do projeto usando esta estrutura será a primeira story de implementação.

---

## Core Architectural Decisions

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**
- ORM: SQLAlchemy (para abstração de banco e type safety)
- Estrutura de projeto: Layered structure (api/, services/, models/)
- Gerenciamento de sessão: Session ID gerado automaticamente
- Tratamento de erros: Exception handlers customizados

**Important Decisions (Shape Architecture):**
- Migrations: Criação manual de tabelas (sem Alembic no MVP)
- Estrutura de pastas: Separação por camadas

**Deferred Decisions (Post-MVP):**
- Alembic para migrations versionadas (pode ser adicionado depois)
- Rate limiting (não necessário no MVP)
- Caching (não necessário no MVP)
- Logging estruturado avançado (básico é suficiente)

### Data Architecture

**ORM Selection: SQLAlchemy**

- **Version:** Latest stable (2.x)
- **Rationale:** 
  - Abstração de banco de dados facilita manutenção
  - Type safety com models Python
  - Integração nativa com FastAPI
  - Padrão da indústria para Python APIs
  - Facilita evolução futura (trocar SQLite por PostgreSQL, por exemplo)
- **Affects:** Todos os componentes de acesso a dados
- **Provided by Starter:** Não - decisão arquitetural

**Database Access Pattern:**

- **Pattern:** Repository pattern via SQLAlchemy models
- **Rationale:** Separação de responsabilidades, facilita testes
- **Affects:** Services layer

**Migration Strategy:**

- **Decision:** Criação manual de tabelas no código de inicialização
- **Rationale:** 
  - MVP muito simples (2-3 tabelas apenas)
  - Evita complexidade desnecessária
  - Pode migrar para Alembic depois se necessário
- **Version:** N/A (sem Alembic no MVP)
- **Affects:** Database initialization
- **Deferred:** Alembic pode ser adicionado em fase posterior

**Data Validation:**

- **Decision:** Pydantic models (fornecido pelo FastAPI)
- **Version:** Incluído no FastAPI
- **Rationale:** Validação automática de tipos e constraints
- **Affects:** API layer (request/response validation)

### Authentication & Security

**Authentication Method:**

- **Decision:** Sem autenticação (sessão anônima)
- **Rationale:** Definido no PRD - MVP não requer autenticação
- **Affects:** Todos os endpoints (todos públicos)
- **Deferred:** Autenticação pode ser adicionada em fase posterior

**Session Management:**

- **Decision:** Session ID gerado automaticamente pela API
- **Implementation:** 
  - API gera UUID na primeira requisição ao carrinho
  - Cliente armazena e envia em header `X-Session-ID` ou cookie
  - Se não fornecido, API cria nova sessão
- **Rationale:** 
  - Simples para o cliente (não precisa gerar ID)
  - API tem controle total sobre formato e validação
  - Facilita evolução futura (adicionar expiração, etc.)
- **Affects:** Cart endpoints
- **Storage:** Session ID armazenado junto com carrinho no banco

**Security Considerations:**

- **Decision:** Validação básica de inputs (Pydantic)
- **Rationale:** MVP local, sem requisitos de segurança complexos
- **Deferred:** 
  - Rate limiting
  - Input sanitization avançada
  - CORS policies (se necessário para frontend)

### API & Communication Patterns

**API Design Pattern:**

- **Decision:** REST (definido no PRD)
- **Rationale:** Padrão simples e bem compreendido
- **Affects:** Todos os endpoints

**Error Handling:**

- **Decision:** Exception handlers customizados no FastAPI
- **Implementation:**
  - Handlers globais para diferentes tipos de exceção
  - Respostas JSON consistentes com código HTTP apropriado
  - Mensagens de erro claras
- **Rationale:** 
  - Melhor controle sobre formato de erros
  - Consistência em toda a API
  - Facilita debugging
- **Error Codes:** 200, 201, 400, 404, 500 (conforme PRD)
- **Affects:** Todos os endpoints

**Request/Response Format:**

- **Decision:** JSON (definido no PRD)
- **Content-Type:** application/json
- **Encoding:** UTF-8
- **Affects:** Todos os endpoints

**API Documentation:**

- **Decision:** Swagger UI automático do FastAPI
- **Endpoint:** `/docs` e `/redoc`
- **Rationale:** Fornecido automaticamente pelo FastAPI
- **Affects:** Nenhum (automático)

### Project Structure

**Code Organization:**

- **Decision:** Layered structure (separation of concerns)
- **Structure:**
  ```
  app/
    api/          # FastAPI routers e endpoints
    services/     # Business logic
    models/       # SQLAlchemy models e Pydantic schemas
    database.py   # Database connection e setup
    main.py       # FastAPI app initialization
  ```
- **Rationale:** 
  - Separação clara de responsabilidades
  - Fácil de entender e manter
  - Escalável para adicionar features
  - Padrão comum em projetos FastAPI
- **Affects:** Toda a organização do código

**Configuration Management:**

- **Decision:** Variáveis de ambiente simples (se necessário)
- **Rationale:** MVP local, configuração mínima
- **Deferred:** Arquivo de configuração estruturado (pode ser adicionado depois)

### Infrastructure & Deployment

**Hosting Strategy:**

- **Decision:** Local development only (MVP)
- **Rationale:** Definido no PRD - execução 100% local
- **Deferred:** Deploy em produção (não no escopo do MVP)

**Environment Configuration:**

- **Decision:** Configuração mínima (database path, etc.)
- **Rationale:** MVP simples, sem necessidade de múltiplos ambientes
- **Affects:** Database initialization

**Logging:**

- **Decision:** Logging básico do Python
- **Rationale:** Suficiente para MVP local
- **Deferred:** Logging estruturado (pode ser adicionado depois)

**Monitoring:**

- **Decision:** Nenhum (MVP local)
- **Rationale:** Não necessário para desenvolvimento local
- **Deferred:** Monitoring e métricas (para produção futura)

### Decision Impact Analysis

**Implementation Sequence:**

1. **Database Setup** (SQLAlchemy + SQLite)
   - Criar models (Product, Cart, CartItem)
   - Configurar conexão com SQLite
   - Criar tabelas manualmente

2. **Project Structure**
   - Criar estrutura de pastas (api/, services/, models/)
   - Configurar FastAPI app (main.py)

3. **Services Layer**
   - ProductService (CRUD de produtos)
   - CartService (gerenciamento de carrinho)

4. **API Layer**
   - Product endpoints (POST, PUT, GET)
   - Cart endpoints (POST, DELETE, GET)

5. **Error Handling**
   - Exception handlers customizados
   - Validações com Pydantic

**Cross-Component Dependencies:**

- **SQLAlchemy models** → **Services** → **API endpoints**
- **Pydantic schemas** → **API endpoints** (request/response validation)
- **Database connection** → **Services** (via dependency injection)
- **Session management** → **CartService** (gerenciamento de sessão anônima)

**Technology Versions:**

- **FastAPI:** Latest stable (0.104+)
- **SQLAlchemy:** Latest stable (2.0+)
- **Uvicorn:** Latest stable (0.24+)
- **Pydantic:** Incluído no FastAPI (v2)
- **Python:** 3.8+ (compatibilidade com FastAPI)

---

## Implementation Patterns & Consistency Rules

### Pattern Categories Defined

**Critical Conflict Points Identified:**
5 áreas principais onde agentes de IA poderiam fazer escolhas diferentes: Naming, Structure, Format, Communication, e Process patterns.

### Naming Patterns

**Database Naming Conventions:**

- **Tables:** `snake_case` plural
  - ✅ `products`, `cart_items`, `carts`
  - ❌ `Products`, `Product`, `CartItem`

- **Columns:** `snake_case`
  - ✅ `user_id`, `created_at`, `product_name`
  - ❌ `userId`, `createdAt`, `productName`

- **Foreign Keys:** `{referenced_table}_id`
  - ✅ `product_id`, `cart_id`
  - ❌ `fk_product`, `productId`, `ProductId`

- **Indexes:** `idx_{table}_{column}` (se necessário)
  - ✅ `idx_products_name`, `idx_cart_items_cart_id`
  - ❌ `products_name_index`, `cart_items_cart_id_idx`

**API Naming Conventions:**

- **Endpoints:** Plural nouns, RESTful
  - ✅ `GET /products`, `POST /products`, `GET /cart/items`
  - ❌ `GET /product`, `POST /product`, `GET /cart/item`

- **Route Parameters:** `{id}` (FastAPI padrão)
  - ✅ `GET /products/{id}`, `DELETE /cart/items/{id}`
  - ❌ `GET /products/:id`, `DELETE /cart/items/<id>`

- **Query Parameters:** `snake_case`
  - ✅ `?page_size=10&page=1`, `?user_id=123`
  - ❌ `?pageSize=10&page=1`, `?userId=123`

- **Headers:** `X-` prefix para custom headers
  - ✅ `X-Session-ID`, `X-Request-ID`
  - ❌ `Session-ID`, `session-id`

**Code Naming Conventions:**

- **Files:** `snake_case.py`
  - ✅ `user_service.py`, `product_model.py`, `cart_schemas.py`
  - ❌ `UserService.py`, `userService.py`, `product-model.py`

- **Classes:** `PascalCase`
  - ✅ `UserService`, `ProductModel`, `CartItemSchema`
  - ❌ `user_service`, `userService`, `user-service`

- **Functions/Methods:** `snake_case`
  - ✅ `get_user`, `create_product`, `calculate_total`
  - ❌ `getUser`, `GetUser`, `get-user`

- **Variables:** `snake_case`
  - ✅ `user_id`, `product_list`, `cart_total`
  - ❌ `userId`, `productList`, `cartTotal`

- **Constants:** `UPPER_SNAKE_CASE`
  - ✅ `MAX_CART_SIZE`, `DEFAULT_PAGE_SIZE`
  - ❌ `maxCartSize`, `MaxCartSize`

### Structure Patterns

**Project Organization:**

```
app/
├── api/              # FastAPI routers
│   ├── products.py   # Product endpoints
│   └── cart.py       # Cart endpoints
├── services/         # Business logic
│   ├── product_service.py
│   └── cart_service.py
├── models/          # SQLAlchemy models
│   ├── product.py
│   └── cart.py
├── schemas/         # Pydantic schemas
│   ├── product.py
│   └── cart.py
├── utils/           # Shared utilities
│   └── exceptions.py
├── database.py      # Database connection
└── main.py          # FastAPI app
```

**File Structure Patterns:**

- **Tests:** Pasta `tests/` separada, espelha estrutura do código
  - ✅ `tests/api/test_products.py`, `tests/services/test_cart_service.py`
  - ❌ `app/api/test_products.py` (co-localizado)

- **Utils:** Pasta `utils/` para helpers compartilhados
  - ✅ `utils/exceptions.py`, `utils/validators.py`
  - ❌ Helpers dentro de cada módulo

- **Schemas:** Separados de models (Pydantic vs SQLAlchemy)
  - ✅ `schemas/product.py` (Pydantic), `models/product.py` (SQLAlchemy)
  - ❌ Tudo em `models/product.py`

- **Config:** Arquivo `config.py` na raiz de `app/` (se necessário)
  - ✅ `app/config.py`
  - ❌ `config/settings.py` (complexidade desnecessária para MVP)

### Format Patterns

**API Response Formats:**

- **Success Response:** Resposta direta, sem wrapper
  - ✅ `{"id": 1, "name": "Product", "price": 10.99}`
  - ❌ `{"data": {"id": 1, ...}, "error": null}`

- **Error Response:** Formato FastAPI padrão
  - ✅ `{"detail": "Product not found"}`
  - ❌ `{"error": {"message": "...", "code": "..."}}`

- **List Response:** Array direto
  - ✅ `[{"id": 1, ...}, {"id": 2, ...}]`
  - ❌ `{"items": [...], "count": 2}`

- **Date/Time Format:** ISO 8601 strings
  - ✅ `"2024-01-15T10:30:00Z"`, `"2024-01-15T10:30:00+00:00"`
  - ❌ `1642239000` (timestamp), `"15/01/2024"` (formato customizado)

**Data Exchange Formats:**

- **JSON Field Naming:** `snake_case` (convenção Python)
  - ✅ `{"user_id": 1, "created_at": "2024-01-15T10:30:00Z"}`
  - ❌ `{"userId": 1, "createdAt": "2024-01-15T10:30:00Z"}`

- **Boolean Values:** `true`/`false` (não `1`/`0`)
  - ✅ `{"active": true, "available": false}`
  - ❌ `{"active": 1, "available": 0}`

- **Null Handling:** `null` para valores ausentes
  - ✅ `{"description": null}`
  - ❌ `{"description": ""}` (string vazia), omitir campo

- **Empty Arrays:** Array vazio `[]`, não `null`
  - ✅ `{"items": []}`
  - ❌ `{"items": null}`

### Communication Patterns

**Logging Patterns:**

- **Format:** Texto simples com contexto
  - ✅ `logger.info("Product created", extra={"product_id": 1, "name": "Product"})`
  - ❌ `logger.info("Product created")` (sem contexto)

- **Log Levels:**
  - **DEBUG:** Desenvolvimento, detalhes técnicos
  - **INFO:** Operações normais (criar produto, adicionar ao carrinho)
  - **WARNING:** Situações anômalas mas recuperáveis
  - **ERROR:** Erros que requerem atenção

- **Structured Logging:** Usar `extra` para contexto
  - ✅ `logger.error("Failed to create product", extra={"error": str(e), "data": product_data})`
  - ❌ `logger.error(f"Failed: {e}")` (sem estrutura)

**Error Handling Patterns:**

- **Exception Classes:** Custom exceptions por tipo
  - ✅ `ProductNotFoundError`, `ValidationError`, `CartError`
  - ❌ Usar apenas `Exception` genérica

- **User Messages:** Mensagens claras e amigáveis
  - ✅ `"Product not found"`, `"Invalid price: must be greater than 0"`
  - ❌ `"Error 404"`, `"Validation failed"` (muito genérico)

- **Technical Details:** Apenas em logs, não em resposta ao usuário
  - ✅ Log: `"Database connection failed: timeout after 5s"`
  - ✅ User: `"Service temporarily unavailable"`
  - ❌ User: `"Database connection failed: timeout after 5s"`

### Process Patterns

**Error Handling:**

- **Global Exception Handlers:** Handlers customizados no FastAPI
  - ✅ `@app.exception_handler(ProductNotFoundError)`
  - ❌ Tratamento inline em cada endpoint

- **Validation:** Pydantic models para validação automática
  - ✅ Usar Pydantic schemas em endpoints
  - ❌ Validação manual com if/else

- **Error Recovery:** Retornar erro apropriado, não silenciar
  - ✅ `raise ProductNotFoundError("Product not found")`
  - ❌ `return None` ou `return {}` silenciosamente

**Loading States:**

- **N/A para MVP:** API não tem loading states (é síncrona)
- **Deferred:** Loading states serão relevantes quando houver frontend

**Session Management:**

- **Session ID Generation:** UUID v4
  - ✅ `import uuid; session_id = str(uuid.uuid4())`
  - ❌ IDs sequenciais ou timestamps

- **Session Storage:** Banco de dados (tabela `carts`)
  - ✅ Session ID armazenado em `carts.session_id`
  - ❌ Memória (não persiste)

### Enforcement Guidelines

**All AI Agents MUST:**

- Seguir convenções de naming (snake_case para Python)
- Usar estrutura de pastas definida (api/, services/, models/, schemas/)
- Retornar erros no formato FastAPI padrão (`{"detail": "..."}`)
- Usar Pydantic schemas para validação de request/response
- Implementar exception handlers customizados
- Seguir padrão de logging (níveis apropriados, contexto estruturado)

**Pattern Enforcement:**

- **Code Review:** Verificar padrões durante revisão
- **Linting:** Usar ferramentas como `black`, `flake8` para formatação
- **Documentation:** Padrões documentados neste arquivo
- **Examples:** Seguir exemplos de "Good Examples" abaixo

**Process for Updating Patterns:**

- Padrões podem ser refinados durante implementação
- Mudanças devem ser documentadas neste arquivo
- Todos os agentes devem seguir padrões atualizados

### Pattern Examples

**Good Examples:**

**Database Model:**
```python
# models/product.py
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
```

**API Endpoint:**
```python
# api/products.py
@router.get("/products/{id}", response_model=ProductSchema)
async def get_product(id: int):
    product = await product_service.get_by_id(id)
    if not product:
        raise ProductNotFoundError(f"Product {id} not found")
    return product
```

**Service Layer:**
```python
# services/product_service.py
class ProductService:
    async def get_by_id(self, product_id: int) -> Product:
        product = await self.repository.get(product_id)
        if not product:
            raise ProductNotFoundError(f"Product {product_id} not found")
        return product
```

**Error Response:**
```json
{
  "detail": "Product not found"
}
```

**Anti-Patterns:**

❌ **Inconsistent Naming:**
```python
# BAD: Mixed naming conventions
class productService:  # Should be ProductService
    def getUserData(self):  # Should be get_user_data
        userId = 123  # Should be user_id
```

❌ **Wrong Response Format:**
```python
# BAD: Custom wrapper instead of direct response
return {"data": product, "error": None}  # Should return product directly
```

❌ **Missing Validation:**
```python
# BAD: Manual validation instead of Pydantic
if not name or len(name) < 1:
    raise ValueError("Invalid")  # Should use Pydantic schema
```

❌ **Inconsistent Error Format:**
```json
// BAD: Custom error format
{
  "error": {
    "message": "Not found",
    "code": "404"
  }
}
// Should be: {"detail": "Not found"}
```

---

## Project Structure & Boundaries

### Complete Project Directory Structure

```
hyper-bmad/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .env                         # Environment variables (local, gitignored)
├── .gitignore                   # Git ignore rules
├── .python-version              # Python version (if using pyenv)
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app initialization
│   ├── database.py              # SQLAlchemy database setup
│   ├── config.py                # Configuration management (if needed)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── products.py          # Product endpoints (FR1-FR5)
│   │   ├── cart.py              # Cart endpoints (FR6-FR10)
│   │   └── dependencies.py      # Shared dependencies (DB session, etc.)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── product_service.py   # Product business logic
│   │   └── cart_service.py      # Cart business logic
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py              # SQLAlchemy Base
│   │   ├── product.py           # Product model (FR11)
│   │   └── cart.py              # Cart and CartItem models (FR12)
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── product.py           # Product Pydantic schemas
│   │   └── cart.py              # Cart Pydantic schemas
│   └── utils/
│       ├── __init__.py
│       └── exceptions.py        # Custom exceptions
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── api/
│   │   ├── __init__.py
│   │   ├── test_products.py     # Product API tests
│   │   └── test_cart.py         # Cart API tests
│   ├── services/
│   │   ├── __init__.py
│   │   ├── test_product_service.py
│   │   └── test_cart_service.py
│   └── utils/
│       └── test_exceptions.py
├── database.db                  # SQLite database file (gitignored)
└── .github/                     # GitHub workflows (optional)
    └── workflows/
        └── ci.yml               # CI pipeline (optional)
```

### Architectural Boundaries

**API Boundaries:**

- **External API Endpoints:**
  - `GET /products` - List all products (FR3)
  - `POST /products` - Create product (FR1)
  - `PUT /products/{id}` - Update product (FR2)
  - `GET /cart` - Get cart with items (FR8)
  - `POST /cart/items` - Add item to cart (FR6)
  - `DELETE /cart/items/{id}` - Remove item from cart (FR7)

- **Internal Service Boundaries:**
  - `ProductService` - Handles all product business logic
  - `CartService` - Handles all cart business logic and total calculation (FR9)
  - Services communicate only through defined interfaces
  - Services do not call other services directly (if needed, use dependency injection)

- **Data Access Layer Boundaries:**
  - SQLAlchemy models in `models/` directory
  - Services use models via repository pattern (models act as repositories)
  - No direct database access from API layer
  - Database connection managed in `database.py`

**Component Boundaries:**

- **API Layer (`app/api/`):**
  - Handles HTTP requests/responses
  - Validates input using Pydantic schemas
  - Calls services for business logic
  - Returns JSON responses (FR13)
  - Does NOT contain business logic

- **Service Layer (`app/services/`):**
  - Contains all business logic
  - Validates business rules (FR4, FR5)
  - Performs calculations (FR9)
  - Manages session/cart association (FR10)
  - Does NOT handle HTTP concerns

- **Model Layer (`app/models/`):**
  - SQLAlchemy ORM models
  - Database schema definition
  - Data persistence (FR11, FR12)
  - Does NOT contain business logic

- **Schema Layer (`app/schemas/`):**
  - Pydantic models for request/response validation
  - API contract definition
  - Does NOT interact with database

**Data Boundaries:**

- **Database Schema:**
  - `products` table - Stores product data
  - `carts` table - Stores cart sessions (FR10)
  - `cart_items` table - Stores cart items (many-to-many relationship)
  - SQLite database file: `database.db` (local)

- **Data Access Patterns:**
  - Services access models via SQLAlchemy session
  - Session dependency injected via FastAPI dependencies
  - Transactions managed at service level
  - No raw SQL queries (use SQLAlchemy ORM)

- **Session Management:**
  - Session ID stored in `carts.session_id` column
  - Session ID generated as UUID v4
  - Session ID passed via header `X-Session-ID` or cookie

### Requirements to Structure Mapping

**Feature/FR Category Mapping:**

**Product Management (FR1-FR5):**
- **API Endpoints:** `app/api/products.py`
  - `POST /products` → `create_product()` (FR1)
  - `PUT /products/{id}` → `update_product()` (FR2)
  - `GET /products` → `list_products()` (FR3)
- **Business Logic:** `app/services/product_service.py`
  - `create_product()` - Validates and creates product (FR4, FR5)
  - `update_product()` - Validates and updates product (FR4, FR5)
  - `get_all_products()` - Retrieves all products
  - `get_product_by_id()` - Retrieves single product
- **Data Model:** `app/models/product.py`
  - `Product` model - Database table `products` (FR11)
- **Schemas:** `app/schemas/product.py`
  - `ProductCreate` - Request schema for creation
  - `ProductUpdate` - Request schema for update
  - `ProductResponse` - Response schema (FR13)
- **Tests:** `tests/api/test_products.py`, `tests/services/test_product_service.py`

**Cart Management (FR6-FR10):**
- **API Endpoints:** `app/api/cart.py`
  - `GET /cart` → `get_cart()` (FR8)
  - `POST /cart/items` → `add_cart_item()` (FR6)
  - `DELETE /cart/items/{id}` → `remove_cart_item()` (FR7)
- **Business Logic:** `app/services/cart_service.py`
  - `get_or_create_cart()` - Gets cart by session or creates new (FR10)
  - `add_item_to_cart()` - Adds product to cart (FR6)
  - `remove_item_from_cart()` - Removes item from cart (FR7)
  - `calculate_cart_total()` - Calculates total (FR9)
  - `get_cart_with_items()` - Retrieves cart with all items (FR8)
- **Data Models:** `app/models/cart.py`
  - `Cart` model - Database table `carts` (FR12, FR10)
  - `CartItem` model - Database table `cart_items` (FR12)
- **Schemas:** `app/schemas/cart.py`
  - `CartItemCreate` - Request schema for adding item (FR6)
  - `CartItemResponse` - Response schema for cart item
  - `CartResponse` - Response schema for cart with items and total (FR8, FR9)
- **Tests:** `tests/api/test_cart.py`, `tests/services/test_cart_service.py`

**Data Persistence (FR11-FR13):**
- **Database Setup:** `app/database.py`
  - SQLAlchemy engine and session factory
  - Database initialization
  - Table creation (FR11, FR12)
- **Base Model:** `app/models/base.py`
  - SQLAlchemy declarative base
  - Common model fields (id, created_at, etc.)
- **JSON Serialization:** Handled by Pydantic schemas (FR13)
  - FastAPI automatically serializes Pydantic models to JSON

**Cross-Cutting Concerns:**

**Error Handling:**
- **Custom Exceptions:** `app/utils/exceptions.py`
  - `ProductNotFoundError` - Product not found
  - `CartNotFoundError` - Cart not found
  - `ValidationError` - Input validation errors
- **Exception Handlers:** `app/main.py`
  - Global exception handlers for custom exceptions
  - Standard FastAPI error responses

**Validation:**
- **Input Validation:** Pydantic schemas in `app/schemas/`
  - Automatic validation by FastAPI
  - Business rule validation in services (FR4, FR5)

**Session Management:**
- **Session ID Generation:** `app/services/cart_service.py`
  - UUID v4 generation
  - Session storage in `carts` table
- **Session Retrieval:** Via header `X-Session-ID` or cookie
  - Dependency in `app/api/dependencies.py`

### Integration Points

**Internal Communication:**

- **API → Service:**
  - API endpoints call service methods
  - Services return domain models or DTOs
  - No direct database access from API layer

- **Service → Model:**
  - Services use SQLAlchemy models via session
  - Models provide data access abstraction
  - Services handle business logic, models handle persistence

- **API → Schema:**
  - Request validation via Pydantic schemas
  - Response serialization via Pydantic schemas
  - Schemas define API contract

**External Integrations:**

- **None in MVP:** No external service integrations
- **Future:** Payment gateways, email services, etc. would go in `app/services/external/`

**Data Flow:**

1. **Request Flow:**
   ```
   Client → FastAPI Router (api/) → Pydantic Schema Validation → 
   Service Layer → Model Layer → SQLite Database
   ```

2. **Response Flow:**
   ```
   SQLite Database → Model Layer → Service Layer → 
   Pydantic Schema Serialization → FastAPI Router → Client (JSON)
   ```

3. **Error Flow:**
   ```
   Any Layer → Custom Exception → Exception Handler → 
   FastAPI Error Response → Client (JSON)
   ```

### File Organization Patterns

**Configuration Files:**

- **Root Level:**
  - `requirements.txt` - Python dependencies
  - `.env.example` - Environment variables template
  - `.env` - Local environment variables (gitignored)
  - `.gitignore` - Git ignore rules

- **Application Config:**
  - `app/config.py` - Configuration management (if needed)
  - Database URL, app settings, etc.

**Source Organization:**

- **Layered Architecture:**
  - `api/` - HTTP layer (FastAPI routers)
  - `services/` - Business logic layer
  - `models/` - Data access layer (SQLAlchemy)
  - `schemas/` - API contract layer (Pydantic)
  - `utils/` - Shared utilities

- **Feature-Based Within Layers:**
  - Each feature (products, cart) has files in each layer
  - Clear separation of concerns
  - Easy to locate code by feature or layer

**Test Organization:**

- **Mirrors Source Structure:**
  - `tests/api/` - API endpoint tests
  - `tests/services/` - Service layer tests
  - `tests/utils/` - Utility tests

- **Test Fixtures:**
  - `tests/conftest.py` - Shared pytest fixtures
  - Database fixtures, test data, mocks

**Asset Organization:**

- **Database:**
  - `database.db` - SQLite database file (gitignored)
  - Created automatically on first run

- **No Static Assets:** MVP has no static files (images, etc.)
- **Future:** Static assets would go in `static/` or `public/` directory

### Development Workflow Integration

**Development Server Structure:**

- **Entry Point:** `app/main.py`
  - FastAPI app initialization
  - Router registration
  - Exception handler registration
  - Database initialization

- **Development Command:**
  ```bash
  uvicorn app.main:app --reload
  ```
  - Hot reload enabled for development
  - Runs on `http://localhost:8000`

- **API Documentation:**
  - Swagger UI: `http://localhost:8000/docs`
  - ReDoc: `http://localhost:8000/redoc`

**Build Process Structure:**

- **No Build Step:** Python is interpreted, no compilation needed
- **Dependency Installation:**
  ```bash
  pip install -r requirements.txt
  ```

- **Database Initialization:**
  - Tables created on first run via SQLAlchemy
  - No migration system in MVP (manual table creation)

**Deployment Structure:**

- **Local Development:**
  - SQLite database file in project root
  - Environment variables in `.env`
  - No deployment configuration needed for MVP

- **Future Production:**
  - Environment-specific config files
  - Database migration system (Alembic)
  - Docker containerization
  - CI/CD pipeline configuration

---

## Architecture Validation Results

### Coherence Validation ✅

**Decision Compatibility:**

✅ **Technology Stack Compatibility:**
- FastAPI (0.104+) + SQLAlchemy (2.0+) + SQLite: Fully compatible
- Python 3.8+ supports all chosen technologies
- Uvicorn (0.24+) works seamlessly with FastAPI
- Pydantic v2 (included in FastAPI) compatible with SQLAlchemy 2.0
- No version conflicts identified

✅ **Architectural Decision Alignment:**
- ORM choice (SQLAlchemy) aligns with FastAPI best practices
- Layered structure supports chosen technology stack
- Session management (UUID v4) compatible with SQLite storage
- Error handling approach (custom exceptions) works with FastAPI patterns
- All decisions reinforce each other without contradictions

✅ **Pattern-Technology Alignment:**
- Naming conventions (snake_case) align with Python standards
- Structure patterns (layered architecture) support FastAPI + SQLAlchemy
- API patterns (REST, JSON) native to FastAPI
- Data patterns (ORM, migrations) standard for SQLAlchemy

**Pattern Consistency:**

✅ **Naming Consistency:**
- Database: snake_case (tables, columns, foreign keys) - consistent
- API: RESTful plural endpoints, snake_case query params - consistent
- Code: snake_case files, PascalCase classes, snake_case functions - consistent
- All naming patterns follow Python conventions throughout

✅ **Structure Consistency:**
- Layered architecture consistently applied (api/, services/, models/, schemas/)
- Test structure mirrors source structure consistently
- Utils organized in dedicated directory
- No structural inconsistencies identified

✅ **Format Consistency:**
- API responses: Direct JSON (no wrapper) - consistent across all endpoints
- Error format: FastAPI standard `{"detail": "..."}` - consistent
- Date format: ISO 8601 - consistent standard
- JSON field naming: snake_case - consistent with Python conventions

**Structure Alignment:**

✅ **Project Structure Supports Architecture:**
- Directory structure enables layered architecture decisions
- Component boundaries clearly defined and supported by structure
- Integration points properly structured (dependencies.py for shared deps)
- File organization aligns with implementation patterns

✅ **Boundaries Properly Defined:**
- API layer boundaries: Clear separation from services
- Service layer boundaries: Business logic isolated from HTTP concerns
- Data layer boundaries: Models separate from business logic
- Schema layer boundaries: API contracts separate from data models

✅ **Structure Enables Patterns:**
- Naming patterns enforceable through structure (clear file organization)
- Communication patterns supported (dependencies, exception handlers)
- Process patterns enabled (error handling, validation flow)

### Requirements Coverage Validation ✅

**Functional Requirements Coverage:**

✅ **Product Management (FR1-FR5):**
- **FR1 (Create Product):** ✅ Covered
  - Endpoint: `POST /products` in `app/api/products.py`
  - Service: `ProductService.create_product()` in `app/services/product_service.py`
  - Model: `Product` model in `app/models/product.py`
  - Schema: `ProductCreate` in `app/schemas/product.py`
  
- **FR2 (Edit Product):** ✅ Covered
  - Endpoint: `PUT /products/{id}` in `app/api/products.py`
  - Service: `ProductService.update_product()` in `app/services/product_service.py`
  - Schema: `ProductUpdate` in `app/schemas/product.py`
  
- **FR3 (List Products):** ✅ Covered
  - Endpoint: `GET /products` in `app/api/products.py`
  - Service: `ProductService.get_all_products()` in `app/services/product_service.py`
  
- **FR4 (Validate Name Required):** ✅ Covered
  - Pydantic schema validation in `ProductCreate`/`ProductUpdate`
  - Business logic validation in `ProductService`
  
- **FR5 (Validate Price > 0):** ✅ Covered
  - Pydantic schema validation (positive number constraint)
  - Business logic validation in `ProductService`

✅ **Cart Management (FR6-FR10):**
- **FR6 (Add Item to Cart):** ✅ Covered
  - Endpoint: `POST /cart/items` in `app/api/cart.py`
  - Service: `CartService.add_item_to_cart()` in `app/services/cart_service.py`
  - Model: `CartItem` model in `app/models/cart.py`
  - Schema: `CartItemCreate` in `app/schemas/cart.py`
  
- **FR7 (Remove Item from Cart):** ✅ Covered
  - Endpoint: `DELETE /cart/items/{id}` in `app/api/cart.py`
  - Service: `CartService.remove_item_from_cart()` in `app/services/cart_service.py`
  
- **FR8 (View Cart):** ✅ Covered
  - Endpoint: `GET /cart` in `app/api/cart.py`
  - Service: `CartService.get_cart_with_items()` in `app/services/cart_service.py`
  - Schema: `CartResponse` with items and total in `app/schemas/cart.py`
  
- **FR9 (Calculate Total):** ✅ Covered
  - Service: `CartService.calculate_cart_total()` in `app/services/cart_service.py`
  - Included in `CartResponse` schema
  
- **FR10 (Session Management):** ✅ Covered
  - Session ID generation (UUID v4) in `CartService.get_or_create_cart()`
  - Session storage in `Cart.session_id` column
  - Session retrieval via header `X-Session-ID` or cookie

✅ **Data Persistence (FR11-FR13):**
- **FR11 (Persist Products):** ✅ Covered
  - `Product` model with SQLAlchemy in `app/models/product.py`
  - Database table `products` defined
  - Service layer uses SQLAlchemy session for persistence
  
- **FR12 (Persist Cart):** ✅ Covered
  - `Cart` and `CartItem` models in `app/models/cart.py`
  - Database tables `carts` and `cart_items` defined
  - Service layer uses SQLAlchemy session for persistence
  
- **FR13 (JSON Response):** ✅ Covered
  - FastAPI automatically serializes Pydantic schemas to JSON
  - All response schemas defined in `app/schemas/`
  - Content-Type: application/json

**Non-Functional Requirements Coverage:**

✅ **Performance (NFR1-NFR3):**
- **NFR1 (API < 500ms):** ✅ Architecturally Supported
  - FastAPI async/await enables high performance
  - SQLite local database provides fast access
  - No external API calls or complex processing
  - Architecture supports performance requirements (monitoring can be added)
  
- **NFR2 (GET < 200ms):** ✅ Architecturally Supported
  - SQLite read operations are fast
  - SQLAlchemy ORM is efficient for simple queries
  - No complex joins or aggregations in MVP
  - Architecture supports fast read operations
  
- **NFR3 (POST/PUT/DELETE < 500ms):** ✅ Architecturally Supported
  - SQLite write operations are fast for MVP scale
  - SQLAlchemy provides efficient ORM operations
  - No complex transactions or validations
  - Architecture supports write performance requirements

**Note:** Performance requirements are architecturally supported. Actual performance will depend on implementation quality and can be monitored/optimized during development.

### Implementation Readiness Validation ✅

**Decision Completeness:**

✅ **Critical Decisions Documented:**
- Technology stack: FastAPI, SQLAlchemy, SQLite, Uvicorn - versions specified
- ORM choice: SQLAlchemy - rationale provided
- Session management: UUID v4 - implementation approach defined
- Error handling: Custom exceptions - structure defined
- Project structure: Layered architecture - complete structure provided

✅ **Implementation Patterns Comprehensive:**
- Naming patterns: Complete with examples (good and anti-patterns)
- Structure patterns: Full directory structure with all files
- Format patterns: API response, error, date formats specified
- Communication patterns: Logging, error handling defined
- Process patterns: Validation, error recovery specified

✅ **Consistency Rules Clear:**
- All patterns have clear enforcement guidelines
- Examples provided for each pattern category
- Anti-patterns documented to avoid confusion
- Rules are enforceable by AI agents

**Structure Completeness:**

✅ **Complete Project Tree:**
- All directories defined: `app/`, `api/`, `services/`, `models/`, `schemas/`, `utils/`, `tests/`
- All key files specified: `main.py`, `database.py`, endpoint files, service files, model files
- Configuration files: `requirements.txt`, `.env.example`, `.gitignore`
- Test structure: Complete mirror of source structure

✅ **Integration Points Specified:**
- API → Service communication: Documented
- Service → Model communication: Documented
- Data flow: Request and response flows documented
- Error flow: Exception handling flow documented

✅ **Component Boundaries Well-Defined:**
- API layer boundaries: Clear (no business logic)
- Service layer boundaries: Clear (business logic only)
- Model layer boundaries: Clear (data access only)
- Schema layer boundaries: Clear (API contracts only)

**Pattern Completeness:**

✅ **All Conflict Points Addressed:**
- Naming conflicts: Database, API, code naming all specified
- Structure conflicts: Project organization fully defined
- Format conflicts: API response, error, data formats specified
- Communication conflicts: Logging, error handling patterns defined
- Process conflicts: Validation, error recovery patterns defined

✅ **Naming Conventions Comprehensive:**
- Database: Tables, columns, foreign keys, indexes
- API: Endpoints, route params, query params, headers
- Code: Files, classes, functions, variables, constants
- All with examples and anti-patterns

✅ **Communication Patterns Fully Specified:**
- Logging: Format, levels, structured logging
- Error handling: Custom exceptions, user messages, technical details
- API communication: Request/response flow, error flow

✅ **Process Patterns Complete:**
- Error handling: Global exception handlers, validation approach
- Session management: UUID generation, storage, retrieval
- Validation: Pydantic schemas, business logic validation

### Gap Analysis Results

**Critical Gaps:** None identified ✅

All critical architectural decisions are complete and documented. No blocking gaps found.

**Important Gaps:**

1. **Performance Monitoring:** 
   - Status: Not critical for MVP
   - Impact: Low (can be added during implementation)
   - Recommendation: Add basic logging/metrics during implementation if needed

2. **Database Initialization Script:**
   - Status: Mentioned but not detailed
   - Impact: Low (can be created during implementation)
   - Recommendation: Create initialization function in `database.py` during first implementation story

3. **Environment Configuration Details:**
   - Status: `.env.example` mentioned but contents not specified
   - Impact: Low (standard FastAPI/SQLite config)
   - Recommendation: Define during implementation (DATABASE_URL, etc.)

**Nice-to-Have Gaps:**

1. **Development Scripts:**
   - `scripts/dev.sh` or `scripts/run.sh` for easy startup
   - Impact: Convenience only
   - Recommendation: Optional, can be added during implementation

2. **API Documentation Enhancement:**
   - Custom OpenAPI tags, descriptions
   - Impact: Better developer experience
   - Recommendation: Can be added incrementally

3. **Test Utilities:**
   - Test database fixtures, factory functions
   - Impact: Better test organization
   - Recommendation: Can be added during test implementation

### Validation Issues Addressed

**No Critical Issues Found** ✅

All architectural decisions are coherent, requirements are covered, and the architecture is ready for implementation.

**Minor Enhancements Identified:**

- Performance monitoring can be added during implementation (not blocking)
- Database initialization details can be specified during first implementation story
- Environment configuration can be detailed during setup

These are implementation details that don't block architectural decisions and can be handled naturally during development.

### Architecture Completeness Checklist

**✅ Requirements Analysis**

- [x] Project context thoroughly analyzed
- [x] Scale and complexity assessed
- [x] Technical constraints identified
- [x] Cross-cutting concerns mapped

**✅ Architectural Decisions**

- [x] Critical decisions documented with versions
- [x] Technology stack fully specified
- [x] Integration patterns defined
- [x] Performance considerations addressed

**✅ Implementation Patterns**

- [x] Naming conventions established
- [x] Structure patterns defined
- [x] Communication patterns specified
- [x] Process patterns documented

**✅ Project Structure**

- [x] Complete directory structure defined
- [x] Component boundaries established
- [x] Integration points mapped
- [x] Requirements to structure mapping complete

### Architecture Readiness Assessment

**Overall Status:** ✅ **READY FOR IMPLEMENTATION**

**Confidence Level:** **HIGH** - Architecture is complete, coherent, and all requirements are covered. AI agents have clear guidance for consistent implementation.

**Key Strengths:**

1. **Complete Coverage:** All 13 functional requirements and 3 non-functional requirements are architecturally supported
2. **Clear Patterns:** Comprehensive implementation patterns with examples prevent agent conflicts
3. **Well-Defined Structure:** Complete project structure with all files and directories specified
4. **Technology Alignment:** All technology choices are compatible and well-integrated
5. **Boundary Clarity:** Clear separation of concerns across all layers
6. **Implementation Guidance:** Detailed examples and anti-patterns provide clear direction

**Areas for Future Enhancement:**

1. **Performance Monitoring:** Add metrics/logging during implementation if needed
2. **Database Migrations:** Migrate to Alembic when project grows beyond MVP
3. **API Versioning:** Add versioning strategy when API evolves
4. **Advanced Error Handling:** Enhance error responses with error codes if needed
5. **Testing Infrastructure:** Expand test utilities and fixtures as test suite grows

### Implementation Handoff

**AI Agent Guidelines:**

- Follow all architectural decisions exactly as documented
- Use implementation patterns consistently across all components
- Respect project structure and boundaries defined in this document
- Refer to this document for all architectural questions
- Use provided examples as reference for correct patterns
- Avoid documented anti-patterns

**First Implementation Priority:**

1. **Project Setup:**
   ```bash
   # Install dependencies
   pip install fastapi uvicorn sqlalchemy
   
   # Create project structure
   mkdir -p app/{api,services,models,schemas,utils}
   mkdir -p tests/{api,services,utils}
   ```

2. **Database Initialization:**
   - Create `app/database.py` with SQLAlchemy setup
   - Create `app/models/base.py` with declarative base
   - Initialize database connection

3. **Core Models:**
   - Implement `app/models/product.py` (Product model)
   - Implement `app/models/cart.py` (Cart and CartItem models)
   - Create database tables

4. **Schemas:**
   - Implement `app/schemas/product.py` (ProductCreate, ProductUpdate, ProductResponse)
   - Implement `app/schemas/cart.py` (CartItemCreate, CartItemResponse, CartResponse)

5. **Services:**
   - Implement `app/services/product_service.py` (ProductService)
   - Implement `app/services/cart_service.py` (CartService)

6. **API Endpoints:**
   - Implement `app/api/products.py` (POST, PUT, GET endpoints)
   - Implement `app/api/cart.py` (GET, POST, DELETE endpoints)
   - Create `app/main.py` with FastAPI app and router registration

7. **Error Handling:**
   - Create `app/utils/exceptions.py` with custom exceptions
   - Add exception handlers in `app/main.py`

**Implementation Order Recommendation:**

1. Database setup → Models → Schemas → Services → API → Error handling
2. This order ensures dependencies are available at each step
3. Test each layer before moving to the next

**Architecture Document Status:** ✅ **COMPLETE AND VALIDATED**
