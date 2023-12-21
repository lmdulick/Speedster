'''
Author: Lauren Dulick
Date: December 18, 2022 - December 31, 2022
Title: "Speedster"
File: game.py
'''

# main file / gameMain() func

import pygame, sys
import math, random
import time
from pygame.locals import QUIT
from gameboard import Gameboard

pygame.init()
pygame.display.set_caption("Four Color Game")
# window measurements: (width=400, height=400)
screen = pygame.display.set_mode((400, 400))

# COLORS
lightPink = (255,182,193)                    # Q6B, Q4C
pink = (255,110,180)                         # Q3C
maroon = (139,0,0)                           # Q1C
red = (255,0,0)                              # Q2, Q3B, Q2C
lightOrange = (255,153,18)                   # Q9B, Q5C
orange = (255,97,3)                          # Q14C
lightYellow = (255,236,139)                  # Q2B, Q13C
yellow = (255,255,0)                         # Q4, Q7B, Q12C
lightGreen = (202,255,112)                   # Q6C
green = (50, 205, 50)                        # Q1, Q1B, Q15C
darkGreen = (61,145,64)                      # Q16C
cyan = (151,255,255)                         # Q8B, Q11C
blue = (99,184,255)                          # Q3, Q5B, Q7C
darkBlue = (0,0,255)                         # Q8C
lightPurple = (171,130,255)                  # Q4B, Q9C
purple = (145,44,238)                        # Q10C

white = (255,255,255)                        # box change color
black = (0,0,0)                              # font color
lightBlue = (204,229,255)                    # background color
orangeLoss = (255,153,18)                    # lose screen color
greenWin = (124,252,0)                       # win screen color

# FONT SIZES
font140 = pygame.font.Font(None, 140)
font80 = pygame.font.Font(None, 80)
font50 = pygame.font.Font(None, 50)
font30 = pygame.font.Font(None, 30)

width = 400
height = 400
count = 0

# GAME 1: change color of box to white for period of time
def flashWhite1(qsurface, color, qrect, time):
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    newBoard = Gameboard(1, 2, screen)
    newBoard.drawGame1()
    pygame.display.flip()
    pygame.time.delay(time)
    qsurface.fill(white)
    screen.blit(qsurface, qrect)
    newBoard = Gameboard(1, 2, screen)
    newBoard.drawGame1()
    pygame.display.flip()
    pygame.time.delay(time)
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    newBoard = Gameboard(1, 2, screen)
    newBoard.drawGame1()
    pygame.display.flip()

# GAME 2: change color of box to white for period of time
def flashWhite2(qsurface, color, qrect, time):
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    newBoard2 = Gameboard(1, 2, screen)
    newBoard2.drawGame2()
    pygame.display.flip()
    pygame.time.delay(time)
    qsurface.fill(white)
    screen.blit(qsurface, qrect)
    newBoard2 = Gameboard(1, 2, screen)
    newBoard2.drawGame2()
    pygame.display.flip()
    pygame.time.delay(time)
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    newBoard2 = Gameboard(1, 2, screen)
    newBoard2.drawGame2()
    pygame.display.flip()

# GAME 3: change color of box to white for period of time
def flashWhite3(qsurface, color, qrect, time):
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    newBoard3 = Gameboard(1, 2, screen)
    newBoard3.drawGame3()
    pygame.display.flip()
    pygame.time.delay(time)
    qsurface.fill(white)
    screen.blit(qsurface, qrect)
    newBoard3 = Gameboard(1, 2, screen)
    newBoard3.drawGame3()
    pygame.display.flip()
    pygame.time.delay(time)
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    newBoard3 = Gameboard(1, 2, screen)
    newBoard3.drawGame3()
    pygame.display.flip()

# change color of box to black when user clicks
def flashBlack(qsurface, color, qrect):
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    pygame.display.flip()
    pygame.time.delay(100)
    qsurface.fill(black)
    screen.blit(qsurface, qrect)
    pygame.display.flip()
    pygame.time.delay(100)
    qsurface.fill(color)
    screen.blit(qsurface, qrect)
    pygame.display.flip()


