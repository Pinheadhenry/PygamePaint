import pygame
from Colors import Color

class Slider:
    def __init__(self, x, y):
        self.length = 100
        self.height = 8
        self.xPos = x
        self.yPos = y

        self.xTogglePos = (self.xPos + (self.length/2) - (self.length/20))
        self.yTogglePos = self.yPos - (self.height*0.5)

        self.value = round(((self.xTogglePos - self.xPos + self.length/20) / self.length) * 10, 0)

    def draw(self, screen, color):
        sliderRect = pygame.Rect(self.xPos, self.yPos, self.length, self.height)
        pygame.draw.rect(screen, color, sliderRect)

       

        sliderToggleRect = pygame.Rect(self.xTogglePos, self.yTogglePos, self.length/10, self.height * 2)
        pygame.draw.rect(screen, Color.WHITE, sliderToggleRect)

        self.sliding(screen)
    
    def sliding(self, screen):
        if pygame.mouse.get_pressed()[0] == True:
            x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            if x > self.xTogglePos and x < self.xTogglePos + (self.length/10) and y > self.yTogglePos and y < self.yTogglePos + (self.height * 2):
                if self.xTogglePos < self.xPos:
                    self.xTogglePos = self.xPos
                elif self.xTogglePos > self.xPos + self.length - self.length/10:
                    self.xTogglePos = self.xPos + self.length - self.length/10
                else:
                    self.xTogglePos = x - self.length/20
        self.value = round(((self.xTogglePos - self.xPos + self.length/20) / self.length) * 10, 0)