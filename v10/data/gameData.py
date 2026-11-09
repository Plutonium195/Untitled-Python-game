from clrprint import *

from datetime import datetime

import math, time, random, pickle, os

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

fishlist = ['a snapper','a snapper','a snapper','a snapper','a salmon','a salmon','a salmon','a salmon','a bass',
            'a bass','a bass','a bass','a trout','a trout','a trout','a trout','an old boot','some scrap metal',
            'some scrap metal','a tuna','a tuna','a sack of gold']

foragelist = ['some berries','some wild mushrooms','a nest of eggs','some healing herbs']

#huntstats format: ['animal name',xp amount]
huntstats = [['deer',3],['rabbit',1],['boar',5]]
huntlist = ['a deer','a deer','a deer','a deer','a deer','a rabbit','a rabbit','a rabbit','a rabbit','a rabbit','a rabbit','a rabbit','a boar','a boar','a bear']

#shoplist format: ['item name',cost]
shoplist1 = [['trusty sword',20],['basic fishing rod', 12],['health potion',8],['fishing bait',5]]

shoplist2 = [['big fishing rod',15],['tasty fishing bait',10]]

#smithlist format: ['item name',cost in gold,[cost in scrap]]
smithlist = [['sharpened sword', 30, [15]], ['old gambeson', 20, [10]], ['cuirass', 37, [17]], ['plate', 55, [25]],['big shield', 30, [13]], ['mace', 14, [8]], ['bear trap', 31, [21]]]

#foodhealthmod format: ['food name',value]
foodhealthmod = [['snapper',2],['salmon',2],['bass',2],['trout',2],['tuna',5],['eggs',2],['berries',2],['wild mushrooms',2]]

destinations = ['tamworth','tarrin','northwards','point garmsby','ledgetown','bamburgh','pendle','saxondale','squalls end','dunwich']

randomnames = [['Marjorie Dickmane'],['Edison Brookee'],['Eadda Wakefielde'],['Eduart Hightowere'],['Cedrica Burns'],['Lari Summers'],['Dena Haileye']]

#communitynotice format: ['author','message']
random_index = random.randint(0, len(randomnames) - 1)
communitynotice = [['Mayor Berny','I would like to announce a holiday tommorow in honor of you all and your amazing work'],
                   ['Mayor Berny',f'I would like to say happy birthday to {randomnames[random_index][0]}'],[f'{randomnames[random_index][0]}','Need help fixing my house']]

