import pygame
import random
pygame.init()
print("easy\n")
print("medium\n")
print("hard\n")
Hard=input("请选择难度")
if(Hard=="easy"):
    dif=5
elif(Hard=="medium"):
    dif=15
elif(Hard=="hard"):
    dif=25
else:
    print("input error ！")
    pygame.quit()
font1 = pygame.font.SysFont("kaiti", 30)
font2 = pygame.font.SysFont("kaiti", 30)
score = 0   
fighter = 3