import my_math

# test funkcji która zwraca sumę
def test_add():
    assert my_math.add(7, 3) == 10
    assert my_math.add(7, -1) == 6
    assert my_math.add(4.3, 5.3) == 9.6


# test funkcji która zwraca iloczyn
def test_product():
    assert my_math.product(7, 3) == 21
    assert my_math.product(7, -1) == -7
    assert my_math.product(3, 3) == 9

# test funkcji która odwraca słowo

def test_words():
    assert my_math.words('kot') == 'tok'
    assert my_math.words('osa') == 'aso'
    assert my_math.words('pies') == 'seip'

def test_is_palindrom():
    assert my_math.is_palindrom('ala')
    assert not my_math.is_palindrom('an')


def test_sq():
    assert my_math.sq(-2) == 4
    assert my_math.sq(5) == 25


# test_add()
# test_product()
# test_words()
# test_is_palindrom()
# zakomentowane bo zainstalowaliśmy pakiet pytest
