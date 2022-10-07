from cmu_graphics import *
import random

#Intitiating program
app.background = fill='lightBlue'
app.stepsPerSecond = 60



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


class game_over():
    #Initiating class
    def __init__(self, x, y):
        self.score = Label('', 150, 125, size = 20)
        self.object = Group(
            Rect(0, 0, 300, 200, fill=None, borderWidth=10, border='black'),
            Label('Game Over', 150, 75, size = 25),
            self.score
        )
        self.object.centerX = x
        self.object.centerY = y
        self.object.visible = False

    #Used to get the score from the end of the game
    def game_end(self):
        self.score.value = 'Your score: {}'.format(Player.score_func())
    
    #Game over on step functions
    def constants(self):
        self.game_end()


class player():
    #Initiating class
    def __init__(self, x, y, sp, hp, ammo):
        self.object = Group(
            Rect(x, y, 25, 20),
            Circle(x + 25, y + 10, 10)
        )
        self.speed = sp
        self.object.visible = False
        self.hp = hp
        self.score = 0
        self.hud = Label(self.score_func(), 200, 10)
        self.hud.visible = False

        self.ammo = ammo
        self.bullet_speed = sp * 2
        self.bullet = Rect(0, 0, 10, 10, fill='red', visible = False)

    #Moving Player
    def move(self, keys):
        if 'up' in keys and self.object.top > 0:
            self.object.centerY -= 1 * self.speed
        elif 'down' in keys and self.object.bottom < 400:
            self.object.centerY += 1 * self.speed

    #Checks collision
    def collision(self):
        if self.object.hitsShape(Rocks.rocks_group):
            self.hp -= 1

        if  self.hp == 0:
            Game_Manager.state = 'game over'

    #Shooting
    def shoot(self, key):
        if key == 'space' and not self.ammo == 0:
            self.bullet.centerX = self.object.centerX
            self.bullet.centerY = self.object.centerY
            self.bullet.visible = True
            self.ammo -= 1
    
    #Moves bullet
    def update_bullet(self):
        self.bullet.centerX += 1 * self.bullet_speed
        if self.bullet.left > 400:
            self.ammo = 1

    #Restart function
    def restart(self):
        self.hp = 3
        self.score = 0
    
    #Get score
    def score_func(self):
        return self.score
        
    #Player key press functions
    def key_press(self, key):
        self.shoot(key)

    #Player on step functions
    def constants(self):
        self.update_bullet()
        self.collision()
        self.hud.value = self.score
        self.score_func()
        

    #player on key hold functions
    def key_holds(self, keys):
        self.move(keys)


class rocks():
    #Initiating class
    def __init__(self, sp):
        self.object1 = Circle(430, 300, 10, fill='gray', borderWidth=1)
        self.object2 = Circle(450, 100, 10, fill='gray', borderWidth=1)
        self.object3 = Circle(400, 180, 10, fill='gray', borderWidth=1)
        self.object4 = Circle(400, 360, 10, fill='gray', borderWidth=1)
        self.object5 = Circle(400, 20, 10, fill='gray', borderWidth=1)
        self.rocks_group = Group(self.object1, self.object2, self.object3, self.object4, self.object5)
        self.rocks_list = [self.object1, self.object2, self.object3, self.object4, self.object5] #Creates a list to easily reshape each object
        self.speed = sp
        self.rocks_group.visible = False

    #Restart function
    def restart(self, object):
        object.left = 400
        object.centerY = random.randint(0, 400)
        object.height = random.randint(25, 100)

    def reset_speed(self):
        self.speed = 3
    
    #Fixes dimensions of rocks
    def fix_dims(self, object):
        object.width = object.height

    #Movement
    def move(self):
        for n in range(0, 5):
            self.rocks_list[n].centerX -= 1 * self.speed
            self.fix_dims(self.rocks_list[n])
            #Update score
            if self.rocks_list[n].right < 0:
                self.restart(self.rocks_list[n])
                Player.score += 1
            
            #Accelarate based on player score
            if Player.score == 25:
                self.speed = 4
            
            if Player.score == 50:
                self.speed = 5

            if Player.score == 75:
                self.speed = 6

            if Player.score == 100:
                self.speed = 7
                

    #Collision
    def collision(self):
        for n in range(0, 5):
            if self.rocks_list[n].hitsShape(Player.bullet):
                self.restart(self.rocks_list[n])
                Player.score += 1
                Player.bullet.centerX = 500
    
    #Rock on step functions
    def constants(self):
        self.move()
        self.collision()
            

class game_manager():
    #Initiate class
    def __init__(self, state):
        self.state = state

    #managing states
    def management(self):
        if self.state == 'start':
            Start.object.visible = True

            Player.object.visible = False
            Player.hud.visible = False
            Player.bullet.visible = False
            Rocks.rocks_group.visible = False
            Rocks.restart(Rocks.rocks_group)
            Rocks.reset_speed()
            Player.restart()

            Game_Over.object.visible = False
            return 'start'
        
        elif self.state == 'game':
            Start.object.visible = False
            Player.object.visible = True
            Player.hud.visible = True
            Player.bullet.visible = True
            Rocks.rocks_group.visible = True

            Game_Over.object.visible = False
            return 'game'
        
        elif self.state == 'game over':
            Game_Over.object.visible = True
            Start.object.visible = False

            Player.object.visible = False
            Player.hud.visible = False
            Player.bullet.visible = False
            Rocks.rocks_group.visible = False
            return 'game over'
    
    #Quickly change game states, testing purposes only
    def changing_state(self, key):
        if self.state == 'start':
            if key == 'space':
                Rocks.restart(Rocks.rocks_group)
                self.state = 'game'
            elif key == 'd':
                Rocks.restart(Rocks.rocks_group)
                self.state = 'game over'

        elif self.state == 'game':
            if key == 'r':
                Rocks.restart(Rocks.rocks_group)
                self.state = 'start'
            elif key == 'd':
                Rocks.restart(Rocks.rocks_group)
                self.state = 'game over'
        
        elif self.state == 'game over':
            if key == 'r':
                Rocks.restart(Rocks.rocks_group)
                self.state = 'game'
            elif key == 'space':
                Rocks.restart(Rocks.rocks_group)
                self.state = 'start'


#Running code with inbuilt functions
def onKeyPress(key):
    Game_Manager.changing_state(key)
    if Game_Manager.management() == 'game':
        Player.key_press(key)

def onKeyHold(keys):
    if Game_Manager.management() == 'game':
        Player.key_holds(keys)

def onStep():
    Game_Manager.management()
    if Game_Manager.management() == 'game':
        Rocks.constants()
        Player.constants()
    
    if Game_Manager.management() == 'game over':
        Game_Over.constants()
    

#Defining classes
Game_Manager = game_manager('start')
Start = start(200, 200)
Player = player(100, 100, 3, 3, 1)
Game_Over = game_over(200, 200)
Rocks = rocks(3)

cmu_graphics.run()