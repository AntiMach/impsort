from __future__ import annotations

from impsort.load import Import, ImportFrom
from typing import Iterable, Iterator


def sort_order(imp: Import) -> int:
    if isinstance(imp, ImportFrom):
        return 


def sort_imports(imports: Iterable[Import]) -> Iterator[Import]:
    return sorted(imports, key=sort_order)
