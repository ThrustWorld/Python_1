"""
Esercizio P2.5 del libro di testo.

Disegnare una faccina con la libreria ezgraphics.
"""

from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

canvas.drawLine(100, 250, 300, 250)   # bocca
canvas.setLineWidth(3)                # imposto larghezza delle linee da usare da ora in poi
canvas.setOutline("red")              # imposto il colore da usare per le linee da usare da ora in poi
canvas.drawOval(0, 0, 399, 399)       # faccia
canvas.drawOval(100, 100, 50, 50)     # occhio sinistro
canvas.setFill("black")               # imposto un colore per il riempimento da usare da ora in poi
canvas.drawOval(250, 100, 50, 50)     # ochhio destro (riempito di nero)
win.wait()                            # aspetta che l'utente chiuda la finestra

# In mancanza dell'ultima istruzione, il programma disegna la faccina ma esce immediatamente,
# rendendo difficile vedere quello che ha fatto. Con la funzione wait, invece, aspetta che l'utente
# chiuda la finestra.
