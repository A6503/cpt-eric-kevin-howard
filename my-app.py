img = None
def setup():
    size(1000, 500)
    global img

img = createGraphics(width/4, height/4) # Width and Length is not defined
img.beginDraw()
img.background(0)
img.fill(255, 0, 0)
for i in range(15):
    x = random(img.width)
    y = random(img.length)
    img.line(x, y, random(1, 50), random(1, 50))
img.endDraw()
    # TANK 1
tank = PVector(400, 400)
turn = 0
speed = 0
# Moving tank 1
moveUp = False
moveBack = False
turnCCW = False
turnCW = False

# TANK 2
tank2 = PVector(200, 200)
turn2 = 0
speed2 = 0
# Moving tank 2
moveUp2 = False
moveBack2 = False
turnCCW2 = False
turnCW2 = False

def draw():
    global img
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    background(255)
    image(img, 50, 50)
    fill(0, 255, 0)
   
    translate(tank.x, tank.y)
    rotate(radians(turn))
    fill(0, 255, 0)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
   
    fill(0, 255, 0)
    ellipse(0, 0, 25, 25)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
        turn += 180
    elif tank.x <= 0:
        tank.x = 1
        turn += 180
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if tank.y >= 500 or tank.y <= 0:
        turn *= -1
    elif turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
       
    resetMatrix()
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2

    fill(0, 255, 0)
   
    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    fill(255, 0, 0)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
   
    fill(255, 0, 0)
    ellipse(0, 0, 25, 25)
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
        turn2 += 180
    elif tank2.x <= 0:
        tank2.x = 1
        turn2 += 180
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if tank2.y >= 500 or tank2.y <= 0:
        turn2 *= -1
    elif turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4
def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    if key == "w":
        moveUp = True
        moveBack = False
    if key == "s":
        moveBack = True
        moveUp = False
    if key == "a":
        turnCCW = True
        turnCW = False
    if key == "d":
        turnCW = True
        turnCCW = False
        
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    if keyCode == UP:
        moveUp2 = True
        moveBack2 = False
    if keyCode == DOWN:
        moveBack2 = True
        moveUp2 = False
    if keyCode == LEFT:
        turnCCW2 = True
        turnCW2 = False
    if keyCode == RIGHT:
        turnCW2 = True
        turnCCW2 = False
def keyReleased():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    if key == "w":
        moveUp = False
    if key == "s":
        moveBack = False
    if key == "a":
        turnCCW = False
    if key == "d":
        turnCW = False
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    if keyCode == UP:
        moveUp2 = False
    if keyCode == DOWN:
        moveBack2 = False
    if keyCode == LEFT:
        turnCCW2 = False
    if keyCode == RIGHT:
        turnCW2 = False
