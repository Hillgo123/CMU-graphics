from cmu_graphics import *
import numpy as np

app.background = fill='saddleBrown'
app.stepsPerSecond = 60

app.grid_array = np.full((3, 3), 'empty')
app.turn = 'cross1'


#Grid
top_left = Rect(30, 30, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
top_center = Rect(30 + 340/3, 30, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
top_right = Rect(30 + 680/3, 30, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)

left = Rect(30, 30 + 340/3, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
center = Rect(30 + 340/3, 30 + 340/3, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
right = Rect(30 + 680/3, 30 + 340/3, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)

bottom_left = Rect(30, 30 + 680/3, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
bottom_center = Rect(30 + 340/3, 30 + 680/3, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
bottom_right = Rect(30 + 680/3, 30 + 680/3, 340/3, 340/3, fill=None, border='black', borderWidth=7.5)
print(app.grid_array)


#Cross
cross1 = Rect(50, 50, 100, 20, fill='blue', rotateAngle=45, visible = False)
cross1_ = Rect(50, 50, 100, 20, fill='blue', rotateAngle=-45, visible = False)
cross2 = Rect(50, 50, 100, 20, fill='blue', rotateAngle=45, visible = False)
cross2_ = Rect(50, 50, 100, 20, fill='blue', rotateAngle=-45, visible = False)
cross3 = Rect(50, 50, 100, 20, fill='blue', rotateAngle=45, visible = False)
cross3_ = Rect(50, 50, 100, 20, fill='blue', rotateAngle=-45, visible = False)

#Circle
circle1 = Circle(50, 50, 50, fill=None, visible = False, border='green', borderWidth=10)
circle2 = Circle(50, 50, 50, fill=None, visible = False, border='green', borderWidth=10)
circle3 = Circle(50, 50, 50, fill=None, visible = False, border='green', borderWidth=10)


app.cricle = []
app.cross = []
    
def onMousePress(mouseX, mouseY):

    #Moving cross
    if app.turn == 'cross1':
        # app.cross1 = cross(mouseX, mouseY)
        cross1.visible = True
        cross1_.visible = True
        cross1.centerX = mouseX
        cross1.centerY = mouseY
        cross1_.centerX = mouseX
        cross1_.centerY = mouseY

        app.turn = 'circle1'

    elif app.turn == 'cross2':
        cross2.visible = True
        cross2_.visible = True
        cross2.centerX = mouseX
        cross2.centerY = mouseY
        cross2_.centerX = mouseX
        cross2_.centerY = mouseY

        app.turn = 'circle2'

    elif app.turn == 'cross3':
        cross3.visible = True
        cross3_.visible = True
        cross3.centerX = mouseX
        cross3.centerY = mouseY
        cross3_.centerX = mouseX
        cross3_.centerY = mouseY

        app.turn = 'circle3'


    #Moving Circle
    elif app.turn == 'circle1':
        circle1.visible = True
        circle1.centerX = mouseX
        circle1.centerY = mouseY

        app.turn = 'cross2'

    elif app.turn == 'circle2':
        circle2.visible = True
        circle2.centerX = mouseX
        circle2.centerY = mouseY

        app.turn = 'cross3'

    elif app.turn == 'circle3':
        circle3.visible = True
        circle3.centerX = mouseX
        circle3.centerY = mouseY

        app.turn = 'cross1'






cmu_graphics.run()
