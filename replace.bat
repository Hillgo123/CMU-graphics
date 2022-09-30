@echo off 
echo INSTRUCTIONS:
echo add ';' to ALL ur line endings
echo ctrl+a, ctlr+c
echo.

set /p name=type file name: 
set /p str=paste ur code: 

set str=%str: + = {+} % 
set str=%str: - = {-} % 
set str=%str: * = {*} % 
set str=%str:(={(}% 
set str=%str:)={)}% 
set str=%str:;={ENTER}%
set str=%str:{ENTER} ={ENTER}%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%
set str=%str: =%

echo set wShell = createObject("wscript.shell") > %name%.vbs
echo WScript.sleep(3000) >> %name%.vbs
echo wShell.sendKeys("%str%") >> %name%.vbs

echo.
echo done! open %name%.vbs, tab to ur web-browser, and wait 3 secs.
echo script doesnt do indents, so add them if necessary (for loops)

pause