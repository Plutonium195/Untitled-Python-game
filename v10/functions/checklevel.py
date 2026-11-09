from clrprint import *
import math

class checklevel:
    def checklevel():
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
        pdata.update({'playerlvl': playerlvl, 'playerhp': playerhp, 'playerhpmax': playerhpmax, 'combat': combat, 'combatxp': combatxp, 'combatmax': combatmax,
                      'hunting': hunting, 'huntingxp': huntingxp,'huntingmax': huntingmax, 'foraging': foraging, 'foragingxp': foragingxp,
                      'foragingmax': foragingmax,'fishing': fishing, 'fishingxp': fishingxp, 'fishingmax': fishingmax, 'luck': luck,
                      'luckxp': luckxp, 'luckmax': luckmax})
        with open('data/playerData.py','w') as file:
            for key in pdata:
                  val = pdata[key]
                  file.write(f'{key}={val}\n')
