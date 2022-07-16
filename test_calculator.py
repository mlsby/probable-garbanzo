from calculator import add, power, factorial


def test_add():
    assert 2 == add(1, 1)

def test_power():
    assert 16 == power(4, 2)

def test_factorial():
    assert 6 == factorial(3)

