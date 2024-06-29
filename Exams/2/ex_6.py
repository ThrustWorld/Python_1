from ezgraphics import GraphicsWindow

OFFSET_SQUARE = 40
SIDE_SQUARE = 40

n = int(input("N rows: "))
m = int(input("M columns: "))
center_text = 0

win = GraphicsWindow(900,600)
win.setTitle("Ex_6")

canvas = win.canvas()
for i in range(n):
    for j in range(m):
        
        x = j * SIDE_SQUARE
        y = i * SIDE_SQUARE
        canvas.drawRect(x + OFFSET_SQUARE, y + OFFSET_SQUARE, SIDE_SQUARE, SIDE_SQUARE)
        
        text_x = x + SIDE_SQUARE 
        text_y = y + SIDE_SQUARE
        
        center_text += 1
        canvas.drawText( text_x + 15, text_y + 10, center_text)



win.wait()