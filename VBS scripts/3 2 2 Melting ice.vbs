set wShell = createObject("wscript.shell") 
WScript.sleep(3000)
wShell.sendKeys("if iceCube1.opacity > 0:{ENTER}iceCube1.opacity -= 10{ENTER}iceCube2.opacity -= 10{ENTER}iceCube3.opacity -= 10{ENTER}juice.height {+}= 2{ENTER}juice.top -= 2{ENTER}")