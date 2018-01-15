# Screen and button variables
time = 50
homeScreen = True
buttonColor = color(0, 200, 200)
buttonColor2 = color(200, 200, 0)
buttonColor3 = color(255, 0, 0)
helpScreen = False
def setup():
    # Main screen setup
    size(1000, 500)
    global img
    img = createGraphics(1000, 500)
    img.beginDraw()
    img.background(255)
    img.fill(0, 0, 255)
    # obstacles on the map
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
tank = PVector(800, 200)
turn = 180
speed = PVector(0, 0)
# Moving tank 1
move = True
moveUp = False
moveBack = False
turnCCW = False
turnCW = False
# Bullet
bullet = PVector(800, 200)
shot = False
frag = False
bulletSpeed = PVector(0, 0)
# TANK 2
tank2 = PVector(400, 200)
turn2 = 0
speed2 = PVector(0,0)
# Moving tank 2
move2 = True
moveUp2 = False
moveBack2 = False
turnCCW2 = False
turnCW2 = False
#Bullet 2
bullet2 = PVector(400, 200)
shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)

def draw():
    global img
    global home
    global homeScreen
    global helpScreen    
    global time
    # TANK 1 Global
    global speed
    global turn
    global tank
    global move
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    # TANK 2 Global
    global speed2
    global turn2
    global tank2
    global move2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    
    # Motion Control
    if move == False:
        moveUp = False
        moveBack = False
        turnCW = False
        turnCCW = False
    
    if move2 == False:
        moveUp2 = False
        moveBack2 = False
        turnCW2 = False
        turnCCW2 = False
    
    font = createFont("Ubuntu Mono Bold", 20)# PrimaryFont
    font2 = createFont("URW Bookman L Demi Bold", 20)# Decorative Font
    # Different settings for screens
    if homeScreen == True:
        background(0)
        global buttonColor
        global buttonColor2
        global buttonColor3
        background(150)
        noStroke()
        fill(0)
        textFont(font2)
        textSize(120)
        # Main title
        text("TANK", 200, 100)
        text("GAME", 400, 200)
        fill(buttonColor)
        rect(250, 210, 480, 220)
        fill(0)
        textFont(font)
        textSize(200)
        text("PLAY", 290, 380)
        fill(buttonColor2)
        rect(20, 20, 150, 40)
        fill(0)
        textSize(24)
        text("How to play", 25, 45)
        # Selecting between screens and controls on the screens
        
        # Tanks stay still on home screen
        tank.add(speed.mult(3))
        tank2.add(speed2.mult(3))
    elif helpScreen == True:
        background(255)
        text("player 1: Use WASD to move, and Q to shoot.", 100, 100)
        text("player 2: Use the arrow keys to move, and space to shoot.", 100, 200)
        fill(buttonColor3)
        rect(0, 0, 30, 30)
        fill(0)
        textSize(30)
        text("X", 10, 30)
    # Main game screen
    else:
        background(img)
        stroke(0)
        

        # Bullets for tank 1
    fill(0)
    speed = PVector.fromAngle(radians(turn))
    ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(tank)
        bulletSpeed.set(speed.mult(6))
        global bulletTime
        global breakTime
        bulletTime = 0
        breakTime = 0
    else:
        global bulletTime
        global breakTime
        bullet.add(bulletSpeed)
        if breakTime >= 7:
            if get(int(bullet.x+10), int(bullet.y)) != -1:
                bulletSpeed.x *= -1
                breakTime = 0
            elif get(int(bullet.x-10), int(bullet.y)) != -1:
                bulletSpeed.x *= -1
                breakTime = 0
            if get(int(bullet.x), int(bullet.y+10)) != -1:
                bulletSpeed.y *= -1
                breakTime = 0
            elif get(int(bullet.x), int(bullet.y-10)) != -1:
                bulletSpeed.y *= -1
                breakTime = 0
        bulletTime += 1
        breakTime += 1    
        if bulletTime >= 600:
            shot = False
    # Bullets for tank 2
    fill(0)
    speed2 = PVector.fromAngle(radians(turn2))
    ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank2)
        bulletSpeed2.set(speed2.mult(6))
        global bulletTime2
        global breakTime2
        breakTime2 = 0
        bulletTime2 = 0
    else:
        global bulletTime2
        global breakTime2
        bullet2.add(bulletSpeed2)
        if breakTime2 >= 7:
            if get(int(bullet2.x+10), int(bullet2.y)) != -1:
                bulletSpeed2.x *= -1
                breakTime2 = 0
            elif get(int(bullet2.x-10), int(bullet2.y)) != -1:
                bulletSpeed2.x *= -1
                breakTime2 = 0
            if get(int(bullet2.x), int(bullet2.y+10)) != -1:
                bulletSpeed2.y *= -1
                breakTime2 = 0
            elif get(int(bullet2.x), int(bullet2.y-10)) != -1:
                bulletSpeed2.y *= -1
                breakTime2 = 0
        bulletTime2 += 1
        breakTime2 += 1    
        if bulletTime2 >= 600:
            shot2 = False
    b = 38.65980825 # IMPORTANT NUMBER!!!
    # Edge detection
    UL = PVector.fromAngle(radians(turn+180+b)).mult(33) # Upper Left corner
    LL = PVector.fromAngle(radians(turn+180-b)).mult(33) # Lower Left corner
    UR = PVector.fromAngle(radians(turn-b)).mult(33) # Upper Right corner
    LR = PVector.fromAngle(radians(turn+b)).mult(33) # Lower rRght corner

    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    noFill()

    if get(int(tank.x+speed.x*14),int(tank.y+speed.y*14)) != -1:
        tank.sub(speed)
    if get(int(tank.x+UL.x),int(tank.y+UL.y)) != -1:
        tank.add(speed)
        turnCCW = False
    elif get(int(tank.x+LL.x),int(tank.y+LL.y)) != -1:
        tank.add(speed)
        turnCW = False
    if get(int(tank.x+UR.x),int(tank.y+UR.y)) != -1:
        tank.sub(speed)
        turnCCW = False
    elif get(int(tank.x+LR.x),int(tank.y+LR.y)) != -1:
        tank.sub(speed)
        turnCW = False
    # Edge detection for player 2
    UL2 = PVector.fromAngle(radians(turn2+180+b)).mult(33)
    LL2 = PVector.fromAngle(radians(turn2+180-b)).mult(33)
    UR2 = PVector.fromAngle(radians(turn2-b)).mult(33)
    LR2 = PVector.fromAngle(radians(turn2+b)).mult(33)

    speed2 = PVector.fromAngle(radians(turn2))
    noFill()

    speed2.mult(3)
    if get(int(tank2.x+speed2.x*14),int(tank2.y+speed2.y*14)) != -1:
        tank2.sub(speed2)
    if get(int(tank2.x+UL2.x),int(tank2.y+UL2.y)) != -1:
        tank2.add(speed2)
        turnCCW2 = False
    elif get(int(tank2.x+LL2.x),int(tank2.y+LL2.y)) != -1:
        tank2.add(speed2)
        turnCW2 = False
    if get(int(tank2.x+UR2.x),int(tank2.y+UR2.y)) != -1:
        tank2.sub(speed2)
        turnCCW2 = False
    elif get(int(tank2.x+LR2.x),int(tank2.y+LR2.y)) != -1:
        tank2.sub(speed2)
        turnCW2 = False
        
    # TANK 1
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
    #Turning Tank 1
    speed = PVector.fromAngle(radians(turn))
    # Tank 1 movement
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500:
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp == True:
        tank.add(speed.mult(3))
    elif moveBack == True:
        tank.sub(speed.mult(3))
    if turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
    speed = PVector.fromAngle(radians(turn))
    resetMatrix()
