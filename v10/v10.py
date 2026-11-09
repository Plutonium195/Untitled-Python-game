#in terminal, pip install clrprint (required for code to function)

from clrprint import *

from datetime import datetime

import math, time, random, pickle, os

from data.gameData import *

from data.enemyData import *

from functions.forage import forage

from functions.checklevel import *

from functions.stats import *

#from functions.blacksmith import

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


    
def start():
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
    global charname
    charname = 'CHARACTER'
    global debugtrack
    debugtrack = 0
    global playerlvl
    global playerhp
    global playerhpmax
    playerlvl = 1
    playerhp = 20
    playerhpmax = 20
    global gold
    gold = 10
    global playerscrap
    playerscrap = 0
    global inv
    inv = ['basic sword', 'basic crossbow', 'basic fishing rod']
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)
    global combat
    global combatxp
    global combatmax
    combat = 1
    combatxp = 0
    combatmax = 10
    global hunting
    global huntingxp
    global huntingmax
    hunting = 1
    huntingxp = 0
    huntingmax = 10
    global foraging
    global foragingxp
    global foragingmax
    foraging = 1
    foragingxp = 0
    foragingmax = 10
    global fishing
    global fishingxp
    global fishingmax
    fishing = 1
    fishingxp = 0
    fishingmax = 10
    global luck
    global luckxp
    global luckmax
    luck = 1
    luckxp = 0
    luckmax = 10
    global currentdestination
    currentdestination = 'Point Garmsby'
    global mweaponequip
    mweaponequip = 'Nothing'
    global sweaponequip
    sweaponequip = 'Nothing'
    global armorequip
    armorequip = 'Nothing'
    global toolequip1
    toolequip1 = 'Nothing'
    global toolequip2
    toolequip2 = 'Nothing'
    global toolequip3
    toolequip3 = 'Nothing'
    pdata.update({'charname': f"'{charname}'", 'debugtrack': debugtrack, 'playerlvl': playerlvl, 'playerhp': playerhp, 'playerhpmax': playerhpmax, 'gold': gold, 'playerscrap': playerscrap, 'combat': combat, 'combatxp': combatxp, 'combatmax': combatmax, 'hunting': hunting, 'huntingxp': huntingxp,
                  'huntingmax': huntingmax, 'foraging': foraging, 'foragingxp': foragingxp, 'foragingmax': foragingmax, 'fishing': fishing, 'fishingxp': fishingxp, 'fishingmax': fishingmax, 'luck': luck, 'luckxp': luckxp, 'luckmax': luckmax, 'currentdestination': f"'{currentdestination}'", 'mweaponequip': f"'{mweaponequip}'", 'sweaponequip': f"'{sweaponequip}'", 'armorequip': f"'{armorequip}'", 'toolequip1': f"'{toolequip1}'", 'toolequip2': f"'{toolequip2}'", 'toolequip3': f"'{toolequip3}'"})
    with open('data/playerData.py','w') as file:
        for key in pdata:
              val = pdata[key]
              file.write(f'{key}={val}\n')    
    
#    introduction()


def blacksmith():
    global gold
    global smithlist
    global currentdestination
    global playerscrap
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    clrprint('The blacksmith greets you, and offers their sevice...',clr='d')
    time.sleep(0.5)
    buying = None
    while buying != 0:
        clrprint('<=============SHOP============>',clr='d')
        clrprint('Gold / Scrap / Item',clr='d')
        for item in smithlist:
            smithitemname = item[0]
            goldcost = item[1]
            scrapcost = item[2][0]
            clrprint('{} / {} / {}'.format(goldcost, scrapcost, smithitemname), clr='r')
        clrprint('<=============================>',clr='d')
        buyitem = input('What would you like to purchase?\n')
        buyitem = buyitem.strip()
        buyitem = buyitem.lower()
        for sublist in smithlist:
            if buyitem in sublist:
                scraporgold = input('Would you like to use scrap or gold?\n')
                scraporgold = scraporgold.strip()
                scraporgold = scraporgold.lower()
                if scraporgold == 'scrap':
                    if scrapcost <= playerscrap:
                        inv.append(buyitem)
                        playerscrap -= scrapcost
                        clrprint('Purchased', buyitem, 'for', str(scrapcost), 'scrap', clr='g')
                        shopagain = input('Would you like to buy anything else? (y/n)\n')
                        shopagain.strip()
                        shopagain.lower()
                        if 'n' in shopagain:
                            buying = 0
                            break
                        else:
                            buying = 1
                    else:
                        clrprint('You don\'t have enough scrap!',clr='d')
                        buying = 0
                        break
                elif scraporgold == 'gold':
                    for item in globalcost:
                        if buyitem in item[0]:
                            buyitem = item[0]
                            print(buyitem)
                    for sublist in smithlist:
                        if buyitem in sublist:
                            buycost = smithlist.index(sublist)
                            if smithlist[buycost][1] <= gold:
                                inv.append(buyitem)
                                gold -= smithlist[buycost][1]
                                clrprint('Purchased',buyitem,'for',str(smithlist[buycost][1]),'gold',clr='g')
                                shopagain = input('Would you like to buy anything else? (y/n)\n')
                                shopagain.strip()
                                shopagain.lower()
                                if 'n' in shopagain:
                                    buying = 0
                                    break
                            else:
                                clrprint('You don\'t have enough gold!',clr='d')
                                buying = 0
                                break
                else:
                    clrprint('no',clr='r')
            else:
                buying = 0
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)



