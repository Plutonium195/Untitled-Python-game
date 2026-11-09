import pygame, json, math
from data.assetLoader import *

#Import stat change sound
statUpSound = loadSound('levelUp.mp3')
statUpSound.set_volume(0.1)

# Load player data
with openFile("data/playerData", "r") as file:
    playerData = json.load(file)

# Initialize display stats for smooth animation
displayStats = {}
for key in playerData:
    if "Exp" in key or key == "health":
        displayStats[key] = float(playerData[key])

# Function to save data to JSON
def jsonDump(file, data):
    with openFile(file, "w") as file:
        json.dump(data, file, indent=4)

# Updated stats system
def drawStatBar(screen, x, y, label, value, currentExp, maxExp, barColor):
    labelSurf = body1.render(f"{label} {value}", False, color4)
    screen.blit(labelSurf, (x, y))
    
    barWidth = 180
    barHeight = 16
    barX = x
    barY = y + 30
    
    pygame.draw.rect(screen, color2, (barX, barY, barWidth, barHeight))
    
    fillWidth = int((currentExp / maxExp) * barWidth)
    pygame.draw.rect(screen, barColor, (barX, barY, fillWidth, barHeight))
    
    pygame.draw.rect(screen, color4, (barX, barY, barWidth, barHeight), 2)
    
    # Display currentExp as float and maxExp as integer
    expSurf = body2.render(f"{int(currentExp)}/{int(maxExp)}", False, color5)  # Convert maxExp to int
    screen.blit(expSurf, (barX + barWidth + 10, barY - 2))


# Update display stats smoothly
def updateDisplayStats(player, displayDict, speed=0.4):
    for key in displayDict:
        target = player[key]
        current = displayDict[key]
        
        # Smooth interpolation
        displayDict[key] += (target - current) * speed
        
        # Snap if very close
        if abs(displayDict[key] - target) < 0.01:
            displayDict[key] = target

# Stat change function
def statChange(player, statExp, amount):
    stat = statExp.replace("Exp", "")
    expMax = statExp + "Max"
    player[statExp] += amount
    if player[statExp] < 0:
        player[statExp] = 0
    elif player[statExp] >= player[expMax]:
        if player[stat] % 5 == 0:
            player[expMax] = math.floor(player[expMax] * 1.5)
        player[statExp] = 0
        player[stat] += 1
        statUpSound.play()

def healthChange(player, amount):
    player["health"] += amount
    
    # Clamp health so it never exceeds maxHealth
    if player["health"] > player["maxHealth"]:
        player["health"] = player["maxHealth"]
    
    # prevent negative health
    if player["health"] < 0:
        player["health"] = 0

# Draw all stats using display values
def drawAllStats(screen, player, screenWidth, screenHeight):
    startX = 31 * screenWidth / 40 - 20
    startY = screenHeight / 4 + 40
    spacing = 60
    
    drawStatBar(screen, startX, startY,
                "Health",
                f'{player["health"]}/{player["maxHealth"]}',
                displayStats["health"],
                player["maxHealth"],
                color6)
    
    drawStatBar(screen, startX, startY + spacing,
                "Strength",
                player["strength"],
                displayStats["strengthExp"],
                player["strengthExpMax"],
                pygame.Color("#A13D2D"))
    
    drawStatBar(screen, startX, startY + spacing * 2,
                "Agility",
                player["agility"],
                displayStats["agilityExp"],
                player["agilityExpMax"],
                pygame.Color("#2D8A3E"))
    
    drawStatBar(screen, startX, startY + spacing * 3,
                "Constitution",
                player["constitution"],
                displayStats["constitutionExp"],
                player["constitutionExpMax"],
                pygame.Color("#C27C2C"))
    
    drawStatBar(screen, startX, startY + spacing * 4,
                "Intelligence",
                player["intelligence"],
                displayStats["intelligenceExp"],
                player["intelligenceExpMax"],
                pygame.Color("#2D6CC2"))
    
    drawStatBar(screen, startX, startY + spacing * 5,
                "Wisdom",
                player["wisdom"],
                displayStats["wisdomExp"],
                player["wisdomExpMax"],
                pygame.Color("#7A3DB8"))