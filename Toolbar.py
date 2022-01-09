import pygame
from Colors import Color

class ToolBar:
    def __init__(self, screen,  screenLength, screenWidth):
        self.redPos = screenLength/8 * 0
        self.yellowPos = screenLength/8 * 1
        self.greenPos = screenLength/8 * 2
        self.bluePos = screenLength/8 * 3
        self.btnSizeW = 94
        self.btnSizeH = 50

        self.toolbarH = 100

        self.screen = screen

    def draw(self, screenLength):
        toolbarRect = pygame.Rect(0, 0, screenLength, self.toolbarH)
        pygame.draw.rect(self.screen, (96, 96, 96), toolbarRect)

        self.clearStage()
        # self.drawButtons()

    def drawButtons(self):
        redBtn = pygame.Rect(self.redPos, 25, self.btnSizeW, self.btnSizeH)
        yellowBtn = pygame.Rect(self.yellowPos, 25, self.btnSizeW, self.btnSizeH)
        greenBtn = pygame.Rect(self.greenPos, 25, self.btnSizeW, self.btnSizeH)
        blueBtn = pygame.Rect(self.bluePos, 25, self.btnSizeW, self.btnSizeH)

        pygame.draw.rect(self.screen, Color.RED, redBtn)
        pygame.draw.rect(self.screen, Color.YELLOW, yellowBtn)
        pygame.draw.rect(self.screen, Color.GREEN, greenBtn)
        pygame.draw.rect(self.screen, Color.BLUE, blueBtn)

        
    def clearStage(self):
        clearBtn = pygame.Rect(0, 0, 25, 25)
        pygame.draw.rect(self.screen, Color.WHITE, clearBtn)
        pygame.draw.line(self.screen, Color.RED, (0, 0), (25, 25), 3)
        pygame.draw.line(self.screen, Color.RED, (25, 0), (0, 25), 3)

        if pygame.mouse.get_pressed()[0] == True:
            x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            if x > 0 and x < 25 and y > 0 and y < 25:
               self.screen.fill((255, 255, 255))

    def drawCurrentColor(self, color, x, y, s):
        currentColorRect = pygame.Rect(x, y, s, s)
        pygame.draw.rect(self.screen, color, currentColorRect)