def cook():
    global foodhealthmod
    global math
    import math
    global time
    import time
    global inv
    inventory()
    food1 = input('What would you like in your dish?\n').strip().lower()
    food2 = input('Anything else?\n').strip().lower()

    # Check if the user's selected food items are in the list of food items
    if (food1, food2) in [(food[0], food[0]) for food in foodhealthmod]:
        # Sum the health modifiers of the selected food items
        for y in foodhealthmod:
            if food1 in y:
                foodindex1 = foodhealthmod.index(y)
        for y in foodhealthmod:
            if food2 in y:
                foodindex2 = foodhealthmod.index(y)
        healthmod = foodhealthmod[foodindex1][1]+foodhealthmod[foodindex2][1]
        # Check if the total health modifier is less than 2
        if healthmod < 2:
            # If the total health modifier is less than 2, print an error message
            clrprint('That is not an available option!', clr='d')
        else:
            # If the total health modifier is greater than or equal to 2, continue with cooking process
            clrprint('The cook takes away your ingredients...',clr='d')
            time.sleep(1)
            # Determine which dish to cook based on the selected food items
            if food1 == 'eggs' and food2 == 'wild mushrooms':
                dish = 'sauteed mushroom ömelette'
                clrprint('You are served a ' + dish + ' ' + str(healthmod) + '!',clr='g')
            elif food1 in ['snapper', 'salmon', 'bass', 'trout', 'tuna']:
                dish = 'fish soup'
                clrprint('You are served a ' + dish + ' with ' + food2 + ' ' + str(healthmod) + '!',clr='g')
            elif food1 == 'eggs' and food2 != 'wild mushrooms':
                dish = food2 + ' ömelette'
                clrprint('The cook whips up a ' + dish + ' ' + str(healthmod) + '!',clr='g')
            elif food1 == food2:
                dish = 'even bigger ' + food1
                clrprint('The cook looks at you strangely',clr='d')
                clrprint('You are served an ' + dish + ' ' + str(healthmod) + '!',clr='g')
            else:
                # If none of the above conditions are met, print an error message
                clrprint('That is not an available option!', clr='d')
            inv.append('dish '+str(healthmod))
            inv.remove(food1)
            inv.remove(food2)
    else:
        # If none of the above conditions are met, print an error message
        clrprint('That is not an available option!', clr='d')
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)


def debugLevelUpAllSkills(increase):
    global debugtrack
    global combat
    global luck
    global fishing
    global hunting
    global foraging
    debugtrack += 1
    luck += increase
    combat += increase
    foraging += increase
    fishing += increase
    hunting += increase

def dungeon():
    clrprint('You enter the dungeon, and find a dimly lit room filled with cobwebs and dust.',clr='d')
    random1 = random.randint(2,4)
    clrprint('Before you,',str(random1),'ornate stone archways lead further into the dungeon.',clr='d')
    choice1 = input('Which archway will you enter?\n')
    if choice1.isnumeric() == True:
        if choice1 in range(random1):
            return
        else:
            clrprint('That is not a valid input',clr='r')
    else:
        clrprint('That is not a valid input',clr='r')

 

def equipment():
    global mweapon
    global mweaponequip
    global sweapon
    global sweaponequip
    global armor
    global armorequip
    global armorlist 
    global tool
    global toolequip1
    global toolequip2
    global toolequip3
    global toolist
    global inv
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    clrprint('\n<==========EQUIPMENT==========>',clr='d')
    clrprint('+','Main weapon:',mweaponequip,clr='r,d,m')
    clrprint('+','Secondary weapon:',sweaponequip,clr='r,d,m')
    clrprint('+','Armor:',armorequip,clr='r,d,m')
    clrprint('+','Tool slot 1:',toolequip1,clr='r,d,m')
    clrprint('+','Tool slot 2:',toolequip2,clr='r,d,m')
    clrprint('+','Tool slot 3:',toolequip3,clr='r,d,m')
    clrprint('<=============================>',clr='d')
    
    x = input('\nWould you like to change your equipment? (y/n)\n')
    x.strip()
    x.lower()
    if x in 'yes':
        y = 1
        equipchoice = []
        while y == 1:
            z = input('What would you like to change? (main/secondary/armor/tool)\n')
            z.strip()
            z.lower()
            if z in 'main':
                y = 0
                y = 0
                clrprint('You have:',clr='d')
                for sublist in mweaponlist:
                    for a in sublist:
                        if a in inv:
                            clrprint('+',a,clr='r,d')
                            equipchoice.append(a)
                b = input('\nWhat will you equip?\n')
                if b in equipchoice:
                    clrprint(b,'equipped',clr='g')
                    if mweaponequip != 'Nothing':
                        inv.append(mweaponequip)
                    mweaponequip = b
                    inv.remove(b)
            elif z in 'secondary':
                y = 0
                y = 0
                clrprint('You have:',clr='d')
                for sublist in sweaponlist:
                    for a in sublist:
                        if a in inv:
                            clrprint('+',a,clr='r,d')
                            equipchoice.append(a)
                b = input('\nWhat will you equip?\n')
                if b in equipchoice:
                    clrprint(b,'equipped',clr='g')
                    if sweaponequip != 'Nothing':
                        inv.append(sweaponequip)
                    sweaponequip = b
                    inv.remove(b)
            elif z in 'armor':
                y = 0
                y = 0
                clrprint('You have:',clr='d')
                for sublist in armorlist:
                    for a in sublist:
                        if a in inv:
                            clrprint('+',a,clr='r,d')
                            equipchoice.append(a)
                b = input('\nWhat will you equip?\n')
                if b in equipchoice:
                    clrprint(b,'equipped',clr='g')
                    if armorequip != 'Nothing':
                        inv.append(armorequip)
                    armorequip = b
                    inv.remove(b)
            elif z in 'tool':
                x = input('What slot? (1/2/3)\n')
                if x in '1':
                    y = 0
                    y = 0
                    clrprint('You have:',clr='d')
                    for sublist in toolist:
                        for a in sublist:
                            if a in inv:
                                clrprint('+',a,clr='r,d')
                                equipchoice.append(a)
                    b = input('\nWhat will you equip?\n')
                    if b in equipchoice:
                        clrprint(b,'equipped',clr='g')
                        if toolequip1 != 'Nothing':
                            inv.append(toolequip1)
                        toolequip1 = b
                        inv.remove(b)
                elif x in '2':
                    y = 0
                    y = 0
                    clrprint('You have:',clr='d')
                    for sublist in toolist:
                        for a in sublist:
                            if a in inv:
                                clrprint('+',a,clr='r,d')
                                equipchoice.append(a)
                    b = input('\nWhat will you equip?\n')
                    if b in equipchoice:
                        clrprint(b,'equipped',clr='g')
                        if toolequip2 != 'Nothing':
                            inv.append(toolequip2)
                        toolequip2 = b
                        inv.remove(b)
                elif x in '3':
                    y = 0
                    y = 0
                    clrprint('You have:',clr='d')
                    for sublist in toolist:
                        for a in sublist:
                            if a in inv:
                                clrprint('+',a,clr='r,d')
                                equipchoice.append(a)
                    b = input('\nWhat will you equip?\n')
                    if b in equipchoice:
                        clrprint(b,'equipped',clr='g')
                        if toolequip3 != 'Nothing':
                            inv.append(toolequip3)
                        toolequip3 = b
                        inv.remove(b)
                else:
                    clrprint('Incorrect input. Please try again.',clr='r')
            else:
                clrprint('Incorrect input. Please try again.',clr='r')
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)


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

