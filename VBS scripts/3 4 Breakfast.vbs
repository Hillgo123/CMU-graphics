set wShell = createObject("wscript.shell") 
WScript.sleep(3000)
wShell.sendKeys("if 400 - mouseY >= mouseX:{ENTER}drawOrangeJuice{(}mouseX, mouseY{)}{ENTER}{BS}else:{ENTER}drawBacon{(}mouseX, mouseY{)}{ENTER}")