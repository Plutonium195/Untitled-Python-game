#-Change list: V6.1
#-> Added comments to def start() with possible additions
#-> Added things to TO D' list
#-> Ticked off a few things on TO D' list
#-> Added a new shoplist (shoplist2)
#-> Added food heatlh values
#-> Updated checklevel() into all of gamble()
#-> Added playerlvl to start(), checklvl() and stats()
#-> Player hp and level will increase after grinding
#-> Added debugLevelUpAllSkills()
#-> Added debug tracker
#-> Bugfix
#-> Changed goblin health to 3
#-> Changed enemy health, base damage and base armor to be afftected by player level
#-> Enemy armor mod now affects its damage taken (damage threshold effectivly)
#-> Bugfix

#-


#----->TO D’
#- [ ] Rebuild combat as semi module 
#- [ ] Better combat stat mechanics
#- [ ] Add armor
#- [√] Add fishing bait to shop list 
#- [√] Set up level increase
#- [ ] Make hunting function
#- [√] Levels influence activities
#- [√] Design map/destination
#- [ ] Make destination functionality
#- [ ] Design save/load system
#- [√] Restrict activities based on equipment/location
#- [ ] Rework loot tables for all functions to have better rarity
#- [ ] Add usage for every item in every loot table
#- [ ] Add a cook that takes food items and combines them to make dishes that add to health
#- [ ] Add a npc that will take scrap metal and any other items that could be used and turns it into useful things
#- [√] Player hp and level will increase after grinding
#- [√] Enemy difficulty is affected by player lvl






#in terminal, run <pip install clrprint>

from clrprint import *

globalcost = [['sharpened sword',25],['basic sword',10],['basic crossbow',10],['basic fishing rod',10],['berries',1],['wild mushrooms',1],['eggs',1],['healing herbs',3],['snapper',4],['salmon',4]
              ,['bass',4],['trout',4],['old boot',1],['scrap metal',1],['tuna',8],['healing potion',6],['fishing bait',5]]

#weaponstats format: ['weapon name',base attack,AP value]
weaponstats = [['basic sword',5,0],['basic crossbow',3,2],['sharpened sword',8,1]]
#enemylist format: ['enemy name',base damage, base hp, base armor, xp amount]
enemylist = [['skeleton',5,10,1,4],['zombie',6,10,2,4],['bear',2,5,0,2],['goblin',2,3,3,1]]

dungeonlist = ['goblin','skeleton','zombie']

def start():
    global math
    import math
    global time
    import time
    global random
    import random
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
    global foodhealthmod
    #foodhelthmod format
    foodhealthmod = [['snapper',2],['salmon',2],['bass',2],['trout',2],['tuna',5],['eggs',2],['berries',2],['wild mushrooms',2]]
    global currentdestination
    currentdestination = 'Point Garmsby'
    global destinations
    destinations = ['tamworth','tarrin','northwards','point garmsby','ledgetown','bamburgh','pendle','saxondale','squalls end','dunwich']
    global enemylootlist
    enemylootlist = ['a rusty sword','some rotten food','an empty money sack','a empty envelope from their family','a trout','an old boot','some scrap metal','a sack of marbles']
    global foragelist
    foragelist = ['some berries','some wild mushrooms','a nest of eggs','some healing herbs']
    global fishlist
    fishlist = ['a snapper','a snapper','a snapper','a snapper','a salmon','a salmon','a salmon','a salmon','a bass',
    'a bass','a bass','a bass','a trout','a trout','a trout','a trout','an old boot','an old boot','some scrap metal','some scrap metal','a tuna','a tuna','a sack of gold']
    global shoplist1
    #add to other shop lists: trusty sword, big fishing rod 
    shoplist1 = [['sharpened sword',30],['basic fishing rod', 12],['healing potion',8],['fishing bait',5]]
    global shoplist2
    shoplist2 = [['trusty sword',20],['big fishing rod',15],['tasty fishing bait',10]]


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
    while (combat + hunting + foraging + fishing + luck) >playerlvl > math.ceil(playerlvl * 4.5):
        playerlvl += 1
        playerhpmax += 5
        playerhp += 5

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

def inventory():
    clrprint('\n<==========INVENTORY==========>',clr='default')
    global inv
    clrprint('+ ',str(gold),'gold',clr='d,r')
    for x in inv:
        clrprint('+ ',x,clr='d,r')
    clrprint('<=============================>',clr='default')

def stats():
    checklevel()
    clrprint('\n<==========CHARACTER==========>',clr='d')
    clrprint('+','Level : '+str(playerlvl),clr='y') 
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
    

