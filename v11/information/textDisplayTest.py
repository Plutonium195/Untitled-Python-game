import pygame

# =====================================================
# TERMINAL DISPLAY FUNCTION (IMAGE ON LEFT, TEXT RIGHT)
# =====================================================

def draw_terminal_display(
    screen,
    text,
    image,
    rect,
    font,
    text_color=(245, 223, 187),
    bg_color=(69, 69, 69),
    border_color=(69, 69, 69),
    padding=10,
    typing_progress=None,
    image_ratio=0.4
):

    # Background + Border
    pygame.draw.rect(screen, bg_color, rect)
    pygame.draw.rect(screen, border_color, rect, 2)

    # ========== IMAGE AREA ==========
    image_width = int(rect.width * image_ratio)

    image_area = pygame.Rect(
        rect.x + padding,
        rect.y + padding,
        image_width - padding,
        rect.height - padding * 2
    )

    scaled_image = pygame.transform.scale(
        image,
        (image_area.width, image_area.height)
    )
    screen.blit(scaled_image, image_area)

    # ========== TEXT AREA ==========
    text_area = pygame.Rect(
        rect.x + image_width + padding,
        rect.y + padding,
        rect.width - image_width - padding * 2,
        rect.height - padding * 2
    )

    # Typing effect
    if typing_progress is not None:
        text = text[:typing_progress]

    # Word wrapping
    wrapped_lines = []
    words = text.split(" ")
    line = ""

    for word in words:
        test_line = line + word + " "
        if font.size(test_line)[0] <= text_area.width:
            line = test_line
        else:
            wrapped_lines.append(line)
            line = word + " "
    wrapped_lines.append(line)

    # Render text
    y_offset = 0
    for line in wrapped_lines:
        rendered = font.render(" " + line.strip(), True, text_color)
        screen.blit(rendered, (text_area.x, text_area.y + y_offset))
        y_offset += font.get_height()


# =====================================================
# MAIN PROGRAM
# =====================================================

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Terminal Display")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Copperplate", 20)

# Load your image
image = pygame.image.load("v11/assets/test.png").convert_alpha()

terminal_rect = pygame.Rect(100, 100, 800, 400)

text = """
It was a long journey, but you've finally reached your destination. You step down from the ship onto the docks at Point Garmsby, the first town you'll visit in this new land. Point Garmsby is a cosy town with a bustling main street. Before you begin exploring, the Mayor approaches you...
"""

typing_progress = 0
typing_speed = 2  # characters per frame

running = True
while running:
    clock.tick(25)
    screen.fill((25, 25, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Typing animation
    if typing_progress < len(text):
        typing_progress += typing_speed

    draw_terminal_display(
        screen,
        text,
        image,
        terminal_rect,
        font,
        typing_progress=typing_progress
    )

    pygame.display.flip()

pygame.quit()
