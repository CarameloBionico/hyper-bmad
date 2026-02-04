"""
Tests for app.main: verify FastAPI app exists and is runnable (Story 1.1).
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app


def test_app_exists():
    """AC: app.main initializes FastAPI app."""
    assert app is not None


def test_docs_available():
    """AC: /docs returns Swagger UI (200)."""
    client = TestClient(app)
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_json_available():
    """FastAPI exposes OpenAPI schema at /openapi.json."""
    client = TestClient(app)
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert "openapi" in data
    assert "info" in data
