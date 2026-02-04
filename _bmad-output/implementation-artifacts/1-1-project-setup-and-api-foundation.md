# Story 1.1: Project Setup and API Foundation

Status: review

<!-- Note: Validation is optional. Run validate-create-story for quality check before dev-story. -->

## Story

As a developer,
I want a runnable FastAPI project with the agreed folder structure and dependencies,
so that I can implement features on a solid base.

## Acceptance Criteria

1. **Given** the project root with no existing app structure,
   **When** I run `pip install fastapi uvicorn sqlalchemy` (or equivalent requirements.txt) and `uvicorn app.main:app --reload`,
   **Then** the API starts and `/docs` returns Swagger UI.
2. **And** the project has folders `app/`, `app/api/`, `app/services/`, `app/models/`, `app/schemas/`, `app/utils/`, and `tests/` with `__init__.py` where needed.
3. **And** `app/main.py` initializes the FastAPI app and is the entry point.

## Tasks / Subtasks

- [x] Task 1: Create project structure and dependencies (AC: 1, 2)
  - [x] 1.1 Create `requirements.txt` with fastapi, uvicorn, sqlalchemy (no versions pinned unless architecture specifies)
  - [x] 1.2 Create folders: `app/`, `app/api/`, `app/services/`, `app/models/`, `app/schemas/`, `app/utils/`, `tests/`
  - [x] 1.3 Add `__init__.py` in each package folder so they are Python packages
- [x] Task 2: Implement FastAPI app entry point (AC: 1, 3)
  - [x] 2.1 Create `app/main.py` that instantiates FastAPI (e.g. `app = FastAPI()`)
  - [x] 2.2 Ensure running `uvicorn app.main:app --reload` starts the server and `/docs` serves Swagger UI
- [x] Task 3: Verify runnability and structure (AC: 1, 2, 3)
  - [x] 3.1 Run the app and confirm `/docs` returns Swagger UI
  - [x] 3.2 Confirm all required folders and `__init__.py` files exist

## Dev Notes

- **Relevant architecture patterns:** Layered structure from [Source: _bmad-output/planning-artifacts/architecture.md]. Estrutura: `app/api/`, `app/services/`, `app/models/`, `app/schemas/`, `app/utils/`; `app/main.py` entry point; `app/database.py` for DB (criar em story posterior). Naming: arquivos/funções/variáveis snake_case, classes PascalCase.
- **Stack:** Python 3.8+, FastAPI (latest stable), Uvicorn (ASGI), SQLAlchemy (2.x) — instalados aqui; uso do banco na próxima story.
- **Source tree to touch:** raiz do projeto (requirements.txt), pasta `app/` e subpastas, `tests/` (vazios ou com __init__ apenas).
- **Testing standards:** Pasta `tests/` espelha estrutura; frameworks de teste podem ser adicionados nesta story ou na seguinte (architecture não exige testes nesta story, mas estrutura de pastas sim).

### Project Structure Notes

- Alignment: [Source: architecture.md] define `app/`, `app/api/`, `app/services/`, `app/models/`, `app/schemas/`, `app/utils/`, `tests/`. Não criar `app/database.py` nesta story (virá com Product/DB na 1.2).
- Naming: arquivos em snake_case (ex: `main.py`), pastas em minúsculas.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md] — Starter Template (FastAPI manual), Core Architectural Decisions, Project Structure, Naming Conventions.
- [Source: _bmad-output/planning-artifacts/epics.md] — Story 1.1 AC e requisitos adicionais (starter template).
- [Source: _bmad-output/planning-artifacts/prd.md] — API Backend requirements, endpoints overview.

## Dev Agent Record

### Agent Model Used

(Preenchido pelo agente Dev durante implementação)

### Debug Log References

### Completion Notes List

- requirements.txt criado com fastapi, uvicorn, sqlalchemy, pytest, httpx.
- Estrutura de pastas: app/, app/api/, app/services/, app/models/, app/schemas/, app/utils/, tests/ com __init__.py em cada uma.
- app/main.py: FastAPI app instanciado; uvicorn app.main:app --reload inicia servidor; /docs retorna Swagger UI (verificado com HTTP 200).
- Testes em tests/test_app_main.py: test_app_exists, test_docs_available, test_openapi_json_available; 3 passed.

### File List

- requirements.txt
- app/__init__.py
- app/main.py
- app/api/__init__.py
- app/services/__init__.py
- app/models/__init__.py
- app/schemas/__init__.py
- app/utils/__init__.py
- tests/__init__.py
- tests/test_app_main.py
