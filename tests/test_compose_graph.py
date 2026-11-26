"""Tests for Docker Compose Graph."""

from compose_graph.parser import compose_to_mermaid


def test_compose_to_mermaid() -> None:
    yml = """
services:
  web:
    depends_on:
      - api
  api:
    depends_on:
      - db
  db: {}
"""
    out = compose_to_mermaid(yml)
    assert "web --> api" in out
    assert "api --> db" in out
