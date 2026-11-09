import pygame
from data.assetLoader import *

pygame.init()

#defines a class for buttons
class Button:
    def __init__(self, x, y, width, height, bgColor, text, font, textColor, hoverColor, sound=None):
        self.rect = pygame.Rect(x-(width/2),y-(height/2),width,height)
        self.margin = self.rect.inflate(20,0)
        self.bgcolor = bgColor
        self.textcolor = textColor
        self.hoverColor = hoverColor
        self.text = text
        self.font = font
        self.sound = sound
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.bgcolor, self.margin, 0, 5)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            textSurface = self.font.render(self.text, False, self.hoverColor)
        else:
            textSurface = self.font.render(self.text, False, self.textcolor)
        textRect = textSurface.get_rect(center = self.rect.center)
        surface.blit(textSurface, textRect)
        
    def pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.sound:
                    self.sound.play()
                return True
        return False