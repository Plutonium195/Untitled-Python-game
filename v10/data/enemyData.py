from clrprint import *

from datetime import datetime

import math, time, random, pickle, os

from data.gameData import *

#enemylist format: ['enemy name',base damage,base hp,base armor,xp amount]
enemylist = [['skeleton',7,20,1,5],['zombie',5,10,2,4],['bear',2,5,0,2],['cave bear',2,6,0,2],['goblin',2,3,3,1],['troll',18,22,2,10],
['minotaur',30,20,2,10],['cave crawler',3,4,0,2],['teacher',1,5,2,0]]


dungeonfloor1 = ['goblin','cave crawler','cave bear']
dungeonfloor2 = ['goblin','cave crawler','zombie']
dungeonfloor3 = ['cave crawler','zombie','skeleton']
dungeonfloor4 = ['cave crawler','skeleton','zombie','troll']
dungeonfloor5 = ['cave crawler','skeleton','troll']
dungeonfloor6 = ['minotaur']
