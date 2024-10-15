import pygame

#=== PYGAME SETUP ===#
pygame.init()
# SCREEN #
screen_width = 1280 
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
# CLOCK
FPS = 60
clock = pygame.time.Clock()
dt = 0

#=== EVENT HANDLER ===#
def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # user clicked X to close window
			return False
	return True

#=== INPUT HANDLER ===#
def input_handler(position):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		position.y -= 300 * dt
	if keys[pygame.K_s]:
		position.y += 300 * dt
	if keys[pygame.K_a]:
		position.x -= 300 * dt
	if keys[pygame.K_d]:
		position.x += 300 * dt
	return position
    


#=== PLAYER SETUP ===#
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


running = True
while running:
    # poll for events
    
    running = event_handler()

    screen.fill((30,30,30))

    pygame.draw.circle(screen, "black", player_pos, 40)

    input_handler(player_pos)

    pygame.display.flip() # update the screen

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pygame.quit()
