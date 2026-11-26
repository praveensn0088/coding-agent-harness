
from harness.context.loader import load_project_context


def test_load_project_context():
    context = load_project_context()

    assert "instructions" in context
    assert "architecture" in context

    assert len(context["instructions"]) > 0
    assert len(context["architecture"]) > 0
