import pytest

import foo_bar_baz as foo_bar_baz_module
from foo_bar_baz import foo_bar_baz


def get_foo_bar_baz():
    imported_module = __import__("foo_bar_baz")

    assert imported_module is not None
    assert hasattr(imported_module, "foo_bar_baz")
    assert callable(imported_module.foo_bar_baz)

    return imported_module.foo_bar_baz


def test_module_imports():
    imported_module = __import__("foo_bar_baz")

    assert imported_module is not None
    assert hasattr(imported_module, "foo_bar_baz")
    assert callable(imported_module.foo_bar_baz)


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "1"),
        (2, "1 2"),
        (3, "1 2 Foo"),
        (4, "1 2 Foo 4"),
        (5, "1 2 Foo 4 Bar"),
        (6, "1 2 Foo 4 Bar Foo"),
        (15, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"),
        (16, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16"),
    ],
)
def test_foo_bar_baz_known_sequences(n, expected):
    assert get_foo_bar_baz()(n) == expected


@pytest.mark.parametrize("n", [1, 2, 3, 10, 15, 16, 31])
def test_space_delimited(n):
    out = get_foo_bar_baz()(n)

    assert out == out.strip()
    assert "  " not in out
    assert out.count(" ") == n - 1

    tokens = out.split(" ")
    assert len(tokens) == n
    assert " ".join(tokens) == out


@pytest.mark.parametrize("n", [0, -1, -10])
def test_non_positive_n_returns_empty_string(n):
    assert get_foo_bar_baz()(n) == ""


def test_replacement_rules_hold_for_larger_n():
    n = 100
    expected_tokens = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            expected_tokens.append("Baz")
        elif i % 3 == 0:
            expected_tokens.append("Foo")
        elif i % 5 == 0:
            expected_tokens.append("Bar")
        else:
            expected_tokens.append(str(i))

    assert get_foo_bar_baz()(n) == " ".join(expected_tokens)


@pytest.mark.parametrize("n", [None, "10", 3.14, [], {}, object()])
def test_invalid_input_types(n):
    with pytest.raises(TypeError):
        get_foo_bar_baz()(n)


@pytest.mark.parametrize("n,expected", [(False, ""), (True, "1")])
def test_bool_inputs(n, expected):
    assert get_foo_bar_baz()(n) == expected
