# Screen and button variables
time = 50
homeScreen = True
buttonColor = color(0, 200, 200)
buttonColor2 = color(200, 200, 0)
buttonColor3 = color(255, 0, 0)
helpScreen = False
tankDraw = True
tank2Draw = True
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
blox = False
blox1 = False
blox2 = False
blox3 = False
blox4 = False
blox5 = False
super = False
super2 = False
# Score
score = 0
score2 = 0

def draw():
    global blox
    global blox2
    global blox3
    global super
    global super2
    global img
    global home
    global homeScreen
    global helpScreen    
    global time
    global tankDraw
    global tank2Draw
    # Scores
    global score
    global score2
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
        strokeWeight(4)
        line(0, 425, 1000, 425)
        noStroke()
        textSize(40)
        fill(0, 255, 100)
        text(score, 250, 480)
        fill(255, 0, 100)
        text(score2, 700, 480)
        stroke(0)
        strokeWeight(1)
        

        # Bullets for tank 1
    speed = PVector.fromAngle(radians(turn))
    if super == True and tankDraw == True and tank2Draw == True:
        noStroke()
        fill(random(1)*255, 0, 0)
        ellipse(bullet.x, bullet.y, 10, 10)
    elif tankDraw == True and tank2Draw == True:
        fill(0)
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
            super = False
    if super == True:
        if shot == True:
            v1 = PVector(tank2.x-bullet.x, tank2.y-bullet.y)
            v2 = v1.heading()
            bulletPoint = bulletSpeed.fromAngle(v2)
            angle1 = bulletSpeed.heading()
            angle2 = bulletPoint.heading()
            angle1 = degrees(angle1)
            angle2 = degrees(angle2)
            if angle1 > -90 and angle1 < 0 and angle2 < 90 and angle2 > 0:
                print("")
            elif angle1 <= 0:
                angle1 += 360
            if angle2 > -90 and angle2 < 0 and angle1 < 90 and angle1 > 0:
                print("")
            elif angle2 <= 0:
                angle2 += 360
            if angle1 > angle2:
                angle1 -= 5
            if angle2 > angle1:
                angle1 += 5
            bulletSpeed.set(PVector.fromAngle(radians(angle1)))
            bulletSpeed.mult(2.5)

        
            
    # Bullets for tank 2
    fill(0)
    speed2 = PVector.fromAngle(radians(turn2))
    if super2 == True and tankDraw == True and tank2Draw == True:
        noStroke()
        fill(random(1)*255, 0, 0)
        ellipse(bullet2.x, bullet2.y, 10, 10)
    elif tankDraw == True and tank2Draw == True:
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
            super2 = False
    if super2 == True:
        if shot2 == True:
            v12 = PVector(tank.x-bullet2.x, tank.y-bullet2.y)
            v22 = v12.heading()
            bulletPoint2 = bulletSpeed2.fromAngle(v22)
            angle3 = bulletSpeed2.heading()
            angle4 = bulletPoint2.heading()
            angle3 = degrees(angle3)
            angle4 = degrees(angle4)
            if angle3 > -90 and angle3 < 0 and angle4 < 90 and angle4 > 0:
                print("")
            elif angle3 <= 0:
                angle3 += 360
            if angle4 > -90 and angle4 < 0 and angle3 < 90 and angle3 > 0:
                print("")
            elif angle4 <= 0:
                angle4 += 360
            if angle3 > angle4:
                angle3 -= 5
            if angle4 > angle3:
                angle3 += 5
    
            bulletSpeed2.set(PVector.fromAngle(radians(angle3)))
            bulletSpeed2.mult(2.5)
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
    stroke(0)
    # TANK 1
    translate(tank.x, tank.y)
    rotate(radians(turn))
    if tankDraw == True:
        fill(50, 50, 50)
        rect(-25, -20, 50, 40)
        rect(-25, -15, 50, 30)
        if super == True:
            rect(0, -6, 45, 12)
        else:     
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
    if tank2Draw == True:
        fill(50, 50, 50)
        rect(-25, -20, 50, 40)
        rect(-25, -15, 50, 30)
        if super2 == True:
            rect(0, -6, 45, 12)
        else:
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
#########################################################################################################################3
    resetMatrix()
    tankDraw = True
    tank2Draw = True
    move = True
    move2 = True
    # Bullet Kills
    if bullet.x-tank2.x <= 20 and bullet.x-tank2.x >= -20 and bullet.y-tank2.y <= 20 and bullet.y-tank2.y >= -20:
        if time <= 150:
            move2 = False
            move = False
            bullet.set(tank2)

            noStroke()
            fill(255, 255, 0)
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        elif time <= 250:
            bullet.set(tank2)
            tank2Draw = False
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        else:
            tank2Draw = True
            move2 = True
            move = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot = False
            shot2 = False
            super = False
            super2 = False
            score += 1
            time = 50
            
    elif bulletTime >= 60 and bullet.x-tank.x <= 20 and bullet.x-tank.x >= -20 and bullet.y-tank.y <= 20 and bullet.y-tank.y >= -20:
        if time <= 150:
            move = False
            move2 = False
            bullet.set(tank)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank.x, tank.y, time, time)
            time+=4
        elif time <= 250:
            bullet.set(tank)
            tankDraw = False
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank.x, tank.y, time, time)
            time+=4
        else:
            tankDraw = True
            move2 = True
            move = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot = False
            shot2 = False
            super = False
            super2 = 
            score2 += 1
            time = 50


    elif bullet2.x-tank.x <= 20 and bullet2.x-tank.x >= -20 and bullet2.y-tank.y <= 20 and bullet2.y-tank.y >= -20:
        if time <= 150:
            move = False
            move2 = False
            bullet2.set(tank)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank.x, tank.y, time, time)
            time+=4
        elif time <= 250:
            bullet2.set(tank)
            tankDraw = False
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank.x, tank.y, time, time)
            time+=4
        else:
            tankDraw = True
            move2 = True
            move = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot2 = False
            shot = False
            super = False
            super2 = False
            score2 += 1
            time = 50
            
    elif bulletTime2 >= 60 and bullet2.x-tank2.x <= 20 and bullet2.x-tank2.x >= -20 and bullet2.y-tank2.y <= 20 and bullet2.y-tank2.y >= -20:
        if time <= 150:
            move2 = False
            move = False
            bullet2.set(tank2)
            noStroke()
            fill(255, 255, 0)
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        elif time <= 250:
            bullet2.set(tank2)
            tank2Draw = False
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank2.x, tank2.y, time, time)
            time+=4
        else:
            tank2Draw = True
            move2 = True
            move = True
            tank2.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            tank.set(random(800), random(300))
            shot2 = False
            shot = False
            super = False
            super2 = False
            score += 1
            time = 50

                               
