import sys
from pathlib import Path

import pytest

# The pure Python reference implementation lives next to the benchmarks;
# put its directory on sys.path so the shared test suite can use it.
_BENCHMARKS_TRIE_DIR = (
    Path(__file__).resolve().parent.parent / "benchmarks" / "trie"
)
sys.path.insert(0, str(_BENCHMARKS_TRIE_DIR))

from fast_collections import Trie as FastTrie  # noqa: E402
from pure_python import Trie as PureTrie  # noqa: E402

IMPLEMENTATIONS = (
    pytest.param(FastTrie, id="fast_collections"),
    pytest.param(PureTrie, id="pure_python"),
)


@pytest.fixture(params=IMPLEMENTATIONS)
def trie(request) -> FastTrie | PureTrie:
    "An empty trie, over both implementations."
    return request.param()