def gamble(amount):
    global luck
    global luckxp
    global gold
    import random
    import math
    global currentdestination
    clrprint('Games:',clr='p')
    clrprint('»Roulette',clr='p')
    clrprint('»Blackjack',clr='p')
    clrprint('»Slots',clr='p')
    gamechoice = input('What game would you like to play?\n')
    gamechoice = gamechoice.strip()
    gamechoice = gamechoice.lower()
    if gamechoice == 'roulette':
        if currentdestination == 'ledgetown' or 'bamburgh' or 'dunwich':
            clrprint('You cant play that here',clr='r')
        else:
            if amount+1 > gold:
                clrprint("You don't have that much money!",clr='r')
            else:
                gold -= amount
                choice = input('Red or Black?\n')
                choice = choice.strip()
                choice = choice.lower()
                jackpotchance = 1
                if random.randint(1, 10000) <= 1*luck:
                    clrprint('You hit the jackpot!',clr='y')
                    clrprint('You won ' + str(amount*100) + ' gold',clr='y')
                    luck = luck + 1
                    gold += amount*100
                    checklevel()
                elif random.randint(1, 10000) > 7000:
                    if choice == 'red':
                        clrprint('It landed on red and you won ' + str(amount*2) + ' gold!',clr='g')
                        luckxp = luckxp + random.randint(1,5)
                        gold += amount*2
                        checklevel()
                    elif choice == 'black':
                        clrprint('It landed on red and you lost!',clr='r')
                elif random.randint(1, 10000) < 3000:
                    if choice == 'black':
                        clrprint('It landed on black and you won ' + str(amount*3) + ' gold!',clr='g')
                        luckxp = luckxp + random.randint(1,5)
                        gold += amount*3
                        checklevel()
                    elif choice == 'red':
                        clrprint('It landed on black and you lost!',clr='r')
                else:
                    clrprint('You lost! :(',clr='r')
                
    elif gamechoice == 'blackjack':
        if currentdestination == 'dunwich' or 'northward' or 'pendle' or 'saxondale':
            clrprint('You cant play that here',clr='r')
        else:
            if amount+1 > gold:
                clrprint("You don't have that much money!",clr='r')
            else:
                gold -= amount
                # Define a function to calculate the value of a hand
                def handvalue(hand):
                    value = 0
                    numaces = 0
                    for card in hand:
                        if card == 'A':
                            numaces += 1
                            value += 11
                        elif card in ['K', 'Q', 'J']:
                            value += 10
                        else:
                            value += int(card)
                    while value > 21 and numaces > 0:
                        value -= 10
                        numaces -= 1
                    return value

                
                # Initialize variables for the game
                deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
                random.shuffle(deck)
                #removing cards from deck and putting them in players hand
                playerhand = [deck.pop(), deck.pop()]
                dealerhand = [deck.pop(), deck.pop()]
                
                # Check if the player has blackjack
                if handvalue(playerhand) == 21:
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
                        if handvalue(playerhand) > 21:
                            print("Bust! You lose.")
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
                    print("You win!")
                    luckxp = luckxp + random.randint(1,5)
                    gold += amount * 2
                    checklevel()
                elif handvalue(playerhand) == handvalue(dealerhand):
                    print("Push.")
                else:
                    print("You lose.")
                
    elif gamechoice == 'slots':
        gold -= amount
        print("Spinning the reels...")
        reel1 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"])
        reel2 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"])
        reel3 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"])
        print(f"The reels stop on: {reel1}, {reel2}, {reel3}")

        # Determine the outcome
        if reel1 == reel2 == reel3 == "seven":
            win = amount * 10
            print("JACKPOT! You win " + str(win) +  " gold!")
            gold += amount * 10
            luck += 1
            checklevel()
        elif reel1 == reel2 == reel3:
            if reel1 == "cherry":
                win = amount * 3
                luckxp += 2
                checklevel()
                print("Three cherries! You win" + str(win) + 'gold!')
            else:
                luckxp += 2
                print(f"Three {reel1}s! You win {amount*3} gold!")
                gold += amount * 3
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            win = amount * 2
            print("Two of a kind! You win " + str(win) +" gold !")
            gold += amount * 2
            luckxp += 1
            checklevel()
        else:
            print("Sorry, you didn't win anything this time.")

