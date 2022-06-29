from typing import Literal

SupportsWrite = tuple


def print(*values: object, sep: str | None = ..., end: str | None = ..., file: SupportsWrite[str] | None = ..., flush: Literal[False] = ...) -> None:
    ...
