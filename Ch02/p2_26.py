from graphics import GraphicsWindow

win = GraphicsWindow(500,300)

canvas = win.canvas()

canvas.setColor("black")
canvas.drawOval(150,50,200,200)
canvas.setColor("white")
canvas.drawOval(180,80,140,140)
canvas.setColor("black")
canvas.drawOval(200,100,100,100)
canvas.setColor("white")
canvas.drawOval(220,120,60,60)
canvas.setColor("black")
canvas.drawOval(235,135,30,30)

win.wait()