def forage():
    global luck
    global foragingxp
    clrprint('You wander through the forest...',clr='d')
    time.sleep(1)
    foragechance = random.randint(1,30)*math.ceil(luck/4)
    forageresult = foragelist[random.randint(0,3)]
    if foragechance > 15:
        clrprint('After searching for a while, you find '+forageresult+'!',clr='d')
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
        clrprint('After searching for a while, you find nothing.',clr='d')
    time.sleep(1)
    encounterchance = random.randint(1, 200)
    if encounterchance <= 10:
        fight()

def fish():
    global gold
    global inv
    global fishlist
    global luck
    global fishingxp
    baitmod = 1

    if 'basic fishing rod' in inv:
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
                clrprint('You found ' + str(fishoutcome)+'!',clr='g')
                fishoutcome = fishoutcome.strip()
                cut = fishoutcome.index(' ') + 1
                inv.append(fishoutcome[cut:])
                fishingxp += random.randint(1,2)
                checklevel()
        else:
            clrprint('You caught nothing.',clr='r')
        time.sleep(1)
        encounterchance = random.randint(1, 400)
        if encounterchance <= 10:
            fight()

    else:
        clrprint('You dont have the adequate equipment to do this!',clr='d')

            
def shop():
    global gold
    global shoplist
    clrprint('The merchant greets you, and displays his wares...',clr='d')
    time.sleep(0.5)
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

def fight():
    global gold
    global inv
    global combatxp
    global combatmax
    global combat
    global playerhp
    global playerhpmax
    global enemylootlist
    global inv
    global enemylist
    global dungeonlist
    if 'basic sword' or 'sharpened sword' in inv:
#determining enemy stats
        enemy = dungeonlist[random.randint(1,len(dungeonlist))-1]
        for y in enemylist:
            if enemy in y:
                enemyindex = enemylist.index(y)
        enemydmg = enemylist[enemyindex][1] + math.ceil(playerlvl/2)
        enemyhp = enemylist[enemyindex][2] + math.ceil(playerlvl/4)
        enemyarmor = enemylist[enemyindex][3] + math.ceil(playerlvl/6)
        enemyxp = enemylist[enemyindex][4]
#fight start func
        clrprint('You encounter a',enemy+'!', clr='d')
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
                    dmg = (random.randint(1, 10) + combat * math.ceil(luck/4)) - enemyarmor
                    if dmg > 0:
                        clrprint('You hit the ' + enemy + ' for ' + str(dmg) + ' damage!', clr='g')
                        enemyhp -= dmg + enemyarmor
                    elif dmg <= 0:
                        clrprint('You deal no damage to the ' + enemy + '!', clr='r')
                    #if enemy not dead the you will be hit by its attack
                    if enemyhp > 0:
                        playerhp -= enemydmg
                        clrprint('The ' + enemy + ' hits you for ' + str(enemydmg) + ' damage!', clr='r')
                        clrprint('You are on ' + str(playerhp) + ' health!')
                elif action == 'heal':
                    if 'some healing herbs' in inv and playerhp < playerhpmax:
                        inv.remove('some healing herbs')
                        hp_gain = random.randint(5, 10)
                        playerhp += hp_gain
                        if playerhp > playerhpmax:
                            playerhp = playerhpmax
                        clrprint('You heal yourself for ' + str(hpgain) + ' HP!', clr='g')
                    elif 'healing potion' in inv and playerhp < playerhpmax:
                        inv.remove('healing potion')
                        hp_gain = random.randint(10, 15)
                        playerhp += hpgain
                        if playerhp > playerhpmax:
                            playerhp = playerhpmax
                        clrprint('You heal yourself for ' + str(hp_gain) + ' HP!', clr='g')
                    else:
                        clrprint('You have no healing herbs or health potions!', clr='r')
                else:
                    clrprint("I'm afraid that that is not an available option!", clr='r')
                if playerhp <= 0:
                    clrprint('You died!', clr='r')
                    enemyhp = -5000
            if -4000 < enemyhp <= 0:
                clrprint('You defeated the ' + enemy + '!', clr='g')
                #loot results for enemy defeat
                lootchance = random.randint(1,60) * math.ceil(luck/4)
                lootresult = enemylootlist[random.randint(0,3)]
                combatxp = combatxp + (enemyxp * random.randint(1,3))
                if lootchance > 75 - random.randint(1, 10) - math.ceil(luck/4):
                    clrprint('In the ' + enemy + ', you find '+lootresult+'!',clr='d')
                    if lootresult != 'a empty envelope from their family' or 'an empty money sack':
                        inv.append(lootresult)
                elif lootchance > 100 - math.ceil(luck/6):
                    dropped_gold = math.ceil(luck/4)
                    clrprint('The ' + enemy + ' dropped ' + str(dropped_gold) + ' gold!',clr='y')
                    gold = dropped_gold + gold
                else:
                    clrprint("The",enemy,'drops nothing', clr='p')
            if enemyhp == -5000:
                print('')
            checklevel()
        else:
            clrprint('Im afraid that that is not an option', clr='d')
    else:
        clrprint('You dont have the adequate equipment to do this!',clr='d')

