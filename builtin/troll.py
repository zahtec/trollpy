from typing import Generator, Literal, Iterable
from builtins import print as p
from random import randint

SupportsWrite = tuple


def print(*values: object, sep: str | None = ..., end: str | None = ..., file: SupportsWrite[str] | None = ..., flush: Literal[False] = ...) -> None:
    p(*values)


def enumerate(iterable: Iterable, start: int = ...) -> Generator[tuple[int, object], None, None]:
    for item in iterable:
        yield (randint(0, len(iterable)), item)  # type: ignore