def game3():
    screen.fill(lightBlue)

    # draw 16 buttons
    # Q1C: maroon
    q1Cbutton = font140.render("X-", 0, maroon)
    # (width, height)
    q1Csurface = pygame.Surface((q1Cbutton.get_size()[0], q1Cbutton.get_size()[1]))
    q1Csurface.fill(maroon)
    q1Csurface.blit(q1Cbutton, (10, 10))
    q1Crect = q1Cbutton.get_rect(center=(350, 50))
    screen.blit(q1Csurface, q1Crect)

    # Q2C: red
    q2Cbutton = font140.render("X-", 0, red)
    # (width, height)
    q2Csurface = pygame.Surface((q2Cbutton.get_size()[0], q2Cbutton.get_size()[1]))
    q2Csurface.fill(red)
    q2Csurface.blit(q2Cbutton, (10, 10))
    q2Crect = q2Cbutton.get_rect(center=(250, 50))
    screen.blit(q2Csurface, q2Crect)

    # Q3C: pink
    q3Cbutton = font140.render("X-", 0, pink)
    # (width, height)
    q3Csurface = pygame.Surface((q3Cbutton.get_size()[0], q3Cbutton.get_size()[1]))
    q3Csurface.fill(pink)
    q3Csurface.blit(q3Cbutton, (10, 10))
    q3Crect = q3Cbutton.get_rect(center=(150, 50))
    screen.blit(q3Csurface, q3Crect)

    # Q4C: lightPink
    q4Cbutton = font140.render("X-", 0, lightPink)
    # (width, height)
    q4Csurface = pygame.Surface((q4Cbutton.get_size()[0], q4Cbutton.get_size()[1]))
    q4Csurface.fill(lightPink)
    q4Csurface.blit(q4Cbutton, (10, 10))
    q4Crect = q4Cbutton.get_rect(center=(50, 50))
    screen.blit(q4Csurface, q4Crect)

    # Q5C: lightOrange
    q5Cbutton = font140.render("X-", 0, lightOrange)
    # (width, height)
    q5Csurface = pygame.Surface((q5Cbutton.get_size()[0], q5Cbutton.get_size()[1]))
    q5Csurface.fill(lightOrange)
    q5Csurface.blit(q5Cbutton, (10, 10))
    q5Crect = q5Cbutton.get_rect(center=(50, 150))
    screen.blit(q5Csurface, q5Crect)

    # Q6C: lightGreen
    q6Cbutton = font140.render("X-", 0, lightGreen)
    # (width, height)
    q6Csurface = pygame.Surface((q6Cbutton.get_size()[0], q6Cbutton.get_size()[1]))
    q6Csurface.fill(lightGreen)
    q6Csurface.blit(q6Cbutton, (10, 10))
    q6Crect = q6Cbutton.get_rect(center=(50, 250))
    screen.blit(q6Csurface, q6Crect)

    # Q7C: blue
    q7Cbutton = font140.render("X-", 0, blue)
    # (width, height)
    q7Csurface = pygame.Surface((q7Cbutton.get_size()[0], q7Cbutton.get_size()[1]))
    q7Csurface.fill(blue)
    q7Csurface.blit(q7Cbutton, (10, 10))
    q7Crect = q7Cbutton.get_rect(center=(50, 350))
    screen.blit(q7Csurface, q7Crect)

    # Q8C: darkBlue
    q8Cbutton = font140.render("X-", 0, darkBlue)
    # (width, height)
    q8Csurface = pygame.Surface((q8Cbutton.get_size()[0], q8Cbutton.get_size()[1]))
    q8Csurface.fill(darkBlue)
    q8Csurface.blit(q8Cbutton, (10, 10))
    q8Crect = q8Cbutton.get_rect(center=(150, 350))
    screen.blit(q8Csurface, q8Crect)

    # Q9C: lightPurple
    q9Cbutton = font140.render("X-", 0, lightPurple)
    # (width, height)
    q9Csurface = pygame.Surface((q9Cbutton.get_size()[0], q9Cbutton.get_size()[1]))
    q9Csurface.fill(lightPurple)
    q9Csurface.blit(q9Cbutton, (10, 10))
    q9Crect = q9Cbutton.get_rect(center=(250, 350))
    screen.blit(q9Csurface, q9Crect)

    # Q10C: purple
    q10Cbutton = font140.render("X-", 0, purple)
    # (width, height)
    q10Csurface = pygame.Surface((q10Cbutton.get_size()[0], q10Cbutton.get_size()[1]))
    q10Csurface.fill(purple)
    q10Csurface.blit(q10Cbutton, (10, 10))
    q10Crect = q10Cbutton.get_rect(center=(350, 350))
    screen.blit(q10Csurface, q10Crect)

    # Q11C: cyan
    q11Cbutton = font140.render("X-", 0, cyan)
    # (width, height)
    q11Csurface = pygame.Surface((q11Cbutton.get_size()[0], q11Cbutton.get_size()[1]))
    q11Csurface.fill(cyan)
    q11Csurface.blit(q11Cbutton, (10, 10))
    q11Crect = q11Cbutton.get_rect(center=(350, 250))
    screen.blit(q11Csurface, q11Crect)

    # Q12C: yellow
    q12Cbutton = font140.render("X-", 0, yellow)
    # (width, height)
    q12Csurface = pygame.Surface((q12Cbutton.get_size()[0], q12Cbutton.get_size()[1]))
    q12Csurface.fill(yellow)
    q12Csurface.blit(q12Cbutton, (10, 10))
    q12Crect = q12Cbutton.get_rect(center=(350, 150))
    screen.blit(q12Csurface, q12Crect)

    # Q13C: lightYellow
    q13Cbutton = font140.render("X-", 0, lightYellow)
    # (width, height)
    q13Csurface = pygame.Surface((q13Cbutton.get_size()[0], q13Cbutton.get_size()[1]))
    q13Csurface.fill(lightYellow)
    q13Csurface.blit(q13Cbutton, (10, 10))
    q13Crect = q13Cbutton.get_rect(center=(width // 2 + 50, height // 2 - 50))
    screen.blit(q13Csurface, q13Crect)

    # Q14C: orange
    q14Cbutton = font140.render("X-", 0, orange)
    # (width, height)
    q14Csurface = pygame.Surface((q14Cbutton.get_size()[0], q14Cbutton.get_size()[1]))
    q14Csurface.fill(orange)
    q14Csurface.blit(q14Cbutton, (10, 10))
    q14Crect = q14Cbutton.get_rect(center=(width // 2 - 50, height // 2 - 50))
    screen.blit(q14Csurface, q14Crect)

    # Q15C: green
    q15Cbutton = font140.render("X-", 0, green)
    # (width, height)
    q15Csurface = pygame.Surface((q15Cbutton.get_size()[0], q15Cbutton.get_size()[1]))
    q15Csurface.fill(green)
    q15Csurface.blit(q15Cbutton, (10, 10))
    q15Crect = q15Cbutton.get_rect(center=(width // 2 - 50, height // 2 + 50))
    screen.blit(q15Csurface, q15Crect)

    # Q16C: darkGreen
    q16Cbutton = font140.render("X-", 0, darkGreen)
    # (width, height)
    q16Csurface = pygame.Surface((q16Cbutton.get_size()[0], q16Cbutton.get_size()[1]))
    q16Csurface.fill(darkGreen)
    q16Csurface.blit(q16Cbutton, (10, 10))
    q16Crect = q16Cbutton.get_rect(center=(width // 2 + 50, height // 2 + 50))
    screen.blit(q16Csurface, q16Crect)

    # draw gameboard
    newBoard3 = Gameboard(1, 2, screen)
    newBoard3.drawGame3()

    presetList3 = []
    # generate randomized list of 16 digits
    for i in range(0, 16):
        y = random.randint(1, 16)
        presetList3.append(y)
    print("presetList3:", presetList3, end=" ")
    finalPresetList3 = presetList3

    # index [0] -> 2000 millisec
    if finalPresetList3[0] == 1:
        flashWhite3(q1Csurface, maroon, q1Crect, 2000)
    elif finalPresetList3[0] == 2:
        flashWhite3(q2Csurface, red, q2Crect, 2000)
    elif finalPresetList3[0] == 3:
        flashWhite3(q3Csurface, pink, q3Crect, 2000)
    elif finalPresetList3[0] == 4:
        flashWhite3(q4Csurface, lightPink, q4Crect, 2000)
    elif finalPresetList3[0] == 5:
        flashWhite3(q5Csurface, lightOrange, q5Crect, 2000)
    elif finalPresetList3[0] == 6:
        flashWhite3(q6Csurface, lightGreen, q6Crect, 2000)
    elif finalPresetList3[0] == 7:
        flashWhite3(q7Csurface, blue, q7Crect, 2000)
    elif finalPresetList3[0] == 8:
        flashWhite3(q8Csurface, darkBlue, q8Crect, 2000)
    elif finalPresetList3[0] == 9:
        flashWhite3(q9Csurface, lightPurple, q9Crect, 2000)
    elif finalPresetList3[0] == 10:
        flashWhite3(q10Csurface, purple, q10Crect, 2000)
    elif finalPresetList3[0] == 11:
        flashWhite3(q11Csurface, cyan, q11Crect, 2000)
    elif finalPresetList3[0] == 12:
        flashWhite3(q12Csurface, yellow, q12Crect, 2000)
    elif finalPresetList3[0] == 13:
        flashWhite3(q13Csurface, lightYellow, q13Crect, 2000)
    elif finalPresetList3[0] == 14:
        flashWhite3(q14Csurface, orange, q14Crect, 2000)
    elif finalPresetList3[0] == 15:
        flashWhite3(q15Csurface, green, q15Crect, 2000)
    elif finalPresetList3[0] == 16:
        flashWhite3(q16Csurface, darkGreen, q16Crect, 2000)

    userList3 = []

    running3 = True

    while running3:
        global count
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # append num to userList3 when box is clicked
                # Q1C: maroon
                if q1Crect.collidepoint(event.pos):
                    flashBlack(q1Csurface, maroon, q1Crect)
                    userList3.append(1)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q2C: red
                elif q2Crect.collidepoint(event.pos):
                    flashBlack(q2Csurface, red, q2Crect)
                    userList3.append(2)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q3C: pink
                elif q3Crect.collidepoint(event.pos):
                    flashBlack(q3Csurface, pink, q3Crect)
                    userList3.append(3)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q4C: lightPink
                elif q4Crect.collidepoint(event.pos):
                    flashBlack(q4Csurface, lightPink, q4Crect)
                    userList3.append(4)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q5C: lightOrange
                elif q5Crect.collidepoint(event.pos):
                    flashBlack(q5Csurface, lightOrange, q5Crect)
                    userList3.append(5)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q6C: lightGreen
                elif q6Crect.collidepoint(event.pos):
                    flashBlack(q6Csurface, lightGreen, q6Crect)
                    userList3.append(6)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q7C: blue
                elif q7Crect.collidepoint(event.pos):
                    flashBlack(q7Csurface, blue, q7Crect)
                    userList3.append(7)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q8C: darkBlue
                elif q8Crect.collidepoint(event.pos):
                    flashBlack(q8Csurface, darkBlue, q8Crect)
                    userList3.append(8)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q9C: lightPurple
                elif q9Crect.collidepoint(event.pos):
                    flashBlack(q9Csurface, lightPurple, q9Crect)
                    userList3.append(9)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q10C: purple
                elif q10Crect.collidepoint(event.pos):
                    flashBlack(q10Csurface, purple, q10Crect)
                    userList3.append(10)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q11C: cyan
                elif q11Crect.collidepoint(event.pos):
                    flashBlack(q11Csurface, cyan, q11Crect)
                    userList3.append(11)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q12C: yellow
                elif q12Crect.collidepoint(event.pos):
                    flashBlack(q12Csurface, yellow, q12Crect)
                    userList3.append(12)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q13C: lightYellow
                elif q13Crect.collidepoint(event.pos):
                    flashBlack(q13Csurface, lightYellow, q13Crect)
                    userList3.append(13)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q14C: orange
                elif q14Crect.collidepoint(event.pos):
                    flashBlack(q14Csurface, orange, q14Crect)
                    userList3.append(14)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q15C: green
                elif q15Crect.collidepoint(event.pos):
                    flashBlack(q15Csurface, green, q15Crect)
                    userList3.append(15)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)
                # Q16C: darkGreen
                elif q16Crect.collidepoint(event.pos):
                    flashBlack(q16Csurface, darkGreen, q16Crect)
                    userList3.append(16)
                    print("\n\nuserList3:  ", userList3)
                    print("presetList3:", presetList3)

                # check if user choice @ index i == preset list @ index i
                for i in range(0, len(userList3)):
                    if len(userList3) == 16 and userList3[15] == finalPresetList3[15]:
                        screen.fill(greenWin)
                        winText = font30.render("You won the Four Color Game!", 0, black)
                        winRect = winText.get_rect(center=(width // 2, height // 2))
                        screen.blit(winText, winRect)
                        pygame.display.flip()
                        pygame.time.delay(5000)

                        # "restart" button

                        # "exit" button

                        sys.exit()
                    elif userList3[i] == finalPresetList3[i]:
                        print("True", end=" ")
                    else:
                        print("\nFalse")
                        screen.fill(orangeLoss)
                        lossText = font80.render("You lose!", 0, black)
                        lossRect = lossText.get_rect(center=(width // 2, height // 2))
                        screen.blit(lossText, lossRect)
                        lossText2 = font30.render("Game over :(", 0, black)
                        lossRect2 = lossText2.get_rect(center=(width // 2, height // 2 + 70))
                        screen.blit(lossText2, lossRect2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        sys.exit()

                # indexes -> millisecs
                # index [1] -> 1500 millisec
                if finalPresetList3[1] == 1 and len(userList3) == 1:
                    flashWhite3(q1Csurface, maroon, q1Crect, 1500)
                elif finalPresetList3[1] == 2 and len(userList3) == 1:
                    flashWhite3(q2Csurface, red, q2Crect, 1500)
                elif finalPresetList3[1] == 3 and len(userList3) == 1:
                    flashWhite3(q3Csurface, pink, q3Crect, 1500)
                elif finalPresetList3[1] == 4 and len(userList3) == 1:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 1500)
                elif finalPresetList3[1] == 5 and len(userList3) == 1:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 1500)
                elif finalPresetList3[1] == 6 and len(userList3) == 1:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 1500)
                elif finalPresetList3[1] == 7 and len(userList3) == 1:
                    flashWhite3(q7Csurface, blue, q7Crect, 1500)
                elif finalPresetList3[1] == 8 and len(userList3) == 1:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 1500)
                elif finalPresetList3[1] == 9 and len(userList3) == 1:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 1500)
                elif finalPresetList3[1] == 10 and len(userList3) == 1:
                    flashWhite3(q10Csurface, purple, q10Crect, 1500)
                elif finalPresetList3[1] == 11 and len(userList3) == 1:
                    flashWhite3(q11Csurface, cyan, q11Crect, 1500)
                elif finalPresetList3[1] == 12 and len(userList3) == 1:
                    flashWhite3(q12Csurface, yellow, q12Crect, 1500)
                elif finalPresetList3[1] == 13 and len(userList3) == 1:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 1500)
                elif finalPresetList3[1] == 14 and len(userList3) == 1:
                    flashWhite3(q14Csurface, orange, q14Crect, 1500)
                elif finalPresetList3[1] == 15 and len(userList3) == 1:
                    flashWhite3(q15Csurface, green, q15Crect, 1500)
                elif finalPresetList3[1] == 16 and len(userList3) == 1:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 1500)

                # index [2] -> 1250 millisec
                if finalPresetList3[2] == 1 and len(userList3) == 2:
                    flashWhite3(q1Csurface, maroon, q1Crect, 1250)
                elif finalPresetList3[2] == 2 and len(userList3) == 2:
                    flashWhite3(q2Csurface, red, q2Crect, 1250)
                elif finalPresetList3[2] == 3 and len(userList3) == 2:
                    flashWhite3(q3Csurface, pink, q3Crect, 1250)
                elif finalPresetList3[2] == 4 and len(userList3) == 2:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 1250)
                elif finalPresetList3[2] == 5 and len(userList3) == 2:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 1250)
                elif finalPresetList3[2] == 6 and len(userList3) == 2:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 1250)
                elif finalPresetList3[2] == 7 and len(userList3) == 2:
                    flashWhite3(q7Csurface, blue, q7Crect, 1250)
                elif finalPresetList3[2] == 8 and len(userList3) == 2:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 1250)
                elif finalPresetList3[2] == 9 and len(userList3) == 2:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 1250)
                elif finalPresetList3[2] == 10 and len(userList3) == 2:
                    flashWhite3(q10Csurface, purple, q10Crect, 1250)
                elif finalPresetList3[2] == 11 and len(userList3) == 2:
                    flashWhite3(q11Csurface, cyan, q11Crect, 1250)
                elif finalPresetList3[2] == 12 and len(userList3) == 2:
                    flashWhite3(q12Csurface, yellow, q12Crect, 1250)
                elif finalPresetList3[2] == 13 and len(userList3) == 2:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 1250)
                elif finalPresetList3[2] == 14 and len(userList3) == 2:
                    flashWhite3(q14Csurface, orange, q14Crect, 1250)
                elif finalPresetList3[2] == 15 and len(userList3) == 2:
                    flashWhite3(q15Csurface, green, q15Crect, 1250)
                elif finalPresetList3[2] == 16 and len(userList3) == 2:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 1250)

                # index [3] -> 1000 millisec
                if finalPresetList3[3] == 1 and len(userList3) == 3:
                    flashWhite3(q1Csurface, maroon, q1Crect, 1000)
                elif finalPresetList3[3] == 2 and len(userList3) == 3:
                    flashWhite3(q2Csurface, red, q2Crect, 1000)
                elif finalPresetList3[3] == 3 and len(userList3) == 3:
                    flashWhite3(q3Csurface, pink, q3Crect, 1000)
                elif finalPresetList3[3] == 4 and len(userList3) == 3:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 1000)
                elif finalPresetList3[3] == 5 and len(userList3) == 3:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 1000)
                elif finalPresetList3[3] == 6 and len(userList3) == 3:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 1000)
                elif finalPresetList3[3] == 7 and len(userList3) == 3:
                    flashWhite3(q7Csurface, blue, q7Crect, 1000)
                elif finalPresetList3[3] == 8 and len(userList3) == 3:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 1000)
                elif finalPresetList3[3] == 9 and len(userList3) == 3:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 1000)
                elif finalPresetList3[3] == 10 and len(userList3) == 3:
                    flashWhite3(q10Csurface, purple, q10Crect, 1000)
                elif finalPresetList3[3] == 11 and len(userList3) == 3:
                    flashWhite3(q11Csurface, cyan, q11Crect, 1000)
                elif finalPresetList3[3] == 12 and len(userList3) == 3:
                    flashWhite3(q12Csurface, yellow, q12Crect, 1000)
                elif finalPresetList3[3] == 13 and len(userList3) == 3:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 1000)
                elif finalPresetList3[3] == 14 and len(userList3) == 3:
                    flashWhite3(q14Csurface, orange, q14Crect, 1000)
                elif finalPresetList3[3] == 15 and len(userList3) == 3:
                    flashWhite3(q15Csurface, green, q15Crect, 1000)
                elif finalPresetList3[3] == 16 and len(userList3) == 3:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 1000)

                # index [4] -> 900 millisec
                if finalPresetList3[4] == 1 and len(userList3) == 4:
                    flashWhite3(q1Csurface, maroon, q1Crect, 900)
                elif finalPresetList3[4] == 2 and len(userList3) == 4:
                    flashWhite3(q2Csurface, red, q2Crect, 900)
                elif finalPresetList3[4] == 3 and len(userList3) == 4:
                    flashWhite3(q3Csurface, pink, q3Crect, 900)
                elif finalPresetList3[4] == 4 and len(userList3) == 4:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 900)
                elif finalPresetList3[4] == 5 and len(userList3) == 4:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 900)
                elif finalPresetList3[4] == 6 and len(userList3) == 4:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 900)
                elif finalPresetList3[4] == 7 and len(userList3) == 4:
                    flashWhite3(q7Csurface, blue, q7Crect, 900)
                elif finalPresetList3[4] == 8 and len(userList3) == 4:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 900)
                elif finalPresetList3[4] == 9 and len(userList3) == 4:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 900)
                elif finalPresetList3[4] == 10 and len(userList3) == 4:
                    flashWhite3(q10Csurface, purple, q10Crect, 900)
                elif finalPresetList3[4] == 11 and len(userList3) == 4:
                    flashWhite3(q11Csurface, cyan, q11Crect, 900)
                elif finalPresetList3[4] == 12 and len(userList3) == 4:
                    flashWhite3(q12Csurface, yellow, q12Crect, 900)
                elif finalPresetList3[4] == 13 and len(userList3) == 4:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 900)
                elif finalPresetList3[4] == 14 and len(userList3) == 4:
                    flashWhite3(q14Csurface, orange, q14Crect, 900)
                elif finalPresetList3[4] == 15 and len(userList3) == 4:
                    flashWhite3(q15Csurface, green, q15Crect, 900)
                elif finalPresetList3[4] == 16 and len(userList3) == 4:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 900)

                # index [5] -> 800 millisec
                if finalPresetList3[5] == 1 and len(userList3) == 5:
                    flashWhite3(q1Csurface, maroon, q1Crect, 800)
                elif finalPresetList3[5] == 2 and len(userList3) == 5:
                    flashWhite3(q2Csurface, red, q2Crect, 800)
                elif finalPresetList3[5] == 3 and len(userList3) == 5:
                    flashWhite3(q3Csurface, pink, q3Crect, 800)
                elif finalPresetList3[5] == 4 and len(userList3) == 5:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 800)
                elif finalPresetList3[5] == 5 and len(userList3) == 5:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 800)
                elif finalPresetList3[5] == 6 and len(userList3) == 5:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 800)
                elif finalPresetList3[5] == 7 and len(userList3) == 5:
                    flashWhite3(q7Csurface, blue, q7Crect, 800)
                elif finalPresetList3[5] == 8 and len(userList3) == 5:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 800)
                elif finalPresetList3[5] == 9 and len(userList3) == 5:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 800)
                elif finalPresetList3[5] == 10 and len(userList3) == 5:
                    flashWhite3(q10Csurface, purple, q10Crect, 800)
                elif finalPresetList3[5] == 11 and len(userList3) == 5:
                    flashWhite3(q11Csurface, cyan, q11Crect, 800)
                elif finalPresetList3[5] == 12 and len(userList3) == 5:
                    flashWhite3(q12Csurface, yellow, q12Crect, 800)
                elif finalPresetList3[5] == 13 and len(userList3) == 5:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 800)
                elif finalPresetList3[5] == 14 and len(userList3) == 5:
                    flashWhite3(q14Csurface, orange, q14Crect, 800)
                elif finalPresetList3[5] == 15 and len(userList3) == 5:
                    flashWhite3(q15Csurface, green, q15Crect, 800)
                elif finalPresetList3[5] == 16 and len(userList3) == 5:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 800)

                # index [6] -> 700 millisec
                if finalPresetList3[6] == 1 and len(userList3) == 6:
                    flashWhite3(q1Csurface, maroon, q1Crect, 700)
                elif finalPresetList3[6] == 2 and len(userList3) == 6:
                    flashWhite3(q2Csurface, red, q2Crect, 700)
                elif finalPresetList3[6] == 3 and len(userList3) == 6:
                    flashWhite3(q3Csurface, pink, q3Crect, 700)
                elif finalPresetList3[6] == 4 and len(userList3) == 6:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 700)
                elif finalPresetList3[6] == 5 and len(userList3) == 6:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 700)
                elif finalPresetList3[6] == 6 and len(userList3) == 6:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 700)
                elif finalPresetList3[6] == 7 and len(userList3) == 6:
                    flashWhite3(q7Csurface, blue, q7Crect, 700)
                elif finalPresetList3[6] == 8 and len(userList3) == 6:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 700)
                elif finalPresetList3[6] == 9 and len(userList3) == 6:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 700)
                elif finalPresetList3[6] == 10 and len(userList3) == 6:
                    flashWhite3(q10Csurface, purple, q10Crect, 700)
                elif finalPresetList3[6] == 11 and len(userList3) == 6:
                    flashWhite3(q11Csurface, cyan, q11Crect, 700)
                elif finalPresetList3[6] == 12 and len(userList3) == 6:
                    flashWhite3(q12Csurface, yellow, q12Crect, 700)
                elif finalPresetList3[6] == 13 and len(userList3) == 6:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 700)
                elif finalPresetList3[6] == 14 and len(userList3) == 6:
                    flashWhite3(q14Csurface, orange, q14Crect, 700)
                elif finalPresetList3[6] == 15 and len(userList3) == 6:
                    flashWhite3(q15Csurface, green, q15Crect, 700)
                elif finalPresetList3[6] == 16 and len(userList3) == 6:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 700)

                # index [7] -> 600 millisec
                if finalPresetList3[7] == 1 and len(userList3) == 7:
                    flashWhite3(q1Csurface, maroon, q1Crect, 600)
                elif finalPresetList3[7] == 2 and len(userList3) == 7:
                    flashWhite3(q2Csurface, red, q2Crect, 600)
                elif finalPresetList3[7] == 3 and len(userList3) == 7:
                    flashWhite3(q3Csurface, pink, q3Crect, 600)
                elif finalPresetList3[7] == 4 and len(userList3) == 7:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 600)
                elif finalPresetList3[7] == 5 and len(userList3) == 7:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 600)
                elif finalPresetList3[7] == 6 and len(userList3) == 7:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 600)
                elif finalPresetList3[7] == 7 and len(userList3) == 7:
                    flashWhite3(q7Csurface, blue, q7Crect, 600)
                elif finalPresetList3[7] == 8 and len(userList3) == 7:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 600)
                elif finalPresetList3[7] == 9 and len(userList3) == 7:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 600)
                elif finalPresetList3[7] == 10 and len(userList3) == 7:
                    flashWhite3(q10Csurface, purple, q10Crect, 600)
                elif finalPresetList3[7] == 11 and len(userList3) == 7:
                    flashWhite3(q11Csurface, cyan, q11Crect, 600)
                elif finalPresetList3[7] == 12 and len(userList3) == 7:
                    flashWhite3(q12Csurface, yellow, q12Crect, 600)
                elif finalPresetList3[7] == 13 and len(userList3) == 7:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 600)
                elif finalPresetList3[7] == 14 and len(userList3) == 7:
                    flashWhite3(q14Csurface, orange, q14Crect, 600)
                elif finalPresetList3[7] == 15 and len(userList3) == 7:
                    flashWhite3(q15Csurface, green, q15Crect, 600)
                elif finalPresetList3[7] == 16 and len(userList3) == 7:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 600)

                # index [8] -> 500 millisec
                if finalPresetList3[8] == 1 and len(userList3) == 8:
                    flashWhite3(q1Csurface, maroon, q1Crect, 500)
                elif finalPresetList3[8] == 2 and len(userList3) == 8:
                    flashWhite3(q2Csurface, red, q2Crect, 500)
                elif finalPresetList3[8] == 3 and len(userList3) == 8:
                    flashWhite3(q3Csurface, pink, q3Crect, 500)
                elif finalPresetList3[8] == 4 and len(userList3) == 8:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 500)
                elif finalPresetList3[8] == 5 and len(userList3) == 8:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 500)
                elif finalPresetList3[8] == 6 and len(userList3) == 8:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 500)
                elif finalPresetList3[8] == 7 and len(userList3) == 8:
                    flashWhite3(q7Csurface, blue, q7Crect, 500)
                elif finalPresetList3[8] == 8 and len(userList3) == 8:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 500)
                elif finalPresetList3[8] == 9 and len(userList3) == 8:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 500)
                elif finalPresetList3[8] == 10 and len(userList3) == 8:
                    flashWhite3(q10Csurface, purple, q10Crect, 500)
                elif finalPresetList3[8] == 11 and len(userList3) == 8:
                    flashWhite3(q11Csurface, cyan, q11Crect, 500)
                elif finalPresetList3[8] == 12 and len(userList3) == 8:
                    flashWhite3(q12Csurface, yellow, q12Crect, 500)
                elif finalPresetList3[8] == 13 and len(userList3) == 8:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 500)
                elif finalPresetList3[8] == 14 and len(userList3) == 8:
                    flashWhite3(q14Csurface, orange, q14Crect, 500)
                elif finalPresetList3[8] == 15 and len(userList3) == 8:
                    flashWhite3(q15Csurface, green, q15Crect, 500)
                elif finalPresetList3[8] == 16 and len(userList3) == 8:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 500)

                # index [9] -> 400 millisec
                if finalPresetList3[9] == 1 and len(userList3) == 9:
                    flashWhite3(q1Csurface, maroon, q1Crect, 400)
                elif finalPresetList3[9] == 2 and len(userList3) == 9:
                    flashWhite3(q2Csurface, red, q2Crect, 400)
                elif finalPresetList3[9] == 3 and len(userList3) == 9:
                    flashWhite3(q3Csurface, pink, q3Crect, 400)
                elif finalPresetList3[9] == 4 and len(userList3) == 9:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 400)
                elif finalPresetList3[9] == 5 and len(userList3) == 9:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 400)
                elif finalPresetList3[9] == 6 and len(userList3) == 9:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 400)
                elif finalPresetList3[9] == 7 and len(userList3) == 9:
                    flashWhite3(q7Csurface, blue, q7Crect, 400)
                elif finalPresetList3[9] == 8 and len(userList3) == 9:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 400)
                elif finalPresetList3[9] == 9 and len(userList3) == 9:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 400)
                elif finalPresetList3[9] == 10 and len(userList3) == 9:
                    flashWhite3(q10Csurface, purple, q10Crect, 400)
                elif finalPresetList3[9] == 11 and len(userList3) == 9:
                    flashWhite3(q11Csurface, cyan, q11Crect, 400)
                elif finalPresetList3[9] == 12 and len(userList3) == 9:
                    flashWhite3(q12Csurface, yellow, q12Crect, 400)
                elif finalPresetList3[9] == 13 and len(userList3) == 9:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 400)
                elif finalPresetList3[9] == 14 and len(userList3) == 9:
                    flashWhite3(q14Csurface, orange, q14Crect, 400)
                elif finalPresetList3[9] == 15 and len(userList3) == 9:
                    flashWhite3(q15Csurface, green, q15Crect, 400)
                elif finalPresetList3[9] == 16 and len(userList3) == 9:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 400)

                # index [10] -> 300 millisec
                if finalPresetList3[10] == 1 and len(userList3) == 10:
                    flashWhite3(q1Csurface, maroon, q1Crect, 300)
                elif finalPresetList3[10] == 2 and len(userList3) == 10:
                    flashWhite3(q2Csurface, red, q2Crect, 300)
                elif finalPresetList3[10] == 3 and len(userList3) == 10:
                    flashWhite3(q3Csurface, pink, q3Crect, 300)
                elif finalPresetList3[10] == 4 and len(userList3) == 10:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 300)
                elif finalPresetList3[10] == 5 and len(userList3) == 10:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 300)
                elif finalPresetList3[10] == 6 and len(userList3) == 10:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 300)
                elif finalPresetList3[10] == 7 and len(userList3) == 10:
                    flashWhite3(q7Csurface, blue, q7Crect, 300)
                elif finalPresetList3[10] == 8 and len(userList3) == 10:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 300)
                elif finalPresetList3[10] == 9 and len(userList3) == 10:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 300)
                elif finalPresetList3[10] == 10 and len(userList3) == 10:
                    flashWhite3(q10Csurface, purple, q10Crect, 300)
                elif finalPresetList3[10] == 11 and len(userList3) == 10:
                    flashWhite3(q11Csurface, cyan, q11Crect, 300)
                elif finalPresetList3[10] == 12 and len(userList3) == 10:
                    flashWhite3(q12Csurface, yellow, q12Crect, 300)
                elif finalPresetList3[10] == 13 and len(userList3) == 10:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 300)
                elif finalPresetList3[10] == 14 and len(userList3) == 10:
                    flashWhite3(q14Csurface, orange, q14Crect, 300)
                elif finalPresetList3[10] == 15 and len(userList3) == 10:
                    flashWhite3(q15Csurface, green, q15Crect, 300)
                elif finalPresetList3[10] == 16 and len(userList3) == 10:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 300)

                # index [11] -> 200 millisec
                if finalPresetList3[11] == 1 and len(userList3) == 11:
                    flashWhite3(q1Csurface, maroon, q1Crect, 200)
                elif finalPresetList3[11] == 2 and len(userList3) == 11:
                    flashWhite3(q2Csurface, red, q2Crect, 200)
                elif finalPresetList3[11] == 3 and len(userList3) == 11:
                    flashWhite3(q3Csurface, pink, q3Crect, 200)
                elif finalPresetList3[11] == 4 and len(userList3) == 11:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 200)
                elif finalPresetList3[11] == 5 and len(userList3) == 11:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 200)
                elif finalPresetList3[11] == 6 and len(userList3) == 11:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 200)
                elif finalPresetList3[11] == 7 and len(userList3) == 11:
                    flashWhite3(q7Csurface, blue, q7Crect, 200)
                elif finalPresetList3[11] == 8 and len(userList3) == 11:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 200)
                elif finalPresetList3[11] == 9 and len(userList3) == 11:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 200)
                elif finalPresetList3[11] == 10 and len(userList3) == 11:
                    flashWhite3(q10Csurface, purple, q10Crect, 200)
                elif finalPresetList3[11] == 11 and len(userList3) == 11:
                    flashWhite3(q11Csurface, cyan, q11Crect, 200)
                elif finalPresetList3[11] == 12 and len(userList3) == 11:
                    flashWhite3(q12Csurface, yellow, q12Crect, 200)
                elif finalPresetList3[11] == 13 and len(userList3) == 11:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 200)
                elif finalPresetList3[11] == 14 and len(userList3) == 11:
                    flashWhite3(q14Csurface, orange, q14Crect, 200)
                elif finalPresetList3[11] == 15 and len(userList3) == 11:
                    flashWhite3(q15Csurface, green, q15Crect, 200)
                elif finalPresetList3[11] == 16 and len(userList3) == 11:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 200)

                # index [12] -> 100 millisec
                if finalPresetList3[12] == 1 and len(userList3) == 12:
                    flashWhite3(q1Csurface, maroon, q1Crect, 100)
                elif finalPresetList3[12] == 2 and len(userList3) == 12:
                    flashWhite3(q2Csurface, red, q2Crect, 100)
                elif finalPresetList3[12] == 3 and len(userList3) == 12:
                    flashWhite3(q3Csurface, pink, q3Crect, 100)
                elif finalPresetList3[12] == 4 and len(userList3) == 12:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 100)
                elif finalPresetList3[12] == 5 and len(userList3) == 12:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 100)
                elif finalPresetList3[12] == 6 and len(userList3) == 12:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 100)
                elif finalPresetList3[12] == 7 and len(userList3) == 12:
                    flashWhite3(q7Csurface, blue, q7Crect, 100)
                elif finalPresetList3[12] == 8 and len(userList3) == 12:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 100)
                elif finalPresetList3[12] == 9 and len(userList3) == 12:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 100)
                elif finalPresetList3[12] == 10 and len(userList3) == 12:
                    flashWhite3(q10Csurface, purple, q10Crect, 100)
                elif finalPresetList3[12] == 11 and len(userList3) == 12:
                    flashWhite3(q11Csurface, cyan, q11Crect, 100)
                elif finalPresetList3[12] == 12 and len(userList3) == 12:
                    flashWhite3(q12Csurface, yellow, q12Crect, 100)
                elif finalPresetList3[12] == 13 and len(userList3) == 12:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 100)
                elif finalPresetList3[12] == 14 and len(userList3) == 12:
                    flashWhite3(q14Csurface, orange, q14Crect, 100)
                elif finalPresetList3[12] == 15 and len(userList3) == 12:
                    flashWhite3(q15Csurface, green, q15Crect, 100)
                elif finalPresetList3[12] == 16 and len(userList3) == 12:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 100)

                # index [13] -> 70 millisec
                if finalPresetList3[13] == 1 and len(userList3) == 13:
                    flashWhite3(q1Csurface, maroon, q1Crect, 70)
                elif finalPresetList3[13] == 2 and len(userList3) == 13:
                    flashWhite3(q2Csurface, red, q2Crect, 70)
                elif finalPresetList3[13] == 3 and len(userList3) == 13:
                    flashWhite3(q3Csurface, pink, q3Crect, 70)
                elif finalPresetList3[13] == 4 and len(userList3) == 13:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 70)
                elif finalPresetList3[13] == 5 and len(userList3) == 13:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 70)
                elif finalPresetList3[13] == 6 and len(userList3) == 13:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 70)
                elif finalPresetList3[13] == 7 and len(userList3) == 13:
                    flashWhite3(q7Csurface, blue, q7Crect, 70)
                elif finalPresetList3[13] == 8 and len(userList3) == 13:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 70)
                elif finalPresetList3[13] == 9 and len(userList3) == 13:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 70)
                elif finalPresetList3[13] == 10 and len(userList3) == 13:
                    flashWhite3(q10Csurface, purple, q10Crect, 70)
                elif finalPresetList3[13] == 11 and len(userList3) == 13:
                    flashWhite3(q11Csurface, cyan, q11Crect, 70)
                elif finalPresetList3[13] == 12 and len(userList3) == 13:
                    flashWhite3(q12Csurface, yellow, q12Crect, 70)
                elif finalPresetList3[13] == 13 and len(userList3) == 13:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 70)
                elif finalPresetList3[13] == 14 and len(userList3) == 13:
                    flashWhite3(q14Csurface, orange, q14Crect, 70)
                elif finalPresetList3[13] == 15 and len(userList3) == 13:
                    flashWhite3(q15Csurface, green, q15Crect, 70)
                elif finalPresetList3[13] == 16 and len(userList3) == 13:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 70)

                # index [14] -> 50 millisec
                if finalPresetList3[14] == 1 and len(userList3) == 14:
                    flashWhite3(q1Csurface, maroon, q1Crect, 50)
                elif finalPresetList3[14] == 2 and len(userList3) == 14:
                    flashWhite3(q2Csurface, red, q2Crect, 50)
                elif finalPresetList3[14] == 3 and len(userList3) == 14:
                    flashWhite3(q3Csurface, pink, q3Crect, 50)
                elif finalPresetList3[14] == 4 and len(userList3) == 14:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 50)
                elif finalPresetList3[14] == 5 and len(userList3) == 14:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 50)
                elif finalPresetList3[14] == 6 and len(userList3) == 14:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 50)
                elif finalPresetList3[14] == 7 and len(userList3) == 14:
                    flashWhite3(q7Csurface, blue, q7Crect, 50)
                elif finalPresetList3[14] == 8 and len(userList3) == 14:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 50)
                elif finalPresetList3[14] == 9 and len(userList3) == 14:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 50)
                elif finalPresetList3[14] == 10 and len(userList3) == 14:
                    flashWhite3(q10Csurface, purple, q10Crect, 50)
                elif finalPresetList3[14] == 11 and len(userList3) == 14:
                    flashWhite3(q11Csurface, cyan, q11Crect, 50)
                elif finalPresetList3[14] == 12 and len(userList3) == 14:
                    flashWhite3(q12Csurface, yellow, q12Crect, 50)
                elif finalPresetList3[14] == 13 and len(userList3) == 14:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 50)
                elif finalPresetList3[14] == 14 and len(userList3) == 14:
                    flashWhite3(q14Csurface, orange, q14Crect, 50)
                elif finalPresetList3[14] == 15 and len(userList3) == 14:
                    flashWhite3(q15Csurface, green, q15Crect, 50)
                elif finalPresetList3[14] == 16 and len(userList3) == 14:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 50)

                # index [15] -> 30 millisec
                if finalPresetList3[15] == 1 and len(userList3) == 15:
                    flashWhite3(q1Csurface, maroon, q1Crect, 30)
                elif finalPresetList3[15] == 2 and len(userList3) == 15:
                    flashWhite3(q2Csurface, red, q2Crect, 30)
                elif finalPresetList3[15] == 3 and len(userList3) == 15:
                    flashWhite3(q3Csurface, pink, q3Crect, 30)
                elif finalPresetList3[15] == 4 and len(userList3) == 15:
                    flashWhite3(q4Csurface, lightPink, q4Crect, 30)
                elif finalPresetList3[15] == 5 and len(userList3) == 15:
                    flashWhite3(q5Csurface, lightOrange, q5Crect, 30)
                elif finalPresetList3[15] == 6 and len(userList3) == 15:
                    flashWhite3(q6Csurface, lightGreen, q6Crect, 30)
                elif finalPresetList3[15] == 7 and len(userList3) == 15:
                    flashWhite3(q7Csurface, blue, q7Crect, 30)
                elif finalPresetList3[15] == 8 and len(userList3) == 15:
                    flashWhite3(q8Csurface, darkBlue, q8Crect, 30)
                elif finalPresetList3[15] == 9 and len(userList3) == 15:
                    flashWhite3(q9Csurface, lightPurple, q9Crect, 30)
                elif finalPresetList3[15] == 10 and len(userList3) == 15:
                    flashWhite3(q10Csurface, purple, q10Crect, 30)
                elif finalPresetList3[15] == 11 and len(userList3) == 15:
                    flashWhite3(q11Csurface, cyan, q11Crect, 30)
                elif finalPresetList3[15] == 12 and len(userList3) == 15:
                    flashWhite3(q12Csurface, yellow, q12Crect, 30)
                elif finalPresetList3[15] == 13 and len(userList3) == 15:
                    flashWhite3(q13Csurface, lightYellow, q13Crect, 30)
                elif finalPresetList3[15] == 14 and len(userList3) == 15:
                    flashWhite3(q14Csurface, orange, q14Crect, 30)
                elif finalPresetList3[15] == 15 and len(userList3) == 15:
                    flashWhite3(q15Csurface, green, q15Crect, 30)
                elif finalPresetList3[15] == 16 and len(userList3) == 15:
                    flashWhite3(q16Csurface, darkGreen, q16Crect, 30)

        pygame.display.update()


