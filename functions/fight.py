from clrprint import *
import math, time, random

class Fight:
    def __init__(self, enemylist, mweaponlist, armorlist, checklevel):
        self.enemylist = enemylist
        self.mweaponlist = mweaponlist
        self.armorlist = armorlist
        self.checklevel = checklevel

        self.pdata = {}
        self.inv = []

    def load_player_data(self):
        with open('data/playerData.py', 'r') as file:
            for line in file:
                key, val = line.strip().split('=')
                if val.isnumeric():
                    val = int(val)
                self.pdata[key] = val

        self.playerhp = self.pdata["playerhp"]
        self.playerhpmax = self.pdata["playerhpmax"]
        self.combat = self.pdata["combat"]
        self.combatxp = self.pdata["combatxp"]
        self.mweaponequip = self.pdata["mweaponequip"]
        self.armorequip = self.pdata["armorequip"]
        self.foodhealthmod = self.pdata["foodhealthmod"]

    def load_inventory(self):
        with open('data/inventory.txt', 'r') as file:
            self.inv = file.read().split(',')[:-1]

    def get_enemy_stats(self, enemy_name):
        for e in self.enemylist:
            if enemy_name in e:
                enemydmg = e[1] + math.ceil(self.combat / 2)
                enemyhp = e[2] + math.ceil(self.combat / 4)
                enemyarmor = e[3] + math.ceil(self.combat / 6)
                enemyxp = e[4]
                return enemydmg, enemyhp, enemyarmor, enemyxp

        raise ValueError("Enemy not found")

    def get_weapon_damage(self):
        for w in self.mweaponlist:
            if self.mweaponequip in w:
                return w[1]
        return 1  # fists

    def get_armor_defence(self):
        for a in self.armorlist:
            if self.armorequip in a:
                return a[1]
        return 0

    def save(self):
        self.pdata.update({
            "playerhp": self.playerhp,
            "combatxp": self.combatxp
        })

        with open('data/playerData.py', 'w') as file:
            for key, val in self.pdata.items():
                file.write(f"{key}={val}\n")

        with open('data/inventory.txt', 'w') as file:
            for i in self.inv:
                file.write(i + ",")

    def start(self, enemy_name):
        self.load_player_data()
        self.load_inventory()

        if "basic sword" not in self.inv and "sharpened sword" not in self.inv:
            clrprint("You dont have the adequate equipment to do this!", clr="d")
            return

        enemydmg, enemyhp, enemyarmor, enemyxp = self.get_enemy_stats(enemy_name)

        clrprint(f"You encounter a {enemy_name}!", clr="d")
        clrprint(f"HP = {self.playerhp}/{self.playerhpmax}", clr="p")

        while True:
            choice = input("Would you like to fight or run?\n").strip().lower()
            if choice == "run":
                clrprint("You run away", clr="d")
                return
            elif choice == "fight":
                break

        while enemyhp > 0:
            action = input("What will you do? (attack/heal)\n").strip().lower()

            if action == "attack":
                weapon_dmg = self.get_weapon_damage()
                dmg = weapon_dmg + self.combat + random.randint(1, 4)

                enemyhp -= dmg
                clrprint(f"You hit the {enemy_name} for {dmg} damage!", clr="g")

                if enemyhp > 0:
                    armour = self.get_armor_defence()
                    taken = max(0, enemydmg - armour)
                    self.playerhp -= taken
                    clrprint(f"The {enemy_name} hits you for {taken} damage!", clr="r")

            elif action == "heal":
                if "health potion" in self.inv and self.playerhp < self.playerhpmax:
                    self.inv.remove("health potion")
                    heal = random.randint(10, 15)
                    self.playerhp = min(self.playerhp + heal, self.playerhpmax)
                    clrprint(f"You heal {heal} HP!", clr="g")
                else:
                    clrprint("No healing items!", clr="r")

            else:
                clrprint("That is not a valid action!", clr="r")

            if self.playerhp <= 0:
                clrprint("You died!", clr="r")
                time.sleep(1)
                gameover()
                return

        clrprint(f"You defeated the {enemy_name}!", clr="g")
        self.combatxp += enemyxp
        self.checklevel.checklevel()
        self.save()
