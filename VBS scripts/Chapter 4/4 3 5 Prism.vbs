set wShell = createObject("wscript.shell")
WScript.sleep(3000)
wShell.sendKeys("app.background = 'black'{ENTER}{ENTER}rainbow = Polygon{(}200, 185, 200, 195, 400, 202, 400, 178,fill=gradient{(}'indigo', 'blue', 'green', 'orange', 'red',start='bottom'{)}{)}{ENTER}{ENTER}prism = RegularPolygon{(}200, 200, 120, 3, border='white'{)}{ENTER}{ENTER}beam = Line{(}0, 265, 200, 190,fill=gradient{(}'white', 'lightCyan', 'black', start='left'{)}{)}{ENTER}{ENTER}{ENTER}{BS}def onMousePress{(}mouseX, mouseY{)}:{ENTER}# If you click on the prism, move the y coordinates of the light beam and{ENTER}# the rainbow according to where you click.{ENTER}### Place Your Code Here ###{ENTER}if {(}prism.hits{(}mouseX, mouseY{)} == True{)}:{ENTER}beam.y2 = mouseY{ENTER}rainbow.centerY = mouseY {ENTER}")