from calculator import add, power, factorial, subtract


def test_add():
    assert 2 == add(1, 1)

def test_power():
    assert 16 == power(4, 2)

def test_factorial():
    assert 6 == factorial(3)

def test_subtract():
    assert 1 == subtract(3, 2)
