
import pygame
import time
pygame.init()

ok = True
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))
x=10
y=10
gas = 0
spir = 0

while ok:
    pygame.time.delay(90)
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok=False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            ok = False
        if keys[pygame.K_d]:
            if gas == 3:
                for n in range(1,20):
                    x=x-2
                time.sleep(0.1)
                for n in range(1,10):
                    x=x-2
            gas = 1
        if keys[pygame.K_s]:
            if gas == 4:
                for n in range(1,20):
                    y=y-2
                time.sleep(0.1)
                for n in range(1,10):
                    y=y-2
            gas = 2 
        if keys[pygame.K_a]:
            if gas == 1:
                for n in range(1,20):
                    x=x+2
                time.sleep(0.1)
                for n in range(1,10):
                    x=x+2
            gas = 3 
        if keys[pygame.K_w]:
            if gas == 2:
                for n in range(1,20):
                    y=y+2
                time.sleep(0.1)
                for n in range(1,10):
                    y=y+2
            gas = 4 
        if keys[pygame.K_SPACE]:
            spir = 1
    if gas == 1:
        x=x+10      
    if gas == 2:
        y=y+10
    if gas == 3:
        x=x-10
    if gas == 4:
        y=y-10


    if spir == 1:
        if gas == 1:
            for n in range(1,2):
                for n in range(1,5):
                    x=x+3
                time.sleep(0.03)
                for n in range(1,4):
                    x=x+2
                time.sleep(0.03)
                for n in range(1,3):
                    x=x+1
            x=x+0
            spir=0
            gas = 0
        if gas == 2:
            for n in range(1,2):
                for n in range(1,5):
                    y=y+3
                time.sleep(0.03)
                for n in range(1,4):
                    y=y+2
                time.sleep(0.03)
                for n in range(1,3):
                    y=y+1
            y=y+0
            spir=0
            gas = 0
        if gas == 3:
            for n in range(1,2):
                for n in range(1,5):
                    x=x-3
                time.sleep(0.03)
                for n in range(1,4):
                    x=x-2
                time.sleep(0.03)
                for n in range(1,3):
                    x=x-1
            x=x+0
            spir=0
            gas = 0
        if gas == 4:
            for n in range(1,2):
                for n in range(1,5):
                    y=y-3
                time.sleep(0.03)
                for n in range(1,4):
                    y=y-2
                time.sleep(0.03)
                for n in range(1,3):
                    y=y-1
            y=y+0
            spir=0
            gas = 0
        
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,200), (x,y,30,30))
    pygame.display.update()

pygame.quit()