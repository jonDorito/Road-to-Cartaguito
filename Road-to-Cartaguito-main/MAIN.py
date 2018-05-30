import pygame as pg
import time
import loader
import enemy
import Player

#Inicializar pygame
pg.init()
clock = pg.time.Clock()
S_width = 960
S_height = 720
screen = pg.display.set_mode((S_width, S_height))

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fps = 30

#hacemos un grupo de todos los sprites que se actualizan por fotograma
all_sprites = pygame.sprite.Group()
#hagregamos los sprites a el grupo
player = Player()
        ###corregir clase enemy a Enemy
enemy = Enemy()
bullet = Bullet()

all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(bullet)

#game loop
running = True

while running:
    clock.tick(fps)
         
     #check events
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()        
        elif event.type == pg.KEYDOWN:               
            if event.key == pg.K_LEFT:
                pressed_left = True
            elif event.key == pg.K_RIGHT:     
                pressed_right = True
            elif event.key == pg.K_UP:       
                pressed_up = True
            elif event.key == pg.K_DOWN:    
                pressed_down = True
        elif event.type == pg.KEYUP:           
            if event.key == pg.K_LEFT:
                pressed_left = False
            elif event.key == pg.K_RIGHT:
                pressed_right = False
            elif event.key == pg.K_UP:        
                pressed_up = False
            elif event.key == pg.K_DOWN:     
                pressed_down = False

    if pressed_up and pressed_right:
        Player.moveUp(), Player.moveRight()
    if pressed_up and pressed_left  :
        Player.moveUp(), Player.moveLeft()
    if pressed_down and pressed_right:
        Player.moveDown(), Player.moveRight()
    if pressed_down and pressed_left:
        Player.moveDown(), Player.moveLeft()
    if pressed_up:
        Player.moveUp()
    if pressed_down:
        Player.moveDown()
    if pressed_left:
        Player.moveLeft()
    if pressed_right:
        Player.moveRight()
                       
     #update todo
    all_sprites.update()
         
     #draw en la pantalla
    all_sprites.draw(gameDisplay)




pg.quit()
quit()


