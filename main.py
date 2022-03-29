import pygame
from Colors import Color
from Toolbar import ToolBar
from Pen import Pen
from Slider import Slider
from Redo import Redo

pygame.init()

SCREEN_LENGTH = 750
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
clock = pygame.time.Clock()

toolbar = ToolBar(screen, SCREEN_LENGTH, SCREEN_WIDTH)

redSlider = Slider(50, 25)
greenSlider = Slider(50, 50)
blueSlider = Slider(50, 75)

currentColor = (redSlider.value * 25.5, greenSlider.value * 25.5, blueSlider.value * 25.5)

sizeSlider = Slider(400, 50)
pen = Pen()
redo = Redo()

screen.fill((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            redo.clicked(screen, sizeSlider.value)
        if event.type == pygame.MOUSEBUTTONUP:
            redo.addHistory()

    currentColor = (redSlider.value * 25.5, greenSlider.value * 25.5, blueSlider.value * 25.5)

    toolbar.draw(SCREEN_LENGTH)
    pen.draw(toolbar.toolbarH, screen, SCREEN_LENGTH, SCREEN_WIDTH, sizeSlider.value, currentColor, redo)
    sizeSlider.draw(screen, Color.BLACK)
    redSlider.draw(screen, Color.RED)
    greenSlider.draw(screen, Color.GREEN)
    blueSlider.draw(screen, Color.BLUE)
    toolbar.drawCurrentColor(currentColor, 175, 25, 50)
    redo.drawButton(screen)
    
    clock.tick(1000)
    pygame.display.update()