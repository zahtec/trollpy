from typing import Literal, Iterable

SupportsWrite = tuple


def print(*values: object, sep: str | None = ..., end: str | None = ..., file: SupportsWrite[str] | None = ..., flush: Literal[False] = ...) -> None:
    ...


def enumerate(iterable: Iterable[enumerate], start: int = ...) -> None:
    ...
