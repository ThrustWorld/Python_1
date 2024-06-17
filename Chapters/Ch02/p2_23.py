from graphics import GraphicsWindow

win = GraphicsWindow(500,300)

canvas = win.canvas()

canvas.setColor("blue")
canvas.drawRect(150,100,200,100)

canvas.setColor("red")
canvas.drawText(240,140,"Jhon")

win.wait()