def fish():
    global gold
    global inv
    global fishlist
    global luckxp
    global luck
    global fishingxp
    global playerscrap
    baitmod = 1
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    if 'basic fishing rod' == toolequip1 or 'basic fishing rod' == toolequip2 or 'basic fishing rod' == toolequip3:
        clrprint('You find a lake surrounded by trees with a small jetty in front of you',clr='d')
        time.sleep(1)
        if 'fishing bait' in inv:
            bait = input('Would you like to use some bait?\n')
            bait = bait.strip()
            bait = bait.lower()
            if bait == 'yes':
                baitmod = 2
        clrprint('You sit down on the jetty and cast your lure...',clr='d')
        time.sleep(1)
        fishchance = random.randint(1, 30) * math.ceil(luck/4) * baitmod
        fishoutcome = fishlist[random.randint(0,21)]
        if fishchance > 20:
            if fishoutcome == 'a sack of gold':
                gold += 10
                clrprint('You found ' + str(fishoutcome)+ ' with 10 gold inside!',clr='y')
                fishingxp += 3
                luckxp += 1
                checklevel.checklevel()
            else:
                clrprint('You caught ' + str(fishoutcome)+'!',clr='g')
                if fishoutcome == 'some scrap metal':
                    playerscrap += random.randint(1,3)
                    fishingxp += random.randint(1,2)
                    checklevel.checklevel()
                else:
                    fishoutcome = fishoutcome.strip()
                    cut = fishoutcome.index(' ') + 1
                    inv.append(fishoutcome[cut:])
                    fishingxp += random.randint(1,2)
                    checklevel.checklevel()
        else:
            clrprint('You caught nothing.',clr='r')
    else:
        clrprint('You don\'t have a fishing rod equipped!',clr='r')
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)

