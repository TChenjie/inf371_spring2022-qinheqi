import pygame
import random
pygame.init()
#Output difficulty selection
print("easy\n")
print("medium\n")
print("hard\n")
Hard=input("请选择难度")
#Get the difficulty selection by getting screen input
if(Hard=="easy"):
    dif=2
elif(Hard=="medium"):
    dif=5
elif(Hard=="hard"):
    dif=8
else:
    print("input error !")
    pygame.quit()
#Define font1
font1 = pygame.font.SysFont("kaiti", 30)
font2 = pygame.font.SysFont("kaiti", 30)
#Sets the initial score and health
score = 0   
fighter = 3
#define rect of myplane
Myplane_rect=pygame.Rect(100,500,60,60)
#define EVENT1
MY_ENDEVENT1 = pygame.USEREVENT + 1  
#define EVENT2
MY_ENDEVENT2 = pygame.USEREVENT + 1  
#define EVENT3
MY_ENDEVENT3 = pygame.USEREVENT + 1  
#Defining the Background class
class Background():
    def __init__(self, is_alt = -700):
        #Define background image
        self.back = pygame.image.load("3.png")
        self.back_rect = self.back.get_rect()
        self.back_rect.y = is_alt
    def update(self):
        self.back_rect.y += 1
        if self.back_rect.y >= 700:
            self.back_rect.y = -700
    def draw(self):
        screen.blit(self.back,self.back_rect)
Enemy_x=random.randint(0,300)
jiange1=random.randint(60,200)
jiange2=random.randint(60,200)
screen = pygame.display.set_mode((480, 700))
Enemy1_rect=pygame.Rect(Enemy_x,0,60,60)
Enemy2_rect=pygame.Rect(Enemy_x,0,60,60)
Enemy3_rect=pygame.Rect(Enemy_x,0,60,60)
bulte_rect=pygame.Rect(100,450,30,69)
bg1=Background(0)
bg2=Background(-700)
