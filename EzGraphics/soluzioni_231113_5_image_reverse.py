from ezgraphics import GraphicsImage, GraphicsWindow

def reverse(img: GraphicsImage):
    """
    Restituisce la versione in negativo dell'immagine 'img'.
    """
    # Determina altezza e larghezza immagine
    h = img.height()
    w = img.width()
    # Crea nuova immagine vuota delle stesse dimension di img
    img2 = GraphicsImage(w, h)
    # Scandisce tutti i pixel di img
    for y in range(h):
        for x in range(w):
            # Estrae componenti rosso, verde e blu del pixel di coordinate (x, y) di img.
            # Invece di usare getRed, getGreen e getBlue, uso getPixel che restituisce
            # contemporaneamente le tre componenti (un po' come getMouse restituisce entrambe
            # le coordinate del punto dove è stato fatto click col mouse)
            red, green, blue = img.getPixel(y, x)
            # Setto lo stesso pixel in img2 con i valori rosso, verde e blu in negativo.
            img2.setPixel(y, x, 255 - red, 255 - green, 255 - blue)
    # Restituisce la nuova immagine
    return img2

win = GraphicsWindow()
canvas = win.canvas()
# Carico l'immagine queen-mary
img = GraphicsImage("queen-mary.gif")
# Uso la funzione reverse per ottenere l'immagine in negativo
img = reverse(img)
# Disegno l'immagine in negativo
canvas.drawImage(img)

win.wait()