#######################################################################################    

    # TANK 2
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
    # Turning tank 2
    speed2 = PVector.fromAngle(radians(turn2))
    # Tank 2 movement
    if tank2.x >= 1000 :
        tank2.x = 999
    elif tank2.x <= 0:
        tank2.x = 1
    elif tank2.y >= 500 :
        tank2.y = 499
    elif tank2.y <= 0:
        tank2.y = 1
    elif moveUp2 == True:
        tank2.add(speed2.mult(3))
    elif moveBack2 == True:
        tank2.sub(speed2.mult(3))
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4
    speed2 = PVector.fromAngle(radians(turn2))
    
    resetMatrix()
    # Bullet Kills
    if bullet.x-tank2.x <= 20 and bullet.x-tank2.x >= -20 and bullet.y-tank2.y <= 20 and bullet.y-tank2.y >= -20:
        if time <= 150:
            move2 = False
            bulletSpeed.set(0, 0)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        elif time <= 250:
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        else:
            move2 = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot = False
            shot2 = False
            time = 50
            # Death Animation
    elif bulletTime >= 60 and bullet.x-tank.x <= 20 and bullet.x-tank.x >= -20 and bullet.y-tank.y <= 20 and bullet.y-tank.y >= -20:
        if time <= 150:
            move = False
            bulletSpeed.set(0, 0)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank.x, tank.y, time, time)
            time+=4
        elif time <= 250:
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank.x, tank.y, time, time)
            time+=4
        else:
            move = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot = False
            shot2 = False
            time = 50

    if bullet2.x-tank.x <= 20 and bullet2.x-tank.x >= -20 and bullet2.y-tank.y <= 20 and bullet2.y-tank.y >= -20:
        if time <= 150:
            move = False
            bulletSpeed2.set(0, 0)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank.x, tank.y, time, time)
            time+=4
        elif time <= 250:
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank.x, tank.y, time, time)
            time+=4
        else:
            move = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot2 = False
            shot = False
            time = 50
   
    elif bulletTime2 >= 60 and bullet2.x-tank2.x <= 20 and bullet2.x-tank2.x >= -20 and bullet2.y-tank2.y 
            <= 20 and bullet2.y-tank2.y >= -20:t
        if time <= 150:
            move2 = False
            bulletSpeed2.set(0, 0)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        elif time <= 250:
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        else:
            move2 = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot2 = False
            shot = False
            time = 50
