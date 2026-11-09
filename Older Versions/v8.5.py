#-Changelog v6.1
#-> Added comments to def start() with possible additions
#-> Added things to TO DO list
#-> Ticked off a few things on TO DO list
#-> Added a new shoplist (shoplist2)
#-> Added food health values
#-> Updated checklevel() into all of gamble()
#-> Added playerlvl to start(), checklvl() and stats()
#-> Player hp and level will increase after grinding
#-> Added debugLevelUpAllSkills()
#-> Added debug tracker
#-> Bugfixed debug tracker
#-> Changed goblin health to 3
#-> Changed enemy health, base damage and base armor to be afftected by player level
#-> Enemy armor mod now affects its damage taken (damage threshold effectivly)
#-> Bugfixed playerlvl and damage threshold

#-Changelog v6.2
#-> Fixed title of TO DO list
#-> Added contents of shoplist2 to globalcost
#-> Changed playerlvl modifier on enemy stats from * to +

#-Changelog v6.3
#-> Minor bugfixes for shop lists
#-> Fixes grammatical errors in gamble, fish and travel functions
#-> Discovered new bug: Roulette and blackjack remain unplayable no matter which town is set as currentdestination. Temporarily disabled destination checking
#-> Added suits to blackjack and displayed hand before bust
#-> Prevented playing slots with more money than owned
#-> Tweaked the combat function to be usable inside other functions or by typing fight('[enemy name here]')
#-> added gameover() function - when called, displays GAME OVER ('Bloody' font) then restarts the game
#-> Changed game name to GAME NAME and changed the font to 'Delta Corps Priest 1' on http://patorjk.com/software/taag/

#-Changelog v6.4
#-> Moved unnecessary items out of start()
#-> Forage chance is now affected by forage skill level instead of luck
#-> Shop menu is affected by current destination

#-Changelog v6.5
#-> Added cook function
#-> Orderded all functions except for start() load() map() and gameover() in alphabetical order
#-> Dishes created by cook() function have a use in the fight() function

#-Changelog v6.6
#-> What if the name had somthing to do with the name? - my cousin
#-> Added credits to gameover() function 
#-> Added charname, player can now name their charecter at start of game

#-Changelog v6.7
#-> Added tool to equipment function with its appropriate lists
#-> Fixed bug with tool in equipment fuction, after tool is equipped, doesn't show up
#-> Removed unessesary enemyarmor from player dmg
#-> Added main weapon has fuction in combat
#-> Fixed all problems adding main weapon combat
#-> Note: player will now have to equip weapon before combat otherwise error appears
#-> Added currently useless enemy difficulty, scale up in difficulty with 1 being oneshot and it gets harder and harder
#-> Added 2 more tool slots
#-> Changed defining enemy stats at the start of fight to use combat lvl not player lvl
#-> Fixed bug with unequiped main weapons not working
#-> Added armor has fuction in combat
#-> Fixed all problems created by adding armor to combat

#-Changelog v6.8
#-> Wrote an introduction that incorporates charname
#-> Built and tested a limited input only system to control player inputs (currently commented out)
#-> Removed the word 'Current' from equipment menu layout so as to fit better within the menu box

#-Changelog v7.0
#-> Finally added hunt() function

#-Changelog v7.1
#-> Fixed bug where fighting enemys wont give xp
#-> Fixed bug in hunt so the loop now is functional
#-> Added 2 thing to the bottom of the to do list
#-> Fixed fishing bug with sack of gold

#-Changelog v7.2
#-> Deleted enemylootlist as it was unessesary
#-> Added smithlist
#-> Added 2 things to the bottom of to do list
#-> Added plate to armorlist
#-> Added playerscrap

#-Changelog v8.0
#-> Added save / load functions that uses library pickle
#-> Added to the bottom so the code is more easily seen as a group

#-Changelog v8.1
#-> Finished blacksmith
#-> Added somthing to bottom of To Do list

#-Changelog v8.2
#-> Now import datetime
#-> Multipule save slots
#-> Save slots now display time last modified

#Changelog v8.3
#-> Incomplete bugfixes to blacksmith and other functions

#-Changelog v8.4
#-> Revammped save() to work on other computers
#-> Added global filedirect to bottom of file
#-> Redid the chance of gamble
#-> Added so the game asks the location of the savefiles