def gamble():
    global luck
    global luckxp
    global gold
    import random
    import math
    global currentdestination
    clrprint('How much would you like to put up?', clr='g')
    amount = int(input('>>>'))
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    if amount > gold:
      clrprint("You don't have that much money!",clr='r')
    else:
        clrprint('Games:',clr='p')
        clrprint('»Roulette',clr='p')
        clrprint('»Blackjack',clr='p')
        clrprint('»Slots',clr='p')
        gamechoice = input('What game would you like to play?\n')
        gamechoice = gamechoice.strip()
        gamechoice = gamechoice.lower()
        if gamechoice == 'roulette':
    #        if currentdestination == 'Ledgetown' or 'Bamburgh' or 'Dunwich':
    #            clrprint('You can\'t play that here',clr='r')
    #        else:
                    gold -= amount
                    choice = input('Red or Black?\n')
                    choice = choice.strip()
                    choice = choice.lower()
                    jackpotchance = 1
                    if random.randint(1, 100000) <= 1*luck:
                        clrprint('You hit the jackpot!',clr='y')
                        clrprint('You won ' + str(amount*100) + ' gold',clr='y')
                        luckxp += 30 
                        gold += amount*100
                        checklevel.checklevel()
                    elif random.randint(1, 10000) > 8500:
                        if choice == 'red':
                            luckxp = luckxp + random.randint(1,5)
                            winnings = amount*random.randint(2,5)
                            clrprint('It landed on red and you won ' + winnings + ' gold!',clr='g')
                            gold += winnings
                            checklevel.checklevel()
                        elif choice == 'black':
                            clrprint('It landed on red and you lost!',clr='r')
                    elif random.randint(1, 10000) < 1500:
                        if choice == 'black':
                            luckxp = luckxp + random.randint(1,5)
                            winnings = amount*random.randint(2,5)
                            clrprint('It landed on red and you won ' + winnings + ' gold!',clr='g')
                            gold += winnings
                            checklevel.checklevel()
                        elif choice == 'red':
                            clrprint('It landed on black and you lost!',clr='r')
                    else:
                        clrprint('You lost! :(',clr='r')
                    
        elif gamechoice == 'blackjack':
    #        if currentdestination == 'Dunwich' or 'Northward' or 'Pendle' or 'Saxondale':
    #            clrprint('You can\'t play that here',clr='r')
    #        else:
                if amount > gold:
                    clrprint("You don't have that much money!",clr='r')
                else:
                    gold -= amount
                    # Define a function to calculate the value of a hand
                    def handvalue(hand):
                        value = 0
                        numaces = 0
                        for card in hand:
                            card = card[1:]
                            if card == 'A':
                                numaces += 1
                                value += 11
                            elif card in ['K','Q','J']:
                                value += 10
                            else:
                                value += int(card)
                        while value > 21 and numaces > 0:
                            value -= 10
                            numaces -= 1
                        return value

                    
                    # Initialize variables for the game
                    deck = ['♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♠A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K','♥A',
                            '♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♣A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K','♦A',
                            '♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♠A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K','♥A',
                            '♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♣A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K','♦A']
                    random.shuffle(deck)
                    #removing cards from deck and putting them in players hand
                    playerhand = [deck.pop(), deck.pop()]
                    dealerhand = [deck.pop(), deck.pop()]
                    
                    # Check if the player has blackjack
                    if handvalue(playerhand) == 21 and handvalue(dealerhand) != 21:
                        print(f"You have blackjack! You win {amount*2}!")
                        gold += amount * 2
                        luckxp = luckxp + random.randint(1,5)
                        checklevel.checklevel()
                        return
                    
                    # Player's turn
                    while True:
                        print("Your hand:", playerhand)
                        print("Dealer's faceup card:", dealerhand[0])
                        action = input("Do you want to hit or stand?\n")
                        if action.lower() == 'hit':
                            playerhand.append(deck.pop())
                            print('You drew a',playerhand[len(playerhand)-1])
                            if handvalue(playerhand) > 21:
                                clrprint("Bust! You lose.",clr='r')
                                return
                        elif action.lower() == 'stand':
                            break
                    
                    # Dealer's turn
                    while handvalue(dealerhand) < 17:
                        dealerhand.append(deck.pop())
                    print("Dealer's hand:", dealerhand)
                    
                    # Determine the winner
                    if handvalue(dealerhand) > 21:
                        print(f"Dealer busts! You win {amount*2}!")
                        luckxp = luckxp + random.randint(1,5)
                        gold += amount * 2
                        checklevel.checklevel()
                    elif handvalue(playerhand) > handvalue(dealerhand):
                        print(f"You won {amount*2}!")
                        clrprint('You got',amount*2,'gold!',clr='y')
                        luckxp = luckxp + random.randint(1,5)
                        gold += amount * 2
                        checklevel.checklevel()
                    elif handvalue(playerhand) == handvalue(dealerhand):
                        print("Push. All bets returned")
                        gold += amount
                    else:
                        print("You lose.")
                    
        elif gamechoice == 'slots':
            if amount > gold:
                clrprint("You don't have that much money!",clr='r')
            else:
                gold -= amount
                print("Spinning the reels...")
                reel1 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven", "apple", "coin", "kettle"])
                reel2 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven", "apple", "coin", "kettle"])
                reel3 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven", "apple", "coin", "kettle"])
                print(f"The reels stop on: {reel1}, {reel2}, {reel3}")

                # Determine the outcome
                if reel1 == reel2 == reel3 == "seven":
                    win = amount * 10
                    print("JACKPOT! You win " + str(win) +  " gold!")
                    gold += amount * 10
                    luckxp += 30
                    checklevel.checklevel()
                elif reel1 == reel2 == reel3:
                    if reel1 == "cherry":
                        win = amount * 3
                        luckxp += 2
                        checklevel.checklevel()
                        clrprint("Three cherries! You win" + str(win) + 'gold!',clr='y')
                    else:
                        luckxp += 2
                        print(f"Three {reel1}s! You win {amount*2} gold!")
                        gold += amount * 2
                elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
                    win = amount * 2
                    print("Two of a kind! You win " + str(win) +" gold !")
                    gold += amount * 2
                    luckxp += 1
                    checklevel.checklevel()
                else:
                    print("Sorry, you didn't win anything this time.")
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)

