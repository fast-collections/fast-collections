from importlib import util
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

from fast_collections import Trie as FastTrie

_BENCHMARKS_TRIE_DIR = (
    Path(__file__).resolve().parent.parent / "benchmarks" / "trie"
)
_PURE_PYTHON_TRIE_PATH = _BENCHMARKS_TRIE_DIR / "pure_python.py"


def _load_pure_python_module() -> ModuleType:
    "Load the pure Python trie reference kept next to the benchmarks."
    spec = util.spec_from_file_location("pure_python", _PURE_PYTHON_TRIE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(
            f"cannot load the pure Python trie from {_PURE_PYTHON_TRIE_PATH}"
        )
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_PURE_PYTHON_TRIE = _load_pure_python_module().Trie

IMPLEMENTATIONS = (
    pytest.param(FastTrie, id="fast_collections"),
    pytest.param(_PURE_PYTHON_TRIE, id="pure_python"),
)


@pytest.fixture(params=IMPLEMENTATIONS)
def trie(request: pytest.FixtureRequest) -> Any:
    "An empty trie, over both implementations."
    return request.param()
