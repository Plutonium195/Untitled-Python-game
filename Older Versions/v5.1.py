
#in terminal, run <pip install clrprint>

from clrprint import *

globalcost = [['basic sword',10],['basic crossbow',10],['basic fishing rod',10],['some berries',1],['some wild mushrooms',1],['some eggs',1],['some healing herbs',3],['a snapper',4]
              ,['a salmon',4],['a bass',4],['a trout',4],['an old boot',1],['some scrap metal',1],['a tuna',8],['a rusty sword',3],['some rotten food',1],['a sack of marbles',5]]

def start():
    global math
    import math
    global time
    import time
    global random
    import random
    global playerhp
    global playerhpmax
    playerhp = 20
    playerhpmax = 20
    global gold
    gold = 10
    global inv
    inv = ['basic sword', 'basic crossbow', 'basic fishing rod']
    global combat
    global combatxp
    global combatmax
    global enemylootlist
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
    global enemylootlist
    enemylootlist = ['a rusty sword','some rotten food','an empty money sack','a empty envelope from their family','a trout','an old boot','some scrap metal','a sack of marbles']
    global foragelist
    foragelist = ['some berries','some wild mushrooms','a nest of eggs','some healing herbs']
    global fishlist
    fishlist = ['a snapper','a snapper','a snapper','a snapper','a salmon','a salmon','a salmon','a salmon','a bass',
    'a bass','a bass','a bass','a trout','a trout','a trout','a trout','an old boot','an old boot','some scrap metal','some scrap metal','a tuna','a tuna','a sack of gold']
    global shoplist
    shoplist = []

def debugGiveStick():
    inv.append('Test Stick')

def inventory():
    clrprint('\n<==========INVENTORY==========>',clr='default')
    global inv
    clrprint('+ ',str(gold),'gold',clr='d,r')
    for x in inv:
        clrprint('+ ',x,clr='d,r')
    clrprint('<=============================>',clr='default')

def stats():
    clrprint('\n<==========CHARACTER==========>',clr='d')
    clrprint('Current Health : '+str(playerhp)+'/'+str(playerhpmax)+'\n',clr='y')
    clrprint('Combat level : '+str(combat),clr='red')
    clrprint('- Level progress : '+str(combatxp)+'/'+str(combatmax),clr='purple')
    clrprint('Hunting level : '+str(hunting),clr='red')
    clrprint('- Level progress : '+str(huntingxp)+'/'+str(huntingmax),clr='purple')
    clrprint('Foraging level : '+str(foraging),clr='red')
    clrprint('- Level progress : '+str(foragingxp)+'/'+str(foragingmax),clr='purple')
    clrprint('Fishing level : '+str(fishing),clr='red')
    clrprint('- Level progress : '+str(fishingxp)+'/'+str(fishingmax),clr='purple')
    clrprint('Luck level : '+str(luck),clr='red')
    clrprint('- Level progress : '+str(luckxp)+'/'+str(luckmax),clr='purple')
    clrprint('<=============================>',clr='d')

def gamble(amount):
    global luck
    global luckxp
    global gold
    import random
    import math
    if amount > gold:
        clrprint("You don't have that much money!",clr='r')
    else:
        gold = gold - amount
        choice = input('Red or Black?\n')
        choice = choice.strip()
        choice = choice.lower()
        jackpotchance = 1
        if random.randint(1, 10000) <= 1*luck:
            clrprint('You hit the jackpot!',clr='y')
            clrprint('You won ' + str(amount*100) + ' gold',clr='y')
            luck = luck + 1
            gold += amount*100
        elif random.randint(1, 10000) > 3000:
            if choice == 'red':
                clrprint('It landed on red and you won ' + str(amount*2) + ' gold!',clr='g')
                luckxp = luckxp + 1
                gold += amount*2
            elif choice == 'black':
                clrprint('It landed on red and you lost!',clr='r')
        elif random.randint(1, 10000) < 3000:
            if choice == 'black':
                clrprint('It landed on black and you won ' + str(amount*3) + ' gold!',clr='g')
                luckxp = luckxp + 1
                gold += amount*3
            elif choice == 'red':
                clrprint('It landed on black and you lost!',clr='r')
        else:
            clrprint('You lost! :(',clr='r')

def forage():
    global luck
    clrprint('You wander through the forest...',clr='d')
    time.sleep(1)
    foragechance = random.randint(1,30)*math.ceil(luck/4)
    forageresult = foragelist[random.randint(0,3)]
    if foragechance > 15:
        clrprint('After searching for a while, you find '+forageresult+'!',clr='d')
        if forageresult == 'a nest of eggs':
            inv.append('some eggs')
        else:
            inv.append(forageresult)
    else:
        clrprint('After searching for a while, you find nothing.',clr='d')