#-Changelog v8.5
#-> Gold now works fine was just a language error not a code error
#-> Added more items to blacksmith and locaition sort of affects blacksmith shop list
#-> Added a bear trap to hunt() function, max distance for an animal -2 when trap is laid
#-> Bear trap was causing to much greif so disabled it fo now, it still can be bought but has no function
#-> Location no longer affects balcksmith lists
#->.Doubled deck size for blackjack
#-> Now 1 in 100000 chance to hit jackpot in roulette as well a lower chances of winning overall for roulette
#-> Fully revamped gamble for all games to be less chance of winning

#----->TO DO
#- [ ] Write and implement a basic story/quest for the game
#- [√] Trial an 'input only' style of game, where the player's function options are restricted to prevent them from accessing dev tools
#- [√] Rebuild combat as mini-module 
#- [√] Better combat stat mechanics
#- [√] Add armor/blacksmith
#- [√] Add fishing bait to shop list 
#- [√] Set up level increase
#- [√] Make hunting function
#- [√] Levels influence activities
#- [√] Design map/destination
#- [√] Make destination functionality
#- [√] Design save/load system (pipe dream)
#- [√] Restrict activities based on equipment/location
#- [ ] Rework loot tables for all functions to have better rarity
#- [ ] Add usage for every item in every loot table
#- [√] Add a cook that takes food items and combines them to make dishes that add to health
#- [ ] Add a npc that will take scrap metal and any other items that could be used and turns it into useful things, i.e. blacksmith
#- [√] Player hp and level will increase after grinding
#- [√] Enemy difficulty is affected by player lvl
#- [√] Make some kind of equipment menu to equip weapons and armor
#- [√] Fix cook() so that only food items can be cooked; and so that every dish isn't printed as fish soup
#- [ ] Add dungeon for more exploration and loot as well as challange players with fighting enemies
#- [ ] Add apothacary for a specilised shop for healing and if spell will be added somthing to do with that
#-.[ ] Decrease the global sell cost of all items so gold is less common
#- [√] Revamp gamble so you dont win as often, like a 1/4 win/lose rate
#- [ } Make blacksmith shop lists vary depending on location



#in terminal, pip install clrprint

from clrprint import *

from datetime import datetime




import math
import time
import random
import pickle
import os


#globalcost format: ['item name',cost] - This is how much every item sells for
globalcost = [['sharpened sword',25],['trusty sword',15],['basic sword',10],['heavy crossbow',20],['basic crossbow',10],['basic fishing rod',10],['berries',1],['wild mushrooms',1],['eggs',1],
              ['healing herbs',3],['snapper',4],['salmon',4],['bass',4],['trout',4],['tuna',8],['health potion',6],['fishing bait',5],['big fishing rod',10],
              ['tasty fishing bait',8],['old gambeson',12],['cuirass',20],['shortbow',8],['longbow',8],['big shield',15],['mace',6],['bear trap',20]]

#mweaponlist format: ['weapon name',base attack,AP value]
global mweaponlist
mweaponlist = [['basic sword',5,0],['sharpened sword',8,1],['trusty sword',6,2],['mace',6,0]]

#sweaponlist format: ['weapon name',base attack,range]
global sweaponlist
sweaponlist = [['basic crossbow',3,5],['heavy crossbow',6,3],['shortbow',3,6],['longbow',5,10]]

#armorlist format: ['armor name',armor value]
global armorlist
armorlist = [['old gambeson',1],['cuirass',3],['plate',8],['big shield',2]]

#toollist format: ['tool name',tool bonus]
global toolist
toolist = [['basic fishing rod',1],['big fishing rod',2],['bear trap',4]]

#enemylist format: ['enemy name',base damage,base hp,base armor,xp amount]
enemylist = [['skeleton',7,20,1,5],['zombie',5,10,2,4],['bear',2,5,0,2],['goblin',2,3,3,1],['troll',18,22,2,10],['minotaur',28,15,2,10],['cave crawler',3,4,0,2]]

#foodhealthmod format: ['food name',value]
foodhealthmod = [['snapper',2],['salmon',2],['bass',2],['trout',2],['tuna',5],['eggs',2],['berries',2],['wild mushrooms',2]]

