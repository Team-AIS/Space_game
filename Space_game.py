
import pygame
pygame.init()

x1=50
wc1=0
xx1=10
yy1=10
y1=10
yl1=y1
xl1=x1
im=True
a1=True
b1=False
def sepiq(xx1,yy1):
    global wc1
    if wc1 + 1 >= 27:
        wc1 = 0
    if im1:
        win.blit(im1[wc1//3], (x1,y1))
        wc1 += 1
    else:
        win.blit(im2, (x1, y1))
        walkCount = 0
    pygame.display.update()
im1=[pygame.image.load('sepiq1.png'),pygame.image.load('sepiq2.png'),pygame.image.load('sepiq3.png'),pygame.image.load('sepiq4.png'),pygame.image.load('sepiq3.png'),pygame.image.load('sepiq2.png'),pygame.image.load('sepiq3.png'),pygame.image.load('sepiq4.png'),pygame.image.load('sepiq3.png')]
im2=pygame.image.load('sepiq1.png')
win = pygame.display.set_mode((1378, 700))
right=False
left=False
up=False
down=False
wc=0
ok= True
x=50
y=50
width=40
height=60
vel=25
walkRight = [pygame.image.load('4.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),pygame.image.load('4.png'),pygame.image.load('4.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),pygame.image.load('4.png'),pygame.image.load('4.png')]
walkLeft = [pygame.image.load('44.png'),pygame.image.load('22.png'),pygame.image.load('33.png'),pygame.image.load('44.png'),pygame.image.load('44.png'),pygame.image.load('22.png'),pygame.image.load('33.png'),pygame.image.load('44.png'),pygame.image.load('44.png')]
Up = [pygame.image.load('43.png'),pygame.image.load('23.png'),pygame.image.load('37.png'),pygame.image.load('43.png'),pygame.image.load('43.png'),pygame.image.load('23.png'),pygame.image.load('37.png'),pygame.image.load('43.png'),pygame.image.load('43.png')]
Down = [pygame.image.load('45.png'),pygame.image.load('25.png'),pygame.image.load('35.png'),pygame.image.load('45.png'),pygame.image.load('45.png'),pygame.image.load('25.png'),pygame.image.load('35.png'),pygame.image.load('45.png'),pygame.image.load('45.png')]

char = pygame.image.load('1.png')
clock = pygame.time.Clock()

def redrawGameWindow():
    global wc
    
    if wc + 1 >= 27:
        wc = 0
    if left:
        win.blit(walkLeft[wc//3], (x,y))
        wc += 1 
    elif right:
        win.blit(walkRight[wc//3], (x,y))
        wc += 1
    elif up:
        win.blit(Up[wc//3], (x,y))
        wc += 1
    elif down:
        win.blit(Down[wc//3], (x,y))
        wc += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
    pygame.display.update()

while ok:
    pygame.time.delay(100)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok=False

    keys = pygame.key.get_pressed()

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
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x1+45,yl1,10,50))
    yl1=yl1+15
    if yl1==700:
        yl1=y1
    sepiq(xx1,yy1)
    if keys[pygame.K_a] and x>vel:
        x=x-vel
        left = True
        right = False
    elif keys[pygame.K_d] and x<1378-width-vel:
        x=x+vel
        left=False
        right=True
    elif keys[pygame.K_s]:
        y=y+vel
        down=True
        left=False
        right=False
        up=False
    elif keys[pygame.K_w]:
        up=True
        left=False
        right=False
        down=False
        y=y-vel
    else:
        left = False
        right = False
        wc = 0
    
    sepiq(xx1,yy1)
    redrawGameWindow()
pygame.quit()
