#This is a template for a pygame videogame
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

#define colors 

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# set up assets folders

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "player.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center =  (WIDTH/2, HEIGHT -50 )
        self.speed_x = 0


    def update(self):
        self.speed_x = 0         
        key_state = pygame.key.get_pressed()

        if key_state[pygame.K_LEFT]:
            self.speed_x = -10

        if key_state[pygame.K_RIGHT]:
            self.speed_x = 10

        self.rect.x += self.speed_x
        
        #screen controls
        if self.rect.x > WIDTH:
            self.rect.x = 0
        
        if self.rect.x < 0:
            self.rect.x = WIDTH


#initialize pyagme and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Game loop
running = True
while running:
    #keep runing at the rigth speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update
    all_sprites.update()
    #draw and reder
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after draw something flip the display
    pygame.display.flip()
