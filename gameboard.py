'''
Author: Lauren Dulick
Date: December 18, 2022 - December 31, 2022
Title: "Speedster"
File: gameboard.py
'''

# draw gameboard

import math, random
import pygame

class Gameboard:

    boxes = []

    # constructor method
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

    # draw lines of game1
    def drawGame1(self):
        lineColor = (0,0,0)
        squareSize = 100

        # draw horizontal lines
        for i in range(0, 3):
            pygame.draw.line(self.screen, lineColor, (98, i * squareSize + 100), (302, i * squareSize + 100), 5)

        # draw vertical lines
        for j in range(0, 3):
            pygame.draw.line(self.screen, lineColor, (j * squareSize + 100, 100), (j * squareSize + 100, 300), 5)

    # draw lines of game2
    def drawGame2(self):
        lineColor = (0,0,0)
        squareSize = 100

        # draw horizontal lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, lineColor, (48, i * squareSize + 50), (352, i * squareSize + 50), 5)

        # draw vertical lines
        for j in range(0, 4):
            pygame.draw.line(self.screen, lineColor, (j * squareSize + 50, 50), (j * squareSize + 50, 350), 5)

    # draw lines of game3
    def drawGame3(self):
        lineColor = (0,0,0)
        squareSize = 100

        # draw horizontal lines
        for i in range(0, 5):
            pygame.draw.line(self.screen, lineColor, (0, i * squareSize), (400, i * squareSize), 5)

        # draw vertical lines
        for j in range(0, 5):
            pygame.draw.line(self.screen, lineColor, (j * squareSize, 0), (j * squareSize, 400), 5)