################################################################################################################################
    
    resetMatrix()
    RNJesus = int(random(200))
    if RNJesus == 5:                   
        blox = True
    if blox == True:                
        fill(140)
        rect(230, 120, 40, 40)
        fill(0)
        ellipse(250, 140, 18, 18) 
        if ((tank2.x - 230)**2 <= 400 or (tank2.x - 270)**2 <= 400) and ((tank2.y - 120)**2 <= 400 or (tank2.y - 160)**2 <= 400):                                                
            blox = False
            super2 = True
        elif ((tank.x - 230)**2 <= 400 or (tank.x - 270)**2 <= 400) and ((tank.y - 120)**2 <= 400 or (tank.y - 160)**2 <= 400):                                                
            blox = False
            super = True
    if RNJesus == 69:                   
        blox2 = True
    if blox2 == True:                
        fill(140)
        rect(830, 240, 40, 40)
        fill(0)
        ellipse(850, 260, 18, 18) 
        if ((tank2.x - 830)**2 <= 400 or (tank2.x - 870)**2 <= 400) and ((tank2.y - 240)**2 <= 400 or (tank2.y - 280)**2 <= 400):                                                
            blox2 = False
            super2 = True
        elif ((tank.x - 830)**2 <= 400 or (tank.x - 870)**2 <= 400) and ((tank.y - 240)**2 <= 400 or (tank.y - 280)**2 <= 400):                                                
            blox2 = False
            super = True
    if RNJesus == 37:                   
        blox3 = True
    if blox3 == True:                
        fill(140)
        rect(320, 370, 40, 40)
        fill(0)
        ellipse(390, 440, 18, 18) 
        if ((tank2.x - 390)**2 <= 400 or (tank2.x - 430)**2 <= 400) and ((tank2.y - 420)**2 <= 400 or (tank2.y - 460)**2 <= 400):                                                
            blox3 = False
            super2 = True
        elif ((tank.x - 390)**2 <= 400 or (tank.x - 430)**2 <= 400) and ((tank.y - 420)**2 <= 400 or (tank.y - 460)**2 <= 400):                                                
            blox3 = False
            super = True
        
                        
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
