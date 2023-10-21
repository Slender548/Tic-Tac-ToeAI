import pygame
from pygame.locals import *
import psycopg2

cursor = psycopg2.connect(user='postgres',
                          password='1234',
                          host='127.0.0.1',
                          port='5432').cursor()
cursor.execute("""CREATE TABLE TicTacToe(
first int, second int, third int, fourth int, fifth int, sixth int, seventh int, eighth int, nineth int);""")
cursor.execute("""SELECT * FROM TicTacToe""")
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-Tac-Toe")
touches = {(400, 400): 9, (200, 400): 8, (0, 400): 7,
           (400, 200): 6, (200, 200): 5, (0, 200): 4,
           (400, 0): 3, (200, 0): 2, (0, 0): 1}
game_running = True
screen.fill((255, 255, 255))
for i in [200, 400]:
    pygame.draw.line(screen, (0, 0, 0), [i, 600], [i, 0], 5)
for i in [200, 400]:
    pygame.draw.line(screen, (0, 0, 0), [0, i], [600, i], 5)
field = ["", "", "", "", "", "", "", "", ""]

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
]


def out_o(position: tuple):
    pygame.draw.circle(screen, (0, 0, 0), position, 75, 5)


def out_x(position: tuple):
    x = position[0]
    y = position[1]
    pygame.draw.line(screen, (0, 0, 0), (x - 75, y - 75), (x + 75, y + 75), width=5)
    pygame.draw.line(screen, (0, 0, 0), (x + 75, y - 75), (x - 75, y + 75), width=5)


player = True
winner = False


def check_winner(field):
    for combination in winning_combinations:
        a, b, c = combination
        if field[a] == field[b] == field[c] and field[a] != "":
            pygame.draw.rect(screen, (255, 255, 255), [100, 150, 400, 350])
            pygame.draw.line(screen, (0, 0, 0), (100, 150), (100, 500))
            pygame.draw.line(screen, (0, 0, 0), (500, 150), (500, 500))
            pygame.draw.line(screen, (0, 0, 0), (100, 150), (500, 150))
            pygame.draw.line(screen, (0, 0, 0), (100, 500), (500, 500))
            font = pygame.font.Font('freesansbold.ttf', 32)
            winner = True
            if not player:
                text = font.render('Player Wins!', True, (255, 255, 255), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (600 // 2, 625 // 2)
                screen.blit(text, textRect)
                print("Player wins!")
                # pygame.draw.rect(screen, )
            else:
                text = font.render('Player Wins!', True, (255, 255, 255), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (600 // 2,  625 // 2)
                screen.blit(text, textRect)
                print("AI wins!")


def draw_step(cell: int) -> None:
    global player
    global field
    coords = {1: (100, 100), 2: (300, 100), 3: (500, 100),
              4: (100, 300), 5: (300, 300), 6: (500, 300),
              7: (100, 500), 8: (300, 500), 9: (500, 500)}
    if player:
        if field[cell - 1] == "":
            field[cell - 1] = "O"
            out_o(coords[cell])
            player = False
    elif not player:
        if field[cell - 1] == "":
            field[cell - 1] = "X"
            out_x(coords[cell])
            player = True
    check_winner(field)
    return player


while game_running:
    for event in pygame.event.get():
        x, y = "", ""
        if event.type == MOUSEBUTTONDOWN:
            inpt = str(event)[37:45]
            for i in range(4):
                if inpt[i] == ',':
                    k = i
                    break
                x += inpt[i]
            for i in range(int(k) + 1, len(inpt)):
                if inpt[i] == ')':
                    break
                y += inpt[i]
            for i in touches:
                if int(x) > i[0] and int(y) > i[1]:
                    touch = touches[i]
                    break
            if not winner:
                draw_step(touch)
            print(field)
        if event.type == QUIT:
            game_running = False
    pygame.display.update()
pygame.quit()
