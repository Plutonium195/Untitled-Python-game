import clrprint
import random, time, math

class Forage:
    def __init__(self, foragelist, fight, checklevel):
        self.foragelist = foragelist
        self.fight = fight
        self.checklevel = checklevel

    def forage(self):
        with open('data/inventory.txt','r') as file:
            f = file.read()
            inv = f.split(',')[:-1]

        pdata = {}
        with open('data/playerData.py','r') as file:
            for line in file:
                key, val = line.strip().split('=')
                if val.isnumeric():
                    val = int(val)
                pdata[key] = val
                globals()[key] = val  # Option 1 globals

        global foraging, foragingxp

        clrprint('You wander through the forest...', clr='d')
        time.sleep(1)

        foragechance = random.randint(1,30) * math.ceil(int(foraging)/4)
        forageresult = self.foragelist[random.randint(0, len(self.foragelist)-1)]

        if foragechance > 15:
            clrprint('After searching for a while, you find ' + forageresult + '!', clr='g')
            cut = forageresult.index(' ') + 1
            inv.append(forageresult[cut:])
            foragingxp += random.randint(1,4)
        else:
            clrprint('After searching for a while, you find nothing.', clr='r')

        encounterchance = random.randint(1, 20)
        if encounterchance == 1:
            self.fight.fight('bear')   # ✅ Use injected Fight object

        pdata.update({'foragingxp': foragingxp, 'playerhp': playerhp})

        with open('data/playerData.py','w') as file:
            for key, val in pdata.items():
                file.write(f'{key}={val}\n')

        self.checklevel.checklevel()   # ✅ OOP call

        with open('data/inventory.txt','w') as file:
            for i in inv:
                file.write(i + ',')
