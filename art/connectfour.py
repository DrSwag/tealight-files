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

 
def drawcircle(color, x, y):
  color(str(color))
  
  x = 125 + (x*80)
  y = 125 + (x*80)
  
  spot(x, y, 37.5)
  
    
setgrid()

drawcircle("red", 4, 3)