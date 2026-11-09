import json
from data.assetLoader import *
from functions.buttonClass import Button
from functions.textDisplay import *
#contains two functions:
#one to call inside game.event() loop
#and another to call inside main game() loop


class Equipment:
    def __init__(self, titleRect, bodyRect, buttonRect, color, buttonColor1, buttonColor2, hoverColor, sound):
        self.titleRect = titleRect
        self.bodyRect = bodyRect
        self.buttonRect = buttonRect
        self.textColor = color
        self.sound = sound
        with openFile("data/equipment.json","r") as file:
            self.equipmentList = json.load(file)
        self.title = heading1.render("Equipment", False, color)
        self.body = f"""Main: {self.equipmentList["mainWeapon"]}\n
Secondary: {self.equipmentList["secondWeapon"]}\n
Armor: {self.equipmentList["armor"]}\n
Tool 1: {self.equipmentList["tool1"]}\n
Tool 2: {self.equipmentList["tool2"]}\n
Tool 3: {self.equipmentList["tool3"]}
    """
        self.button = Button(buttonRect.x, buttonRect.y, buttonRect.width, buttonRect.height, buttonColor1, "Change equipment?", body1, buttonColor2, hoverColor, sound)

    
    def pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.buttonRect.collidepoint(event.pos):
                if self.sound:
                    self.sound.play()
                return True
        return False
    
    def display(self, surface):
        surface.blit(self.title, self.titleRect)
        drawText(surface, self.body, body1, self.textColor, self.bodyRect)
        self.button.draw(surface)