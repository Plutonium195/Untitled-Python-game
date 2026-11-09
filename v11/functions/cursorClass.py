import pygame
from data.assetLoader import *

def cursorDefault():
    #Set custom cursor
    cursorSurface = loadImage('sprites/cursorOpen.png')
    cursorSurface = pygame.transform.scale(cursorSurface, (60, 60))
    hotspot = (20, 20)
    customCursor = pygame.cursors.Cursor(hotspot, cursorSurface)
    pygame.mouse.set_cursor(customCursor)

def cursorClick():
    #Set custom cursor
    cursorSurface = loadImage('sprites/cursorClosed.png')
    cursorSurface = pygame.transform.scale(cursorSurface, (60, 60))
    hotspot = (20, 20)
    customCursor = pygame.cursors.Cursor(hotspot, cursorSurface)
    pygame.mouse.set_cursor(customCursor)