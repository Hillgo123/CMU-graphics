from telnetlib import GA
from cmu_graphics import *
import random

#Intitiating program
app.background = fill='lightBlue'
app.stepsPerSecond = 60


#Start screen
class start():
    #Initiating class
    def __init__(self, x, y):
        self.object = Group(
            Rect(0, 0, 300, 200, fill=None, borderWidth=10, border='black'),
            Label('Press Space to Start', 150, 100, size = 25)
        )
        self.object.centerX = x
        self.object.centerY = y
        self.object.visible = False

    #start screen key press functions
    def key_press(self, key):
        pass

class game_over():
    def __init__(self, x, y):
        self.object = Group(
            Rect(0, 0, 300, 200, fill=None, borderWidth=10, border='black'),
            Label('Game Over', 150, 100, size = 25)
        )
        self.object.centerX = x
        self.object.centerY = y
        self.object.visible = False

    def key_press(self, key):
        pass
        

#Player
class player():
    #initiating class
    def __init__(self, x, y, sp, hp):
        self.object = Group(
            Rect(x, y, 25, 20),
            Circle(x + 25, y + 10, 10)
        )
        self.speed = sp
        self.object.visible = False
        self.hp = hp
        self.hud = Group(
            Label(self.hp, 200, 10)
        )
        self.hud.visible = False

    #player on key hold functions
    def key_holds(self, keys):
        if 'up' in keys and self.object.top > 0:
            self.object.centerY -= 1 * self.speed
        elif 'down' in keys and self.object.bottom < 400:
            self.object.centerY += 1 * self.speed

    #Player key press functions
    def key_press(self, key):
        pass

    def collision(self):
        if self.object.contains(Rocks.object1):
            self.hp -= 1

        if  self.hp == 0:
            Game_Manager.state = 'game over'

class rocks():
    def __init__(self, y, r, sp, a):
        self.object1 = Group(
            Circle(400, y, r, fill='gray', borderWidth=1),
            Circle(400, y - r, r/2, fill='lightGray', borderWidth=1)
        )
        self.speed = sp
        self.acceleration = a
        self.object1.visible = False

    #Movement
    def move(self):
        self.object1.centerX -= 1 * self.speed
        if self.object1.right < 0:
            self.speed += self.acceleration
            self.object1.left = 400
            self.object1.centerY = random.randint(0, 400)
            

#Game manager
class game_manager():
    def __init__(self, state):
        self.state = state

    #managing states
    def management(self):
        if self.state == 'start':
            Start.object.visible = True

            Player.object.visible = False
            Player.hud.visible = False
            Rocks.object1.visible = False
            Rocks.object1.centerX = 400
            Rocks.object1.centerY = random.randint(0, 400)

            Game_Over.object.visible = False
            return 'start'
        
        elif self.state == 'game':
            Start.object.visible = False
            Player.object.visible = True
            Player.hud.visible = True
            Rocks.object1.visible = True

            Game_Over.object.visible = False
            return 'game'
        
        elif self.state == 'game over':
            Game_Over.object.visible = True
            Start.object.visible = False

            Player.object.visible = False
            Player.hud.visible = False
            Rocks.object1.visible = False
            Rocks.object1.centerX = 400
            Rocks.object1.centerY = random.randint(0, 400)
            return 'game over'
    
    #Quickly change game states, testing purposes only
    def changing_state(self, key):
        if self.state == 'start':
            if key == 'space':
                self.state = 'game'
            elif key == 'd':
                self.state = 'game over'

        elif self.state == 'game':
            if key == 'r':
                self.state = 'start'
            elif key == 'd':
                self.state = 'game over'
        
        elif self.state == 'game over':
            if key == 'r':
                self.state = 'game'
            elif key == 'space':
                self.state = 'start'
        




#Running code with inbuilt functions
def onKeyPress(key):
    Game_Manager.changing_state(key)
    if Game_Manager.management() == 'start':
        Start.key_press(key)
    
    if Game_Manager.management() == 'game':
        Player.key_press(key)



def onKeyHold(keys):
    if Game_Manager.management() == 'game':
        Player.key_holds(keys)

def onStep():
    Game_Manager.management()
    if Game_Manager.management() == 'game':
        Rocks.move()

#Defining classes
Game_Manager = game_manager('game')
Start = start(200, 200)
Game_Over = game_over(200, 200)
Player = player(100, 100, 2, 3)
Rocks = rocks(random.randint(0, 400), random.randint(25, 50), 1, 0.5)


cmu_graphics.run()