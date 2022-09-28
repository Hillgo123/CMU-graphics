from cmu_graphics import *


app.stepsPerSecond = 60

app.a1 = 0
app.a2 = -5
app.a3 = -10
app.a4 = -15
app.a5 = -20

c5 = Circle(200, 50, 20, fill="gainsboro")
c4 = Circle(200, 50, 25, fill="lightGrey")
c3 = Circle(200, 50, 30, fill="silver")
c2 = Circle(200, 50, 35, fill="darkGrey")
c1 = Circle(200, 50, 40, fill="grey")

def onStep():
    app.a1 += 2
    app.a2 += 2
    app.a3 += 2
    app.a4 += 2
    app.a5 += 2
    x1 = getPointInDir(200, 200, app.a1, 150)
    x2 = getPointInDir(200, 200, app.a2, 150)
    x3 = getPointInDir(200, 200, app.a3, 150)
    x4 = getPointInDir(200, 200, app.a4, 150)
    x5 = getPointInDir(200, 200, app.a5, 150)
    c1.centerX = x1[0]
    c1.centerY = x1[1]
    c2.centerX = x2[0]
    c2.centerY = x2[1]
    c3.centerX = x3[0]
    c3.centerY = x3[1]
    c4.centerX = x4[0]
    c4.centerY = x4[1]
    c5.centerX = x5[0]
    c5.centerY = x5[1]


    




cmu_graphics.run()