from __future__ import annotations

import ast
from typing import Iterator
from io import TextIOWrapper
from functools import lru_cache
from dataclasses import dataclass


@dataclass
class NameAlias:
    name: str
    alias: str | None

    def __str__(self):
        return f"{self.name} as {self.alias}" if self.alias else self.name


@dataclass
class Import:
    start_line: int
    end_line: int
    symbols: list[NameAlias]

    def __str__(self):
        aliases = ", ".join(str(alias) for alias in self.symbols)
        return f"import {aliases}"


@dataclass
class ImportFrom(Import):
    module: str
    level: int

    @property
    @lru_cache(None)
    def parts(self):
        return self.module.split(".")

    def __str__(self):
        return f"from {'.' * self.level}{self.module} {super().__str__()}"


def read_top_imports(fp: TextIOWrapper) -> Iterator[str]:
    node = ast.parse(fp.read())

    for child in node.body:
        if import_ := read_import(child):
            yield import_
        else:
            return


def read_import(node: ast.stmt) -> Import:
    match node:
        case ast.Import(
            names=names,
            lineno=start_line,
            end_lineno=end_line,
        ):
            return Import(
                start_line,
                end_line,
                [
                    NameAlias(name.name, name.asname)
                    for name in names
                ],
            )
        case ast.ImportFrom(
            module=module,
            names=names,
            level=level,
            lineno=start_line,
            end_lineno=end_line,
        ):
            return ImportFrom(
                start_line,
                end_line,
                [
                    NameAlias(name.name, name.asname)
                    for name in names
                ],
                module or "",
                level
            )
    
    return None
