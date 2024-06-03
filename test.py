from typing import Annotated


def test_func(x: Annotated[int, (0, 10)]) -> int:
    return x * 2

result = test_func(11)

print(result)
