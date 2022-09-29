#Copy code thats supposed to be converted into a vbs file in the 'code.txt' file

#Make sure to add {BS} at the end of if, elif and else statements and also at the end of functions, while and for loops

#In case the code contains anything where they split one line into two lines, see example
#Polygon(390, 65, 325, 95, 340, 110, 360, 105, 355, 125, 370, 130,
        # fill='floralWhite', border='black')
#make it into one line of code
# Polygon(390, 65, 325, 95, 340, 110, 360, 105, 355, 125, 370, 130,fill='floralWhite', border='black')

with open('vbs_creator/code.txt', 'r') as file:
    code = file.read().replace('(','{(}').replace(')', '{)}').replace('+', '{+}').replace('  ', '').replace('\n', '{ENTER}')

with open('vbs_creator/code.txt', 'w') as file:
    file.write('set wShell = createObject("wscript.shell")\nWScript.sleep(3000)\nwShell.sendKeys("')
    file.write(code)
    file.write('")')

#Occasionally the code will somehow get messed up and add extre ')' at the end of the code. If this happens add {RIGHT}{BS} for each extre ')'

#Copy the code into a new file or rename it to {filename}.vbs