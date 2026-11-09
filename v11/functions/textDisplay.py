import pygame
pygame.init()


def drawText(surface, text, font, color, rect):
    lines = []
    paragraphs = text.split("\n")
    
    for paragraph in paragraphs:
        words = paragraph.split(" ")
        currentLine = ""
        
        for word in words:
            testLine = currentLine + word + " "
            if font.size(testLine)[0] <= rect.width:
                currentLine = testLine
            else:
                lines.append(currentLine)
                currentLine = word + " "
        
        lines.append(currentLine)
        
    spacing = 0
    for line in lines:
        if spacing + font.get_height() > rect.height:
            break
        
        textSurface = font.render(line, False, color)
        surface.blit(textSurface, (rect.x, rect.y + spacing))
        spacing += font.get_height()