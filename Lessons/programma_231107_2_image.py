# Questo programma visualizza l'immagine "queen-mary.gif" in una finestra, poi in una seconda
# finestra visualizza una immagine alterata, più chiara o più scura a seconda del valore della
# costante FACTOR. È importante che il file queen-mary.gif sia nella directory corrente nella
# quale viene eseguito Python.

from ezgraphics import GraphicsWindow, GraphicsImage

# Costante moltiplicativa per le intensità delle componenti RGB di un pixel. Se
# questo valore è maggiore di 1, la seconda immagine sarà più chiara, se è minore
# di 1 sarà più scura.
FACTOR = 1.5

# Carico l'immagine e la metto nella variabile img
img = GraphicsImage("queen-mary.gif")

# I metodi height() e width() restituiscono altezza e larghezza dell'immagine in pixel
height = img.height()
width = img.width()

# Creo una finestra delle dimensioni esattamente uguali all'immagine
win = GraphicsWindow(width, height)
canvas = win.canvas()

# Visualizzo l'immagine nella finestra
canvas.drawImage(img)

# Carico di nuovo l'immagine per modificarla
img2 = GraphicsImage("queen-mary.gif")

# Con due cicli for, scandisco tutti i pixel dell'immagine. Le variabili x ed y
# conterranno di volta in volta le coordinate di un pixel dell'immagine.
for y in range(height):
    for x in range(width):
        # Il metodo getRed() restituisce la quantità di rosso presente nel pixel di coordinate (x,y).
        # Analogamente getGreen() e getBlue() per gli altri due colori primari.
        red = img2.getRed(y,x)
        green = img2.getGreen(y,x)
        blue = img2.getBlue(y,x)
        # Determina il valore di rosso per l'immagine modificata. Moltiplica il vecchio valore per il
        # numero FACTOR e poi converte in intero. Siccome se FACTOR > 1 c'è il rischio che il risultato
        # sia maggiore di 255, e poiché 255 è il valore massimo ammesso per l'intensità di un colore,
        # faccio il minimo con 255 per non sforare. Stessa cosa per le componenti verdi e blu.
        new_red = min(int(red * FACTOR), 255)
        new_green = min(int(green * FACTOR), 255)
        new_blue = min(int(blue * FACTOR), 255)
        # Il metodo setPixel() modifica il colore del pixel alle coordinate (x,y) con i valori di rosso,
        # vere e blu forniti come argomento.
        img2.setPixel(y, x, new_red, new_green, new_blue)

# Apro la seconda finestra e visualizza l'immagine modificata
win2 = GraphicsWindow(width, height)
canvas2 = win2.canvas()
canvas2.drawImage(img2)

win.wait()
