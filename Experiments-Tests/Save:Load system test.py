

import pickle


def start():

    global charname
    charname = 'yourname'
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

global savelist
savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
            'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
            'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
            'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
savestring = ",".join(savelist)
def save():
    global savelist
    global savestring
    # pickle the list
    with open("savefile.pkl", "wb") as f:
        pickle.dump(savestring, f)
def load():
    global savestring
    global savelist
    # unpickle the list
    with open("savefile.pkl", "rb") as f:
        savestring = pickle.load(f)
    charname = savestring[0]
    debugtrack = savestring[1]
    playerlvl = savestring[2]
    playerhp = savestring[3]
    playerhpmax = savestring[4]
    gold = savestring[5]
    inv = savestring[6]
    combat = savestring[7]
    combatxp = savestring[8]
    combatmax = savestring[9]
    hunting = savestring[10]
    huntingxp = savestring[11]
    huntingmax = savestring[12]
    foraging = savestring[13]
    foragingxp = savestring[14]
    foragingmax = savestring[15]
    fishing = savestring[16]
    fishingxp = savestring[17]
    fishingmax = savestring[18]
    luck = savestring[19]
    luckxp = savestring[20]
    luckmax = savestring[21]
    currentdestination = savestring[22]
    mweaponequip = savestring[23]
    sweaponequip = savestring[24]
    toolequip1 = savestring[25]
    toolequip2 = savestring[26]
    toolequip3 = savestring[27]
    playerscrap = savestring[28]
def devsave():
    # unpickle the list
    with open("neworld.pkl", "rb") as f:
        savestring = pickle.load(f)
def devload():
    savestring = ",".join(savelist)
    # pickle the list
    with open("neworld.pkl", "wb") as f:
        pickle.dump(savestring, f)
  
