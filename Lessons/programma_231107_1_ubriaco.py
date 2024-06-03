from ezgraphics import GraphicsWindow
from random import randint

# Crea finestra.

win = GraphicsWindow()
win.setTitle("Ubriaco")
canvas = win.canvas()

# Le variabili x ed y contengono la coordinata x ed y dell'ubriaco. Come griglia
# in cui l'ubriaco si muove consideriamo il sistema di coordinate della finestra
# grafica, che va da (0,0) per il punto in alto a sinistra a (399, 399) per il punto
# in basso a destra. Pertanto, il centro della finestra ha coordinate (200, 200).
x = 200
y = 200

while True:
    # Mettiamo un un punt nella posizione attuale dell'ubriaco
    canvas.drawPoint(x, y)
    # Genero un numero casuale tra 1 e 4, che individua una delle 4 direzioni
    # in cui su può muovere l'ubriaco
    dir = randint(1,4)
    # A seconda del valore di 1, muovo l'ubriaco alterando la variabile di stato x o y
    if dir == 1:
        # a destra
        x += 1
    elif dir == 2:
        # a sinstra
        x -= 1
    elif dir == 3:
        # in basso
        y += 1
    else:
        # in alto
        y -= 1