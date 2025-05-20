from maytinh import add, subtract, tru


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2

def test_tru():
    assert tru(2, 3) == 6
