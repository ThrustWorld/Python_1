from ezgraphics import GraphicsWindow

# costante con la dimensione di una casella
SQUARE_SIZE = 20

n = int(input("Immetti dimensione scacchiera: "))
# quando creo la finestra, la imposto delle dimensioni corrette per la scacchiera
win = GraphicsWindow(n*SQUARE_SIZE, n*SQUARE_SIZE)
win.setTitle("Scacchiera")
canvas = win.canvas()
canvas.setColor("black")
# questi due for scandiscono tutte le righe (i) e colonne (j) della scacchiera
for i in range(n):      # i va da 0 ad n-1
    for j in range(n):  # i va da 0 ad n-1
        # determino se la casella è nera, altrimenti non c'è bisogno di visulizzare nulla
        if (i+j) % 2 == 0:
            # visualizza la casella alla riga i, colonna j
            canvas.drawRectangle(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
win.wait()
