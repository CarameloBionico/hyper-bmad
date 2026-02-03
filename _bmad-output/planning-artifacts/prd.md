---
stepsCompleted: ['step-01-init', 'step-02-discovery', 'step-03-success', 'step-04-journeys', 'step-05-domain', 'step-06-innovation', 'step-07-project-type', 'step-08-scoping', 'step-09-functional', 'step-10-nonfunctional', 'step-11-polish']
inputDocuments: ['_bmad-output/planning-artifacts/product-brief-hyper-bmad-2026-02-03-144132.md']
workflowType: 'prd'
briefCount: 1
researchCount: 0
brainstormingCount: 0
projectDocsCount: 0
classification:
  projectType: api_backend
  domain: general
  complexity: low
  projectContext: greenfield
---

# Product Requirements Document - E-commerce API MVP

**Author:** Pena
**Date:** 2026-02-03

## Project Classification

- **Tipo:** API Backend
- **Domínio:** E-commerce (General)
- **Complexidade:** Baixa
- **Contexto:** Greenfield

---

## Success Criteria

### User Success

- Administrador consegue cadastrar e gerenciar produtos
- Cliente consegue adicionar/remover items do carrinho
- Carrinho calcula total corretamente

### Technical Success

- API REST responde em todos endpoints
- Dados persistem corretamente no SQLite
- Validações básicas funcionam (preço > 0, nome obrigatório)
- Tempo de resposta < 500ms

---

## Product Scope

### MVP

- POST/PUT/GET /products
- POST/DELETE/GET /cart
- SQLite para persistência
- Validações básicas

### Out of Scope (Future)

- Autenticação
- Categorias
- Pagamento
- Busca/filtros
- Upload de imagens
- Pedidos/histórico

---

## User Journeys

### Journey 1: Administrador - Cadastrar Produto

**Persona:** Ana, gerente da loja online
**Situação:** Precisa adicionar novos produtos ao catálogo
**Jornada:**
1. Ana acessa a API (via cliente HTTP/Postman)
2. Envia POST /products com nome, descrição e preço
3. API valida dados (nome obrigatório, preço > 0)
4. Produto é salvo no SQLite
5. API retorna produto criado com ID

**Sucesso:** Produto disponível para clientes

### Journey 2: Cliente - Montar Carrinho

**Persona:** João, consumidor
**Situação:** Quer comprar alguns produtos
**Jornada:**
1. João consulta GET /products para ver catálogo
2. Escolhe produto e envia POST /cart/items com product_id e quantity
3. API adiciona item ao carrinho da sessão
4. João adiciona mais produtos
5. João consulta GET /cart para ver total
6. (MVP termina aqui - sem checkout)

**Sucesso:** Carrinho montado com itens e total calculado

### Journey 3: Cliente - Remover Item do Carrinho

**Persona:** João, consumidor
**Situação:** Mudou de ideia sobre um produto
**Jornada:**
1. João consulta GET /cart
2. Identifica item que quer remover
3. Envia DELETE /cart/items/{id}
4. API remove item e recalcula total
5. João confirma com GET /cart

**Sucesso:** Item removido, total atualizado

### Journey Requirements Summary

| Journey | Endpoints Necessários |
|---------|----------------------|
| Cadastrar Produto | POST /products |
| Editar Produto | PUT /products/{id} |
| Listar Produtos | GET /products |
| Adicionar ao Carrinho | POST /cart/items |
| Remover do Carrinho | DELETE /cart/items/{id} |
| Ver Carrinho | GET /cart |

---

## API Backend Specific Requirements

### Project-Type Overview

API REST simples em Python para gerenciamento de produtos e carrinho de compras. Foco em endpoints essenciais sem complexidade desnecessária.

### Technical Architecture Considerations

**Stack:**
- Backend: Python (Flask/FastAPI)
- Database: SQLite (local)
- Formato: JSON para request/response

**Endpoints:**
- POST /products - Criar produto
- PUT /products/{id} - Editar produto
- GET /products - Listar produtos
- POST /cart/items - Adicionar item ao carrinho
- DELETE /cart/items/{id} - Remover item do carrinho
- GET /cart - Visualizar carrinho

### Authentication Model

- **MVP:** Sem autenticação
- **Sessão:** Anônima (carrinho por sessão)
- **Future:** Autenticação pode ser adicionada posteriormente

### Data Formats

- **Request/Response:** JSON
- **Content-Type:** application/json
- **Encoding:** UTF-8

### Error Codes

- **200 OK** - Sucesso
- **201 Created** - Recurso criado
- **400 Bad Request** - Dados inválidos
- **404 Not Found** - Recurso não encontrado
- **500 Internal Server Error** - Erro do servidor

### Implementation Considerations

- **Versionamento:** Não necessário no MVP
- **Rate Limiting:** Não necessário no MVP (pode ser adicionado depois)
- **Documentação:** OpenAPI/Swagger pode ser adicionado
- **Validação:** Validações básicas (nome obrigatório, preço > 0)

---

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach:** Problem-Solving MVP
- Resolve problema core: gerenciar produtos e carrinho
- Funcionalidade mínima que funciona
- Sem features extras

**Resource Requirements:**
- 1 desenvolvedor
- Stack simples (Python + SQLite)
- Sem infraestrutura complexa

### MVP Feature Set (Phase 1)

**Core User Journeys Supported:**
- Administrador cadastra/edita produtos
- Cliente monta carrinho
- Cliente remove items do carrinho

**Must-Have Capabilities:**
- CRUD de produtos
- Gerenciamento de carrinho (sessão anônima)
- Validações básicas
- Persistência SQLite

### Post-MVP Features

**Phase 2 (Post-MVP):**
- Autenticação de usuários
- Categorias de produtos
- Busca e filtros
- Rate limiting

**Phase 3 (Expansion):**
- Pagamento/checkout
- Pedidos/histórico
- Upload de imagens
- API versionamento

### Risk Mitigation Strategy

**Technical Risks:** Baixo - stack simples e conhecida
**Market Risks:** N/A - projeto de demonstração
**Resource Risks:** Baixo - MVP muito simples

---

## Functional Requirements

### Product Management

- FR1: Administrador pode criar produtos com nome, descrição e preço
- FR2: Administrador pode editar produtos existentes
- FR3: Cliente pode listar todos os produtos disponíveis
- FR4: Sistema valida que nome do produto é obrigatório
- FR5: Sistema valida que preço do produto é maior que zero

### Cart Management

- FR6: Cliente pode adicionar produtos ao carrinho especificando quantidade
- FR7: Cliente pode remover items do carrinho
- FR8: Cliente pode visualizar carrinho com todos os items
- FR9: Sistema calcula total do carrinho automaticamente
- FR10: Sistema mantém carrinho por sessão anônima

### Data Persistence

- FR11: Sistema persiste produtos no banco de dados
- FR12: Sistema persiste carrinho no banco de dados
- FR13: Sistema retorna dados em formato JSON

---

## Non-Functional Requirements

### Performance

- NFR1: API responde a requisições em menos de 500ms
- NFR2: Operações de leitura (GET) completam em menos de 200ms
- NFR3: Operações de escrita (POST/PUT/DELETE) completam em menos de 500ms
