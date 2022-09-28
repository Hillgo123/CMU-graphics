set wShell = createObject("wscript.shell") 
WScript.sleep(3000) 
wShell.sendKeys("{ENTER}{ENTER}drawEye{(}centerX-25, centerY-55{)}{ENTER}drawEye{(}centerX{+}20, centerY-55{)}{ENTER}{ENTER}drawFeet{(}centerX, centerY{+}40, color{)}{ENTER}Label{(}name, centerX, centerY{+}70, fill='white', font='monospace', size=25{)}")