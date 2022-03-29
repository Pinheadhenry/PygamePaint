import pygame
from Colors import Color

class Redo:
    def __init__(self):
        self.history = {}
        self.section = []
        self.count = 1
        self.img = pygame.image.load('./Assets/redo.png')
        self.img = pygame.transform.scale(self.img, (25, 25))

    def addSection(self, x, y):
        if not (0 < x < 100 and 100 < y < 125) and (x, y) not in self.section:
            self.section.append((x, y))
    def addHistory(self):
        if self.section:
            self.history[self.count] = self.section
            print(self.count)
            self.section = []
            self.count += 1 
        

    def clicked(self, screen, size):
        x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if x > 0 and x < 25 and y > 100 and y < 125:
            self.redo(screen, size)
            

    def redo(self, screen, size):
        if self.count > 1:
            for i in self.history[self.count-1]:
                pygame.draw.circle(screen, Color.WHITE, i, size)
            self.count = self.count - 1
        print(self.count)
        

    def drawButton(self, screen):
        screen.blit(self.img, (00, 100))