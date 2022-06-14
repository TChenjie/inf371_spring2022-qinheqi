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
        #Define rect of background image 
        self.back_rect = self.back.get_rect()
        #Define the background length
        self.back_rect.y = is_alt
    #Defining update methods
    def update(self):
        #Define background move down
        self.back_rect.y += 1
        #Insert the next image when the background image is moved down the screen
        if self.back_rect.y >= 700:
            self.back_rect.y = -700
    #Draw the background on the screen
    def draw(self):
        screen.blit(self.back,self.back_rect)
#Randomly define enemy 1 refresh position
Enemy_x=random.randint(0,300)
#Defines the refresh interval between remaining enemy aircraft and previous enemy aircraft
jiange1=random.randint(60,200)
#Defines the refresh interval between remaining enemy aircraft and previous enemy aircraft
jiange2=random.randint(60,200)
#Define the screen
screen = pygame.display.set_mode((480, 700))
#define the rect of enemy1
Enemy1_rect=pygame.Rect(Enemy_x,0,60,60)
#define the rect of enemy2
Enemy2_rect=pygame.Rect(Enemy_x,0,60,60)
#define the rect of enemy3
Enemy3_rect=pygame.Rect(Enemy_x,0,60,60)
#define the rect of bullte
bulte_rect=pygame.Rect(100,450,30,69)
bg1=Background(0)
bg2=Background(-700)