def fish():
    global gold
    global inv
    global fishlist
    global luck
    baitmod = 1
    
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
    fishoutcome = fishlist[random.randint(0,3)]
    if fishchance > 20:
        if fishoutcome == 'a sack of gold!':
            gold += 10
            clrprint('You found' + str(fishoutcome)+ ' and gained 10 gold!',clr='d')
        else:
            clrprint('You found ' + str(fishoutcome)+'!',clr='d')
            fishoutcome = fishoutcome.strip()
            inv.append(fishoutcome)
    else:
        clrprint('You caught nothing.',clr='d')

            
def shop():
    global gold
    clrprint('The merchant greets you, and displays his wares...',clr='d')
    time.sleep(1)
    bors = input('Here to buy or sell?\n')
    bors = bors.strip()
    bors = bors.lower()
    if 'buy' in bors:
        print(shoplist)
    elif 'sell' in bors:
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
            
    else:
        print("I'm afraid that that is not an available option")


def fight():
    global gold
    global inv
    global combatxp
    global combatmax
    global combat
    global playerhp
    global playerhpmax
    global enemylootlist
    enemy = random.choice(['goblin','goblin','goblin','skeleton','skeleton','zombie'])
    if enemy == 'goblin':
        enemy_danger = 2 - math.ceil(luck/4)
        enemy_hp = random.randint(5, 10) * enemy_danger - math.ceil(luck/4)
        enemy_dmg = random.randint(1, 2) * enemy_danger - math.ceil(luck/4)
        enemy_drop_chance = 1
    elif enemy == 'skeleton':
        enemy_danger = 3 - math.ceil(luck/4)
        enemy_hp = random.randint(10, 20) * enemy_danger - math.ceil(luck/4)
        enemy_dmg = random.randint(1, 5) * enemy_danger - math.ceil(luck/4)
        enemy_drop_chance = 2
    elif enemy == 'zombie':
        enemy_danger = 3 - math.ceil(luck/4)
        enemy_hp = random.randint(10, 20) * enemy_danger - math.ceil(luck/4)
        enemy_dmg = random.randint(1, 10) * enemy_danger - math.ceil(luck/4)
        enemy_drop_chance = 3
    clrprint('You encounter a ' + enemy + '!', clr='d')
    while enemy_hp > 0:
        action = input('What will you do? (attack/heal)\n')
        action = action.strip()
        action = action.lower()
        if action == 'attack':
            dmg = random.randint(1, 10) * combat * math.ceil(luck/4)
            enemy_hp -= dmg
            clrprint('You hit the ' + enemy + ' for ' + str(dmg) + ' damage!', clr='g')
            if enemy_hp > 0:
                enemy_dmg_taken = enemy_dmg
                playerhp -= enemy_dmg_taken
                clrprint('The ' + enemy + ' hits you for ' + str(enemy_dmg_taken) + ' damage!', clr='r')
                clrprint('You are on ' + str(playerhp) + ' health!')
        elif action == 'heal':
            if 'some healing herbs' in inv and playerhp < playerhpmax:
                inv.remove('some healing herbs')
                hp_gain = random.randint(5, 10)
                playerhp += hp_gain
                if playerhp > playerhpmax:
                    playerhp = playerhpmax
                clrprint('You heal yourself for ' + str(hp_gain) + ' HP!', clr='g')
            else:
                clrprint('You have no healing herbs!', clr='r')
        else:
            clrprint("I'm afraid that that is not an available option!", clr='r')
        if playerhp <= 0:
            clrprint('You died!', clr='r')
            start()
    clrprint('You defeated the ' + enemy + '!', clr='g')
    lootchance = random.randint(1,60) * enemy_drop_chance * math.ceil(luck/4)
    lootresult = enemylootlist[random.randint(0,3)]
    if lootchance > 75 - random.randint(1, 10) - math.ceil(luck/4):
        clrprint('In the ' + enemy + ', you find '+lootresult+'!',clr='d')
        if lootresult != 'a empty envelope from their family' or 'an empty money sack':
            inv.append(lootresult)
    elif lootchance > 100 - math.ceil(luck/6):
        dropped_gold = enemy_drop_chance + math.ceil(luck/4)
        clrprint('The ' + enemy + ' dropped ' + str(dropped_gold) + ' gold!',clr='y')
        gold = dropped_gold + gold
    elif lootchance <= 1:
        clrprint('The ' + enemy + ' dropped a note ?!',clr='p')
        suicidenote = input('What would you like to read it?\n')
        suicidenote.strip()
        suicidenote.lower()
        if suicidenote == 'yes':
            clrprint('You open the note and read what it says\n','p')
            clrprint('"Ive had enough of this life/n Im going to the forest to end my miserable excuse for a life"','p')
        elif suicidenote == 'no':
            clrprint('Very well then','p')
        else:
            clrprint("I'm afraid that that is not an option", clr='p')
