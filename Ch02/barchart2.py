from graphics import GraphicsWindow

win = GraphicsWindow(400,400)
canvas = win.canvas()



# Rettangoli con posizione x fissa a 0 che crescono in larghezza
canvas.setColor("red")
canvas.drawRect(0, 10, 200, 10)
canvas.setColor("green")
canvas.drawRect(0, 30, 300, 10)
canvas.setColor("blue")
canvas.drawRect(0, 50, 100, 10)

win.wait()