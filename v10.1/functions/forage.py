from clrprint import *

import math, time, random, pickle, os

from data.gameData import *

from functions.checklevel import *

from functions.fight import fight


class forage:
    def forage():
        with open('data/inventory.txt','r') as file:
            f = file.read()
            inv = f.split(',')[:-1]
        pdata = {}
        with open('data/playerData.py','r') as file:
            for line in file:
                (key,val) = line.split('=')
                val = val[:-1]
                if val.isnumeric() == True:
                    val = int(val)
                pdata[key] = val
            for key, value in pdata.items():
                globals()[key] = value
        global foraging
        global foragingxp
        clrprint('You wander through the forest...',clr='d')
        time.sleep(1)
        foragechance = random.randint(1,30)*math.ceil(int(foraging)/4)
        forageresult = foragelist[random.randint(0,3)]
        if foragechance > 15:
            clrprint('After searching for a while, you find '+forageresult+'!',clr='g')
            if forageresult == 'a nest of eggs':
                forageresult = 'some eggs'
                cut = forageresult.index(' ') + 1
                inv.append(forageresult[cut:])
                foragingxp += random.randint(1,4)
            else:
                cut = forageresult.index(' ') + 1
                inv.append(forageresult[cut:])
                foragingxp += random.randint(1,4)
        else:
            clrprint('After searching for a while, you find nothing.',clr='r')
        encounterchance = random.randint(1, 20)
        if encounterchance == 1:
            fight('bear')

        pdata.update({'foragingxp':foragingxp, 'playerhp':playerhp})
        with open('data/playerData.py','w') as file:
            for key in pdata:
                  val = pdata[key]
                  file.write(f'{key}={val}\n')

        checklevel.checklevel()
                  
        with open('data/inventory.txt','w') as file:
            for i in inv:
                i += ','
                file.write(i)
