set wShell = createObject("wscript.shell") 
WScript.sleep(3000) 
wShell("Line{(}0, 0, 400 - mouseX, 400 - mouseY, fill=gradient{(}'black', 'lime'{)}{)}{ENTER}{ENTER}Line{(}0, 400, 400- mouseX, 400  - mouseY, fill=gradient{(}'black', 'lime'{)}{)}{ENTER}Line{(}400, 0, 400 - mouseX, 400  - mouseY, fill=gradient{(}'black', 'lime'{)}{)}{ENTER}Line{(}400, 400, 400 - mouseX, 400  - mouseY, fill=gradient{(}'black', 'lime'{)}{)}{ENTER}Circle{(}400 - mouseX, 400  - mouseY, 5, fill='lime'{)}")
