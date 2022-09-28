set wShell = createObject("wscript.shell") 
WScript.sleep(3000) 
wShell.sendKeys("if foodPile.height <= 30:{ENTER}foodPile.width {+}= 5{ENTER}foodPile.height {+}= 2{ENTER}foodPile.centerY = 325 - foodPile.height/2{ENTER}if foodPile.height >= 30:{ENTER}message.value = 'meow'{ENTER}leftTear.centerY = 1000{ENTER}rightTear.centerY = 1000{ENTER}") 