from collections.abc import Callable
from typing import Any, cast # avoid using when possible
# cast is useful for checkers

def greeting(name: str) -> str:
    return f"Hello, {name}"

def greeting_type_defined(name: str | None = None) -> str:
    return f"Hello, {name if name else 'Anonymous'}"

ConditionFunction = Callable[[int], bool]

def filter_list(l: list[int], condition: ConditionFunction) -> list[int]:
    return [i for i in l if condition(i)]

def is_even(i: int) -> bool:
    return i % 2 == 0

print(filter_list([1, 2, 3, 4, 5], is_even))

def f(x: Any) -> Any:
    return x

a = f("a") # inferred is "Any"
b = cast(str, f("a"))  # forced to be "str'"