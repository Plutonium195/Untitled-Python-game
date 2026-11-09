from clrprint import *

import math, time, random, pickle, os

from data.gameData import *

from functions.checklevel import *

def fight(enemy):
    global mweaponlist
    global enemylootlist
    global enemylist
    global dungeonlist
    global playerhp
    global combatxp
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
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    if 'basic sword' or 'sharpened sword' in inv:
#determining enemy stats
        for y in enemylist:
            if enemy in y:
                enemyindex = enemylist.index(y)
        enemydmg = enemylist[enemyindex][1] + math.ceil(combat/2)
        enemyhp = enemylist[enemyindex][2] + math.ceil(combat/4)
        enemyarmor = enemylist[enemyindex][3] + math.ceil(combat/6)
        enemyxp = enemylist[enemyindex][4]
#fight start func
        clrprint('You encounter a',enemy+'!', clr='d')
        clrprint('HP =',str(playerhp)+'/'+str(playerhpmax),clr='p')
        retry = True
        while retry:
            initiate = input('Would you like to fight or run?\n')
            initiate = initiate.strip()
            initiate = initiate.lower()
            if initiate == 'run':
                retry = False
                clrprint('You run away',clr='d')
            elif initiate == 'fight':
                retry = False
                    #while the enemy is above 0 hp the fight will continue
                while enemyhp > 0:
                    action = input('What will you do? (attack/heal)\n')
                    action = action.strip()
                    action = action.lower()
                    if action == 'attack':
                        #player dmg defined
                        mweapondmgindex = False
                        for y in mweaponlist:
                            if mweaponequip == 'Nothing':
                                mweapondmgindex = 1
                            elif  mweaponequip in y:
                                mweapondmgindex = y[1]
                        playerdmg = mweapondmgindex
                        dmg = (int(playerdmg) + combat + random.randint(1,4))
                        if dmg > 0:
                            clrprint('You hit the ' + enemy + ' for ' + str(dmg) + ' damage!', clr='g')
                            enemyhp -= dmg
                        elif dmg <= 0:
                            clrprint('You deal no damage to the ' + enemy + '!', clr='r')
                        #if enemy not dead then you will be hit by its attack
                        #player dmg defined
                        for y in armorlist:
                            if armorequip == 'Nothing':
                                armorindex = 0
                            elif  armorequip in y:
                                armorindex = y[1]
                            else:
                                print('Error assigning armor index')
                                print(f'Armor equip assigned as {armorequip}')
                                armorindex = 0
                        if enemyhp > 0:
                            playerhp -= enemydmg - armorindex
                            clrprint('The ' + enemy + ' hits you for ' + str(enemydmg) + ' damage!', clr='r')
                            clrprint('You are on ' + str(playerhp) + ' health!')
                    elif action == 'heal':
                        if 'dish[1]' in inv or 'dish[2]' in inv or 'dish[3]' in inv or 'dish[4]' in inv or 'dish[5]' in inv or 'dish[6]' in inv or 'dish[7]' in inv or 'dish[8]' in inv or 'dish[8]' in inv or 'dish[10]' in inv and playerhp < playerhpmax:
                            consumedish = input('Would you like to eat your dish? yes/no \n')
                            consumedish = consumedish.strip()
                            consumedish = consumedish.lower()
                            if consumedish == 'yes':
                                inv.remove('dish')
                                hpgain = foodhealthmod
                                playerhp += hpgain
                                if playerhp > playerhpmax:
                                    playerhp = playerhpmax
                                clrprint('You eat your dish and gain ',str(hpgain),' HP!', clr='g')
                            elif consumedish == 'no':
                                if 'healing herbs' in inv and playerhp < playerhpmax:
                                    inv.remove('healing herbs')
                                    hpgain = random.randint(5, 10)
                                    playerhp += hpgain
                                    if playerhp > playerhpmax:
                                        playerhp = playerhpmax
                                    clrprint('Using some healing herbs, you heal yourself for',str(hpgain),'HP!', clr='g')
                                elif 'health potion' in inv and playerhp < playerhpmax:
                                    inv.remove('health potion')
                                    hpgain = random.randint(10, 15)
                                    playerhp += hpgain
                                    if playerhp > playerhpmax:
                                        playerhp = playerhpmax
                                    clrprint('Using a health potion, you heal yourself for',str(hpgain),'HP!', clr='g')
                                else:
                                    clrprint('You have no healing herbs or health potions!', clr='r')
                            else:
                                clrprint("I'm afraid that that is not an available option!", clr='r')
                                clrprint('wrong-heal-action-error', clr='r')
                        else:
                            if 'healing herbs' in inv and playerhp < playerhpmax:
                                    inv.remove('healing herbs')
                                    hpgain = random.randint(5, 10)
                                    playerhp += hpgain
                                    if playerhp > playerhpmax:
                                        playerhp = playerhpmax
                                    clrprint('Using some healing herbs, you heal yourself for',str(hpgain),'HP!', clr='g')
                            elif 'health potion' in inv and playerhp < playerhpmax:
                                inv.remove('health potion')
                                hpgain = random.randint(10, 15)
                                playerhp += hpgain
                                if playerhp > playerhpmax:
                                    playerhp = playerhpmax
                                    clrprint('Using a health potion, you heal yourself for',str(hpgain),'HP!', clr='g')
                            else:
                                clrprint('You have no healing herbs or health potions!', clr='r')
                    else:
                        clrprint("I'm afraid that that is not an available option!", clr='r')
                        clrprint('wrong-action-error', clr='r')
                        continue

                    if playerhp <= 0:
                        clrprint('You died!\n', clr='r')
                        time.sleep(1)
                        gameover()
                        enemyhp = -10000000
                    pdata.update({'playerhp': playerhp})
                        
                if -10000000 < enemyhp <= 0:
                    combatxp += enemyxp
                    clrprint('You defeated the ' + enemy + '!', clr='g')
                    checklevel.checklevel()
                if enemyhp == -10000000:
                    combatxp += enemyxp
                    print('')
                checklevel.checklevel()
            else:
                clrprint('Im afraid that that is not an option', clr='r')
                clrprint('fight-run-error', clr='r')
            
    else:
        clrprint('You dont have the adequate equipment to do this!',clr='d')
    
    pdata.update({'playerlvl': playerlvl, 'playerhp': playerhp,'playerhpmax': playerhpmax, 'combat': combat, 'combatxp': combatxp})
    with open('data/playerData.py','w') as file:
        for key in pdata:
              val = pdata[key]
              file.write(f'{key}={val}\n')
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)
