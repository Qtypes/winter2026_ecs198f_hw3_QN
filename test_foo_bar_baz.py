import pytest

from foo_bar_baz import foo_bar_baz


def expected_output(n: int) -> str:
    if n <= 0:
        return ""

    parts = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            parts.append("Baz")
        elif i % 3 == 0:
            parts.append("Foo")
        elif i % 5 == 0:
            parts.append("Bar")
        else:
            parts.append(str(i))
    return " ".join(parts)


def test_edge_cases() -> None:
    for n in [-5, -1, 0, 1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 16, 18, 20, 29, 30]:
        assert foo_bar_baz(n) == expected_output(n)


def test_space_delimited() -> None:
    for n in [0, 1, 2, 3, 5, 15, 30]:
        result = foo_bar_baz(n)

        assert isinstance(result, str)
        if n <= 0:
            assert result == ""
        else:
            parts = result.split(" ")
            assert result == result.strip()
            assert "  " not in result
            assert len(parts) == n
            assert " ".join(parts) == result
