l: list[int] = [1, 2, 3, 4, 5]
t: tuple[int, str, float] = (1, "hello", 3.14)
s: set[int] = {1, 2, 3, 4, 5}
d: dict[str, int] = {"a": 1, "b": 2, "c": 3}

l2: list[int | float] = [1, 2.5, 3.14, 5]

IntStringFloatTuple = tuple[int, str, float]
t2: IntStringFloatTuple = (1, "hello", 3.14)