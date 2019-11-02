import pygame

pygame.init()

#BIlt drwaws the imgage to the screen
def car(carImg,x,y):
    gameDisplay.blit(carImg, (x, y))

display_width = 1600
display_height = 900

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')

x = (display_width * 0.3)
y = (display_height * 0.3)
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(carImg,x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()