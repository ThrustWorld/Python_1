from ex_3 import somma_opposti
from random import randint

def test_somma_opposti():
    assert somma_opposti([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert somma_opposti([1,1,1]) == True
    assert somma_opposti([1,2,2,10]) == False
    assert somma_opposti([]) == True

def test_somma_opposti_2():
    for i in range(10):
        elemento_lista = randint(0,99)
        lunghezza_lista = randint(0,99)
        lista = [elemento_lista] * lunghezza_lista
        assert somma_opposti(lista) == True

test_somma_opposti_2()