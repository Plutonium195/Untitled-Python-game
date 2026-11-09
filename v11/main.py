import pygame, sys, json, random
from functions.cursorClass import *
from functions.textDisplay import *
from functions.buttonClass import *
from data.assetLoader import *
from functions.equipmentClass import *
from functions.playerStats import *

# VERY NECESSARY LINE OF CODE
pygame.init()
pygame.mixer.init()

screenWidth = 1200
screenHeight = 700
clock = pygame.time.Clock()
gameState = 'title'
invOpen = False
equipmentOpen = False

# track repeat setup
currentMusic = None
MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)
tracks = ("mainTrack1.mp3", "mainTrack2.mp3", "mainTrack3.mp3")

# Load inventory
with openFile("data/inventory.txt", "r") as file:
    inv = file.read().split(',')[:-1]
invText = ""
for i in inv:
    invText += f"• {i}\n"

# Load player data
with openFile("data/playerData", "r") as file:
    playerData = json.load(file)

# Initialize screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game Name")
logo = loadImage('sprites/logo.png')
pygame.display.set_icon(logo)

# Set custom cursor
cursorDefault()

# Load sounds
buttonPress = loadSound('buttonPress.mp3')
buttonPress.set_volume(10)



# Load and scale background for title screen
titleBackground = loadImage("backgrounds/titleBackground.png")
titleBackground = pygame.transform.scale2x(titleBackground)

# Render title text
titleSurf = title1.render("Game Name", False, color5)
titleRect = titleSurf.get_rect(center=(screenWidth / 2, screenHeight / 2))

# Definitions for various surfaces and rects to be used in display
borderRect = pygame.rect.Rect(30, 30, screenWidth - 60, screenHeight - 60)
invBackgroundRect = pygame.rect.Rect(3 * screenWidth / 4, 40, (screenWidth / 4) - 40, screenHeight - 80)
invTextRect = pygame.rect.Rect(31 * screenWidth / 40, screenHeight / 5, (screenWidth / 6) + 30, 3 * screenHeight / 4)
invTitleSurf = heading1.render("Pockets", False, color4)
invTitleRect = invTitleSurf.get_rect(bottomleft=(31 * screenWidth / 40, (screenHeight / 5) - 10))
playerNameSurf = heading1.render(playerData["name"], False, color4)
playerNameRect = playerNameSurf.get_rect(bottomleft=(31 * screenWidth / 40, (screenHeight / 3) - 30))
playerDataTextRect = pygame.rect.Rect(31 * screenWidth / 40, screenHeight / 4 + 15, (screenWidth / 6), 3 * screenHeight / 5 + 20)
gameOverSurf = title1.render("Game Over", False, color0)
gameOverRect = gameOverSurf.get_rect(center=(screenWidth/2,screenHeight/2))
creditsSurf = title1.render("Credits", False, color4)
creditsRect = creditsSurf.get_rect(center=(screenWidth/2, 80))

# Sets rect for background images to fit to
imageRect = pygame.rect.Rect(35, 35, 415, 630)
testBackground = loadImage("backgrounds/testBackground.png")
testBackground2 = loadImage("backgrounds/testBackground2.png")
testBackground2 = pygame.transform.scale(testBackground2, (415, 630))

# Load animated background frames (GIF)
backgroundFrames = []
for i in range(6):  # change 6 to however many frames in the gif
    frame = loadImage(f"backgrounds/testGif/testFrame{i}.png")
    frame = pygame.transform.scale(frame, (415, 630))
    backgroundFrames.append(frame)

currentFrame = 0
animationSpeed = 0.15  # lower = slower animation