def hunt():
    global huntstats
    global hunting
    global huntingxp
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    #if you don't have a secondary weapon, you can't hunt
    if sweaponequip == 'Nothing':
        clrprint('You\'ll need to equip a secondary weapon before you can hunt!',clr='r')
    else:
        clrprint('You walk through the forest, your',sweaponequip,'in hand...',clr='d')
        time.sleep(0.1)
        #pick a random result from the huntlist list
        huntresult = huntlist[random.randint(0,len(huntlist)-1)]
        if huntresult == 'a bear':
            #if result is a bear, fight it
            clrprint('You hear a thrashing in the undergrowth...')
            fight('bear')
        else:
            #retrieve range value of equipped secondary weapon
            for sublist in sweaponlist:
                if sweaponequip in sublist:
                    weaponrange = sublist[2]
            #determine distance of target from player
            distance = random.randint(3, 11)
            clrprint('You notice',huntresult,'nearby.')
            while distance > 2:
                #if the target is further than the range of your weapon
                if distance > weaponrange:
                    print('It\'s out of normal range for your weapon.')
                    choice = input('Will you shoot anyway or sneak closer?\n')
                    choice.strip()
                    choice.lower()
                    if 'sneak' in choice:
                        #move closer by 1 distance unit
                        distance -= 1
                    elif 'shoot' in choice:
                        clrprint(f'Your shot misses and the {huntresult[2:]} gets away.',clr='r')
                        if hunting-(distance-weaponrange) < 1:
                            break
                #if the target is in range of your weapon
                elif distance <= weaponrange:
                    choice = input('It\'s in range of your weapon, but you can sneak closer for a better shot.\n')
                    choice.strip()
                    choice.lower()
                    if distance <= 2:
                        #if you get too close to the target, it runs away
                        clrprint('You were too loud and the',huntresult[2:],'got away.',clr='r')
                    elif 'sneak' in choice:
                        distance -= 1
                    elif 'shoot' in choice:
                        clrprint('You hit the',huntresult[2:],'and it collapses to the ground',clr='g')
                        #get xp amount of huntresult
                        for sublist in huntstats:
                            if huntresult in sublist:
                                huntxpgain = sublist[1]
                                huntingxp += huntxpgain
                        checklevel.checklevel()
                        break
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)
            

def inventory():
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    clrprint('\n<==========INVENTORY==========>',clr='d')
    clrprint('+ ',str(gold),'gold',clr='d,r')
    if playerscrap > 0:
        clrprint('+ ',str(playerscrap),'scrap',clr='d,r')
    for x in inv:
        clrprint('+ ',x,clr='d,r')
    clrprint('<=============================>',clr='d')

def name():
    global charname
    clrprint('This idiot fogot their name.',clr='b')
    time.sleep(0.5)
    clrprint("Here I'll tell you.",clr='b')
    time.sleep(0.5)
    clrprint('Your name is '+ charname,clr='p')
    
def shop():
    global gold
    global shoplist1
    global shoplist2
    global currentdestination
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    clrprint('The merchant greets you, and displays his wares...',clr='d')
    time.sleep(0.5)
    if currentdestination == 'Point Garmsby':
        shoplist = shoplist1
    else:
        shoplist = shoplist2
    bors = input('Here to buy or sell?\n')
    bors = bors.strip()
    bors = bors.lower()
    if 'buy' in bors:
        buying = None
        while buying != 0:
            clrprint('<=============SHOP============>',clr='d')
            tlist = [item[0] for item in shoplist]
            clist = [item[1] for item in shoplist]
            printlist = zip(tlist,clist)
            clrprint('Cost / Item',clr='d')
            for x in printlist:
                clrprint('{:4}{:10}'.format(x[1],'  '+x[0]),clr='r')
            clrprint('<=============================>',clr='d')
            buyitem = input('What would you like to purchase?\n')
            buyitem = buyitem.strip()
            buyitem = buyitem.lower()
            if len(buyitem) == 0:
                buying = 0
            else:
                for item in tlist:
                    if buyitem in item:
                        buyitem = item
                for sublist in shoplist:
                    if buyitem in sublist:
                        buycost = shoplist.index(sublist)
                        if shoplist[buycost][1] <= gold:
                            inv.append(buyitem)
                            gold -= shoplist[buycost][1]
                            clrprint('Purchased',buyitem,'for',str(shoplist[buycost][1]),'gold',clr='g')
                            shopagain = input('Would you like to buy anything else? (y/n)\n')
                            shopagain.strip()
                            shopagain.lower()
                            if 'n' in shopagain:
                                buying = 0
                                break
                        else:
                            clrprint('You don\'t have enough gold!',clr='d')
                            buying = 0
                            break
            
                return
    elif 'sell' in bors:
        sellitem = None
        while sellitem != 0:
            inventory()
            sellitem = input('What would you like to sell?\n')
            sellitem = sellitem.strip()
            sellitem = sellitem.lower()
            for x in inv:
                if sellitem in x:
                    sellitem = x
            for sublist in globalcost:
                if sellitem in sublist:
                    itemcost = globalcost.index(sublist)
            inv.remove(sellitem)
            gold += globalcost[itemcost][1]
            clrprint(sellitem,'sold for',str(globalcost[itemcost][1]),'gold.',clr='r')
            sellitem = input('Would you like to sell anything else? (y/n)\n')
            sellitem.strip()
            sellitem.lower()
            if 'n' in sellitem:
                sellitem = 0
            
    else:
        print("I'm afraid that that is not an available option")
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)

    

