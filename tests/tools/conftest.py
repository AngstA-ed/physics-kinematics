"""Shared pytest fixtures for tools tests."""
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def schema_path() -> Path:
    return ROOT / "tools" / "lesson_schema.yaml"
