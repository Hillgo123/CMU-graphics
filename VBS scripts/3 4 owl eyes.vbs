set wShell = createObject("wscript.shell") 
WScript.sleep(3000)
wShell.sendKeys("leftEye.centerX = 150 {+} mouseX / 10 - 35/2{ENTER}rightEye.centerX = 250 {+} mouseX / 10 - 35/2{ENTER}{ENTER}rightEye.centerY =  130 {+} mouseY / 10 - 35/2{ENTER}leftEye.centerY =  130 {+} mouseY / 10 - 35/2{ENTER}")