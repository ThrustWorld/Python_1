from soluzioni_231204_matrici import *

def test_somma_matrici():
    a = [
        [1, 2, 3],
        [4, 5]
    ]
    b = [
        [0, 1, -1],
        [2, 3]
    ]

    somma_matrici(a, b)

    assert a == [
        [1, 3, 2],
        [6, 8]
    ]


def test_somma_matrici2():
    a = [
        [1, 2, 3],
        [4, 5]
    ]
    b = [
        [0, 1, -1],
        [2, 3]
    ]

    assert somma_matrici2(a, b) == [
        [1, 3, 2],
        [6, 8]
    ]