destinations = ['tamworth','tarrin','northwards','point garmsby','ledgetown','bamburgh','pendle','saxondale','squalls end','dunwich']

foragelist = ['some berries','some wild mushrooms','a nest of eggs','some healing herbs']

fishlist = ['a snapper','a snapper','a snapper','a snapper','a salmon','a salmon','a salmon','a salmon','a bass',
            'a bass','a bass','a bass','a trout','a trout','a trout','a trout','an old boot','some scrap metal','some scrap metal','a tuna','a tuna','a sack of gold']
#huntstats format: ['animal name',xp amount]
global huntstats
huntstats = [['deer',3],['rabbit',1],['boar',5]]
huntlist = ['a deer','a deer','a deer','a deer','a deer','a rabbit','a rabbit','a rabbit','a rabbit','a rabbit','a rabbit','a rabbit','a boar','a boar','a bear']

#shoplist format: ['item name',cost]
shoplist1 = [['trusty sword',20],['basic fishing rod', 12],['health potion',8],['fishing bait',5]]

shoplist2 = [['big fishing rod',15],['tasty fishing bait',10]]

#smithlist format: ['item name',cost in gold,[cost in scrap]]
smithlist = [['sharpened sword', 30, [15]], ['old gambeson', 20, [10]], ['cuirass', 37, [17]], ['plate', 55, [25]],['big shield', 30, [13]], ['mace', 14, [8]], ['bear trap', 31, [21]]]


global now
now = datetime.now()

global dt_string
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def start():

    global charname
    charname = 'N/A'
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
    global inv
    inv = ['basic sword', 'basic crossbow', 'basic fishing rod']
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
    global playerscrap
    playerscrap = 0
    
    
#    introduction()


def blacksmith():
    global gold
    global smithlist
    global currentdestination
    global playerscrap
    clrprint('The blacksmith greets you, and offers their sevice...',clr='d')
    time.sleep(0.5)
    buying = None
    while buying != 0:
        for y in smithlist:
            smithindex = smithlist.index(y)
        for item in smithlist:
            smithitemname = item[0]
            goldcost = item[1]
            scrapcost = item[2]
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
                        if buyitem in item:
                            buyitem = item
                    for sublist in smithlist:
                        if buyitem in sublist:
                            buycost = smithlist.index(sublist)
                            if smithlist[buycost][1] <= gold:
                                inv.append(buyitem)
                                gold -= smithlist[buycost][1]
                                clrprint('Purchased',buyitem,'for',str(smithlist[buycost][1]),'scrap',clr='g')
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

def checklevel():
    global combat
    global combatxp
    global combatmax
    while combatxp >= combatmax:
        combatxp -= combatmax
        combat += 1
        combatmax += 5
        clrprint('Your combat skill is now level',str(combat)+'!',clr='g')
    global hunting
    global huntingxp
    global huntingmax
    while huntingxp >= huntingmax:
        huntingxp -= huntingmax
        hunting += 1
        huntingmax += 5
        clrprint('Your hunting skill is now level',str(hunting)+'!',clr='g')
    global foraging
    global foragingxp
    global foragingmax
    while foragingxp >= foragingmax:
        foragingxp -= foragingmax
        foraging += 1
        foragingmax += 5
        clrprint('Your foraging skill is now level',str(foraging)+'!',clr='g')
    global fishing
    global fishingxp
    global fishingmax
    while fishingxp >= fishingmax:
        fishingxp -= fishingmax
        fishing += 1
        fishingmax += 5
        clrprint('Your fishing skill is now level',str(fishing)+'!',clr='g')
    global luck
    global luckxp
    global luckmax
    while luckxp >= luckmax:
        luckxp -= luckmax
        luck += 1
        luckmax += 5
        clrprint('Your luck skill is now level',str(luck)+'!',clr='g')
    global playerlvl
    global playerhp
    global playerhpmax
    while (combat + hunting + foraging + fishing + luck) > math.ceil(playerlvl * 4.5):
        playerlvl += 1
        playerhpmax += 5
        playerhp += 5

def cook():
    global foodhealthmod
    global math
    import math
    global time
    import time
    global inv
    inventory()
    food1 = input('What woud you like in your dish?\n').strip().lower()
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