creditsText = '''
                        [[[---Developed by---]]]
               [[[---┏┓•               ┏┓    ┓•   ---]]]
               [[[---┣ ┓┏┓┏┓┏╋┏┓┏┓┏┳┓  ┗┓╋┓┏┏┫┓┏┓┏---]]]
               [[[---┻ ┗┛ ┗ ┛┗┗┛┛ ┛┗┗  ┗┛┗┗┻┗┻┗┗┛┛---]]]
                  [[[-----------------------------]]]                    
     
                  [[[---Designed and Produced by---]]]
                      [[[---Lucian Van Horne---]]]
                              [[[------]]]
                        [[[---Spencer Holt---]]]
                              [[[------]]]
                     [[[---Special Thanks To ---]]]
                   [[[---Those nerds at Github ---]]]
           [[[---The little helpers at Stackoverflow---]]]
                              [[[------]]]
                       [[[---And You!---]]]
                              [[[------]]]
'''
creditsTextRect = pygame.Rect(0, 0, screenWidth - 200, screenHeight - 200)
creditsTextRect.center = (screenWidth // 2, screenHeight // 2 + 40)

# Stand in for description text (replace with modular system)
sampleText = """Non-Disclosure Agreement to protect confidential Information disclosed by Everline Capital Investment Holdings Group LLC (the Company) in respect to the Company’s practice and procedures as well as all current and future projects, products and plans. This Agreement is issued by the Company for the purpose of safeguarding, preserving, and protecting its Confidential Information, whether presently existing or hereafter developed, disclosed, or acquired.

By executing this Agreement, both parties acknowledge that any and all Confidential Information pertaining to the Company is considered the full and total property of the Company; any distribution of confidential information by or on behalf of the recipient is strictly prohibited. The term “Confidential Information” shall be interpreted in the broadest and most inclusive manner permissible under applicable law and encompasses any and all information defined above, as well as information not necessarily marked as ‘confidential’, ‘proprietary’, or similar, but also information that, by its nature, content, or context, a reasonable person exercising prudent business judgment would understand to be confidential, proprietary, or sensitive. The failure to label or identify any information as confidential shall in no way diminish or negate its status as Confidential Information under this Agreement.
"""
sampleTextRect = pygame.rect.Rect((3 * screenWidth / 8) + 15, 45, (3 * screenWidth / 8) - 20, (3 * screenHeight / 5) - 50)

# Assign buttons
newGameButton = Button(screenWidth / 2, 2 * screenHeight / 3, 100, 40, color1, "New Game", body2, color3, color3light, buttonPress)
loadGameButton = Button(screenWidth / 2, 2 * screenHeight / 3 + 50, 100, 40, color1, "Load Game", body2, color3, color3light, buttonPress)
quitButton = Button(screenWidth / 2, 2 * screenHeight / 3 + 100, 100, 40, color1, "Quit", body2, color3, color3light, buttonPress)
backButton = Button(screenWidth - 65, 55, 40, 40, color1, "Back", body2, color4, color4light, buttonPress)
invButton = Button(screenWidth - 75, 55, 50, 30, color1, "Pockets", body2, color4, color4light, buttonPress)
settingsButton = Button(3 * screenWidth / 4 + 40, 55, 70, 40, color1, "Settings", body2, color4, color4light, buttonPress)
equipmentButton = Button(3 * screenWidth / 4 + 54, 85, 100, 40, color1, "Equipment", body2, color4, color4light, buttonPress)
restartButton = Button(screenWidth / 2, 2 * screenHeight / 3, 100, 40, color6, "Restart", body2, color0, color4light, buttonPress)
creditsButton = Button(screenWidth / 2, 2 * screenHeight / 3 + 50, 100, 40, color6, "Credits", body2, color0, color4light, buttonPress)

# Assign debug buttons
debugHurtButton = Button(screenWidth - 65, 85, 40, 30, color1, "Hurt", body2, color4, color4light, buttonPress)
debugHealButton = Button(screenWidth - 65, 115, 40, 30, color1, "Heal", body2, color4, color4light, buttonPress)
debugUpStatButton = Button(screenWidth - 65, 145, 40, 30, color1, "StatUp", body2, color4, color4light, buttonPress)
debugDownStatButton = Button(screenWidth - 65, 175, 40, 30, color1, "StatDown", body2, color4, color4light, buttonPress)

equipmentButtonRect = pygame.rect.Rect(screenWidth-200, screenHeight-250, 150, 100)
equipment = Equipment(invTitleRect, invTextRect, equipmentButtonRect, color4, color1, color3, color3light, buttonPress)


# Main loop
while True:
    clock.tick(60)
    currentFrame += animationSpeed
    #if animated images (GIF)
    if currentFrame >= len(backgroundFrames):
        currentFrame = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursorClick()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            cursorDefault()
 
        # track repeat logic
        if event.type == MUSIC_END and gameState == "alive":
            pygame.mixer.music.load(soundPath(random.choice(tracks)))
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()

        if gameState == 'title':
            # title screen music
            if gameState == "title" and currentMusic != "title":
                pygame.mixer.music.load(soundPath("titleMusic.mp3"))
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
                currentMusic = "title"

            if newGameButton.pressed(event):
                gameState = 'alive'
                playerData["health"] = playerData["maxHealth"]
                jsonDump("data/playerData", playerData)
            elif loadGameButton.pressed(event):
                None
            elif quitButton.pressed(event):
                pygame.quit()
                sys.exit()
            
        elif gameState == 'alive':
            if gameState == "alive" and currentMusic != "alive":
                pygame.mixer.music.load(soundPath(random.choice(tracks)))
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
                currentMusic = "alive"
            if invOpen == False and equipmentOpen == False:
                if invButton.pressed(event):
                    invOpen = True
                elif settingsButton.pressed(event):
                    gameState = 'settings'
                elif equipmentButton.pressed(event):
                    equipmentOpen = True
                elif debugHurtButton.pressed(event):
                    healthChange(playerData, -1)
                    jsonDump("data/playerData", playerData)
                elif debugHealButton.pressed(event):
                    healthChange(playerData, 1)
                    jsonDump("data/playerData", playerData)
                elif debugUpStatButton.pressed(event):
                    statChange(playerData, "strengthExp", 5)
                    jsonDump("data/playerData", playerData)
                elif debugDownStatButton.pressed(event):
                    statChange(playerData, "strengthExp", -1)
                    jsonDump("data/playerData", playerData)
            
            elif invOpen == True:
                if backButton.pressed(event):
                    invOpen = False
                    
            elif equipmentOpen == True:
                if backButton.pressed(event):
                    equipmentOpen = False
                elif equipment.pressed(event):
                    None
            
        elif gameState == 'settings':
            if backButton.pressed(event):
                gameState = 'alive'
            
        elif gameState == 'dead':
            if gameState == "dead" and currentMusic != "gameOver":
                pygame.mixer.music.load(soundPath("deathSound.mp3"))
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                currentMusic = "gameOver"
            if restartButton.pressed(event):
                gameState = 'alive'
                playerData["health"] = playerData["maxHealth"]
                jsonDump("data/playerData", playerData)
            elif creditsButton.pressed(event):
                gameState = 'credits'
            
        elif gameState == 'credits':
            if gameState == "credits" and currentMusic != "creditsRoll":
                pygame.mixer.music.load(soundPath("creditsRoll.mp3"))
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                currentMusic = "creditsRoll"

        else:
            print('gameState error: event')
    
    if gameState == 'title':
        screen.blit(titleBackground, (0, 0))
        screen.blit(titleSurf, titleRect)
        
        newGameButton.draw(screen)
        loadGameButton.draw(screen)
        quitButton.draw(screen)
        
    elif gameState == 'alive':
        screen.fill(color1)
        #if using gif (GIF)
        screen.blit(backgroundFrames[int(currentFrame)], imageRect)
        #if static background (GIF)
        #screen.blit(testBackground2, imageRect)
        
        if invOpen == True:
            pygame.draw.rect(screen, color1, invBackgroundRect)
            backButton.draw(screen)
            screen.blit(invTitleSurf, invTitleRect)
            drawText(screen, invText, body1, color4, invTextRect)
            
        elif equipmentOpen == True:
            pygame.draw.rect(screen, color1, invBackgroundRect)
            backButton.draw(screen)
            equipment.display(screen)
            
        elif invOpen == False and equipmentOpen == False:
            invButton.draw(screen)
            settingsButton.draw(screen)
            equipmentButton.draw(screen)
            debugHurtButton.draw(screen)
            debugHealButton.draw(screen)
            debugUpStatButton.draw(screen)
            debugDownStatButton.draw(screen)
            screen.blit(playerNameSurf, playerNameRect)
            drawAllStats(screen, playerData, screenWidth, screenHeight)
        
        pygame.draw.rect(screen, color2, borderRect, 10)
        pygame.draw.line(screen, color2, (3 * screenWidth / 4, 30), (3 * screenWidth / 4, screenHeight - 32), 5)
        pygame.draw.line(screen, color2, (3 * screenWidth / 8, 30), (3 * screenWidth / 8, screenHeight - 32), 5)
        pygame.draw.line(screen, color2, (3 * screenWidth / 8, 3 * screenHeight / 5), (3 * screenWidth / 4, 3 * screenHeight / 5), 5)
        
        drawText(screen, sampleText, body1, color4, sampleTextRect)

    elif gameState == 'settings':
        screen.fill(color1)
        backButton.draw(screen)
        pygame.draw.rect(screen, color2, borderRect, 10)

    elif gameState == 'dead':
        screen.fill(color6)
        
        screen.blit(gameOverSurf, gameOverRect)
        restartButton.draw(screen)
        creditsButton.draw(screen)

    elif gameState == 'credits':
        screen.fill(color1)
        screen.blit(creditsSurf, creditsRect)
        lines = creditsText.split("\n")
        
        line_height = body1.get_height()
        total_height = len(lines) * line_height

        start_y = creditsTextRect.centery - total_height // 2

        for i, line in enumerate(lines):
            line_surface = body1.render(line.strip(), True, color4)
            line_rect = line_surface.get_rect(center=(screenWidth // 2, start_y + i * line_height))
            screen.blit(line_surface, line_rect)
    else:
        print('gameState error: gameloop')
    
    # Update display stats every frame
    if gameState == 'alive':
        updateDisplayStats(playerData, displayStats)
        if playerData["health"] <= 0:
           gameState = "dead"
    # Update screen with all changes made in current frame
    pygame.display.update()
