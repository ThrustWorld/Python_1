from graphics import GraphicsWindow

win = GraphicsWindow(500,300)

canvas = win.canvas()

canvas.drawOval(150,50,200,200)
canvas.drawOval(200,100,25,25)
canvas.drawOval(275,100,25,25)
canvas.drawLine(200,175,300,175)


win.wait()