import pygame

mouse_image_filename = "images/mouse.png"
mouse_cursor = pygame.image.load(mouse_image_filename)

def intmouse(screen):
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    pygame.mouse.set_visible(False)
    screen.blit(mouse_cursor, (x, y))