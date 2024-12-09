import pgzrun
import random
import time
HEIGHT=600
WIDTH=800
start=0
end=0
total=0
satellites=[]
lines=[]
next=0
def draw():
  global number
  global total
  screen.clear()
  screen.blit('space_bg',(0,0))
  number=1
  for line in lines: 
    screen.draw.line(line[0],line[1],"white")
  for satellite in satellites: 
    satellite.draw()
    screen.draw.text(str(number),(satellite.x,satellite.y+20))
    number+=1
  if next<10:
    total = time.time()-start
    screen.draw.text(str(total),(0,0),fontsize=24)
  else:
    screen.draw.text(str(total),(0,0),fontsize=24)
    
for i in range (10):  
  satellite=Actor('satellite')
  satellite.pos=(random.randint(0,800),random.randint(0,600))
  satellites.append(satellite)

start = round(time.time())

def on_mouse_down(pos):
  global next
  if next<10:
    if satellites[next].collidepoint(pos):
      if next>0:
        lines.append((satellites[next-1].pos,satellites[next].pos))
      next+=1
    else:
      lines.clear()
      next=0


pgzrun.go()
