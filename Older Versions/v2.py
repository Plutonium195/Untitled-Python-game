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

def gamble(amount):
    global luck
    global luckxp
    global gold
    import random
    import math
    gold = gold - amount
    choice = input('Red or Black?\n')
    choice = choice.strip()
    choice = choice.lower()
    jackpotchance = 1
    if random.randint(1, 10000) <= 1*luck:
        print('You hit the jackpot!')
        print('You won ' + str(amount*100) + ' gold')
        luck = luck + 1
        gold = gold + amount*100
    elif random.randint(1, 10000) > 3000:
        if choice == 'red':
            print('It landed on red and you won ' + str(amount*2) + ' gold!')
            luckxp = luckxp + 1
            gold = gold + amount*2
        elif choice == 'black':
            print('It landed on red and you lost!')
    elif random.randint(1, 10000) < 3000:
        if choice == 'black':
            print('It landed on black and you won ' + str(amount*3) + ' gold!')
            luckxp = luckxp + 1
            gold = gold + amount*3
        elif choice == 'red':
            print('It landed on black and you lost!')
    else:
        print('You lost!')
