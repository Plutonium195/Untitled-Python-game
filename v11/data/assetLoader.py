import pygame, os
pygame.init()

BASE = os.path.dirname(os.path.dirname(__file__))
ASSET_PATH = os.path.join(BASE, "assets")

#set default paths to be from v11 folder
def fontPath(name):
    return os.path.join(ASSET_PATH, "fonts", name)

def soundPath(name):
    return os.path.join(ASSET_PATH, "sounds", name)

def imagePath(name):
    return os.path.join(ASSET_PATH, "images", name)

def filePath(name):
    return os.path.join(BASE, name)


#import font file
def loadFont(name, size):
    return pygame.font.Font(fontPath(name), size)

#import sound file
def loadSound(name):
    return pygame.mixer.Sound(soundPath(name))

#import image file
def loadImage(name):
    return pygame.image.load(imagePath(name)).convert_alpha()

#open any file (usually data files)
def openFile(name, mode):
    return open(filePath(name), mode)


#define fonts
title1 = loadFont('black_chancery/BLKCHCRY.TTF', 140)
heading1 = loadFont('berylium/Berylium Rg.otf', 40)
heading2 = loadFont('berylium/Berylium Bd.ttf', 40)
body1 = loadFont('berylium/Berylium Rg.otf', 20)
body2 = loadFont('berylium/Berylium Bd.ttf', 20)

# Define fonts
color0 = pygame.Color("#0F0505")
color1 = pygame.Color('#253031')
color2 = pygame.Color("#315659")
color3 = pygame.Color("#2978A0")
color3light = pygame.Color("#4899C2")
color4 = pygame.Color("#BCAB79")
color4light = pygame.Color("#DCD3BA")
color5 = pygame.Color("#C6E0FF")
color6 = pygame.Color("#6c1712")