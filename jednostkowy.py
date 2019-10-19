
# funkcja która zwraca sumę i testy do niej
def add(x, y):
    return x + y


def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5.3) == 9.6

test_add()

# funkcja która zwraca iloczyn i testy do niej

def product(x, y):
    return x * y


def test_product():
    assert product(7, 3) == 21
    assert product(7, -1) == -7
    assert product(3, 3) == 9

test_product()