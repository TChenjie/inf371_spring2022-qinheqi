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

#Play background music according to difficulty
if Hard=="easy":
    bgm1= pygame.mixer.music.load("zhou.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(MY_ENDEVENT1)
if Hard=="medium":
    bgm2= pygame.mixer.music.load("huoyuanjia.mp3")
    pygame.mixer.music.play()#播放音乐
    pygame.mixer.music.set_endevent(MY_ENDEVENT2)
if Hard=="hard":
    bgm3= pygame.mixer.music.load("CompendiumOfMateriaMedica.mp3")
    pygame.mixer.music.play()#播放音乐
    pygame.mixer.music.set_endevent(MY_ENDEVENT3)

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
#Define the Background class Bg1 variable
bg1=Background(0)
#Define the Background class Bg2 variable
bg2=Background(-700)
# Map aircraft
    # 1> Loading fighter images
Myplane = pygame.image.load("1.gif")
# Draw bullet image
    # 1> Loading bullet images
bulte = pygame.image.load("4.gif")
# Draw an image of enemy
    # 1> Load enemy1 plane image
Enemy1 = pygame.image.load("2.gif")
    # 2> Load enemy2 plane image
Enemy2 = pygame.image.load("2.gif")
    # 2> Load enemy3 plane image
Enemy3 = pygame.image.load("2.gif")
#
clock = pygame.time.Clock()
i = 0
while True:

    # Set the screen refresh frame rate
    clock.tick(360)
    i += 1
    # Specifies how often code inside the body of the loop executes
    clock.tick(360)
    #background motion
    bg1.update()
    bg1.draw()
 
    bg2.update()
    bg2.draw()
    #Draws the screen contents in easy mode
    if Hard=="easy":
        # Draw an image of enemy enemy1
        screen.blit(Enemy1, Enemy1_rect)
        # Draw a myplane image
        screen.blit(Myplane, Myplane_rect)
        #Draw a bullte image
        screen.blit(bulte, bulte_rect)
    #Draws the screen contents in medium mode
    if Hard=="medium":
        # Draw an image of enemy enemy1
        screen.blit(Enemy1, Enemy1_rect)
        # Draw an image of enemy enemy2
        screen.blit(Enemy2, Enemy2_rect)
        # Draw a myplane image
        screen.blit(Myplane, Myplane_rect)
        #Draw a bullte image
        screen.blit(bulte, bulte_rect)
    #Draws the screen contents in hard mode
    if Hard=="hard":
        # Draw an image of enemy enemy1
        screen.blit(Enemy1, Enemy1_rect)
        # Draw an image of enemy enemy2
        screen.blit(Enemy2, Enemy2_rect)
        # Draw an image of enemy enemy3
        screen.blit(Enemy3, Enemy3_rect)
        # Draw a myplane image
        screen.blit(Myplane, Myplane_rect)
        #Draw a bullte image
        screen.blit(bulte, bulte_rect)
    #The enemy plane movement
    Enemy1_rect.y+=dif
    Enemy2_rect.y+=dif
    Enemy3_rect.y+=dif
    #The bullet movement
    bulte_rect.y-=10
    # Update screen display
    pygame.display.update()
    #Judge refresh enemy position
    Enemy_x=random.randint(0,300)
    jiange1=random.randint(60,200)
    jiange2=random.randint(60,200)
    if Enemy1_rect.y>=900:
        Enemy1_rect.y=0
        Enemy1_rect.x=Enemy_x
    if Enemy2_rect.y>=900:
        Enemy2_rect.y=0
        Enemy2_rect.x=Enemy_x+jiange1
    if Enemy3_rect.y>=900:
        Enemy3_rect.y=0
        Enemy3_rect.x=Enemy_x+jiange2+jiange1
    #Collision detection
        #The enemy plane collided with the bullets
    if Enemy1_rect.y+60>=bulte_rect.y and bulte_rect.y+69>=Enemy1_rect.y and Enemy1_rect.y and (Enemy1_rect.x-bulte_rect.x+60>=0 and Enemy1_rect.x-bulte_rect.x<=30):
        Enemy1_rect.y=0
        Enemy1_rect.x=Enemy_x
        score+=1
    elif Enemy2_rect.y+60>=bulte_rect.y and bulte_rect.y+69>=Enemy2_rect.y and (Enemy2_rect.x-bulte_rect.x+60>=0 and Enemy2_rect.x-bulte_rect.x<=30):
        Enemy2_rect.y=0
        Enemy2_rect.x=Enemy_x+jiange1
        score+=1
    elif Enemy3_rect.y+60>=bulte_rect.y and bulte_rect.y+69>=Enemy3_rect.y and (Enemy3_rect.x-bulte_rect.x+60>=0 and Enemy3_rect.x-bulte_rect.x<=30):
        Enemy3_rect.y=0
        Enemy3_rect.x=Enemy_x+jiange2+jiange1
        score+=1
    #The enemy planes collided with the planes
    if (Myplane_rect.x-Enemy1_rect.x<=60 and Myplane_rect.x-Enemy1_rect.x+60>=0) and Myplane_rect.y<=Enemy1_rect.y+60 and Myplane_rect.y>=Enemy1_rect.y-60:
        Enemy1_rect.y=0
        Enemy1_rect.x=Enemy_x
        fighter-=1
        Myplane_rect.x=200
        Myplane_rect.y=600
    if (Myplane_rect.x-Enemy2_rect.x<=60 and Myplane_rect.x-Enemy2_rect.x+60>=0) and Myplane_rect.y<=Enemy2_rect.y+60 and Myplane_rect.y>=Enemy2_rect.y-60:
        Enemy2_rect.y=0
        Enemy2_rect.x=Enemy_x+jiange1
        fighter-=1
        Myplane_rect.x=200
        Myplane_rect.y=600
    if (Myplane_rect.x-Enemy3_rect.x<=60 and Myplane_rect.x-Enemy3_rect.x+60>=0) and Myplane_rect.y<=Enemy3_rect.y+60 and Myplane_rect.y>=Enemy3_rect.y-60:
        Enemy3_rect.y=0
        Enemy3_rect.x=Enemy_x+jiange1+jiange2
        fighter-=1
        Myplane_rect.x=200
        Myplane_rect.y=600
    #Determine the reload position
    if bulte_rect.y<=0:
        bulte_rect.y=Myplane_rect.y-70
        bulte_rect.x=Myplane_rect.x+15
    #Exit the game when health reaches zero
    if fighter==0:
        pygame.quit()
    for event in pygame.event.get():

        #Determine whether the user has clicked the close button 
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            #Exit the system directly
            break
        #Realize keyboard operation of aircraft
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if Myplane_rect.x>0:
                    Myplane_rect.x-=50
                if Myplane_rect.x<=0:
                    Myplane_rect.x+=50
            if event.key==pygame.K_RIGHT:
                Myplane_rect.x=Myplane_rect.x+50 if Myplane_rect.x>=0 else Myplane_rect.x-50
            if event.key==pygame.K_UP:
                Myplane_rect.y=Myplane_rect.y-50 if Myplane_rect.y>=0 else Myplane_rect.y+50
            if event.key==pygame.K_DOWN:
                if Myplane_rect.y>0:
                    Myplane_rect.y+=50
                if Myplane_rect.y<=0:
                    Myplane_rect.y-=50
        #Adjust the difficulty according to the music
    if event.type == MY_ENDEVENT1:  # Detects the event type that is emitted when playback ends
        # Draw an image of enemy2
        screen.blit(Enemy2, Enemy2_rect)
    if event.type == MY_ENDEVENT2:  # Detects the event type that is emitted when playback ends
        # Draw an image of enemy3
        screen.blit(Enemy3, Enemy3_rect)
    if event.type == MY_ENDEVENT3:  # Detects the event type that is emitted when playback ends
            finalresult=font1.render("victory！ %s" , True, (0, 0, 0))