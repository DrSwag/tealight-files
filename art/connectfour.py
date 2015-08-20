from tealight.art import (color, line, spot, circle, box, image, text, background)


color("blue")
box(50,50,725,725)


def setgrid():
  
  x = 125
  y = 125
  color("white")

  for i in range(8):
    for j in range(8):
      spot(x,y,37.5)
      x += 80
    x = 125
    y += 80
  
  grid = [[0 for j in range(8)] for i in range(8)]
  
  return grid

 
def drawcircle(player, x, y, grid):
  
  color(player)
  
  x = 125 + (x*80)
  y = 125 + (y*80)
  
  spot(x, y, 37.5)
  
  grid[x][y] = player
  
    for i in range(8):
      for j in range(8):
        print grid[i][j]
  
  return grid
  
  



grid = setgrid()

grid = drawcircle("yellow", 0, 7, grid)