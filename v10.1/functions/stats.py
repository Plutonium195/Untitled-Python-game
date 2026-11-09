from clrprint import *

import math

from functions.checklevel import *


class stats:
    def stats():
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
        checklevel.checklevel()
        # header is 25 characters long - halfway is 12
        global charname

        if (len(charname) % 2) == 0:
            #length is an even number
            even = True
        else:
            even = False

        edge = (math.floor((29 - len(charname))/2))

        print('<',end='')
        for i in range(edge):
            print('=',end='')
        print(charname,end='')
        for i in range(edge):
            print('=',end='')
        if even == True:
            print('=',end='')
        print('>')
        clrprint('+','Level : '+str(playerlvl),clr='y') 
        clrprint('+','Current Health : '+str(playerhp)+'/'+str(playerhpmax),clr='y')
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

        pdata.update({'playerlvl': playerlvl, 'playerhp': playerhp, 'playerhpmax': playerhpmax, 'combat': combat, 'combatxp': combatxp, 'combatmax': combatmax, 'hunting': hunting, 'huntingxp': huntingxp,
                  'huntingmax': huntingmax, 'foraging': foraging, 'foragingxp': foragingxp, 'foragingmax': foragingmax, 'fishing': fishing, 'fishingxp': fishingxp, 'fishingmax': fishingmax, 'luck': luck, 'luckxp': luckxp, 'luckmax': luckmax})
        with open('data/playerData.py','w') as file:
            for key in pdata:
                  val = pdata[key]
                  file.write(f'{key}={val}\n')


        
