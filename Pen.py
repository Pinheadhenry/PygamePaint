import pygame
from Colors import Color
from Redo import Redo

class Pen:
    def __init__(self):
        self.size = 5
        self.color = Color.BLACK

    def draw(self, start, screen, screenLength, screenWidth, size, color, redo):

        if pygame.mouse.get_pressed()[0] == True:
            x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            if x > 0 and x < screenLength and y > start + self.size and y < screenWidth:
                pygame.draw.circle(screen, color, (x, y), size)
                redo.addSection(x, y)
