from ezgraphics import GraphicsWindow
from forza4 import *

# CELL_SIZE è la dimensione di una cella di Forza 4, definita
# nel file forza4.py

win = GraphicsWindow(7*CELL_SIZE, 6*CELL_SIZE)
canvas = win.canvas()
l = [
  [  0,  0,  0,  0,  0,  0,  0 ],
  [  0,  1,  0,  0,  0,  0,  0 ],
  [ -1, -1,  0,  0,  1,  0,  0 ],
  [ -1,  1,  1,  0, -1,  0,  0 ],
  [ -1,  1,  1,  0, -1,  0,  0 ],
  [  1, -1,  1,  0, -1,  1, -1 ]
]
show_board(l, canvas)
win.wait()
