set wShell = createObject("wscript.shell")
WScript.sleep(3000)
wShell.sendKeys("app.background = gradient{(}'skyBlue', rgb{(}235, 235, 235{)}, start='top'{)}{ENTER}{ENTER}app.volcanoHasErupted = False{ENTER}{ENTER}lava = Oval{(}200, 120, 90, 20, fill=rgb{(}255, 200, 0{)}, border='peru',borderWidth=4{)}{ENTER}lava.green = 200{ENTER}{ENTER}rock = Polygon{(}0, 400, 0, 380, 50, 340, 70, 300, 125, 225, 140, 180, 153, 120,175, 125, 200, 120, 220, 108, 235, 105, 247, 110, 255, 175, 270,210, 310, 250, 350, 325, 400, 375, 400, 400,fill=gradient{(}'peru', 'sienna', start='top'{)}{)}{ENTER}{ENTER}burst = Polygon{(}100, 0, 310, 0, 260, 30, 245, 60, 240, 110, 235, 105, 220,108, 200, 120, 175, 125, 160, 120, 150, 60, 130, 25,fill=gradient{(}rgb{(}255, 200, 75{)}, rgb{(}235, 10, 20{)}, start='bottom'{)},visible=False{)}{ENTER}{ENTER}{ENTER}{BS}def drawSpill{(}{)}:{ENTER}Polygon{(}153, 120, 175, 125, 165, 195, 145, 260,80, 315, 125, 260, 150, 200, 155, 160,fill=gradient{(}rgb{(}255, 200, 75{)}, rgb{(}235, 10, 20{)}, start='top'{)}{)}{ENTER}Polygon{(}200, 120, 220, 108, 230, 160, 230, 210,240, 240, 310, 345, 245, 280, 215, 225, 210, 160,fill=gradient{(}rgb{(}255, 200, 75{)}, rgb{(}235, 10, 20{)}, start='top'{)}{)}{ENTER}Polygon{(}235, 105, 247, 110, 255, 175, 270, 210,310, 250, 255, 215, 240, 170, 240, 130,fill=gradient{(}rgb{(}255, 200, 75{)}, rgb{(}235, 10, 20{)}, start='top'{)}{)}{ENTER}{ENTER}{ENTER}{BS}def onMousePress{(}mouseX, mouseY{)}: {ENTER}{ENTER}{ENTER}if lava.fill == rgb{(}255, 0, 0{)} and burst.visible == False:{ENTER}drawSpill{(}{)}{ENTER}burst.visible = True{ENTER}app.background = gradient{(}'lightSlateGrey', 'lightGrey', start='top'{)}{ENTER}{BS}elif burst.visible == False: {ENTER}lava.green -= 40{ENTER}lava.fill = rgb{(}255, lava.green, 0{)}")