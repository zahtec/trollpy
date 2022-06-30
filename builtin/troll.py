from typing import Generator, Iterable
from random import randint

SupportsWrite = tuple


def enumerate(iterable: Iterable, start: int = ...) -> Generator[tuple[int, object], None, None]:
    for item in iterable:
        yield (randint(0, len(iterable)-1), item)  # type: ignore
