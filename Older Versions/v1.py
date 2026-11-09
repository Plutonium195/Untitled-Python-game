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

def inventory():
    print('<==========INVENTORY==========>')
    for x in inv:
        print(x)
    print('<=============================>')
