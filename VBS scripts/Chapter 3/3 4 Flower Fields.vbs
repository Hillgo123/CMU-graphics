set wShell = createObject("wscript.shell") 
WScript.sleep(3000)
wShell.sendKeys("# water{ENTER}Rect{(}0, 125, 400, 150, fill='cornflowerBlue'{)}{ENTER}{ENTER}# grass and bushes{ENTER}Rect{(}0, 0, 400, 125, fill='lawnGreen'{)}{ENTER}Rect{(}0, 275, 400, 125, fill='lawnGreen'{)}{ENTER}Oval{(}170, 0, 400, 120, fill='greenYellow'{)}{ENTER}Oval{(}330, -10, 300, 190, fill='springGreen'{)}{ENTER}Oval{(}40, 400, 380, 130, fill='paleGreen'{)}{ENTER}Oval{(}310, 410, 280, 190, fill='springGreen'{)}{ENTER}{ENTER}def drawFlower{(}x, y{)}:{ENTER}Oval{(}x, y, 15, 30, fill='dodgerBlue'{)}{ENTER}Oval{(}x, y, 15, 30, fill='dodgerBlue', rotateAngle=60{)}{ENTER}Oval{(}x, y, 15, 30, fill='dodgerBlue', rotateAngle=120{)}{ENTER}Circle{(}x, y, 5, fill='yellow'{)}{ENTER}{BS}{ENTER}{ENTER}def onMousePress{(}mouseX, mouseY{)}:{ENTER}{ENTER}if mouseY < 125:{ENTER}drawFlower{(}mouseX, mouseY{)}{ENTER}{BS}{ENTER}elif mouseY > 275:{ENTER}drawFlower{(}mouseX, mouseY{)}{ENTER}")