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

grid = Group(top_left, top_center, top_right, left, right, center, bottom_left, bottom_center, bottom_right, visible = False)


#Cross
cross1 = Group(Rect(50, 50, 100, 20, fill='blue', rotateAngle=45),
        Rect(50, 50, 100, 20, fill='blue', rotateAngle=-45), visible = False)
cross2 = Group(Rect(50, 50, 100, 20, fill='blue', rotateAngle=45),
        Rect(50, 50, 100, 20, fill='blue', rotateAngle=-45), visible = False)
cross3 = Group(Rect(50, 50, 100, 20, fill='blue', rotateAngle=45),
        Rect(50, 50, 100, 20, fill='blue', rotateAngle=-45), visible = False)

#Circle
circle1 = Circle(50, 50, 40, fill=None, visible = False, border='green', borderWidth=10)
circle2 = Circle(50, 50, 40, fill=None, visible = False, border='green', borderWidth=10)
circle3 = Circle(50, 50, 40, fill=None, visible = False, border='green', borderWidth=10)

start_screen = Group(Label('Press To Start', 200, 200, size = 40), 
        Rect(50, 100, 300, 200, fill = None, border='black', borderWidth=10))

#Game States
app.start = True
app.game = False
app.win = False
    
def onMousePress(mouseX, mouseY):

    while app.start == True:
        if start_screen.contains(mouseX, mouseY):
            start_screen.visible = False
            app.start = False
            app.game = True


    #Moving cross
    while app.game == True:
        #Cross 1
        if app.turn == 'cross1':
            app.grid_array[app.grid_array == 'x1'] = 'empty'

            #Top Row
            if top_left.contains(mouseX, mouseY) and app.grid_array[0, 0] == 'empty':
                cross1.visible = True
                cross1.centerX = top_left.centerX
                cross1.centerY = top_left.centerY

                app.turn = 'circle1'
                app.grid_array[0, 0] = 'x1'

            elif top_center.contains(mouseX, mouseY) and app.grid_array[0, 1] == 'empty':
                cross1.visible = True
                cross1.centerX = top_center.centerX
                cross1.centerY = top_center.centerY

                app.turn = 'circle1'
                app.grid_array[0, 1] = 'x1'


            elif top_right.contains(mouseX, mouseY) and app.grid_array[0, 2] == 'empty':
                cross1.visible = True
                cross1.centerX = top_right.centerX
                cross1.centerY = top_right.centerY

                app.turn = 'circle1'
                app.grid_array[0, 2] = 'x1'

            #Center Row
            if left.contains(mouseX, mouseY) and app.grid_array[1, 0] == 'empty':
                cross1.visible = True
                cross1.centerX = left.centerX
                cross1.centerY = left.centerY

                app.turn = 'circle1'
                app.grid_array[1, 0] = 'x1'

            elif center.contains(mouseX, mouseY) and app.grid_array[1, 1] == 'empty':
                cross1.visible = True
                cross1.centerX = center.centerX
                cross1.centerY = center.centerY

                app.turn = 'circle1'
                app.grid_array[1, 1] = 'x1'


            elif right.contains(mouseX, mouseY) and app.grid_array[1, 2] == 'empty':
                cross1.visible = True
                cross1.centerX = right.centerX
                cross1.centerY = right.centerY

                app.turn = 'circle1'
                app.grid_array[1, 2] = 'x1'

            #Bottom Row
            if bottom_left.contains(mouseX, mouseY) and app.grid_array[2, 0] == 'empty':
                cross1.visible = True
                cross1.centerX = bottom_left.centerX
                cross1.centerY = bottom_left.centerY

                app.turn = 'circle1'
                app.grid_array[2, 0] = 'x1'

            elif bottom_center.contains(mouseX, mouseY) and app.grid_array[2, 1] == 'empty':
                cross1.visible = True
                cross1.centerX = bottom_center.centerX
                cross1.centerY = bottom_center.centerY

                app.turn = 'circle1'
                app.grid_array[2, 1] = 'x1'


            elif bottom_right.contains(mouseX, mouseY) and app.grid_array[2, 2] == 'empty':
                cross1.visible = True
                cross1.centerX = bottom_right.centerX
                cross1.centerY = bottom_right.centerY

                app.turn = 'circle1'
                app.grid_array[2, 2] = 'x1'
                
        #Cross2
        elif app.turn == 'cross2':
            app.grid_array[app.grid_array == 'x2'] = 'empty'

            #Top Row
            if top_left.contains(mouseX, mouseY) and app.grid_array[0, 0] == 'empty':
                cross2.visible = True
                cross2.centerX = top_left.centerX
                cross2.centerY = top_left.centerY

                app.turn = 'circle2'
                app.grid_array[0, 0] = 'x2'

            elif top_center.contains(mouseX, mouseY) and app.grid_array[0, 1] == 'empty':
                cross2.visible = True
                cross2.centerX = top_center.centerX
                cross2.centerY = top_center.centerY

                app.turn = 'circle2'
                app.grid_array[0, 1] = 'x2'


            elif top_right.contains(mouseX, mouseY) and app.grid_array[0, 2] == 'empty':
                cross2.visible = True
                cross2.centerX = top_right.centerX
                cross2.centerY = top_right.centerY

                app.turn = 'circle2'
                app.grid_array[0, 2] = 'x2'

            #Center Row
            if left.contains(mouseX, mouseY) and app.grid_array[1, 0] == 'empty':
                cross2.visible = True
                cross2.centerX = left.centerX
                cross2.centerY = left.centerY

                app.turn = 'circle2'
                app.grid_array[1, 0] = 'x2'

            elif center.contains(mouseX, mouseY) and app.grid_array[1, 1] == 'empty':
                cross2.visible = True
                cross2.centerX = center.centerX
                cross2.centerY = center.centerY

                app.turn = 'circle2'
                app.grid_array[1, 1] = 'x2'


            elif right.contains(mouseX, mouseY) and app.grid_array[1, 2] == 'empty':
                cross2.visible = True
                cross2.centerX = right.centerX
                cross2.centerY = right.centerY

                app.turn = 'circle2'
                app.grid_array[1, 2] = 'x2'

            #Bottom Row
            if bottom_left.contains(mouseX, mouseY) and app.grid_array[2, 0] == 'empty':
                cross2.visible = True
                cross2.centerX = bottom_left.centerX
                cross2.centerY = bottom_left.centerY

                app.turn = 'circle2'
                app.grid_array[2, 0] = 'x2'

            elif bottom_center.contains(mouseX, mouseY) and app.grid_array[2, 1] == 'empty':
                cross2.visible = True
                cross2.centerX = bottom_center.centerX
                cross2.centerY = bottom_center.centerY

                app.turn = 'circle2'
                app.grid_array[2, 1] = 'x2'


            elif bottom_right.contains(mouseX, mouseY) and app.grid_array[2, 2] == 'empty':
                cross2.visible = True
                cross2.centerX = bottom_right.centerX
                cross2.centerY = bottom_right.centerY

                app.turn = 'circle2'
                app.grid_array[2, 2] = 'x2'

        #Cross 3
        elif app.turn == 'cross3':
            app.grid_array[app.grid_array == 'x3'] = 'empty'

            #Top Row
            if top_left.contains(mouseX, mouseY) and app.grid_array[0, 0] == 'empty':
                cross3.visible = True
                cross3.centerX = top_left.centerX
                cross3.centerY = top_left.centerY

                app.turn = 'circle3'
                app.grid_array[0, 0] = 'x3'

            elif top_center.contains(mouseX, mouseY) and app.grid_array[0, 1] == 'empty':
                cross3.visible = True
                cross3.centerX = top_center.centerX
                cross3.centerY = top_center.centerY

                app.turn = 'circle3'
                app.grid_array[0, 1] = 'x3'


            elif top_right.contains(mouseX, mouseY) and app.grid_array[0, 2] == 'empty':
                cross3.visible = True
                cross3.centerX = top_right.centerX
                cross3.centerY = top_right.centerY

                app.turn = 'circle3'
                app.grid_array[0, 2] = 'x3'

            #Center Row
            if left.contains(mouseX, mouseY) and app.grid_array[1, 0] == 'empty':
                cross3.visible = True
                cross3.centerX = left.centerX
                cross3.centerY = left.centerY

                app.turn = 'circle3'
                app.grid_array[1, 0] = 'x3'

            elif center.contains(mouseX, mouseY) and app.grid_array[1, 1] == 'empty':
                cross3.visible = True
                cross3.centerX = center.centerX
                cross3.centerY = center.centerY

                app.turn = 'circle3'
                app.grid_array[1, 1] = 'x3'


            elif right.contains(mouseX, mouseY) and app.grid_array[1, 2] == 'empty':
                cross3.visible = True
                cross3.centerX = right.centerX
                cross3.centerY = right.centerY

                app.turn = 'circle3'
                app.grid_array[1, 2] = 'x3'

            #Bottom Row
            if bottom_left.contains(mouseX, mouseY) and app.grid_array[2, 0] == 'empty':
                cross3.visible = True
                cross3.centerX = bottom_left.centerX
                cross3.centerY = bottom_left.centerY

                app.turn = 'circle3'
                app.grid_array[2, 0] = 'x3'

            elif bottom_center.contains(mouseX, mouseY) and app.grid_array[2, 1] == 'empty':
                cross3.visible = True
                cross3.centerX = bottom_center.centerX
                cross3.centerY = bottom_center.centerY

                app.turn = 'circle3'
                app.grid_array[2, 1] = 'x3'


            elif bottom_right.contains(mouseX, mouseY) and app.grid_array[2, 2] == 'empty':
                cross3.visible = True
                cross3.centerX = bottom_right.centerX
                cross3.centerY = bottom_right.centerY

                app.turn = 'circle3'
                app.grid_array[2, 2] = 'x3'

        #Moving Circle
        #Circle 1
        elif app.turn == 'circle1':
            app.grid_array[app.grid_array == 'o1'] = 'empty'

            #Top Row
            if top_left.contains(mouseX, mouseY) and app.grid_array[0, 0] == 'empty':
                circle1.visible = True
                circle1.centerX = top_left.centerX
                circle1.centerY = top_left.centerY

                app.turn = 'cross2'
                app.grid_array[0, 0] = 'o1'

            elif top_center.contains(mouseX, mouseY) and app.grid_array[0, 1] == 'empty':
                circle1.visible = True
                circle1.centerX = top_center.centerX
                circle1.centerY = top_center.centerY

                app.turn = 'cross2'
                app.grid_array[0, 1] = 'o1'


            elif top_right.contains(mouseX, mouseY) and app.grid_array[0, 2] == 'empty':
                circle1.visible = True
                circle1.centerX = top_right.centerX
                circle1.centerY = top_right.centerY

                app.turn = 'cross2'
                app.grid_array[0, 2] = 'o1'

            #Center Row
            if left.contains(mouseX, mouseY) and app.grid_array[1, 0] == 'empty':
                circle1.visible = True
                circle1.centerX = left.centerX
                circle1.centerY = left.centerY

                app.turn = 'cross2'
                app.grid_array[1, 0] = 'o1'

            elif center.contains(mouseX, mouseY) and app.grid_array[1, 1] == 'empty':
                circle1.visible = True
                circle1.centerX = center.centerX
                circle1.centerY = center.centerY

                app.turn = 'cross2'
                app.grid_array[1, 1] = 'o1'


            elif right.contains(mouseX, mouseY) and app.grid_array[1, 2] == 'empty':
                circle1.visible = True
                circle1.centerX = right.centerX
                circle1.centerY = right.centerY

                app.turn = 'cross2'
                app.grid_array[1, 2] = 'o1'

            #Bottom Row
            if bottom_left.contains(mouseX, mouseY) and app.grid_array[2, 0] == 'empty':
                circle1.visible = True
                circle1.centerX = bottom_left.centerX
                circle1.centerY = bottom_left.centerY

                app.turn = 'cross2bottom_'
                app.grid_array[2, 0] = 'o1'

            elif bottom_center.contains(mouseX, mouseY) and app.grid_array[2, 1] == 'empty':
                circle1.visible = True
                circle1.centerX = bottom_center.centerX
                circle1.centerY = bottom_center.centerY

                app.turn = 'cross2'
                app.grid_array[2, 1] = 'o1'


            elif bottom_right.contains(mouseX, mouseY) and app.grid_array[2, 2] == 'empty':
                circle1.visible = True
                circle1.centerX = bottom_right.centerX
                circle1.centerY = bottom_right.centerY

                app.turn = 'cross2'
                app.grid_array[2, 2] = 'o1'

        #Circle 2
        elif app.turn == 'circle2':
            app.grid_array[app.grid_array == 'o2'] = 'empty'

            #Top Row
            if top_left.contains(mouseX, mouseY) and app.grid_array[0, 0] == 'empty':
                circle2.visible = True
                circle2.centerX = top_left.centerX
                circle2.centerY = top_left.centerY

                app.turn = 'cross3'
                app.grid_array[0, 0] = 'o2'

            elif top_center.contains(mouseX, mouseY) and app.grid_array[0, 1] == 'empty':
                circle2.visible = True
                circle2.centerX = top_center.centerX
                circle2.centerY = top_center.centerY

                app.turn = 'cross3'
                app.grid_array[0, 1] = 'o2'


            elif top_right.contains(mouseX, mouseY) and app.grid_array[0, 2] == 'empty':
                circle2.visible = True
                circle2.centerX = top_right.centerX
                circle2.centerY = top_right.centerY

                app.turn = 'cross3'
                app.grid_array[0, 2] = 'o2'

            #Center Row
            if left.contains(mouseX, mouseY) and app.grid_array[1, 0] == 'empty':
                circle2.visible = True
                circle2.centerX = left.centerX
                circle2.centerY = left.centerY

                app.turn = 'cross3'
                app.grid_array[1, 0] = 'o2'

            elif center.contains(mouseX, mouseY) and app.grid_array[1, 1] == 'empty':
                circle2.visible = True
                circle2.centerX = center.centerX
                circle2.centerY = center.centerY

                app.turn = 'cross3'
                app.grid_array[1, 1] = 'o2'


            elif right.contains(mouseX, mouseY) and app.grid_array[1, 2] == 'empty':
                circle2.visible = True
                circle2.centerX = right.centerX
                circle2.centerY = right.centerY

                app.turn = 'cross3'
                app.grid_array[1, 2] = 'o2'

            #Bottom Row
            if bottom_left.contains(mouseX, mouseY) and app.grid_array[2, 0] == 'empty':
                circle2.visible = True
                circle2.centerX = bottom_left.centerX
                circle2.centerY = bottom_left.centerY

                app.turn = 'cross3'
                app.grid_array[2, 0] = 'o2'

            elif bottom_center.contains(mouseX, mouseY) and app.grid_array[2, 1] == 'empty':
                circle2.visible = True
                circle2.centerX = bottom_center.centerX
                circle2.centerY = bottom_center.centerY

                app.turn = 'cross3'
                app.grid_array[2, 1] = 'o2'


            elif bottom_right.contains(mouseX, mouseY) and app.grid_array[2, 2] == 'empty':
                circle2.visible = True
                circle2.centerX = bottom_right.centerX
                circle2.centerY = bottom_right.centerY

                app.turn = 'cross3'
                app.grid_array[2, 2] = 'o2'

        #Circle 3
        elif app.turn == 'circle3':
            app.grid_array[app.grid_array == 'o3'] = 'empty'

            #Top Row
            if top_left.contains(mouseX, mouseY) and app.grid_array[0, 0] == 'empty':
                circle3.visible = True
                circle3.centerX = top_left.centerX
                circle3.centerY = top_left.centerY

                app.turn = 'cross1'
                app.grid_array[0, 0] = 'o3'

            elif top_center.contains(mouseX, mouseY) and app.grid_array[0, 1] == 'empty':
                circle3.visible = True
                circle3.centerX = top_center.centerX
                circle3.centerY = top_center.centerY

                app.turn = 'cross1'
                app.grid_array[0, 1] = 'o3'


            elif top_right.contains(mouseX, mouseY) and app.grid_array[0, 2] == 'empty':
                circle3.visible = True
                circle3.centerX = top_right.centerX
                circle3.centerY = top_right.centerY

                app.turn = 'cross1'
                app.grid_array[0, 2] = 'o3'

            #Center Row
            if left.contains(mouseX, mouseY) and app.grid_array[1, 0] == 'empty':
                circle3.visible = True
                circle3.centerX = left.centerX
                circle3.centerY = left.centerY

                app.turn = 'cross1'
                app.grid_array[1, 0] = 'o3'

            elif center.contains(mouseX, mouseY) and app.grid_array[1, 1] == 'empty':
                circle3.visible = True
                circle3.centerX = center.centerX
                circle3.centerY = center.centerY

                app.turn = 'cross1'
                app.grid_array[1, 1] = 'o3'


            elif right.contains(mouseX, mouseY) and app.grid_array[1, 2] == 'empty':
                circle3.visible = True
                circle3.centerX = right.centerX
                circle3.centerY = right.centerY

                app.turn = 'cross1'
                app.grid_array[1, 2] = 'o3'

            #Bottom Row
            if bottom_left.contains(mouseX, mouseY) and app.grid_array[2, 0] == 'empty':
                circle3.visible = True
                circle3.centerX = bottom_left.centerX
                circle3.centerY = bottom_left.centerY

                app.turn = 'cross1'
                app.grid_array[2, 0] = 'o3'

            elif bottom_center.contains(mouseX, mouseY) and app.grid_array[2, 1] == 'empty':
                circle3.visible = True
                circle3.centerX = bottom_center.centerX
                circle3.centerY = bottom_center.centerY

                app.turn = 'cross1'
                app.grid_array[2, 1] = 'o3'


            elif bottom_right.contains(mouseX, mouseY) and app.grid_array[2, 2] == 'empty':
                circle3.visible = True
                circle3.centerX = bottom_right.centerX
                circle3.centerY = bottom_right.centerY

                app.turn = 'cross1'
                app.grid_array[2, 2] = 'o3'


        print(app.grid_array)
        print('')

    #Check if win
    # if app.grid_array[]



cmu_graphics.run()
