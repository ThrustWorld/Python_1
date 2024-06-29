from ezgraphics import GraphicsWindow, GraphicsCanvas

win = GraphicsWindow(400, 400)
win.setTitle('Esercizio 6')
canvas = win.canvas()

# La variabile colors contiene i colori che mi interessano
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

# La variabile i punta sempre al colore con cui devo disegnare il prossimo cerchio,
# ed è un indice per la lista colors. Inizialmente contiene il valore 0 (rosso)
i = 0

# Disegna il "pulsante" Exit
canvas.drawRectangle(350, 350, 50, 50)
canvas.setTextAnchor('center')
canvas.drawText(375, 375, 'Exit')
while True:
    # Prendo le coordinate del mouse
    x, y = win.getMouse()
    # Se le coordinate mi dicono che ho cliccato su Exit, esci dal ciclo while
    if x > 350 and y> 350: break
    # Altrimenti disegna un cerchio centrato su x, y con il colore colors[i] e raggio 10
    canvas.setFill(colors[i])
    canvas.drawOval(x-10, y-10, 20, 20)
    # Passa al colore successivo. Il % serve a far sì che quando i diventi 6, ritorni
    # automaticament a 0, perchè 6 % 6 = 0.
    i = (i + 1) % len(colors)
