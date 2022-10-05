#Copy code thats supposed to be converted into a vbs file in the 'code.txt' file

#In case the code contains anything where they split one line into two lines, see example
#Polygon(390, 65, 325, 95, 340, 110, 360, 105, 355, 125, 370, 130,
        # fill='floralWhite', border='black')
#make it into one line of code
# Polygon(390, 65, 325, 95, 340, 110, 360, 105, 355, 125, 370, 130,fill='floralWhite', border='black')

with open('vbs_creator/code.txt', 'r') as file:
    code = file.read().replace('(','{(}').replace(')', '{)}').replace('+', '{+}').replace('  ', '').replace('\n', '{ENTER}').replace('elif', '{BS}elif').replace('else', '{BS}else').replace('while', '{BS}while').replace('for ', '{BS}for').replace('def', '{ENTER}{BS}def').replace('from cmu_graphics import *', '').replace('cmu_graphics.run()', '').replace('/', '{/}').replace('..','  ')
    code = 'set wShell = createObject("wscript.shell")\nWScript.sleep(3000)\nwShell.sendKeys("{}")'.format(code)
    
with open('vbs_creator/code.txt', 'w') as file:
    file.write(code)
    
#Occasionally the code will somehow get messed up and add extra ')' at the end of the code. If this happens add {RIGHT}{BS} for each extra ')'

#Copy the code into a new file or rename it to {filename}.vbs
