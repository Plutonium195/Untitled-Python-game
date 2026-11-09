from playerData.py import *

playerhp -= 1

#opens playerData.py and saves each line to list 'overwrite'
f = open('playerData.py','r')
overwrite = []
for line in f:
    #if variable in question found, overwrite the line with new variable
    if 'currentHP' in line:
        overwrite.append(f'currentHP = {currentHP}')
    else:
        overwrite.append(line)
f.close
#opens playerData.py in overwrite mode and write each line as an element of list 'overwrite'
f = open('playerData.py','w')
for line in overwrite:
    f.writelines(line)
f.close()

print(currentHP)
