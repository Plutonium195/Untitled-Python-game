#Add a cook that takes 2 food items from an input and combines them to make dishes that add both their health modifiers
global foodhealthmod
foodhealthmod = [['snapper',1],['salmon',2],['bass',3],['trout',4],['tuna',5],['eggs',3],['berries',1],['wild mushrooms',2],['healing herbs', random.randint(1,5)]]

#def cook():
    global foodhealthmod
    global math
    import math
    global time
    import time
    global inv
    inventory()
    food1 = input('What woud you like in your dish?\n')
    food2 = input('Anything else?\n')
    if food1 and food2 in inv:
        food1 = food1.strip()
        food1 = food1.lower()
        food2 = food2.strip()
        food2 = food2.lower()
        inv.remove(food2)
        inv.remove(food1)
        healthmod = 0
        for food in [food1, food2]:
            for item in foodhealthmod:
                if item[0] == food:
                    healthmod += item[1]
                    break
        time.sleep(2)
        if food1 == 'eggs' and food2 == 'wild mushrooms':
            dish = 'sauteed mushroom ömelette'
            clrprint('You are served a ' + dish + ' ' + str(healthmod) + '!',clr='d')
        elif food1  == 'snapper' or 'salmon' or 'bass' or 'trout' or 'tuna':
            dish = 'fish soup'
            clrprint('You are served a ' + dish + ' with ' + food2 + ' ' + str(healthmod) + '!',clr='d')
        elif food1 == 'eggs' and food2 != 'wild mushrooms':
            dish = food2 + ' ömelette'
            clrprint('The cook whips up a ' + dish + ' ' + str(healthmod) + '!',clr='d')
        elif food1 == food2:
            dish = 'even bigger ' + food1
            clrprint('The cook looks at you strangely',clr='d')
            time.sleep(1)
            clrprint('The cook returns and serves you ' + dish + ' ' + str(healthmod),clr='d')
        elif food1 or food2 == 'wild mushrooms':
            dish = 'sauteed mushrooms and ' + (food1 or food2 != 'wild mushrooms')
            clrprint('The cook prepares some ' + dish + ' ' + str(healthmod) + '!',clr='d')
        inv.append(dish + '[' + str(healthmod) + ']')
    else:
        clrprint('You dont have that currently',clr='r')