def townhall():
    global charname
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1][:-1]
##    if currentdestination == 'point garmsby'
    text1 = '''
As you enter the town hall in Point Garmsby, you notice the classic simplicity the building's architecture. The entrance leads to a cozy lobby,
which is adorned with landscape paintings and busts of former mayors. The walls are paneled in dark oak, and the floors are covered in a rich red carpet.

The reception desk is located at the center of the lobby, where a friendly receptionist greets you and asks for your purpose.
The receptionist can guide you to the relevant department or schedule a meeting with Mayor Berny if needed.\n'''
    for x in text1:
        clrprint(x,clr='d',end='')
        time.sleep(0.01)
    clrprint('Hello there ' + charname + ', Mayor Berny said you might be coming round, how can I assist you?\n',clr='d')
    clrprint('<=============Town Hall============>',clr='d')
    clrprint('+ Quests +',clr='p')
    clrprint('+ Help +',clr='p')
    clrprint('+ Community Board +',clr='p')
    clrprint('+ Training Grounds +',clr='p')
    clrprint('<==================================>',clr='d')
    choice = input('> ')
    choice = choice.strip()
    choice = choice.lower()
    if choice in 'training Grounds':
        clrprint('You are directed out the back of the town hall to a small arena where a person stands practicing with a sword')
        time.sleep(0.05)
        clrprint('Hello ' + charname + ', I heard you might be coming round, I can offer some training in combat')
        clrprint('Before we start here are some healing herbs')
        inv.append ('some healing herbs')
        with open('data/inventory.txt','w') as file:
            for i in inv:
                i += ','
        file.write(i)
        time.sleep(0.01)
        fight('teacher')
        clrprint('Well done young adventurer, do be afraid to come back whenever you like.')
        return
    elif choice in 'community board':

        clrprint('<=============Community Board============>',clr='d')
        print()
        if communitynotice:
            notices = 3
            displayed_messages = set()
            while notices != 0:
                random_index = random.randint(0, len(communitynotice) - 1)
                author = communitynotice[random_index][0]
                notice = communitynotice[random_index][1]

                if notice not in displayed_messages:
                    clrprint(f'+ {author} :', clr='p')
                    clrprint(f'» {notice}', clr='p')
                    print()
                    displayed_messages.add(notice)
                    notices -= 1
            if not displayed_messages:
                clrprint("No unique community notices available.",clr='r')
        else:
            print("No community notices available.")
        clrprint('<========================================>',clr='d')
        exit = input('>')




def travel():
    global currentdestination
    global destinations
    map()
    clrprint('You are currently in ' + currentdestination,clr='g')
    destination = input('Where would you like to go?\n')
    destination = destination.strip()
    destination = destination.lower()
    if destination in destinations:
        currentdestination = destination.capitalize()
        load = '''
Loading...0%
Loading...10%
Loading...50%
Loading...90%
Loading...100%
        '''
        for x in load:
            print(x,end='')
            time.sleep(random.randint(2,5)/100)
        print('')
        clrprint('After ' + str(random.randint(1,5)) + ' days you arrive in the town of ' + destination.capitalize(),clr='g')
    else:
        clrprint('That isnt a location!',clr='r')



def save():
    global filedirect
    with open('data/inventory.txt','r') as file:
        f = file.read()
        inv = f.split(',')[:-1]
    #Helpful code at https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python, just replace dill with pickle
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtstring = now.strftime("%d/%m/%Y %H:%M")
    filepath1 = 'saves/savefile1'
    filesize1 = os.path.getsize(filepath1)
    statinfo1 = os.stat(filepath1)
    modificationtime1 = datetime.fromtimestamp(statinfo1.st_mtime)
    filepath2 = 'saves/savefile2'
    filesize2 = os.path.getsize(filepath2)
    statinfo2 = os.stat(filepath2)
    modificationtime2 = datetime.fromtimestamp(statinfo2.st_mtime)
    filepath3 = 'saves/savefile3'
    filesize3 = os.path.getsize(filepath3)
    statinfo3 = os.stat(filepath3)
    modificationtime3 = datetime.fromtimestamp(statinfo3.st_mtime)
    clrprint('What slot would you like to use?')
    clrprint('<==========Slots===========>',clr='d')
    clrprint(f'      |{dtstring}|', clr='b')
    clrprint("+» Slot 1:",clr='p')
    clrprint(f'+{filesize1} bytes | {modificationtime1}', clr='b')
    clrprint("+» Slot 2:",clr='p') 
    clrprint(f'+{filesize2} bytes | {modificationtime2}', clr='b')
    clrprint("+» Slot 3:",clr='p')
    clrprint(f'+{filesize3} bytes | {modificationtime3}', clr='b')
    saveslot = input('')
    saveslot = saveslot.strip()
    saveslot = saveslot.lower()
    if saveslot in 'slot 1':
        file_name = 'saves/savefile1'
        savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
                'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
                'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
                'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
        with open(file_name,'wb') as file:
            pickle.dump(savelist, file, protocol=4)  # Store all the names first
            for value in savelist:
                pickle.dump(eval(value), file, protocol=4) # Store the objects themselves
        loading = '''
        Loading...0%
        Loading...10%
        Loading...20%
        Loading...30%
        Loading...40%
        Loading...50%
        Loading...60%
        Loading...70%
        Loading...80%
        Loading...90%
        Loading...100%
        '''
        for x in loading:
            print(x,end='')
            time.sleep(random.randint(2,8)/100)
        time.sleep(1)
        clrprint('Saved to slot 1',clr='g')
    elif saveslot  in 'slot 2':
        file_name = 'saves/savefile2'
        savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
                'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
                'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
                'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
        with open(file_name,'wb') as file:
            pickle.dump(savelist, file, protocol=4)  # Store all the names first
            for value in savelist:
                pickle.dump(eval(value), file, protocol=4) # Store the objects themselves
        loading = '''
        Loading...0%
        Loading...10%
        Loading...20%
        Loading...30%
        Loading...40%
        Loading...50%
        Loading...60%
        Loading...70%
        Loading...80%
        Loading...90%
        Loading...100%
        '''
        for x in loading:
            print(x,end='')
            time.sleep(random.randint(2,8)/100)
        time.sleep(1)
        clrprint('Saved to slot 2',clr='g')
    elif saveslot in 'slot 3':
        file_name = 'saves/savefile3'
        savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
                'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
                'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
                'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
        with open(file_name,'wb') as file:
            pickle.dump(savelist, file, protocol=4)  # Store all the names first
            for value in savelist:
                pickle.dump(eval(value), file, protocol=4) # Store the objects themselves
        loading = '''
        Loading...0%
        Loading...10%
        Loading...20%
        Loading...30%
        Loading...40%
        Loading...50%
        Loading...60%
        Loading...70%
        Loading...80%
        Loading...90%
        Loading...100%
        '''
        for x in loading:
            print(x,end='')
            time.sleep(random.randint(2,8)/100)
        time.sleep(1)
        clrprint('Saved to slot 3',clr='g')
    else:
        clrprint('Thats not an avalible otption!')
            
