from graphics  import GraphicsWindow # Importare il modulo della libreria grafica

win = GraphicsWindow(500, 300) # Creazione finestra

canvas = win.canvas() # Accesso alle informazioni del pannello canvas

canvas.drawRect(5, 10, 20, 30) # Disegna un rettangolo all'interno della canvas

canvas.drawLine(100, 200, 200, 100) # Disegna una linea all'interno della canvas

win.wait() # Aspetta l'input dell'utente per chiudere la finestra