def debugGiveStick():
    global debugtrack
    debugtrack += 1
    inv.append('Test Stick')

def dungeon():
    x = None    

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
                        if toolist != 'Nothing':
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
                        if toolist != 'Nothing':
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
                        if toolist != 'Nothing':
                            inv.append(toolequip3)
                        toolequip3 = b
                        inv.remove(b)
                else:
                    clrprint('Incorrect input. Please try again.',clr='r')
            else:
                clrprint('Incorrect input. Please try again.',clr='r')

def fight(enemy):
    global gold
    global inv
    global combatxp
    global combatmax
    global combat
    global playerhp
    global playerhpmax
    global enemylootlist
    global mweaponequip
    global armorequip
    global inv
    global enemylist
    global dungeonlist
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
        initiate = input('Would you like to fight or run?\n')
        initiate = initiate.strip()
        initiate = initiate.lower()
        if initiate == 'run':
            clrprint('You run away',clr='d')
        elif initiate == 'fight':
#while the enemy is above 0 hp the fight will continue
            while enemyhp > 0:
                action = input('What will you do? (attack/heal)\n')
                action = action.strip()
                action = action.lower()
                if action == 'attack':
                    #player dmg defined
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
                    #if enemy not dead the you will be hit by its attack
                    #player dmg defined
                    for y in armorlist:
                        if armorequip == 'Nothing':
                            armorindex = 0
                        elif  armorequip in y:
                            armorindex = y[1]
                    playerarmor = armorindex
                    if enemyhp > 0:
                        playerhp -= enemydmg - playerarmor
                        clrprint('The ' + enemy + ' hits you for ' + str(enemydmg) + ' damage!', clr='r')
                        clrprint('You are on ' + str(playerhp) + ' health!')
                elif action == 'heal':
                    if 'dish[1]' or 'dish[2]' or 'dish[3]' or 'dish[4]' or 'dish[5]' or 'dish[6]' or 'dish[7]' or 'dish[8]' or 'dish[8]' or 'dish[10]'in inv and playerhp < playerhpmax:
                        consumedish = input('Would you like to eat your dish? yes/no \n')
                        consumedish = consumedish.strip()
                        consumedish = consumedish.lower()
                        if consumedish == yes:
                            inv.remove('dish')
                            hpgain = foodhealthmod
                            playerhp += hpgain
                            if playerhp > playerhpmax:
                                playerhp = playerhpmax
                            clrprint('You eat your dish and gain ',str(hpgain),' HP!', clr='g')
                        elif consumedish == no:
                            if 'some healing herbs' in inv and playerhp < playerhpmax:
                                inv.remove('some healing herbs')
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
                else:
                    clrprint("I'm afraid that that is not an available option!", clr='r')
                if playerhp <= 0:
                    clrprint('You died!\n', clr='r')
                    time.sleep(1)
                    gameover()
                    enemyhp = -10000000
                    
            if -10000000 < enemyhp <= 0:
                combatxp += enemyxp
                clrprint('You defeated the ' + enemy + '!', clr='g')
                checklevel()
            if enemyhp == -10000000:
                combatxp += enemyxp
                print('')
            checklevel()
        else:
            clrprint('Im afraid that that is not an option', clr='d')
    else:
        clrprint('You dont have the adequate equipment to do this!',clr='d')

def fish():
    global gold
    global inv
    global fishlist
    global luckxp
    global luck
    global fishingxp
    global playerscrap
    baitmod = 1

    if 'basic fishing rod' == toolequip1 or toolequip2 or toolequip3:
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
        fishoutcome = fishlist[random.randint(0,22)]
        if fishchance > 20:
            if fishoutcome == 'a sack of gold':
                gold += 10
                clrprint('You found ' + str(fishoutcome)+ ' with 10 gold inside!',clr='y')
                fishingxp += 3
                luckxp += 1
                checklevel()
            else:
                clrprint('You caught ' + str(fishoutcome)+'!',clr='g')
                if fishoutcome == 'some scrap metal':
                    playerscrap += random.randint(1,3)
                    fishingxp += random.randint(1,2)
                    checklevel()
                else:
                    fishoutcome = fishoutcome.strip()
                    cut = fishoutcome.index(' ') + 1
                    inv.append(fishoutcome[cut:])
                    fishingxp += random.randint(1,2)
                    checklevel()
        else:
            clrprint('You caught nothing.',clr='r')
    else:
        clrprint('You don\'t have a fishing rod equipped!',clr='r')

