from graphics import GraphicsWindow

win = GraphicsWindow(400,400)
canvas = win.canvas()

canvas.setOutline("magenta") # colore magenta

# Rettangoli con posizione x fissa a 0 che crescono in larghezza
canvas.drawRect(0, 10, 200, 10) 
canvas.drawRect(0, 30, 300, 10)
canvas.drawRect(0, 50, 100, 10)

win.wait()