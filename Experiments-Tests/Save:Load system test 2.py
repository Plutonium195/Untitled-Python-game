

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



def save():
    #Helpful code at https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python, just replace dill with pickle
    file_name = 'savefile'
    savelist = ['charname','debugtrack','playerlvl','playerhp','playerhpmax','gold','inv','combat','combatxp',
            'combatmax','hunting','huntingxp','huntingmax','foraging','foragingxp','foragingmax','fishing',
            'fishingxp','fishingmax','luck','luckxp','luckmax','currentdestination','mweaponequip',
            'sweaponequip','toolequip1','toolequip2','toolequip3','playerscrap']
    with open(file_name,'wb') as file:
        pickle.dump(savelist, file)  # Store all the names first
        for value in savelist:
            pickle.dump(eval(value), file) # Store the objects themselves
            
def load():
    #Helpful code at https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python, just replace dill with pickle
    file_name = 'savefile'
    g = globals()
    with open(file_name,'rb') as file:
        savelist = pickle.load(file)  # Get the names of stored objects
        for value in savelist:
            g[value] = pickle.load(file)    # Get the objects themselve
