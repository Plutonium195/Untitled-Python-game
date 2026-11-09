from clrprint import *
import math

class Checklevel:
    def __init__(self):
        self.pdata = {}

    def load_player_data(self):
        self.pdata = {}
        with open('data/playerData.py', 'r') as file:
            for line in file:
                key, val = line.strip().split('=')
                if val.isnumeric():
                    val = int(val)
                self.pdata[key] = val

        # unpack for easier use
        self.combat = self.pdata["combat"]
        self.combatxp = self.pdata["combatxp"]
        self.combatmax = self.pdata["combatmax"]

        self.hunting = self.pdata["hunting"]
        self.huntingxp = self.pdata["huntingxp"]
        self.huntingmax = self.pdata["huntingmax"]

        self.foraging = self.pdata["foraging"]
        self.foragingxp = self.pdata["foragingxp"]
        self.foragingmax = self.pdata["foragingmax"]

        self.fishing = self.pdata["fishing"]
        self.fishingxp = self.pdata["fishingxp"]
        self.fishingmax = self.pdata["fishingmax"]

        self.luck = self.pdata["luck"]
        self.luckxp = self.pdata["luckxp"]
        self.luckmax = self.pdata["luckmax"]

        self.playerlvl = self.pdata["playerlvl"]
        self.playerhp = self.pdata["playerhp"]
        self.playerhpmax = self.pdata["playerhpmax"]

    def save(self):
        self.pdata.update({
            "playerlvl": self.playerlvl,
            "playerhp": self.playerhp,
            "playerhpmax": self.playerhpmax,

            "combat": self.combat,
            "combatxp": self.combatxp,
            "combatmax": self.combatmax,

            "hunting": self.hunting,
            "huntingxp": self.huntingxp,
            "huntingmax": self.huntingmax,

            "foraging": self.foraging,
            "foragingxp": self.foragingxp,
            "foragingmax": self.foragingmax,

            "fishing": self.fishing,
            "fishingxp": self.fishingxp,
            "fishingmax": self.fishingmax,

            "luck": self.luck,
            "luckxp": self.luckxp,
            "luckmax": self.luckmax
        })

        with open('data/playerData.py', 'w') as file:
            for key, val in self.pdata.items():
                file.write(f"{key}={val}\n")

    def checklevel(self):
        self.load_player_data()

        # Combat
        while self.combatxp >= self.combatmax:
            self.combatxp -= self.combatmax
            self.combat += 1
            self.combatmax += 5
            clrprint(f'Your combat skill is now level {self.combat}!', clr='g')

        # Hunting
        while self.huntingxp >= self.huntingmax:
            self.huntingxp -= self.huntingmax
            self.hunting += 1
            self.huntingmax += 5
            clrprint(f'Your hunting skill is now level {self.hunting}!', clr='g')

        # Foraging
        while self.foragingxp >= self.foragingmax:
            self.foragingxp -= self.foragingmax
            self.foraging += 1
            self.foragingmax += 5
            clrprint(f'Your foraging skill is now level {self.foraging}!', clr='g')

        # Fishing
        while self.fishingxp >= self.fishingmax:
            self.fishingxp -= self.fishingmax
            self.fishing += 1
            self.fishingmax += 5
            clrprint(f'Your fishing skill is now level {self.fishing}!', clr='g')

        # Luck
        while self.luckxp >= self.luckmax:
            self.luckxp -= self.luckmax
            self.luck += 1
            self.luckmax += 5
            clrprint(f'Your luck skill is now level {self.luck}!', clr='g')

        # Player level scaling
        while (self.combat + self.hunting + self.foraging + self.fishing + self.luck) > math.ceil(self.playerlvl * 4.5):
            self.playerlvl += 1
            self.playerhpmax += 5
            self.playerhp += 5

        self.save()
