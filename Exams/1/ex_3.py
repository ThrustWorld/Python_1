from ex_1 import frequenza
from random import randint

def test_frequenza_1():
    assert frequenza([1, 2, 3, 1, 9, 9, 7, 1]) == [0, 3, 1, 1, 0, 0, 0, 1, 0, 2]
    assert frequenza([]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def create_random_list():
    
    lunghezza = randint(0, 20)
    risultato = []
    for i in range(lunghezza):
        risultato.append(randint(0,9))
    return risultato

def test_frequenza_2():
    lista = create_random_list()
    risultato = frequenza(lista)
    assert sum(risultato) == len(lista)
    for i in risultato:
        assert i >= 0

test_frequenza_1()
test_frequenza_2()