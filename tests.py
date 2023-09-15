import pytest

from areaCalculatingLib import find_area


@pytest.mark.parametrize(
    ("radius", "a", "b", "c", "result"),
    [
        (None, 4, 6, 6, 11.31371),
        (None, 4, 8, 6, 11.61895),
        (4, None, None, None, 50.26548),
        (5, 3, 4, 5, "78.53982, 6.0"),
    ]
)
def test_area(radius, a, b, c, result):
    assert result == find_area(radius, a, b, c)
    assert result == find_area(radius, a, b, c)
    assert result == find_area(radius, a, b, c)


def test_empty_data():
    assert "Некорректные данные" == find_area()


def test_incorrect_data():
    assert "Некорректные данные" == find_area("a")
    assert "Некорректные данные" == find_area("a", "v", "f", "q")
    assert "Некорректные данные" == find_area(1, 3, 5, "d")
    assert "Некорректные данные" == find_area("a", 3, 4, 5)
    assert "Некорректные данные" == find_area(None, 2, 3, 9)
    assert "Некорректные данные", 7.48331 == find_area(-2, 3, 5, 6)