def game2():
    screen.fill(lightBlue)

    # draw 9 buttons
    # Q1B: green
    q1Bbutton = font140.render("X-", 0, green)
    # (width, height)
    q1Bsurface = pygame.Surface((q1Bbutton.get_size()[0], q1Bbutton.get_size()[1]))
    q1Bsurface.fill(green)
    q1Bsurface.blit(q1Bbutton, (10, 10))
    q1Brect = q1Bbutton.get_rect(center=(300, 100))
    screen.blit(q1Bsurface, q1Brect)

    # Q2B: lightYellow
    q2Bbutton = font140.render("X-", 0, lightYellow)
    # (width, height)
    q2Bsurface = pygame.Surface((q2Bbutton.get_size()[0], q2Bbutton.get_size()[1]))
    q2Bsurface.fill(lightYellow)
    q2Bsurface.blit(q2Bbutton, (10, 10))
    q2Brect = q2Bbutton.get_rect(center=(200, 100))
    screen.blit(q2Bsurface, q2Brect)

    # Q3B: red
    q3Bbutton = font140.render("X-", 0, red)
    # (width, height)
    q3Bsurface = pygame.Surface((q3Bbutton.get_size()[0], q3Bbutton.get_size()[1]))
    q3Bsurface.fill(red)
    q3Bsurface.blit(q3Bbutton, (10, 10))
    q3Brect = q3Bbutton.get_rect(center=(100, 100))
    screen.blit(q3Bsurface, q3Brect)

    # Q4B: lightPurple
    q4Bbutton = font140.render("X-", 0, lightPurple)
    # (width, height)
    q4Bsurface = pygame.Surface((q4Bbutton.get_size()[0], q4Bbutton.get_size()[1]))
    q4Bsurface.fill(lightPurple)
    q4Bsurface.blit(q4Bbutton, (10, 10))
    q4Brect = q4Bbutton.get_rect(center=(100, 200))
    screen.blit(q4Bsurface, q4Brect)

    # Q5B: blue
    q5Bbutton = font140.render("X-", 0, blue)
    # (width, height)
    q5Bsurface = pygame.Surface((q5Bbutton.get_size()[0], q5Bbutton.get_size()[1]))
    q5Bsurface.fill(blue)
    q5Bsurface.blit(q5Bbutton, (10, 10))
    q5Brect = q5Bbutton.get_rect(center=(100, 300))
    screen.blit(q5Bsurface, q5Brect)

    # Q6B: lightPink
    q6Bbutton = font140.render("X-", 0, lightPink)
    # (width, height)
    q6Bsurface = pygame.Surface((q6Bbutton.get_size()[0], q6Bbutton.get_size()[1]))
    q6Bsurface.fill(lightPink)
    q6Bsurface.blit(q6Bbutton, (10, 10))
    q6Brect = q6Bbutton.get_rect(center=(200, 300))
    screen.blit(q6Bsurface, q6Brect)

    # Q7B: yellow
    q7Bbutton = font140.render("X-", 0, yellow)
    # (width, height)
    q7Bsurface = pygame.Surface((q7Bbutton.get_size()[0], q7Bbutton.get_size()[1]))
    q7Bsurface.fill(yellow)
    q7Bsurface.blit(q7Bbutton, (10, 10))
    q7Brect = q7Bbutton.get_rect(center=(300, 300))
    screen.blit(q7Bsurface, q7Brect)

    # Q8B: cyan
    q8Bbutton = font140.render("X-", 0, cyan)
    # (width, height)
    q8Bsurface = pygame.Surface((q8Bbutton.get_size()[0], q8Bbutton.get_size()[1]))
    q8Bsurface.fill(cyan)
    q8Bsurface.blit(q8Bbutton, (10, 10))
    q8Brect = q8Bbutton.get_rect(center=(300, 200))
    screen.blit(q8Bsurface, q8Brect)

    # Q9B: lightOrange
    q9Bbutton = font140.render("X-", 0, lightOrange)
    # (width, height)
    q9Bsurface = pygame.Surface((q9Bbutton.get_size()[0], q9Bbutton.get_size()[1]))
    q9Bsurface.fill(lightOrange)
    q9Bsurface.blit(q9Bbutton, (10, 10))
    q9Brect = q9Bbutton.get_rect(center=(200, 200))
    screen.blit(q9Bsurface, q9Brect)

    # draw gameboard
    newBoard2 = Gameboard(1, 2, screen)
    newBoard2.drawGame2()

    presetList2 = []
    # generate randomized list of 9 digits
    for i in range(0, 9):
        z = random.randint(1, 9)
        presetList2.append(z)
    print("presetList2:", presetList2, end=" ")
    finalPresetList2 = presetList2

    # index [0] -> 2000 millisec
    if finalPresetList2[0] == 1:
        flashWhite2(q1Bsurface, green, q1Brect, 2000)
    elif finalPresetList2[0] == 2:
        flashWhite2(q2Bsurface, lightYellow, q2Brect, 2000)
    elif finalPresetList2[0] == 3:
        flashWhite2(q3Bsurface, red, q3Brect, 2000)
    elif finalPresetList2[0] == 4:
        flashWhite2(q4Bsurface, lightPurple, q4Brect, 2000)
    elif finalPresetList2[0] == 5:
        flashWhite2(q5Bsurface, blue, q5Brect, 2000)
    elif finalPresetList2[0] == 6:
        flashWhite2(q6Bsurface, lightPink, q6Brect, 2000)
    elif finalPresetList2[0] == 7:
        flashWhite2(q7Bsurface, yellow, q7Brect, 2000)
    elif finalPresetList2[0] == 8:
        flashWhite2(q8Bsurface, cyan, q8Brect, 2000)
    elif finalPresetList2[0] == 9:
        flashWhite2(q9Bsurface, lightOrange, q9Brect, 2000)

    userList2 = []

    running2 = True

    while running2:
        global count
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # append num to userList2 when box is clicked
                # Q1B: green
                if q1Brect.collidepoint(event.pos):
                    flashBlack(q1Bsurface, green, q1Brect)
                    userList2.append(1)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q2B: lightYellow
                elif q2Brect.collidepoint(event.pos):
                    flashBlack(q2Bsurface, lightYellow, q2Brect)
                    userList2.append(2)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q3B: red
                elif q3Brect.collidepoint(event.pos):
                    flashBlack(q3Bsurface, red, q3Brect)
                    userList2.append(3)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q4B: lightPurple
                elif q4Brect.collidepoint(event.pos):
                    flashBlack(q4Bsurface, lightPurple, q4Brect)
                    userList2.append(4)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q5B: blue
                elif q5Brect.collidepoint(event.pos):
                    flashBlack(q5Bsurface, blue, q5Brect)
                    userList2.append(5)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q6B: lightPink
                elif q6Brect.collidepoint(event.pos):
                    flashBlack(q6Bsurface, lightPink, q6Brect)
                    userList2.append(6)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q7B: yellow
                elif q7Brect.collidepoint(event.pos):
                    flashBlack(q7Bsurface, yellow, q7Brect)
                    userList2.append(7)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q8B: cyan
                elif q8Brect.collidepoint(event.pos):
                    flashBlack(q8Bsurface, cyan, q8Brect)
                    userList2.append(8)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # Q9B: lightOrange
                elif q9Brect.collidepoint(event.pos):
                    flashBlack(q9Bsurface, lightOrange, q9Brect)
                    userList2.append(9)
                    print("\n\nuserList2:  ", userList2)
                    print("presetList2:", presetList2)

                # if user clicks anywhere other than the 9 boxes
                else:
                    print("\n\nUser clicked on background")
                    # move q1Brect, q2Brect, q3Brect, q4Brect, q5Brect, q6Brect, q7Brect, q8Brect, + q9Brect off screen
                    q1Brect = q1Bbutton.get_rect(center=(width + 100, height + 100))
                    q2Brect = q2Bbutton.get_rect(center=(width + 100, height + 100))
                    q3Brect = q3Bbutton.get_rect(center=(width + 100, height + 100))
                    q4Brect = q4Bbutton.get_rect(center=(width + 100, height + 100))
                    q5Brect = q5Bbutton.get_rect(center=(width + 100, height + 100))
                    q6Brect = q6Bbutton.get_rect(center=(width + 100, height + 100))
                    q7Brect = q7Bbutton.get_rect(center=(width + 100, height + 100))
                    q8Brect = q8Bbutton.get_rect(center=(width + 100, height + 100))
                    q9Brect = q9Bbutton.get_rect(center=(width + 100, height + 100))
                    screen.fill(orangeLoss)
                    # "ERROR: you clicked on the background"
                    lossText = font30.render("ERROR: you clicked on the background", 0, black)
                    lossRect = lossText.get_rect(center=(width // 2, height // 2 - 50))
                    screen.blit(lossText, lossRect)
                    # "Game over :("
                    lossText2 = font50.render("Game over :(", 0, black)
                    lossRect2 = lossText2.get_rect(center=(width // 2, height // 2 + 70))
                    screen.blit(lossText2, lossRect2)

                    # "restart" button

                    # "exit" button

                    pygame.display.flip()
                    pygame.time.delay(2000)
                    sys.exit()

                # check if user choice @ index i == preset list @ index i
                for i in range(0, len(userList2)):
                    if len(userList2) == 9 and userList2[8] == finalPresetList2[8]:
                        # move q1Brect, q2Brect, q3Brect, q4Brect, q5Brect, q6Brect, q7Brect, q8Brect, + q9Brect off screen
                        q1Brect = q1Bbutton.get_rect(center=(width + 100, height + 100))
                        q2Brect = q2Bbutton.get_rect(center=(width + 100, height + 100))
                        q3Brect = q3Bbutton.get_rect(center=(width + 100, height + 100))
                        q4Brect = q4Bbutton.get_rect(center=(width + 100, height + 100))
                        q5Brect = q5Bbutton.get_rect(center=(width + 100, height + 100))
                        q6Brect = q6Bbutton.get_rect(center=(width + 100, height + 100))
                        q7Brect = q7Bbutton.get_rect(center=(width + 100, height + 100))
                        q8Brect = q8Bbutton.get_rect(center=(width + 100, height + 100))
                        q9Brect = q9Bbutton.get_rect(center=(width + 100, height + 100))
                        screen.fill(greenWin)
                        winText = font50.render("You won game 2!", 0, black)
                        winRect = winText.get_rect(center=(width // 2, height // 2 - 50))
                        screen.blit(winText, winRect)
                        winText2 = font30.render("onto game 3.....", 0, black)
                        winRect2 = winText2.get_rect(center=(width // 2, height // 2 + 30))
                        screen.blit(winText2, winRect2)
                        winText3 = font30.render("the final game.", 0, black)
                        winRect3 = winText3.get_rect(center=(width // 2, height // 2 + 125))
                        screen.blit(winText3, winRect3)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running2 = False
                        game3()
                    elif userList2[i] == finalPresetList2[i]:
                        print("True", end=" ")
                    else:
                        print("\nFalse")
                        screen.fill(orangeLoss)
                        lossText = font80.render("You lose!", 0, black)
                        lossRect = lossText.get_rect(center=(width // 2, height // 2))
                        screen.blit(lossText, lossRect)
                        lossText2 = font30.render("Game over :(", 0, black)
                        lossRect2 = lossText2.get_rect(center=(width // 2, height // 2 + 70))
                        screen.blit(lossText2, lossRect2)

                        # "restart" button

                        # "exit" button


                        pygame.display.flip()
                        pygame.time.delay(2000)
                        sys.exit()

                # indexes -> millisecs
                # index [1] -> 1500 millisec
                if finalPresetList2[1] == 1 and len(userList2) == 1:
                    flashWhite2(q1Bsurface, green, q1Brect, 1500)
                elif finalPresetList2[1] == 2 and len(userList2) == 1:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 1500)
                elif finalPresetList2[1] == 3 and len(userList2) == 1:
                    flashWhite2(q3Bsurface, red, q3Brect, 1500)
                elif finalPresetList2[1] == 4 and len(userList2) == 1:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 1500)
                elif finalPresetList2[1] == 5 and len(userList2) == 1:
                    flashWhite2(q5Bsurface, blue, q5Brect, 1500)
                elif finalPresetList2[1] == 6 and len(userList2) == 1:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 1500)
                elif finalPresetList2[1] == 7 and len(userList2) == 1:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 1500)
                elif finalPresetList2[1] == 8 and len(userList2) == 1:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 1500)
                elif finalPresetList2[1] == 9 and len(userList2) == 1:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 1500)

                # index [2] -> 1000 millisec
                if finalPresetList2[2] == 1 and len(userList2) == 2:
                    flashWhite2(q1Bsurface, green, q1Brect, 1000)
                elif finalPresetList2[2] == 2 and len(userList2) == 2:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 1000)
                elif finalPresetList2[2] == 3 and len(userList2) == 2:
                    flashWhite2(q3Bsurface, red, q3Brect, 1000)
                elif finalPresetList2[2] == 4 and len(userList2) == 2:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 1000)
                elif finalPresetList2[2] == 5 and len(userList2) == 2:
                    flashWhite2(q5Bsurface, blue, q5Brect, 1000)
                elif finalPresetList2[2] == 6 and len(userList2) == 2:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 1000)
                elif finalPresetList2[2] == 7 and len(userList2) == 2:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 1000)
                elif finalPresetList2[2] == 8 and len(userList2) == 2:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 1000)
                elif finalPresetList2[2] == 9 and len(userList2) == 2:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 1000)

                # index [3] -> 900 millisec
                if finalPresetList2[3] == 1 and len(userList2) == 3:
                    flashWhite2(q1Bsurface, green, q1Brect, 900)
                elif finalPresetList2[3] == 2 and len(userList2) == 3:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 900)
                elif finalPresetList2[3] == 3 and len(userList2) == 3:
                    flashWhite2(q3Bsurface, red, q3Brect, 900)
                elif finalPresetList2[3] == 4 and len(userList2) == 3:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 900)
                elif finalPresetList2[3] == 5 and len(userList2) == 3:
                    flashWhite2(q5Bsurface, blue, q5Brect, 900)
                elif finalPresetList2[3] == 6 and len(userList2) == 3:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 900)
                elif finalPresetList2[3] == 7 and len(userList2) == 3:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 900)
                elif finalPresetList2[3] == 8 and len(userList2) == 3:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 900)
                elif finalPresetList2[3] == 9 and len(userList2) == 3:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 900)

                # index [4] -> 800 millisec
                if finalPresetList2[4] == 1 and len(userList2) == 4:
                    flashWhite2(q1Bsurface, green, q1Brect, 800)
                elif finalPresetList2[4] == 2 and len(userList2) == 4:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 800)
                elif finalPresetList2[4] == 3 and len(userList2) == 4:
                    flashWhite2(q3Bsurface, red, q3Brect, 800)
                elif finalPresetList2[4] == 4 and len(userList2) == 4:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 800)
                elif finalPresetList2[4] == 5 and len(userList2) == 4:
                    flashWhite2(q5Bsurface, blue, q5Brect, 800)
                elif finalPresetList2[4] == 6 and len(userList2) == 4:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 800)
                elif finalPresetList2[4] == 7 and len(userList2) == 4:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 800)
                elif finalPresetList2[4] == 8 and len(userList2) == 4:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 800)
                elif finalPresetList2[4] == 9 and len(userList2) == 4:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 800)

                # index [5] -> 700 millisec
                if finalPresetList2[5] == 1 and len(userList2) == 5:
                    flashWhite2(q1Bsurface, green, q1Brect, 700)
                elif finalPresetList2[5] == 2 and len(userList2) == 5:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 700)
                elif finalPresetList2[5] == 3 and len(userList2) == 5:
                    flashWhite2(q3Bsurface, red, q3Brect, 700)
                elif finalPresetList2[5] == 4 and len(userList2) == 5:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 700)
                elif finalPresetList2[5] == 5 and len(userList2) == 5:
                    flashWhite2(q5Bsurface, blue, q5Brect, 700)
                elif finalPresetList2[5] == 6 and len(userList2) == 5:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 700)
                elif finalPresetList2[5] == 7 and len(userList2) == 5:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 700)
                elif finalPresetList2[5] == 8 and len(userList2) == 5:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 700)
                elif finalPresetList2[5] == 9 and len(userList2) == 5:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 700)

                # index [6] -> 600 millisec
                if finalPresetList2[6] == 1 and len(userList2) == 6:
                    flashWhite2(q1Bsurface, green, q1Brect, 600)
                elif finalPresetList2[6] == 2 and len(userList2) == 6:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 600)
                elif finalPresetList2[6] == 3 and len(userList2) == 6:
                    flashWhite2(q3Bsurface, red, q3Brect, 600)
                elif finalPresetList2[6] == 4 and len(userList2) == 6:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 600)
                elif finalPresetList2[6] == 5 and len(userList2) == 6:
                    flashWhite2(q5Bsurface, blue, q5Brect, 600)
                elif finalPresetList2[6] == 6 and len(userList2) == 6:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 600)
                elif finalPresetList2[6] == 7 and len(userList2) == 6:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 600)
                elif finalPresetList2[6] == 8 and len(userList2) == 6:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 600)
                elif finalPresetList2[6] == 9 and len(userList2) == 6:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 600)

                # index [7] -> 500 millisec
                if finalPresetList2[7] == 1 and len(userList2) == 7:
                    flashWhite2(q1Bsurface, green, q1Brect, 500)
                elif finalPresetList2[7] == 2 and len(userList2) == 7:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 500)
                elif finalPresetList2[7] == 3 and len(userList2) == 7:
                    flashWhite2(q3Bsurface, red, q3Brect, 500)
                elif finalPresetList2[7] == 4 and len(userList2) == 7:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 500)
                elif finalPresetList2[7] == 5 and len(userList2) == 7:
                    flashWhite2(q5Bsurface, blue, q5Brect, 500)
                elif finalPresetList2[7] == 6 and len(userList2) == 7:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 500)
                elif finalPresetList2[7] == 7 and len(userList2) == 7:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 500)
                elif finalPresetList2[7] == 8 and len(userList2) == 7:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 500)
                elif finalPresetList2[7] == 9 and len(userList2) == 7:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 500)

                # index [8] -> 400 millisec
                if finalPresetList2[8] == 1 and len(userList2) == 8:
                    flashWhite2(q1Bsurface, green, q1Brect, 400)
                elif finalPresetList2[8] == 2 and len(userList2) == 8:
                    flashWhite2(q2Bsurface, lightYellow, q2Brect, 400)
                elif finalPresetList2[8] == 3 and len(userList2) == 8:
                    flashWhite2(q3Bsurface, red, q3Brect, 400)
                elif finalPresetList2[8] == 4 and len(userList2) == 8:
                    flashWhite2(q4Bsurface, lightPurple, q4Brect, 400)
                elif finalPresetList2[8] == 5 and len(userList2) == 8:
                    flashWhite2(q5Bsurface, blue, q5Brect, 400)
                elif finalPresetList2[8] == 6 and len(userList2) == 8:
                    flashWhite2(q6Bsurface, lightPink, q6Brect, 400)
                elif finalPresetList2[8] == 7 and len(userList2) == 8:
                    flashWhite2(q7Bsurface, yellow, q7Brect, 400)
                elif finalPresetList2[8] == 8 and len(userList2) == 8:
                    flashWhite2(q8Bsurface, cyan, q8Brect, 400)
                elif finalPresetList2[8] == 9 and len(userList2) == 8:
                    flashWhite2(q9Bsurface, lightOrange, q9Brect, 400)

        pygame.display.update()


