from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

canvas.drawRectangle(0,0,200,200)
canvas.drawRectangle(200,0,200,200)
canvas.setFontSize(20)
canvas.setTextAnchor("center")
canvas.setOutline("red")
canvas.drawText(100,100, "Rosso")
canvas.setOutline("green")
canvas.drawText(300,100, "Verde")
canvas.setOutline("black")

x, y = win.getMouse()
if y <= 200 and x <= 200:
    canvas.setFill("red")
elif y <= 200 and x > 200:
    # in realtà la condizione x > 200 è superflua, se fosse x<=200 sarebbe
    # stata valida la prima condizione dell'if e non ci ritroveremmo qui
    canvas.setFill("green")
else:
    canvas.setFill("black")
canvas.drawOval(0, 200, 400, 200)
win.wait()