def load():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtstring = now.strftime("%d/%m/%Y %H:%M")
    filepath1 = 'saves/savefile1'  
    filesize1 = os.path.getsize(filepath1)  # Locating the file
    statinfo1 = os.stat(filepath1)          # Getting the date it was last modified
    modificationtime1 = datetime.fromtimestamp(statinfo1.st_mtime)
    filepath2 = 'saves/savefile2'
    filesize2 = os.path.getsize(filepath2)
    statinfo2 = os.stat(filepath2)
    modificationtime2 = datetime.fromtimestamp(statinfo2.st_mtime)
    filepath3 = 'saves/savefile3'
    filesize3 = os.path.getsize(filepath3)
    statinfo3 = os.stat(filepath3)
    modificationtime3 = datetime.fromtimestamp(statinfo3.st_mtime)
    clrprint('What slot would you like to load?',clr='d')
    clrprint('<==========Slots===========>',clr='d')
    clrprint(f'      |{dtstring}|', clr='b')
    clrprint("+» Slot 1:",clr='p')
    clrprint(f'+{filesize1} bytes | {modificationtime1}', clr='b')
    clrprint("+» Slot 2:",clr='p') 
    clrprint(f'+{filesize2} bytes | {modificationtime2}', clr='b')
    clrprint("+» Slot 3:",clr='p')
    clrprint(f'+{filesize3} bytes | {modificationtime3}', clr='b')
    loadslot = input('> ')
    loadslot.strip
    loadslot.lower
    #Helpful code at https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python, just replace dill with pickle
    if loadslot in 'slot 1':
        file_name = 'saves/savefile1'
    elif loadslot in 'slot 2':
        file_name = 'saves/savefile2'
    elif loadslot in 'slot 3':
        file_name = 'saves/savefile3'
    else:
        clrprint('Thats not and avalible option!',clr='r')
        return
    g = globals()
    with open(file_name,'rb') as file:
        savelist = pickle.load(file)  # Get the names of savefiles
        for value in savelist:
            g[value] = pickle.load(file)    # Get the objects themselve
    with open('data/inventory.txt','w') as file:
        for i in inv:
            i += ','
            file.write(i)
    loading = '''
    Loading...0%
    Loading...10%
    Loading...20%
    Loading...30%
    Loading...40%
    Loading...50%
    Loading...60%
    Loading...70%
    Loading...80%
    Loading...90%
    Loading...100%
    '''
    for x in loading:
        print(x,end='')
        time.sleep(random.randint(2,8)/100)
    time.sleep(1)
    clrprint(f'Loaded {loadslot}',clr='g')



        
def loading(): 
    loading = '''
    Loading...0%
    Loading...10%
    Loading...20%
    Loading...30%
    Loading...40%
    Loading...50%
    Loading...60%
    Loading...70%
    Loading...80%
    Loading...90%
    Loading...100%
    '''
    for x in loading:
        print(x,end='')
        time.sleep(random.randint(2,8)/100)
    time.sleep(1)
    clrprint('\nNEW GAME SUCCESSFULLY LOADED\n',clr='g')
    time.sleep(1)
    clrprint('\nWelcome To...\n',clr='d')
    time.sleep(1)
    clrprint('''

   ▄██████▄     ▄████████    ▄▄▄▄███▄▄▄▄      ▄████████      ███▄▄▄▄      ▄████████    ▄▄▄▄███▄▄▄▄      ▄████████ 
  ███    ███   ███    ███  ▄██▀▀▀███▀▀▀██▄   ███    ███      ███▀▀▀██▄   ███    ███  ▄██▀▀▀███▀▀▀██▄   ███    ███ 
  ███    █▀    ███    ███  ███   ███   ███   ███    █▀       ███   ███   ███    ███  ███   ███   ███   ███    █▀  
 ▄███          ███    ███  ███   ███   ███  ▄███▄▄▄          ███   ███   ███    ███  ███   ███   ███  ▄███▄▄▄     
▀▀███ ████▄  ▀███████████  ███   ███   ███ ▀▀███▀▀▀          ███   ███ ▀███████████  ███   ███   ███ ▀▀███▀▀▀     
  ███    ███   ███    ███  ███   ███   ███   ███    █▄       ███   ███   ███    ███  ███   ███   ███   ███    █▄  
  ███    ███   ███    ███  ███   ███   ███   ███    ███      ███   ███   ███    ███  ███   ███   ███   ███    ███ 
  ████████▀    ███    █▀    ▀█   ███   █▀    ██████████       ▀█   █▀    ███    █▀    ▀█   ███   █▀    ██████████ 
                                                                                                                  

    ''',clr='p')

    
