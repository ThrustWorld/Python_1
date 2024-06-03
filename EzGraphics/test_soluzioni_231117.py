from soluzioni_231117 import *

def test_cerca_positivo():
    assert cerca_positivo([-4, 2, 0]) == 2
    assert cerca_positivo([-4, -2]) == -1
    assert cerca_positivo([]) == -1

def test_cerca_positivo_pos():
    assert cerca_positivo_pos([-4, 2, 0]) == 1
    assert cerca_positivo_pos([-4, -2]) == -1
    assert cerca_positivo_pos([]) == -1

def test_count():
    assert count([1, 2, 3, 1, 4], 1) == 2
    assert count([ ], 1) == 0
    assert count([2, 3], 1) == 0

def test_sum_list():
    assert sum_list([1,2,3], [4,5,6]) == [5,7,9]
    assert sum_list([], []) == []

# Non posso effettuare i test per la funzione random_list come per le
# altre funzioni, perchè non so a priori quale sarà il risultato restituito.
# Tuttavia posso verificare che alcune proprietà siano rispettate.

# Proprietà 1: se il primo parametro è 0, la lista restituita è vuota.
def test_random_list_1():
    assert random_list(0, 10) == []
    assert random_list(0, 3) == []

# Proprietà 2: tutti gli elementi della lista restituita da random_list
# sono numeri tra 1 e k (il secondo parametro della funzione).
def test_random_list_2():
    l = random_list(10, 9)
    for v in l:
        assert 1 <= v <= 9
