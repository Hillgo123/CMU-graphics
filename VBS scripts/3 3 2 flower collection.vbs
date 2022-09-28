set wShell = createObject("wscript.shell") 
WScript.sleep(3000) 
wShell.sendKeys("if mouseY <= 200:{ENTER}drawFlower{(}mouseX, mouseY{)}{ENTER}{BS}else:{ENTER}drawLeaf{(}mouseX, mouseY{)}")