def travel():
    global currentdestination
    global destinations
    map()
    clrprint('You are currently in ' + currentdestination,clr='g')
    destination = input('Where would you like to go?\n')
    destination = destination.strip()
    destination = destination.lower()
    if destination in destinations:
        currentdestination = destination
        load = '''
Loading...0%
Loading...10%
Loading...50%
Loading...90%
Loading...100%
        '''
        for x in load:
            print(x,end='')
            time.sleep(random.randint(2,14)/100)
        print('')
        clrprint('After ' + str(random.randint(1,5)) + ' days you arrive in the town of ' + destination,clr='g')
    else:
        clrprint('That isnt a location!',clr='r')
    


    
def map():
    print('....................................................................................................')
    print('....................................................................................................')
    print('....................................................................................................')
    print('....................................................................................................')
    print('..............................:.....................................................................')
    print('.............................::.:..............................:....................................')
    print('..............................: .:.......:.......     :.........  ..................................')
    print('............................:: .  .....::.             .......     :................................')
    print('............................: :...    ..                           .:...............................')
    print('........................:.:.  ...::::                                .... ..:.......................')
    print('........................:          ..                Northwards             :.............:.........')
    print('.........................                                  *                    ......:..:..........')
    print('........................:.                                  |                         . :...........')
    print('........................:.         * Bamburgh_______________|_________              ...:............')
    print('........................                                /              \           .:...............')
    print('.....................                                  /                \         .:................')
    print('..............:.                              Pendle *   .:.. Ledgetown *            ..:............')
    print('...........::..                                      |   .::.........    \             .............')
    print('...........:                                         |     .:........:    \           .:............')
    print('............                                         |      .:.........    \          .:............')
    print('.........:.                                          |       .:......:.     \          :............')
    print('............:.                   _________________Tarrin *  .:.......:.     |          .:...........')
    print('...............:.               /                           :.........:. Point Garmsby.::...........')
    print('................:.             /                           .:.:.................. *  .:.............')
    print('.................:.      _____/                           .:......................:.:...............')
    print('...................     /                         .....  .:.........................................')
    print('................::     /                 .:      .:.................................................')
    print('...........:..  ..   * Tamworth         ...:      :.................................................')
    print('..........:          |             ...:.:..:::    :.................................................')
    print('.........:.          |             .:........:    :..................................:....:.........')
    print('.......:..           |              :........   .:..................................:     .:........')
    print('.......:             * Saxondale              .:.....................................     .:........')
    print('.......:.            |_________             .:..................................:. .....   ...::....')
    print('.........:.                    \            ::..................................:.::.....:...:.:....')
    print('.........:.                     \            ......:............................:...................')
    print('.........:.                      \__               :................................................')
    print('...........:                        \              .:...............................................')
    print('.......... :.                        * Dunwich     .:...............................................')
    print('............:.                        \            .:...............................................')
    print('...........:..           .....         \          .:................................................')
    print('..........:..:....     .:.........      \        .:.................................................')
    print('..................:..................    \        ..:........................::... .................')
    print('.......................................   \_______  ..:.............................   .:...........')
    print('......................................::          \   ..:...........................:   ..:.........')
    print('.......................................:           \     :...........................:..  :.........')
    print('........................................            *    .:............................::...........')
    print('.....................................:.  Squalls End      .:........................................')


start()
load = '''
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
'''
for x in load:
    print(x,end='')
    time.sleep(random.randint(2,14)/100)
clrprint('\nNEW GAME SUCCESSFULLY LOADED\n',clr='g')
time.sleep(2)
clrprint('\nWelcome To...\n',clr='d')
time.sleep(1)
clrprint(' ______   __  __     ______        ______     ______     __    __     ______ ',clr='p')  
clrprint('/\__  _\ /\ \_\ \   /\  ___\      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\ ',clr='p')   
clrprint('\/_/\ \/ \ \  __ \  \ \  __\      \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\  ',clr='p')  
clrprint('   \ \_\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ ',clr='p') 
clrprint('    \/_/   \/_/\/_/   \/_____/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ ',clr='p') 
'''                                                                              
