---
stepsCompleted: [1, 2, 3, 4, 5, 6]
status: complete
inputDocuments: ['_bmad-output/brainstorming/brainstorming-session-2026-02-02-234457.md']
date: 2026-02-03 14:41:32
author: Pena
---

# Product Brief: E-commerce API MVP

## Executive Summary

API REST simples de e-commerce desenvolvida em Python. Permite gerenciar produtos e carrinho de compras. MVP focado em funcionalidades essenciais sem complexidade desnecessária.

**Funcionalidades:**
- Produtos: criar, editar, listar
- Carrinho: adicionar item, remover item, visualizar

**Stack:** Python + SQLite

---

## Core Vision

### Problem Statement

Necessidade de uma API de e-commerce simples para gerenciar catálogo de produtos e carrinho de compras, sem a complexidade de sistemas completos de pagamento ou autenticação.

### Proposed Solution

Um **E-commerce API MVP** em Python com:

**Funcionalidades Core:**
- **Produtos:** CRUD (criar, editar, listar)
- **Carrinho:** Sessão anônima (adicionar/remover items, visualizar)
- **Dados:** SQLite local

**Características Técnicas:**
- Backend REST API em Python
- Validações simples
- Sem autenticação (sessão anônima)
- Sem categorias
- Sem pagamento (termina no carrinho)
- Roda 100% localmente

---

## Target Users

### Administrador
- Gerencia catálogo de produtos (criar, editar, listar)

### Cliente
- Visualiza produtos disponíveis
- Gerencia carrinho de compras (adicionar/remover items)

---

## Success Metrics

### Métricas Funcionais

- API responde corretamente em todos os endpoints
- CRUD de produtos funciona (criar, editar, listar)
- Carrinho funciona (adicionar, remover, visualizar)
- Dados persistem corretamente no SQLite
- Validações simples funcionam como esperado

---

## MVP Scope

### Core Features

**Produtos:**
- Criar produto (nome, descrição, preço)
- Editar produto
- Listar produtos

**Carrinho:**
- Adicionar item ao carrinho
- Remover item do carrinho
- Visualizar carrinho (com total)

### Out of Scope

- Autenticação/usuários
- Categorias de produtos
- Checkout/pagamento
- Busca/filtros avançados
- Upload de imagens
- Pedidos/histórico