def forage():
    global foraging
    global foragingxp
    clrprint('You wander through the forest...',clr='d')
    time.sleep(1)
    foragechance = random.randint(1,30)*math.ceil(foraging/4)
    forageresult = foragelist[random.randint(0,3)]
    if foragechance > 15:
        clrprint('After searching for a while, you find '+forageresult+'!',clr='g')
        if forageresult == 'a nest of eggs':
            forageresult = 'some eggs'
            cut = forageresult.index(' ') + 1
            inv.append(forageresult[cut:])
            foragingxp += random.randint(1,4)
            checklevel()
        else:
            cut = forageresult.index(' ') + 1
            inv.append(forageresult[cut:])
            foragingxp += random.randint(1,4)
            checklevel()
    else:
        clrprint('After searching for a while, you find nothing.',clr='r')
    encounterchance = random.randint(1, 20)
    if encounterchance == 1:
        fight('bear')

def gamble(amount):
    global luck
    global luckxp
    global gold
    import random
    import math
    global currentdestination
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
                        checklevel()
                    elif random.randint(1, 10000) > 8500:
                        if choice == 'red':
                            clrprint('It landed on red and you won ' + str(amount*2) + ' gold!',clr='g')
                            luckxp = luckxp + random.randint(1,5)
                            gold += amount*2
                            checklevel()
                        elif choice == 'black':
                            clrprint('It landed on red and you lost!',clr='r')
                    elif random.randint(1, 10000) < 1500:
                        if choice == 'black':
                            clrprint('It landed on black and you won ' + str(amount*3) + ' gold!',clr='g')
                            luckxp = luckxp + random.randint(1,5)
                            gold += amount*2
                            checklevel()
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
                        print("You have blackjack! You win!")
                        gold += amount * 2
                        luckxp = luckxp + random.randint(1,5)
                        checklevel()
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
                        print("Dealer busts! You win!")
                        luckxp = luckxp + random.randint(1,5)
                        gold += amount * 2
                        checklevel()
                    elif handvalue(playerhand) > handvalue(dealerhand):
                        print("You won!")
                        clrprint('You got',amount*2,'gold!',clr='y')
                        luckxp = luckxp + random.randint(1,5)
                        gold += amount * 2
                        checklevel()
                    elif handvalue(playerhand) == handvalue(dealerhand):
                        print("Push.")
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
                    checklevel()
                elif reel1 == reel2 == reel3:
                    if reel1 == "cherry":
                        win = amount * 3
                        luckxp += 2
                        checklevel()
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
                    checklevel()
                else:
                    print("Sorry, you didn't win anything this time.")

def hunt():
    global huntstats
    global hunting
    global huntingxp
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
                        clrprint('Your shot misses.',clr='r')
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
                        checklevel()
                        break
            

def inventory():
    clrprint('\n<==========INVENTORY==========>',clr='d')
    global inv
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