def mouseMoved():
    global buttonColor
    global buttonColor2
    global buttonColor3
    global helpScreen
    global homeScreen
   # Makes the buttons shange when mouse hovers over
    if mouseX <= 710 and mouseX >= 250 and mouseY <= 400 and mouseY >= 180:
        buttonColor = color(55, 255, 255)
    else:
        buttonColor = color(0, 200, 200)
    if mouseX >= 20 and mouseX <= 170 and mouseY >= 20 and mouseY <= 60:
        buttonColor2 = color(255, 255, 55)
    else:
        buttonColor2 = color(200, 200, 0)
    if mouseX <= 30 and mouseY <= 30:
        buttonColor3 = color(255, 100, 100)
    else:
        buttonColor3 = color(255, 0, 0)
def mouseClicked():
    global homeScreen
    global helpScreen
    #moves to game screen
    if mouseX <= 710 and mouseX >= 250 and mouseY <= 400 and mouseY >= 180:
        homeScreen = False
    #moves to instructions screen
    if mouseX <= 170 and mouseX >= 20 and mouseY >=20 and mouseY <= 60:
        helpScreen = True
        homeScreen = False
    # Moves back to home screen from help screen
    if helpScreen == True and mouseX <= 30 and mouseY <= 30:
        helpScreen = False
        homeScreen = True
def keyPressed():
    # TANK 1
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
    #controls for tank 1
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
    #controls for tank 2
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