def game1():

    # RULES SCREEN
    screen.fill(lightBlue)

    rulesLine1 = font50.render("The rules are simple: ", 0, black)
    rulesRect1 = rulesLine1.get_rect(center=(width // 2 - 15, height // 2 - 150))
    screen.blit(rulesLine1, rulesRect1)

    rulesLine2 = font30.render("  1. Click the box after it blinks white", 0, black)
    rulesRect2 = rulesLine2.get_rect(center=(width // 2, height // 2 - 80))
    screen.blit(rulesLine2, rulesRect2)

    rulesLine3 = font30.render("  and returns to its original color", 0, black)
    rulesRect3 = rulesLine3.get_rect(center=(width // 2 + 5, height // 2 - 50))
    screen.blit(rulesLine3, rulesRect3)

    rulesLine4 = font30.render("  2. That's it!", 0, black)
    rulesRect4 = rulesLine4.get_rect(center=(width // 2 - 115, height // 2 - 10))
    screen.blit(rulesLine4, rulesRect4)

    rulesLine5 = font30.render("Let's play.....", 0, black)
    rulesRect5 = rulesLine5.get_rect(center=(width // 2, height // 2 + 75))
    screen.blit(rulesLine5, rulesRect5)

    rulesLine3 = font30.render("[don't click on this screen]", 0, black)
    rulesRect3 = rulesLine3.get_rect(center=(width // 2, height // 2 + 175))
    screen.blit(rulesLine3, rulesRect3)

    pygame.display.flip()
    pygame.time.delay(8000)
    # pygame.time.delay(100)

    # GAME 1 SCREEN
    screen.fill(lightBlue)

    # draw 4 buttons
    # Q1: green
    q1button = font140.render("X-", 0, green)
    # (width, height)
    q1surface = pygame.Surface((q1button.get_size()[0], q1button.get_size()[1]))
    q1surface.fill(green)
    q1surface.blit(q1button, (10, 10))
    q1rect = q1button.get_rect(center=(width // 2 + 50, height // 2 - 50))
    screen.blit(q1surface, q1rect)

    # Q2: red
    q2button = font140.render("X-", 0, red)
    # (width, height)
    q2surface = pygame.Surface((q2button.get_size()[0], q2button.get_size()[1]))
    q2surface.fill(red)
    q2surface.blit(q2button, (10, 10))
    q2rect = q2button.get_rect(center=(width // 2 - 50, height // 2 - 50))
    screen.blit(q2surface, q2rect)

    # Q3: blue
    q3button = font140.render("X-", 0, blue)
    # (width, height)
    q3surface = pygame.Surface((q3button.get_size()[0], q3button.get_size()[1]))
    q3surface.fill(blue)
    q3surface.blit(q3button, (10, 10))
    q3rect = q3button.get_rect(center=(width // 2 - 50, height // 2 + 50))
    screen.blit(q3surface, q3rect)

    # Q4: yellow
    q4button = font140.render("X-", 0, yellow)
    # (width, height)
    q4surface = pygame.Surface((q4button.get_size()[0], q4button.get_size()[1]))
    q4surface.fill(yellow)
    q4surface.blit(q4button, (10, 10))
    q4rect = q4button.get_rect(center=(width // 2 + 50, height // 2 + 50))
    screen.blit(q4surface, q4rect)


    # draw gameboard
    newBoard = Gameboard(1, 2, screen)
    newBoard.drawGame1()

    '''presetList = []
    # generate randomized list of 14 digits
    for i in range(0, 14):
        x = random.randint(1, 4)
        presetList.append(x)
    print("presetList:", presetList, end=" ")
    finalPresetList = presetList'''

    presetList = []
    # generate randomized list of 4 digits
    for i in range(0, 4):
        x = random.randint(1, 4)
        presetList.append(x)
    print("presetList:", presetList, end=" ")
    finalPresetList = presetList


    # index [0] -> 2000 millisec
    if finalPresetList[0] == 1:
        flashWhite1(q1surface, green, q1rect, 2000)
    elif finalPresetList[0] == 2:
        flashWhite1(q2surface, red, q2rect, 2000)
    elif finalPresetList[0] == 3:
        flashWhite1(q3surface, blue, q3rect, 2000)
    elif finalPresetList[0] == 4:
        flashWhite1(q4surface, yellow, q4rect, 2000)

    userList = []

    running = True

    while running:
        global count
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # append num to userList when box is clicked
                # Q1: green = [1]
                if q1rect.collidepoint(event.pos):
                    flashBlack(q1surface, green, q1rect)
                    userList.append(1)
                    print("\n\nuserList:  ", userList)
                    print("presetList:", presetList)

                # Q2: red = [2]
                elif q2rect.collidepoint(event.pos):
                    flashBlack(q2surface, red, q2rect)
                    userList.append(2)
                    print("\n\nuserList:  ", userList)
                    print("presetList:", presetList)

                # Q3: blue = [3]
                elif q3rect.collidepoint(event.pos):
                    flashBlack(q3surface, blue, q3rect)
                    userList.append(3)
                    print("\n\nuserList:  ", userList)
                    print("presetList:", presetList)

                # Q4: yellow = [4]
                elif q4rect.collidepoint(event.pos):
                    flashBlack(q4surface, yellow, q4rect)
                    userList.append(4)
                    print("\n\nuserList:  ", userList)
                    print("presetList:", presetList)

                # if user clicks anywhere other than the 4 boxes
                else:
                    print("\n\nUser clicked on background")
                    # move q1Rect, q2Rect, q3Rect, + q4Rect off screen
                    q1rect = q1button.get_rect(center=(width + 100, height + 100))
                    q2rect = q2button.get_rect(center=(width + 100, height + 100))
                    q3rect = q3button.get_rect(center=(width + 100, height + 100))
                    q4rect = q4button.get_rect(center=(width + 100, height + 100))
                    screen.fill(orangeLoss)
                    # "ERROR: you clicked on the background"
                    lossText = font30.render("ERROR: you clicked on the background", 0, black)
                    lossRect = lossText.get_rect(center=(width // 2, height // 2 - 50))
                    screen.blit(lossText, lossRect)
                    # "Game over :("
                    lossText2 = font50.render("Game over :(", 0, black)
                    lossRect2 = lossText2.get_rect(center=(width // 2, height // 2 + 70))
                    screen.blit(lossText2, lossRect2)

                    # # "restart" button
                    # restartText = font50.render("restart", 0, black)
                    # restartSurface = pygame.Surface((restartText.get_size()[0] + 20, restartText.get_size()[1] + 20))
                    # restartSurface.fill(lightBlue)
                    # restartSurface.blit(restartText, (10, 10))
                    # restartRect = restartSurface.get_rect(center=(width // 2, height // 2 + 50))
                    # screen.blit(restartSurface, restartRect)

                    # # "exit" button
                    # exitText = font50.render("exit", 0, black)
                    # exitSurface = pygame.Surface((exitText.get_size()[0] + 20, exitText.get_size()[1] + 20))
                    # exitSurface.fill(lightBlue)
                    # exitSurface.blit(exitText, (10, 10))
                    # exitRect = exitSurface.get_rect(center=(width // 2, height // 2 + 100))
                    # screen.blit(exitSurface, exitRect)

                    pygame.display.flip()
                    pygame.time.delay(2000)
                    sys.exit()

                # check if user choice @ index i == preset list @ index i
                for i in range(0, len(userList)):
                    if len(userList) == 4 and userList[3] == finalPresetList[3]:
                        # move q1rect, q2rect, q3rect, + q4rect off screen
                        q1rect = q1button.get_rect(center=(width + 100, height + 100))
                        q2rect = q2button.get_rect(center=(width + 100, height + 100))
                        q3rect = q3button.get_rect(center=(width + 100, height + 100))
                        q4rect = q4button.get_rect(center=(width + 100, height + 100))
                        screen.fill(greenWin)
                        winText = font50.render("You won game 1!", 0, black)
                        winRect = winText.get_rect(center=(width // 2, height // 2 - 50))
                        screen.blit(winText, winRect)
                        winText2 = font30.render("onto game 2.....", 0, black)
                        winRect2 = winText2.get_rect(center=(width // 2, height // 2 + 50))
                        screen.blit(winText2, winRect2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        running = False
                        game2()
                    elif userList[i] == finalPresetList[i]:
                        print("True", end=" ")
                    else:
                        print("\nFalse")
                        screen.fill(orangeLoss)
                        lossText = font80.render("You lose!", 0, black)
                        lossRect = lossText.get_rect(center=(width // 2, height // 2))
                        screen.blit(lossText, lossRect)
                        lossText2 = font30.render("Game over :(", 0, black)
                        lossRect2 = lossText2.get_rect(center=(width // 2, height // 2 + 70))
                        screen.blit(lossText2, lossRect2)

                        # "restart" button

                        # "exit" button

                        pygame.display.flip()
                        pygame.time.delay(2000)
                        sys.exit()

                #indexes -> millisecs
                # index [1] -> 1500 millisec
                if finalPresetList[1] == 1 and len(userList) == 1:
                    flashWhite1(q1surface, green, q1rect, 1500)
                elif finalPresetList[1] == 2 and len(userList) == 1:
                    flashWhite1(q2surface, red, q2rect, 1500)
                elif finalPresetList[1] == 3 and len(userList) == 1:
                    flashWhite1(q3surface, blue, q3rect, 1500)
                elif finalPresetList[1] == 4 and len(userList) == 1:
                    flashWhite1(q4surface, yellow, q4rect, 1500)

                # index [2] -> 1000 millisec
                if finalPresetList[2] == 1 and len(userList) == 2:
                    flashWhite1(q1surface, green, q1rect, 1000)
                elif finalPresetList[2] == 2 and len(userList) == 2:
                    flashWhite1(q2surface, red, q2rect, 1000)
                elif finalPresetList[2] == 3 and len(userList) == 2:
                    flashWhite1(q3surface, blue, q3rect, 1000)
                elif finalPresetList[2] == 4 and len(userList) == 2:
                    flashWhite1(q4surface, yellow, q4rect, 1000)

                # index [3] -> 500 millisec
                if finalPresetList[3] == 1 and len(userList) == 3:
                    flashWhite1(q1surface, green, q1rect, 500)
                elif finalPresetList[3] == 2 and len(userList) == 3:
                    flashWhite1(q2surface, red, q2rect, 500)
                elif finalPresetList[3] == 3 and len(userList) == 3:
                    flashWhite1(q3surface, blue, q3rect, 500)
                elif finalPresetList[3] == 4 and len(userList) == 3:
                    flashWhite1(q4surface, yellow, q4rect, 500)

                '''# index [4] -> 700 millisec
                if finalPresetList[4] == 1 and len(userList) == 4:
                    flashWhite1(q1surface, green, q1rect, 700)
                elif finalPresetList[4] == 2 and len(userList) == 4:
                    flashWhite1(q2surface, red, q2rect, 700)
                elif finalPresetList[4] == 3 and len(userList) == 4:
                    flashWhite1(q3surface, blue, q3rect, 700)
                elif finalPresetList[4] == 4 and len(userList) == 4:
                    flashWhite1(q4surface, yellow, q4rect, 700)

                # index [5] -> 600 millisec
                if finalPresetList[5] == 1 and len(userList) == 5:
                    flashWhite1(q1surface, green, q1rect, 600)
                elif finalPresetList[5] == 2 and len(userList) == 5:
                    flashWhite1(q2surface, red, q2rect, 600)
                elif finalPresetList[5] == 3 and len(userList) == 5:
                    flashWhite1(q3surface, blue, q3rect, 600)
                elif finalPresetList[5] == 4 and len(userList) == 5:
                    flashWhite1(q4surface, yellow, q4rect, 600)

                # index [6] -> 500 millisec
                if finalPresetList[6] == 1 and len(userList) == 6:
                    flashWhite1(q1surface, green, q1rect, 500)
                elif finalPresetList[6] == 2 and len(userList) == 6:
                    flashWhite1(q2surface, red, q2rect, 500)
                elif finalPresetList[6] == 3 and len(userList) == 6:
                    flashWhite1(q3surface, blue, q3rect, 500)
                elif finalPresetList[6] == 4 and len(userList) == 6:
                    flashWhite1(q4surface, yellow, q4rect, 500)

                # index [7] -> 400 millisec
                if finalPresetList[7] == 1 and len(userList) == 7:
                    flashWhite1(q1surface, green, q1rect, 400)
                elif finalPresetList[7] == 2 and len(userList) == 7:
                    flashWhite1(q2surface, red, q2rect, 400)
                elif finalPresetList[7] == 3 and len(userList) == 7:
                    flashWhite1(q3surface, blue, q3rect, 400)
                elif finalPresetList[7] == 4 and len(userList) == 7:
                    flashWhite1(q4surface, yellow, q4rect, 400)

                # index [8] -> 300 millisec
                if finalPresetList[8] == 1 and len(userList) == 8:
                    flashWhite1(q1surface, green, q1rect, 300)
                elif finalPresetList[8] == 2 and len(userList) == 8:
                    flashWhite1(q2surface, red, q2rect, 300)
                elif finalPresetList[8] == 3 and len(userList) == 8:
                    flashWhite1(q3surface, blue, q3rect, 300)
                elif finalPresetList[8] == 4 and len(userList) == 8:
                    flashWhite1(q4surface, yellow, q4rect, 300)

                # index [9] -> 200 millisec
                if finalPresetList[9] == 1 and len(userList) == 9:
                    flashWhite1(q1surface, green, q1rect, 200)
                elif finalPresetList[9] == 2 and len(userList) == 9:
                    flashWhite1(q2surface, red, q2rect, 200)
                elif finalPresetList[9] == 3 and len(userList) == 9:
                    flashWhite1(q3surface, blue, q3rect, 200)
                elif finalPresetList[9] == 4 and len(userList) == 9:
                    flashWhite1(q4surface, yellow, q4rect, 200)

                # index [10] -> 100 millisec
                if finalPresetList[10] == 1 and len(userList) == 10:
                    flashWhite1(q1surface, green, q1rect, 100)
                elif finalPresetList[10] == 2 and len(userList) == 10:
                    flashWhite1(q2surface, red, q2rect, 100)
                elif finalPresetList[10] == 3 and len(userList) == 10:
                    flashWhite1(q3surface, blue, q3rect, 100)
                elif finalPresetList[10] == 4 and len(userList) == 10:
                    flashWhite1(q4surface, yellow, q4rect, 100)

                # index [11] -> 50 millisec
                if finalPresetList[11] == 1 and len(userList) == 11:
                    flashWhite1(q1surface, green, q1rect, 50)
                elif finalPresetList[11] == 2 and len(userList) == 11:
                    flashWhite1(q2surface, red, q2rect, 50)
                elif finalPresetList[11] == 3 and len(userList) == 11:
                    flashWhite1(q3surface, blue, q3rect, 50)
                elif finalPresetList[11] == 4 and len(userList) == 11:
                    flashWhite1(q4surface, yellow, q4rect, 50)

                # index [12] -> 40 millisec
                if finalPresetList[12] == 1 and len(userList) == 12:
                    flashWhite1(q1surface, green, q1rect, 40)
                elif finalPresetList[12] == 2 and len(userList) == 12:
                    flashWhite1(q2surface, red, q2rect, 40)
                elif finalPresetList[12] == 3 and len(userList) == 12:
                    flashWhite1(q3surface, blue, q3rect, 40)
                elif finalPresetList[12] == 4 and len(userList) == 12:
                    flashWhite1(q4surface, yellow, q4rect, 40)

                # index [13] -> 30 millisec
                if finalPresetList[13] == 1 and len(userList) == 13:
                    flashWhite1(q1surface, green, q1rect, 30)
                elif finalPresetList[13] == 2 and len(userList) == 13:
                    flashWhite1(q2surface, red, q2rect, 30)
                elif finalPresetList[13] == 3 and len(userList) == 13:
                    flashWhite1(q3surface, blue, q3rect, 30)
                elif finalPresetList[13] == 4 and len(userList) == 13:
                    flashWhite1(q4surface, yellow, q4rect, 30)'''



        pygame.display.update()

game1()

