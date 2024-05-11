from ezgraphics.graphics import *
from sys import exit

# costanti con la dimensione della finestra
SIZE_X = 600
SIZE_Y = 500

# costante con la altezza del pulsante di uscita
SIZE_BUTTON = 40

# creo la finestra con la dimensione desiderata
win = GraphicsWindow(SIZE_X, SIZE_Y)
win.setTitle("Spezzata")
canvas = win.canvas()

# disegno il pulsante Esci
canvas.drawLine(0, SIZE_Y-SIZE_BUTTON, SIZE_X-1, SIZE_Y-SIZE_BUTTON)
canvas.setTextAnchor("center")
canvas.drawText(SIZE_X // 2, SIZE_Y - SIZE_BUTTON//2, "Esci")

# prendo in input il primo click del mouse
xold, yold = win.getMouse()
# se il click avviene nell'area del pulsante, esco dal programma
if yold > SIZE_Y - SIZE_BUTTON:
    exit()
# prendo le coordinate del nuovo click
x, y = win.getMouse()
while y < SIZE_Y - SIZE_BUTTON:
    # dentro il ciclo while, xold e yold sono le coordinate del precedente click del mouse
    # mentre x, y sono le coordinate del nuovo click

    # visualizzo una linea dalla posizione del vecchio click a quella del nuovo
    canvas.drawLine(xold, yold, x, y)
    # aggiorno le coordinate del vecchio click con quelle del nuovo
    xold = x
    yold = y
    # prendo un nuovo click
    x, y = win.getMouse()
