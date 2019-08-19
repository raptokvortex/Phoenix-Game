import pygame

screen_width = 1000
screen_height = 800

close = False

pygame.init()

win = pygame.display.set_mode([screen_width, screen_height])


menu_loop = True
while menu_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_loop = False
            close = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        pass
    if keys[pygame.K_a]:
        pass

    win.fill((0, 0, 0))

game_loop = True
if close:
    game_loop = False

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_loop = False
            close = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        pass
    if keys[pygame.K_a]:
        pass

    pygame.display.update()
pygame.quit()

# changes