def stats():
    checklevel()
    clrprint('\n<==========CHARACTER==========>',clr='d')
    clrprint('+','Level : '+str(playerlvl),clr='r,y') 
    clrprint('+','Current Health : '+str(playerhp)+'/'+str(playerhpmax),clr='r,y')
    clrprint('+','Combat level : '+str(combat),clr='red')
    clrprint('+','» Level progress : '+str(combatxp)+'/'+str(combatmax),clr='r,p')
    clrprint('+','Hunting level : '+str(hunting),clr='red')
    clrprint('+','» Level progress : '+str(huntingxp)+'/'+str(huntingmax),clr='r,p')
    clrprint('+','Foraging level : '+str(foraging),clr='red')
    clrprint('+','» Level progress : '+str(foragingxp)+'/'+str(foragingmax),clr='r,p')
    clrprint('+','Fishing level : '+str(fishing),clr='red')
    clrprint('+','» Level progress : '+str(fishingxp)+'/'+str(fishingmax),clr='r,p')
    clrprint('+','Luck level : '+str(luck),clr='red')
    clrprint('+','» Level progress : '+str(luckxp)+'/'+str(luckmax),clr='r,p')
    clrprint('<=============================>',clr='d')

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
    #Helpful code at https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python, just replace dill with pickle
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtstring = now.strftime("%d/%m/%Y %H:%M")
    filepath1 = filedirect+'/savefile1'
    filesize1 = os.path.getsize(filepath1)
    statinfo1 = os.stat(filepath1)
    modificationtime1 = datetime.fromtimestamp(statinfo1.st_mtime)
    filepath2 = filedirect+'/savefile3'
    filesize2 = os.path.getsize(filepath2)
    statinfo2 = os.stat(filepath2)
    modificationtime2 = datetime.fromtimestamp(statinfo2.st_mtime)
    filepath3 = filedirect+'/savefile2'
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
        file_name = 'savefile1'
        savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
                'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
                'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
                'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
        with open(file_name,'wb') as file:
            pickle.dump(savelist, file)  # Store all the names first
            for value in savelist:
                pickle.dump(eval(value), file) # Store the objects themselves
        clrprint('Saved to slot 1',clr='g')
    elif saveslot  in 'slot 2':
        file_name = 'savefile2'
        savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
                'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
                'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
                'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
        with open(file_name,'wb') as file:
            pickle.dump(savelist, file)  # Store all the names first
            for value in savelist:
                pickle.dump(eval(value), file) # Store the objects themselves
        clrprint('Saved to slot 2',clr='g')
    elif saveslot in 'slot 3':
        file_name = 'savefile3'
        savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
                'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
                'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
                'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
        with open(file_name,'wb') as file:
            pickle.dump(savelist, file)  # Store all the names first
            for value in savelist:
                pickle.dump(eval(value), file) # Store the objects themselves
        clrprint('Saved to slot 3',clr='g')
    else:
        clrprint('Thats not an avalible otption!')
            
def load():
    global filedirect
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtstring = now.strftime("%d/%m/%Y %H:%M")
    filepath1 = filedirect+'/savefile1'
    filesize1 = os.path.getsize(filepath1)
    statinfo1 = os.stat(filepath1)
    modificationtime1 = datetime.fromtimestamp(statinfo1.st_mtime)
    filepath2 = filedirect+'/savefile3'
    filesize2 = os.path.getsize(filepath2)
    statinfo2 = os.stat(filepath2)
    modificationtime2 = datetime.fromtimestamp(statinfo2.st_mtime)
    filepath3 = filedirect+'/savefile2'
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
    loadslot = input('')
    loadslot.strip
    loadslot.lower
    #Helpful code at https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python, just replace dill with pickle
    if loadslot in 'slot 1':
        file_name = 'savefile1'
    elif loadslot in 'slot 2':
        file_name = 'savefile2'
    elif loadslot in 'slot 3':
        file_name = 'savefile3}'
    else:
        clrprint('Thats not and avalible option!',clr='r')
    g = globals()
    with open(file_name,'rb') as file:
        savelist = pickle.load(file)  # Get the names of stored objects
        for value in savelist:
            g[value] = pickle.load(file)    # Get the objects themselve



        
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
    text1 = '''
It was a long journey, but you've finally reached your destination. You step down from the ship onto the docks at Point Garmsby, the first town you'll vist in this new land.
Point Garmsby is a cosy town, with many houses and a bustling main street. Before you begin exploring the town, a man who must be the Mayor approaches you...'''
    for x in text1:
        clrprint(x,clr='d',end='')
        time.sleep(0.01)
    charname = input('\nGood afternoon young adventurer! My name is Mayor Berny. What is your name?\n')
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
        
global filedirect
#filedirect = input ('Please input your game directory\n')
start()
##while currentdestination == 'Point Garmsby':
##    time.sleep(0.1)
##    clrprint('\nYour available options are: inventory, equipment, fish, forage, shop, cook, town hall',clr='p')
##    action = input()
##    if action == 'inventory':
##        inventory()
##    elif action == 'equipment':
##        equipment()
##    elif action == 'fish':
##        fish()
##    elif action == 'forage':
##        forage()
##    elif action == 'shop':
##        shop()
##    elif action == 'cook':
##        cook()
##    elif action == 'town hall':
##        clrprint('This code does not exist right now',clr='r')
##    else:
##        clrprint('That is not an accepted input. Please try again.',clr='r')
