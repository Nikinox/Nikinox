import pygame

pygame.init()

# creates the player
player = pygame.Rect(102, 102, 50, 50)  #x;y;width;height

# creates the window
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

running = True

while running:
    # manages the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # receives keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_ip(1, 0)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move_ip(0, -1)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move_ip(0, 1)

    # cleans the screen from the color left behind form the player
    screen.fill((0, 0, 0))

    # draws the player
    pygame.draw.rect(screen, (0, 0, 255), player)

    # updates the screen
    pygame.display.update()

pygame.quit()
