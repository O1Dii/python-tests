import random

import pytest

from calc import Calc


@pytest.fixture
def calc():
    return Calc()


@pytest.mark.parametrize("a, b, expected_result", [
    (2, 4, 6),
    ('a', 'b', 'ab'),
    (2.2, 1, 3.2)
])
def test_add(calc, a, b, expected_result):
    assert expected_result == calc.add(a, b)


@pytest.mark.parametrize("a, b", [
    (2, 'a'),
    (1.1, 'b')
])
def test_fail_add(calc, a, b):
    with pytest.raises(TypeError):
        calc.add(a, b)


@pytest.mark.parametrize('a, b, expected_result', [
    (2, 1, 1),
    (3, 1.5, 1.5)
])
def test_subtract(calc, a, b, expected_result):
    assert calc.subtract(a, b) == expected_result


@pytest.mark.parametrize('a, b', [
    (2, 'a'),
    (3.5, 'a')
])
def test_fail_subtract(calc, a, b):
    with pytest.raises(TypeError):
        calc.subtract(a, b)


@pytest.mark.parametrize('a, b, expected_result', [
    (1, 2, 2),
    (2.2, 2, 4.4),
    ('a', 2, 'aa')
])
def test_multiply(calc, a, b, expected_result):
    assert calc.multiply(a, b) == expected_result


@pytest.mark.parametrize('a, b', [
    ('a', 2.2),
    ('a', 'b')
])
def test_fail_multiply(calc, a, b):
    with pytest.raises(TypeError):
        calc(a, b)


@pytest.mark.parametrize('a, b, expected_result', [
    (6, 2, 3),
    (6.6, 2, 3.3)
])
def test_divide(calc, a, b, expected_result):
    assert calc.divide(a, b) == expected_result


@pytest.mark.parametrize('a, b', [
    ('a', 2.2),
    ('a', 'b')
])
def test_fail_divide(calc, a, b):
    with pytest.raises(TypeError):
        calc(a, b)


@pytest.mark.parametrize('randint_result, a, b, expected_result', [
    (1, 1, 2, 3),
    (2, 2, 1, 1),
    (3, 2, 3, 6),
    (4, 8, 2, 4)
])
def test_random(monkeypatch, calc, randint_result, a, b, expected_result):
    def mock_randint(*args):
        return randint_result

    monkeypatch.setattr(random, 'randint', mock_randint)

    assert calc.random_operation(a, b) == expected_result


@pytest.mark.parametrize('randint_result, a, b', [
    (1, 2, 'a'),
    (1, 1.1, 'b'),
    (2, 2, 'a'),
    (2, 3.5, 'a'),
    (3, 'a', 2.2),
    (3, 'a', 'b'),
    (4, 'a', 2.2),
    (4, 'a', 'b')
])
def test_fail_random(monkeypatch, calc, randint_result, a, b):
    def mock_randint(*args):
        return randint_result

    monkeypatch.setattr(random, 'randint', mock_randint)

    with pytest.raises((TypeError, ValueError)):
        assert calc.random_operation(a, b)