def map():
    print('''    ....................................................................................................
    ....................................................................................................
    ....................................................................................................
    ....................................................................................................
    ..............................:.....................................................................
    .............................::.:..............................:....................................
    ..............................: .:.......:.......     :.........  ..................................
    ............................:: .  .....::.             .......     :................................
    ............................: :...    ..                           .:...............................
    ........................:.:.  ...::::                                .... ..:.......................
    ........................:          ..                Northwards             :.............:.........
    .........................                                  *                    ......:..:..........
    ........................:.                                  |                         . :...........
    ........................:.         * Bamburgh_______________|_________              ...:............
    ........................                                /              \           .:...............
    .....................                                  /                \         .:................
    ..............:.                              Pendle *   .:.. Ledgetown *            ..:............
    ...........::..                                      |   .::.........    \             .............
    ...........:                                         |     .:........:    \           .:............
    ............                                         |      .:.........    \          .:............
    .........:.                                          |       .:......:.     \          :............
    ............:.                   _________________Tarrin *  .:.......:.      \___      .:...........
    ...............:.               /                           :.........:. Point Garmsby.::...........
    ................:.             /                           .:.:.................. *  .:.............
    .................:.      _____/                           .:......................:.:...............
    ...................     /                         .....  .:.........................................
    ................::     /                 .:      .:.................................................
    ...........:..  ..   * Tamworth         ...:      :.................................................
    ..........:          |             ...:.:..:::    :.................................................
    .........:.          |             .:........:    :..................................:....:.........
    .......:..           |              :........   .:..................................:     .:........
    .......:             * Saxondale              .:.....................................     .:........
    .......:.            |_________             .:..................................:. .....   ...::....
    .........:.                    \            ::..................................:.::.....:...:.:....
    .........:.                     \            ......:............................:...................
    .........:.                      \__               :................................................
    ...........:                        \              .:...............................................
    .......... :.                        * Dunwich     .:...............................................
    ............:.                        \            .:...............................................
    ...........:..           .....         \          .:................................................
    ..........:..:....     .:.........      \        .:.................................................
    ..................:..................    \        ..:........................::... .................
    .......................................   \_______  ..:.............................   .:...........
    ......................................::          \   ..:...........................:   ..:.........
    .......................................:           \     :...........................:..  :.........
    ........................................            *    .:............................::...........
    .....................................:.  Squalls End      .:........................................''')

def gameover():
    clrprint('''

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
    \n''',clr='d')
    time.sleep(1)
    credits = '''
                        [[[---Developed by---]]]
               [[[---┏┓•               ┏┓    ┓•   ---]]]
               [[[---┣ ┓┏┓┏┓┏╋┏┓┏┓┏┳┓  ┗┓╋┓┏┏┫┓┏┓┏---]]]
               [[[---┻ ┗┛ ┗ ┛┗┗┛┛ ┛┗┗  ┗┛┗┗┻┗┻┗┗┛┛---]]]
                  [[[-----------------------------]]]                    
     
                  [[[---Designed and Produced by---]]]
                      [[[---Lucian Van Horne---]]]
                              [[[------]]]
                        [[[---Spencer Holt---]]]
                              [[[------]]]
                     [[[---Special Thanks To ---]]]
                   [[[---Those nerds at Github ---]]]
           [[[---Those little helpers at Stackoverflow---]]]
                              [[[------]]]
 
    \n'''
    for x in credits:
        print(x,end='')
        time.sleep(random.randint(2,2)/100)
    time.sleep(1)
    y = 'RESTARTING...\n'
    for x in y:
        print(x,end='')
        time.sleep(0.1)
        
    load()
    start()

def introduction():
    global charname
    text1 = '''
It was a long journey, but you've finally reached your destination. You step down from the ship onto the docks at Point Garmsby, the first town you'll visit in this new land.
Point Garmsby is a cosy town, with many houses and a bustling main street. Before you begin exploring the town, a man who must be the Mayor approaches you...'''
    for x in text1:
        clrprint(x,clr='d',end='')
        time.sleep(0.01)
    print('\nGood afternoon young adventurer! My name is Mayor Berny. What is your name?')
    charname = input("> ")
    print(charname+'? Nice to meet you. Let me show you around our town.')
    text2 = '''The Mayor gives you a tour of the town, pointing out major features such as the blacksmith, public kitchen and local apothecary.
He also introduces you to a friendly merchant who will buy just about anything you can sell. Finally, you both reach the end of town.'''
    for x in text2:
        clrprint(x,clr='d',end='')
        time.sleep(0.01)
    print('\n...and that should be everything. There\'s a lake over that hill where you can fish, and the woods nearby are perfect for hunting and foraging. Just watch out for bears.')
    print('If you ever need me for anything, you can find me in the town hall. Goodbye for now.')
    text3 = '''The Mayor shakes your hand, then walks back into town.'''
    for x in text3:
        clrprint(x,clr='d',end='')
        time.sleep(0.01)
        
start()
#any new functions that the player can access must be added to this dictionary
func_dict = {'stats':stats, 'hunt':hunt, 'inventory':inventory, 'equipment':equipment, 'fish':fish, 'forage':forage, 'shop':shop, 'cook':cook, 'town hall':townhall}
while currentdestination == 'Point Garmsby':
    clrprint('\nYour available options are: inventory, stats, equipment, fish, forage, hunt, shop, cook, town hall',clr='p')
    action = input("> ")
    if action in func_dict:
        func_dict[action]()
    else:
        clrprint('That is not an accepted input. Please try again.',clr='r')
##
