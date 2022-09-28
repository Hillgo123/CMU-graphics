set wShell = createObject("wscript.shell") 
WScript.sleep(3000)
wShell.sendKeys("if mouseY < 125:{ENTER}drawFlower{(}mouseX, mouseY{)}{ENTER}{BS}elif mouseY > 275:{ENTER}drawFlower{(}mouseX, mouseY{)}")