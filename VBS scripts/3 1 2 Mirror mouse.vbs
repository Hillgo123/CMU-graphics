set wShell = createObject("wscript.shell") 
WScript.sleep(3000)
wShell.sendKeys("def onMouseMove{(}mouseX, mouseY{)}:{ENTER}dot1.centerX = mouseX{ENTER}dot1.centerY = mouseY{ENTER}{ENTER}dot2.centerX = 400 - mouseX{ENTER}dot2.centerY = mouseY{ENTER}{ENTER}dot3.centerX = mouseX{ENTER}dot3.centerY = 400 - mouseY{ENTER}{ENTER}dot4.centerX = 400 - mouseX{ENTER}dot4.centerY = 400 - mouseY{ENTER}")