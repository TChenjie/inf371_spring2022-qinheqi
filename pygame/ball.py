import pygame
pygame.init()

size=width,height=640,480
ballspeed=[2,2]
black=(0,0,0)
white=(255,255,255)
blue=(0,0,120)
backgroundClolor=(50,50,50)
facespeed=[5,5]
class unit():
    def __init__(self,file,screenSize,speed):
        self.picture=pygame.image.load(file)
        self.rect=self.picture.get_rect()
        self.height=screenSize[0]
        self.weight=screenSize[1]
        self.speed=speed