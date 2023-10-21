import pygame
from pygame.locals import *
import postgresql

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill((255, 255, 255))
# pygame.draw.rect(screen, (255,255,255), [50,0,500,500])
for i in [200, 400]:
    pygame.draw.line(screen, (0, 0, 0), [i, 600], [i, 0], 5)
for i in [200, 400]:
    pygame.draw.line(screen, (0, 0, 0), [0, i], [600, i], 5)
touches = {(400, 400): 9, (200, 400): 8, (0, 400): 7,
           (400, 200): 6, (200, 200): 5, (0, 200): 4,
           (400, 0): 3, (200, 0): 2, (0, 0): 1}
game_running = True

while game_running:
    field = [["", "", ""], ["", "", ""], ["", "", ""]]
    for event in pygame.event.get():
        x = ""
        y = ""
        if event.type == MOUSEBUTTONDOWN:
            inpt = str(event)[37:45]
            for i in range(4):
                if inpt[i] == ',':
                    k = i
                    break
                x += inpt[i]
            for i in range(int(k) + 1, len(inpt)):
                if inpt[i] == ')': break
                y += inpt[i]

            for i in touches:
                if int(x) > i[0] and int(y) > i[1]:
                    print(touches[i])
                    break
        if event.type == QUIT:
            game_running = False
    pygame.display.update()
pygame.quit()
