homeScreen = True
def setup():
    size(1000, 500)
    global img
    global home
    home = createGraphics(1000, 500)
    home.beginDraw()
    home.background(100)
    home.fill(0)
    home.textSize(100)
    home.text("Tank Game", 210, 100)
    home.textSize(200)
    home.text("Play", 290, 350)
    img = createGraphics(1000, 500)
    img.beginDraw()
    img.background(255)
    img.fill(0, 0, 255)
    for i in range(15):
        img.rect(100, 100, 100, 100)
        img.rect(500, 250, 100, 100)
        img.rect(300, 250, 50, 50)
        img.rect(750, 250, 50, 50)
        img.rect(600, 100, 50, 50)
        img.rect(850, 380, 50, 50)
           
        img.rect(100, 350, 75, 75)
        img.rect(850, 100, 50, 50)
        img.rect(325, 100, 60, 60)
        img.endDraw()
    
# TANK 1
tank = PVector(400, 400)
turn = 0
speed = PVector(0, 0)
# Moving tank 1
moveUp = False
moveBack = False
turnCCW = False
turnCW = False
#Bullet
bullet = PVector(400, 400)
shot = False
frag = False
bulletSpeed = PVector(0, 0)
# TANK 2
tank2 = PVector(200, 200)
turn2 = 0
speed2 = PVector(0,0)
# Moving tank 2
moveUp2 = False
moveBack2 = False
turnCCW2 = False
turnCW2 = False
#Bullet 2
bullet2 = PVector(200, 200)
shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    font = createFont("Ubuntu Mono Bold", 20)# Font
    if homeScreen == True:
        background(home)
    else:
        background(img)
    
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    fill(0)
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed)
        global bulletTime
        bulletTime = 0
    else:
        global bulletTime
        bullet.add(bulletSpeed)
        if get(int(bullet.x+10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        elif get(int(bullet.x-10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        if get(int(bullet.x), int(bullet.y+10)) != -1:
            
            bulletSpeed.y *= -1
        elif get(int(bullet.x), int(bullet.y-10)) != -1:
    
            bulletSpeed.y *= -1
        bulletTime += 1
        if bulletTime >= 600:
            shot = False
    translate(tank.x, tank.y)
    rotate(radians(turn))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)  
    resetMatrix()
    translate(tank.x, tank.y)
    fill(0, 255, 100)
    textFont(font)
    text("P1", -10, 5)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    resetMatrix()
#######################################################################################    
#######################################################################################    
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    fill(0)
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2)
        global bulletTime2
        bulletTime2 = 0
    else:
        global bulletTime2
        bullet2.add(bulletSpeed2)
        if get(int(bullet2.x+10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        if get(int(bullet2.x), int(bullet2.y+10)) != -1:
            
            bulletSpeed2.y *= -1
        elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
    
            bulletSpeed2.y *= -1
        bulletTime2 += 1
        if bulletTime2 >= 600:
            shot2 = False

    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)
    resetMatrix()
    translate(tank2.x, tank2.y)
    fill(255, 0, 100)
    textFont(font)
    text("P2", -10, 5)
    
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4

def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
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
    if key == "q":
        shot = True
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
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
    if key == "m":
        shot2 = True
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

shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    font = createFont("Ubuntu Mono Bold", 20)# Font
    if homeScreen == True:
        background(home)
    else:
        background(img)
    
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    fill(0)
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed)
        global bulletTime
        bulletTime = 0
    else:
        global bulletTime
        bullet.add(bulletSpeed)
        if get(int(bullet.x+10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        elif get(int(bullet.x-10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        if get(int(bullet.x), int(bullet.y+10)) != -1:
            
            bulletSpeed.y *= -1
        elif get(int(bullet.x), int(bullet.y-10)) != -1:
    
            bulletSpeed.y *= -1
        bulletTime += 1
        if bulletTime >= 600:
            shot = False
    translate(tank.x, tank.y)
    rotate(radians(turn))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)  
    resetMatrix()
    translate(tank.x, tank.y)
    fill(0, 255, 100)
    textFont(font)
    text("P1", -10, 5)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    resetMatrix()
#######################################################################################    
#######################################################################################    
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    fill(0)
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2)
        global bulletTime2
        bulletTime2 = 0
    else:
        global bulletTime2
        bullet2.add(bulletSpeed2)
        if get(int(bullet2.x+10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        if get(int(bullet2.x), int(bullet2.y+10)) != -1:
            
            bulletSpeed2.y *= -1
        elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
    
            bulletSpeed2.y *= -1
        bulletTime2 += 1
        if bulletTime2 >= 600:
            shot2 = False

    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)
    resetMatrix()
    translate(tank2.x, tank2.y)
    fill(255, 0, 100)
    textFont(font)
    text("P2", -10, 5)
    
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4

def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
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
    if key == "q":
        shot = True
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
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
    if key == "m":
        shot2 = True
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
homeScreen = True
def setup():
    size(1000, 500)
    global img
    global home
    home = createGraphics(1000, 500)
    home.beginDraw()
    home.background(100)
    home.fill(0)
    home.textSize(100)
    home.text("Tank Game", 210, 100)
    home.textSize(200)
    home.text("Play", 290, 350)
    img = createGraphics(1000, 500)
    img.beginDraw()
    img.background(255)
    img.fill(0, 0, 255)
    for i in range(15):
        img.rect(100, 100, 100, 100)
        img.rect(500, 250, 100, 100)
        img.rect(300, 250, 50, 50)
        img.rect(750, 250, 50, 50)
        img.rect(600, 100, 50, 50)
        img.rect(850, 380, 50, 50)
           
        img.rect(100, 350, 75, 75)
        img.rect(850, 100, 50, 50)
        img.rect(325, 100, 60, 60)
        img.endDraw()
    
# TANK 1
tank = PVector(400, 400)
turn = 0
speed = PVector(0, 0)
# Moving tank 1
moveUp = False
moveBack = False
turnCCW = False
turnCW = False
#Bullet
bullet = PVector(400, 400)
shot = False
frag = False
bulletSpeed = PVector(0, 0)
# TANK 2
tank2 = PVector(200, 200)
turn2 = 0
speed2 = PVector(0,0)
# Moving tank 2
moveUp2 = False
moveBack2 = False
turnCCW2 = False
turnCW2 = False
#Bullet 2
bullet2 = PVector(200, 200)
shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    font = createFont("Ubuntu Mono Bold", 20)# Font
    if homeScreen == True:
        background(home)
    else:
        background(img)
    
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    fill(0)
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed)
        global bulletTime
        bulletTime = 0
    else:
        global bulletTime
        bullet.add(bulletSpeed)
        if get(int(bullet.x+10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        elif get(int(bullet.x-10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        if get(int(bullet.x), int(bullet.y+10)) != -1:
            
            bulletSpeed.y *= -1
        elif get(int(bullet.x), int(bullet.y-10)) != -1:
    
            bulletSpeed.y *= -1
        bulletTime += 1
        if bulletTime >= 600:
            shot = False
    translate(tank.x, tank.y)
    rotate(radians(turn))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)  
    resetMatrix()
    translate(tank.x, tank.y)
    fill(0, 255, 100)
    textFont(font)
    text("P1", -10, 5)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    resetMatrix()
#######################################################################################    
#######################################################################################    
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    fill(0)
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2)
        global bulletTime2
        bulletTime2 = 0
    else:
        global bulletTime2
        bullet2.add(bulletSpeed2)
        if get(int(bullet2.x+10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        if get(int(bullet2.x), int(bullet2.y+10)) != -1:
            
            bulletSpeed2.y *= -1
        elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
    
            bulletSpeed2.y *= -1
        bulletTime2 += 1
        if bulletTime2 >= 600:
            shot2 = False

    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)
    resetMatrix()
    translate(tank2.x, tank2.y)
    fill(255, 0, 100)
    textFont(font)
    text("P2", -10, 5)
    
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4

def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
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
    if key == "q":
        shot = True
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
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
    if key == "m":
        shot2 = True
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

shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    font = createFont("Ubuntu Mono Bold", 20)# Font
    if homeScreen == True:
        background(home)
    else:
        background(img)
    
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    fill(0)
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed)
        global bulletTime
        bulletTime = 0
    else:
        global bulletTime
        bullet.add(bulletSpeed)
        if get(int(bullet.x+10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        elif get(int(bullet.x-10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        if get(int(bullet.x), int(bullet.y+10)) != -1:
            
            bulletSpeed.y *= -1
        elif get(int(bullet.x), int(bullet.y-10)) != -1:
    
            bulletSpeed.y *= -1
        bulletTime += 1
        if bulletTime >= 600:
            shot = False
    translate(tank.x, tank.y)
    rotate(radians(turn))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)  
    resetMatrix()
    translate(tank.x, tank.y)
    fill(0, 255, 100)
    textFont(font)
    text("P1", -10, 5)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    resetMatrix()
#######################################################################################    
#######################################################################################    
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    fill(0)
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2)
        global bulletTime2
        bulletTime2 = 0
    else:
        global bulletTime2
        bullet2.add(bulletSpeed2)
        if get(int(bullet2.x+10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        if get(int(bullet2.x), int(bullet2.y+10)) != -1:
            
            bulletSpeed2.y *= -1
        elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
    
            bulletSpeed2.y *= -1
        bulletTime2 += 1
        if bulletTime2 >= 600:
            shot2 = False

    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)
    resetMatrix()
    translate(tank2.x, tank2.y)
    fill(255, 0, 100)
    textFont(font)
    text("P2", -10, 5)
    
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4

def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
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
    if key == "q":
        shot = True
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
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
    if key == "m":
        shot2 = True
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
homeScreen = True
def setup():
    size(1000, 500)
    global img
    global home
    home = createGraphics(1000, 500)
    home.beginDraw()
    home.background(100)
    home.fill(0)
    home.textSize(100)
    home.text("Tank Game", 210, 100)
    home.textSize(200)
    home.text("Play", 290, 350)
    img = createGraphics(1000, 500)
    img.beginDraw()
    img.background(255)
    img.fill(0, 0, 255)
    for i in range(15):
        img.rect(100, 100, 100, 100)
        img.rect(500, 250, 100, 100)
        img.rect(300, 250, 50, 50)
        img.rect(750, 250, 50, 50)
        img.rect(600, 100, 50, 50)
        img.rect(850, 380, 50, 50)
           
        img.rect(100, 350, 75, 75)
        img.rect(850, 100, 50, 50)
        img.rect(325, 100, 60, 60)
        img.endDraw()
    
# TANK 1
tank = PVector(400, 400)
turn = 0
speed = PVector(0, 0)
# Moving tank 1
moveUp = False
moveBack = False
turnCCW = False
turnCW = False
#Bullet
bullet = PVector(400, 400)
shot = False
frag = False
bulletSpeed = PVector(0, 0)
# TANK 2
tank2 = PVector(200, 200)
turn2 = 0
speed2 = PVector(0,0)
# Moving tank 2
moveUp2 = False
moveBack2 = False
turnCCW2 = False
turnCW2 = False
#Bullet 2
bullet2 = PVector(200, 200)
shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    font = createFont("Ubuntu Mono Bold", 20)# Font
    if homeScreen == True:
        background(home)
    else:
        background(img)
    
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    fill(0)
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed)
        global bulletTime
        bulletTime = 0
    else:
        global bulletTime
        bullet.add(bulletSpeed)
        if get(int(bullet.x+10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        elif get(int(bullet.x-10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        if get(int(bullet.x), int(bullet.y+10)) != -1:
            
            bulletSpeed.y *= -1
        elif get(int(bullet.x), int(bullet.y-10)) != -1:
    
            bulletSpeed.y *= -1
        bulletTime += 1
        if bulletTime >= 600:
            shot = False
    translate(tank.x, tank.y)
    rotate(radians(turn))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)  
    resetMatrix()
    translate(tank.x, tank.y)
    fill(0, 255, 100)
    textFont(font)
    text("P1", -10, 5)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    resetMatrix()
#######################################################################################    
#######################################################################################    
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    fill(0)
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2)
        global bulletTime2
        bulletTime2 = 0
    else:
        global bulletTime2
        bullet2.add(bulletSpeed2)
        if get(int(bullet2.x+10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        if get(int(bullet2.x), int(bullet2.y+10)) != -1:
            
            bulletSpeed2.y *= -1
        elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
    
            bulletSpeed2.y *= -1
        bulletTime2 += 1
        if bulletTime2 >= 600:
            shot2 = False

    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)
    resetMatrix()
    translate(tank2.x, tank2.y)
    fill(255, 0, 100)
    textFont(font)
    text("P2", -10, 5)
    
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4

def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
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
    if key == "q":
        shot = True
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
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
    if key == "m":
        shot2 = True
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

shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    font = createFont("Ubuntu Mono Bold", 20)# Font
    if homeScreen == True:
        background(home)
    else:
        background(img)
    
    # TANK 1
    global speed
    global turn
    global tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    fill(0)
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed)
        global bulletTime
        bulletTime = 0
    else:
        global bulletTime
        bullet.add(bulletSpeed)
        if get(int(bullet.x+10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        elif get(int(bullet.x-10), int(bullet.y)) != -1:
            
            bulletSpeed.x *= -1
        if get(int(bullet.x), int(bullet.y+10)) != -1:
            
            bulletSpeed.y *= -1
        elif get(int(bullet.x), int(bullet.y-10)) != -1:
    
            bulletSpeed.y *= -1
        bulletTime += 1
        if bulletTime >= 600:
            shot = False
    translate(tank.x, tank.y)
    rotate(radians(turn))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)  
    resetMatrix()
    translate(tank.x, tank.y)
    fill(0, 255, 100)
    textFont(font)
    text("P1", -10, 5)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    resetMatrix()
#######################################################################################    
#######################################################################################    
    # TANK 2
    global speed2
    global turn2
    global tank2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    fill(0)
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2)
        global bulletTime2
        bulletTime2 = 0
    else:
        global bulletTime2
        bullet2.add(bulletSpeed2)
        if get(int(bullet2.x+10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
            
            bulletSpeed2.x *= -1
        if get(int(bullet2.x), int(bullet2.y+10)) != -1:
            
            bulletSpeed2.y *= -1
        elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
    
            bulletSpeed2.y *= -1
        bulletTime2 += 1
        if bulletTime2 >= 600:
            shot2 = False

    translate(tank2.x, tank2.y)
    rotate(radians(turn2))
    
    fill(50, 50, 50)
    rect(-25, -20, 50, 40)
    rect(-25, -15, 50, 30)
    rect(0, -3, 40, 6)
    ellipse(0, 0, 25, 25)
    resetMatrix()
    translate(tank2.x, tank2.y)
    fill(255, 0, 100)
    textFont(font)
    text("P2", -10, 5)
    
    speed2 = PVector.fromAngle(radians(turn2))
    speed2.mult(3)
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2)
    elif moveBack2 == True:
        tank2.sub(speed2)
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4

def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
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
    if key == "q":
        shot = True
    # TANK 2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
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
    if key == "m":
        shot2 = True
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
