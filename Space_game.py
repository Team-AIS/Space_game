
from pickle import FALSE
import pygame ,sys
import time
import pygame
import button_main
import button
from pygame import mixer
ok=False

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1378

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space game')

start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

start_button = button.Button(350, 300, start_img, 0.8)
exit_button = button.Button(770, 300, exit_img, 0.8)

run = True
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		ok=True
		run=False
	if exit_button.draw(screen):
		run=False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
pygame.init()

x2=10
y2=10
gas2 = 0
spir2 = False
boost2 = False
booster2 = True
i2 = 0 
x1=50
wc1=0
wc=0
xx1=10
winner=1
lose=pygame.image.load('loll.png')
yy1=10
y1=10
yl1=y1
im=True
a1=True
b1=False
im1=[pygame.image.load('sepiq1.png'),pygame.image.load('sepiq2.png'),pygame.image.load('sepiq3.png'),pygame.image.load('sepiq4.png'),pygame.image.load('sepiq3.png'),pygame.image.load('sepiq2.png'),pygame.image.load('sepiq3.png'),pygame.image.load('sepiq4.png'),pygame.image.load('sepiq3.png')]
im2=pygame.image.load('sepiq1.png')
win = pygame.display.set_mode((1378, 700))
def sepiq(xx1,yy1):
    global wc1
    clock.tick(80)

    if wc1 + 1 >= 27:
        wc1 = 0
    if im1:
        win.blit(im1[wc1//3], (x1,y1))
        wc1 += 1
    else:
        win.blit(im2, (x1, y1))
        walkCount = 0
    pygame.display.update()
right=False
left=False
up=False
down=False
wc=0
wc2=0
ybac=10
booman=[pygame.image.load('boom1.png'),pygame.image.load('boom2.png'),pygame.image.load('boom3.png'),pygame.image.load('boom4.png')]
def boomka(x2,y2):
    global wc2
    clock.tick(80)

    if wc2 + 1 >= 27:
        wc2 = 0
    if booman:
        win.blit(booman[wc2//3], (x2,y2))
        wc2 += 1
    else:
        walkCount = 0
    pygame.display.update()
xbac=0
x2=600
y2=350
width=40
height=60
pob=pygame.image.load('lol.png')
vel=25
wr = [pygame.image.load('4.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),pygame.image.load('4.png'),pygame.image.load('4.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),pygame.image.load('4.png'),pygame.image.load('4.png')]
wl = [pygame.image.load('44.png'),pygame.image.load('22.png'),pygame.image.load('33.png'),pygame.image.load('44.png'),pygame.image.load('44.png'),pygame.image.load('22.png'),pygame.image.load('33.png'),pygame.image.load('44.png'),pygame.image.load('44.png')]
Up = [pygame.image.load('43.png'),pygame.image.load('23.png'),pygame.image.load('37.png'),pygame.image.load('43.png'),pygame.image.load('43.png'),pygame.image.load('23.png'),pygame.image.load('37.png'),pygame.image.load('43.png'),pygame.image.load('43.png')]
Down = [pygame.image.load('45.png'),pygame.image.load('25.png'),pygame.image.load('35.png'),pygame.image.load('45.png'),pygame.image.load('45.png'),pygame.image.load('25.png'),pygame.image.load('35.png'),pygame.image.load('45.png'),pygame.image.load('45.png')]
bac=pygame.image.load('back.png')
char = pygame.image.load('4.png')
clock = pygame.time.Clock()

def redrawGameWindow():
    global wc
    pygame.time.delay(1)
    clock.tick(60)
    if wc + 1 >= 27:
        wc = 0
    if left:
        win.blit(wl[wc//3],(x2,y2))
        wc += 1
    elif right:
        win.blit(wr[wc//3], (x2,y2))
        wc += 1
    elif up:
        win.blit(Up[wc//3], (x2,y2))
        wc += 1
    elif down:
        win.blit(Down[wc//3], (x2,y2))
        wc += 1
    else:
        win.blit(char, (x2, y2))
        walkCount = 0
    pygame.display.update()

def backg(xabc,ybac):
    clock.tick(60)
    win.blit(bac,(xbac,ybac))
while ok:
    pygame.time.delay(1)
    clock.tick(60)
    xl1=x1+45
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            ok = False
        if keys[pygame.K_d] and i2==0:
            if gas2 == 3:
                for n2 in range(1,20):
                    x2=x2-2
                time.sleep(0.1)
                for n2 in range(1,10):
                    x2=x2-2
            gas2 = 1
            left=False
            right=True
            up=False
            down=False
        if keys[pygame.K_s] and i2==0:
            if gas2 == 4:
                for n2 in range(1,20):
                    y2=y2-2
                time.sleep(0.1)
                for n2 in range(1,10):
                    y2=y2-2
            gas2 = 2
            down=True
            left=False
            right=False
            up=False
        if keys[pygame.K_a] and i2==0:
            if gas2 == 1:
                for n2 in range(1,20):
                    x2=x2+2
                time.sleep(0.1)
                for n2 in range(1,10):
                    x2=x2+2
            gas2 = 3
            left = True
            right = False
            up=False
            down=False 
        if keys[pygame.K_w] and i2==0:
            if gas2 == 2:
                for n2 in range(1,20):
                    y2=y2+2
                time.sleep(0.1)
                for n2 in range(1,10):
                    y2=y2+2
            gas2 = 4
            up=True
            left=False
            right=False
            down=False
        else:
            left = False
            right = False
            wc = 0
        if keys[pygame.K_g] and i2==0:
            spir2 = True
        if keys[pygame.K_h] and i2==0:
            boost2 = True


    if a1==True:
        x1=x1+10
    if x1==1300:
        a1=False
        b1=True
        yl1=y1
    if b1==True:
        x1=x1-10
    if x1==0:
        a1=True 
        b1=False
        yl1=y1
    
    yl1=yl1+15
    if yl1==700:
        yl1=y1
    
        

        
    if gas2 == 1:
        x2=x2+15
        left=False
        right=True
        up=False
        down=False    
    if gas2 == 2:
        y2=y2+15
    if gas2 == 3:
        x2=x2-15
        left=True
        right=False
        up=False
        down=False
    if gas2 == 4:
        y2=y2-15

    if spir2:
        if gas2 == 1:
            for n2 in range(1,2):
                for n2 in range(1,5):
                    x2=x2+3
                time.sleep(0.03)
                for n2 in range(1,4):
                    x2=x2+2
                time.sleep(0.03)
                for n2 in range(1,3):
                    x2=x2+1
            x2=x2+0
            spir2=0
            gas2 = 0
        if gas2 == 2:
            for n2 in range(1,2):
                for n2 in range(1,5):
                    y2=y2+3
                time.sleep(0.03)
                for n2 in range(1,4):
                    y2=y2+2
                time.sleep(0.03)
                for n2 in range(1,3):
                    y2=y2+1
            y2=y2+0
            spir2=0
            gas2 = 0
        if gas2 == 3:
            for n2 in range(1,2):
                for n2 in range(1,5):
                    x2=x2-3
                time.sleep(0.03)
                for n2 in range(1,4):
                    x2=x2-2
                time.sleep(0.03)
                for n2 in range(1,3):
                    x2=x2-1
            x2=x2+0
            spir2=0
            gas2 = 0
        if gas2 == 4:
            for n2 in range(1,2):
                for n2 in range(1,5):
                    y2=y2-3
                time.sleep(0.03)
                for n2 in range(1,4):
                    y2=y2-2
                time.sleep(0.03)
                for n2 in range(1,3):
                    y2=y2-1
            y2=y2+0
            spir2=False
            gas2 = 0


    
    if boost2:
        if gas2 == 1:
            x2=x2+30
            i2=i2+1
        if gas2 == 3:
            x2=x2-30
            i2=i2+1
        if gas2 == 2:
            y2=y2+30
            i2=i2+1
        if gas2 == 4:
            y2=y2-30
            i2=i2+1
        if i2 == 5:
            boost2 = False
            i2=0
    if y2 < yl1 and y2 > yl1 - 10  and x2 > xl1-100 and x2 < xl1+1:
            ok = False
            winner=3

    if y2 - 10 < y1 and x2 > x1-40 and x2 < x1+1:
            ok = False
            winner=2
    
    win.fill((0,0,0))
    win.blit(pygame.image.load('ops.jpg'),(0,0))
    backg(xbac,ybac)
    pygame.draw.rect(win,(255,0,0),(xl1,yl1-10,10,25))
    sepiq(xx1,yy1)
    pygame.display.update()
    redrawGameWindow()
if winner==2:
        win.blit(pob,(100,100))
        win.blit(pygame.image.load('boom_sepiq.png'),(x1,y1))
        pygame.display.update()
        pygame.time.delay(3000)
if winner==3:
        win.blit(lose,(100,100))
        for n in range (1,3):
            boomka(x2,y2)
            time.sleep(0.01)
        pygame.time.delay(3000)
pygame.quit()
