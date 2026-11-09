


from clrprint import *

def start():
    global math
    import math
    global random
    import random
    global gold
    gold = 10
    global inv
    inv = [str(gold)+' gold', 'basic sword', 'basic crossbow', 'basic fishing rod']
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

def debugGiveStick():
    inv.append('Test Stick')

def inventory():
    clrprint('\n<==========INVENTORY==========>',clr='default')
    for x in inv:
        clrprint('+ ',x,clr='default,red')
    clrprint('<=============================>',clr='default')

def stats():
    clrprint('\n<==========CHARACTER==========>',clr='default')
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
    clrprint('<=============================>',clr='default')
    
def start():
    global math
    import math
    global random
    import random
    global gold
    gold = 10
    global inv
    inv = [str(gold)+' gold', 'basic sword', 'basic crossbow', 'basic fishing rod']
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
    fishlist = [' a snapper',' a salmon',' a bass',' a trout',' a tuna',' an old boot',' some scrap metal',' a sack of gold!']

def inventory():
    print('<==========INVENTORY==========>')
    inv = [str(gold)+' gold', 'basic sword', 'basic crossbow', 'basic fishing rod']
    for x in inv:
        print(x)
    print('<=============================>')

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
            gold = gold + amount*100
        elif random.randint(1, 10000) > 3000:
            if choice == 'red':
                clrprint('It landed on red and you won ' + str(amount*2) + ' gold!',clr='g')
                luckxp = luckxp + 1
                gold = gold + amount*2
            elif choice == 'black':
                clrprint('It landed on red and you lost!',clr='r')
        elif random.randint(1, 10000) < 3000:
            if choice == 'black':
                clrprint('It landed on black and you won ' + str(amount*3) + ' gold!',clr='g')
                luckxp = luckxp + 1
                gold = gold + amount*3
            elif choice == 'red':
                clrprint('It landed on black and you lost!',clr='r')
        else:
            clrprint('You lost! :(',clr='r')

    

