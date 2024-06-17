from graphics import GraphicsWindow

WIN_WIDTH = 500
WIN_HEIGHT = 500

win = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
canvas = win.canvas()
canvas.setOutline("black")

# Proprietà della bandiera
flag_width = 100
flag_pos_x = WIN_WIDTH * 0.5 - (flag_width + flag_width * 0.5)
flag_pos_y = WIN_HEIGHT * 0.5 - flag_width

# Creazione della bandiera
canvas.setFill("green")
canvas.drawRect(flag_pos_x, flag_pos_y, flag_width, flag_width * 2)

canvas.setFill("white")
#canvas.drawRect(flag_pos_x + flag_width, flag_pos_y, flag_width, flag_width * 2)
canvas.drawLine(flag_pos_x + flag_width, flag_pos_y, flag_pos_x + flag_width * 2, flag_pos_y)
canvas.drawLine(flag_pos_x + flag_width, flag_pos_y + flag_width * 2, flag_pos_x + flag_width * 2, flag_pos_y + flag_width * 2)

canvas.setFill("red")
canvas.drawRect(flag_pos_x + flag_width * 2, flag_pos_y, flag_width, flag_width * 2)

win.wait()