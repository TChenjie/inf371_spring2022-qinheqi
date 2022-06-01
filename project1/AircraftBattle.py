import pygame
import random
pygame.init()
print("easy\n")
print("medium\n")
print("hard\n")
Hard=input("请选择难度")
if(Hard=="easy"):
    dif=2
elif(Hard=="medium"):
    dif=5
elif(Hard=="hard"):
    dif=8
else:
    print("input error ！")
    pygame.quit()
font1 = pygame.font.SysFont("kaiti", 30)
font2 = pygame.font.SysFont("kaiti", 30)
score = 0   
fighter = 3
Myplane_rect=pygame.Rect(100,500,60,60)
MY_ENDEVENT1 = pygame.USEREVENT + 1  
MY_ENDEVENT2 = pygame.USEREVENT + 1  
MY_ENDEVENT3 = pygame.USEREVENT + 1  
if Hard=="easy":
    bgm1= pygame.mixer.music.load("zhou.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(MY_ENDEVENT1)
if Hard=="medium":
    bgm2= pygame.mixer.music.load("huoyuanjia.mp3")
    pygame.mixer.music.play()#播放音乐