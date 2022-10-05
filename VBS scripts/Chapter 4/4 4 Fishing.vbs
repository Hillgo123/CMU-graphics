set wShell = createObject("wscript.shell")
WScript.sleep(3000)
wShell.sendKeys("app.background = gradient{(}'lightSkyBlue', 'orange', start='top'{)}{ENTER}{ENTER}# sun and lake{ENTER}Circle{(}250, 335, 50, fill='gold'{)}{ENTER}Rect{(}0, 300, 400, 100, fill='dodgerBlue'{)}{ENTER}{ENTER}# boat and fishing rod{ENTER}Polygon{(}0, 270, 0, 350, 50, 350, 85, 315, 100, 270, fill='sienna'{)}{ENTER}Line{(}0, 240, 140, 160{)}{ENTER}{ENTER}# fishing line, fish body, and fish tail{ENTER}fishingLine = Line{(}140, 160, 140, 340, lineWidth=1{)}{ENTER}fishBody = Oval{(}340, 340, 50, 30, fill='salmon'{)}{ENTER}fishTail = Polygon{(}350, 340, 380, 350, 380, 330, fill='salmon'{)}{ENTER}{ENTER}{ENTER}{BS}def pullUpFish{(}{)}:{ENTER}fishingLine.x2 = 140{ENTER}fishingLine.y2 = 225{ENTER}fishBody.rotateAngle = 90{ENTER}fishBody.centerX = 140{ENTER}fishBody.centerY = 250{ENTER}fishTail.rotateAngle = 90{ENTER}fishTail.centerX = 140{ENTER}fishTail.top = 255{ENTER}{ENTER}{ENTER}{BS}def onKeyPress{(}key{)}:{ENTER}# Release the fish if the correct key is pressed.{ENTER}### Place Your Code Here ###{ENTER}if key == 'r' and fishBody.centerY < 260: {ENTER}fishBody.centerX = 340{ENTER}fishBody.centerY = 340{ENTER}fishTail.centerX = 370{ENTER}fishTail.centerY = 335{ENTER}fishingLine.y2 = 340{ENTER}fishBody.rotateAngle = 0{ENTER}fishTail.rotateAngle = 0 {ENTER}{ENTER}{ENTER}{BS}{ENTER}{BS}def onMouseDrag{(}mouseX, mouseY{)}:{ENTER}# If fish is very close to boat, pull it up.{ENTER}### {(}HINT: Use a helper function.{)}{ENTER}### Place Your Code Here ###'{ENTER}{ENTER}if fishBody. centerY != 250: {ENTER}if mouseX >= {(}fishBody.centerX - 80{)} and mouseX <= {(}fishBody.centerX {+} 10{)} and mouseY > 300: {ENTER}fishingLine.x2 = mouseX{ENTER}fishingLine.y2 = mouseY{ENTER}fishBody.centerX = fishingLine.x2 {+} 25{ENTER}fishBody.centerY = fishingLine.y2{ENTER}fishTail.centerX = fishingLine.x2 {+} 50{ENTER}fishTail.centerY = fishingLine.y2{ENTER}{ENTER}{ENTER}if fishingLine.x2 <= 140: {ENTER}pullUpFish{(}{)}{ENTER}{BS}{BS}elif fishingLine.x2 != fishBody.centerX - 25: {ENTER}fishingLine.x2 = mouseX{ENTER}fishingLine.y2 = mouseY")