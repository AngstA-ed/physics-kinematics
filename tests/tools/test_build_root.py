from pathlib import Path
from tools.build_lessons import resolve_build_root, DEFAULT_REFACTOR


def test_default_root_uses_physics_refactor():
    root, ref = resolve_build_root(None, None)
    assert root == DEFAULT_REFACTOR.resolve()
    expected = DEFAULT_REFACTOR.resolve() / "_assets" / "brand" / "reference.docx"
    # reference is that path when present, else None — never a different location
    assert ref in (expected, None)


def test_custom_root_default_reference_under_that_root(tmp_path):
    brand = tmp_path / "_assets" / "brand"
    brand.mkdir(parents=True)
    (brand / "reference.docx").write_bytes(b"x")
    root, ref = resolve_build_root(str(tmp_path), None)
    assert root == tmp_path.resolve()
    assert ref == tmp_path / "_assets" / "brand" / "reference.docx"


def test_custom_root_missing_reference_returns_none(tmp_path):
    root, ref = resolve_build_root(str(tmp_path), None)
    assert root == tmp_path.resolve()
    assert ref is None


def test_explicit_reference_overrides(tmp_path):
    f = tmp_path / "myref.docx"
    f.write_bytes(b"x")
    root, ref = resolve_build_root(str(tmp_path), str(f))
    assert ref == f
