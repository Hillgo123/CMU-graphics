set wShell = createObject("wscript.shell")
WScript.sleep(3000)
wShell.sendKeys("app.background = 'mediumAquamarine'{ENTER}{ENTER}# apple{ENTER}Oval{(}215, 70, 50, 20, fill='forestGreen', rotateAngle=-45{)}{ENTER}Oval{(}175, 145, 100, 150, fill='fireBrick', rotateAngle=-15{)}{ENTER}Oval{(}225, 145, 100, 150, fill='fireBrick', rotateAngle=15{)}{ENTER}Oval{(}150, 140, 40, 100, fill='white', rotateAngle=-10{)}{ENTER}Oval{(}155, 140, 40, 100, fill='fireBrick', rotateAngle=-10{)}{ENTER}{ENTER}# worm{ENTER}Circle{(}260, 140, 30, fill='mediumAquamarine'{)}{ENTER}Oval{(}235, 140, 10, 20, fill='mediumSeaGreen'{)}{ENTER}Oval{(}245, 145, 10, 20, fill='lightGreen', rotateAngle=-10{)}{ENTER}Oval{(}255, 140, 10, 20, fill='mediumSeaGreen', rotateAngle=10{)}{ENTER}Oval{(}265, 145, 10, 20, fill='lightGreen', rotateAngle=-10{)}{ENTER}Oval{(}275, 140, 10, 20, fill='mediumSeaGreen', rotateAngle=-20{)}{ENTER}Line{(}285, 125, 280, 115, fill='paleGoldenrod'{)}{ENTER}Line{(}280, 115, 275, 120, fill='paleGoldenrod'{)}{ENTER}Line{(}295, 125, 300, 115, fill='paleGoldenrod'{)}{ENTER}Line{(}300, 115, 305, 120, fill='paleGoldenrod'{)}{ENTER}Circle{(}290, 130, 10, fill='forestGreen'{)}{ENTER}Circle{(}285, 125, 2{)}{ENTER}Circle{(}295, 125, 2{)}{ENTER}Circle{(}290, 133, 3, fill=None, border='black'{)}{ENTER}{ENTER}cursor = Label{(}'|', 20, 260, fill='white', size=40{)}{ENTER}{ENTER}{ENTER}{BS}def onKeyPress{(}key{)}:{ENTER}if {(}key != 'space'{)}:{ENTER}Label{(}key, cursor.centerX, cursor.centerY, fill='white', size=40{)}{ENTER}{ENTER}{BS}if {(}cursor.centerX < 380{)}:{ENTER}cursor.centerX {+}= 30{ENTER}{ENTER}{BS}else:{ENTER}cursor.centerX = 20{ENTER}cursor.centerY {+}= 40")