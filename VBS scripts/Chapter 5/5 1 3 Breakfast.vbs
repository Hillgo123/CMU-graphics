set wShell = createObject("wscript.shell")
WScript.sleep(3000)
wShell.sendKeys("# table{ENTER}Rect{(}0, 0, 400, 400, fill=gradient{(}'peru', 'sienna', start='left-top'{)}{)}{ENTER}{ENTER}{ENTER}{BS}def drawBasicBreakfast{(}{)}:{ENTER}# plate{ENTER}Circle{(}200, 220, 150, fill='white'{)}{ENTER}{ENTER}# pancake{ENTER}Circle{(}170, 220, 100, fill='wheat', border='burlyWood'{)}{ENTER}Rect{(}140, 210, 30, 30, fill='yellow'{)}{ENTER}{ENTER}# fruit{ENTER}Circle{(}230, 320, 70, fill='orange'{)}{ENTER}Circle{(}230, 320, 62, fill='lightCoral', border='antiqueWhite', borderWidth=5{)}{ENTER}Star{(}230, 320, 55, 12, fill='antiqueWhite', roundness=0{)}{ENTER}{ENTER}{ENTER}{BS}def drawOrangeJuice{(}{)}:{ENTER}Circle{(}350, 70, 50, fill=gradient{(}'gold', 'orange'{)}, border='white',borderWidth=4{)}{ENTER}{ENTER}{ENTER}{BS}def drawCoffee{(}{)}:{ENTER}Oval{(}85, 65, 50, 20, fill='white'{)}{ENTER}Circle{(}20, 70, 55, fill=rgb{(}112, 73, 60{)}, border='white', borderWidth=10{)}{ENTER}{ENTER}{ENTER}{BS}def drawEggs{(}{)}:{ENTER}Oval{(}265, 160, 110, 100, fill='white', border='lightGrey', rotateAngle=20{)}{ENTER}Circle{(}250, 150, 20, fill='gold'{)}{ENTER}Oval{(}285, 220, 110, 90, fill='white', border='lightGrey', rotateAngle=20{)}{ENTER}Circle{(}300, 220, 20, fill='gold'{)}{ENTER}{ENTER}{ENTER}{BS}def drawSausage{(}{)}:{ENTER}Oval{(}140, 135, 100, 40, fill='maroon', rotateAngle=350{)}{ENTER}Oval{(}190, 130, 100, 40, fill='brown', rotateAngle=320{)}{ENTER}{ENTER}{ENTER}{BS}def drawBreakfast{(}isThirsty, isTired, isVegan, isVegetarian{)}:{ENTER}drawBasicBreakfast{(}{)}{ENTER}{ENTER}if {(}isThirsty{)}:{ENTER}drawOrangeJuice{(}{)}{ENTER}{BS}if {(}isTired{)}:{ENTER}drawCoffee{(}{)}{ENTER}{ENTER}{ENTER}{BS}if not {(}isVegan{)}:{ENTER}drawEggs{(}{)}{ENTER}if not {(}isVegetarian{)}:{ENTER}drawSausage{(}{)}")