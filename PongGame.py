# Ping Pong Game

# Importing the useful libraries
import pygame as pg
import math
import random
from pygame import mixer

# Initializing pygame
pg.init()

# Creating game window
screen = pg.display.set_mode((820, 620))

# Loading background
background = pg.image.load('back.png')

# Setting up title
pg.display.set_caption('Ping-Pong Game')
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

# Background Music
mixer.music.load('background.mp3')
mixer.music.play(-1)

# Creating two players to play
p1_Img = pg.image.load('player1.png')
p1_X = 20
p1_Y = 294
p1_changeY = 0

p2_Img = pg.image.load('player2.png')
p2_X = 736
p2_Y = 294
p2_changeY = 0

# Score Showing
score_1 = 0
score_2 = 0
score_font = pg.font.Font('freesansbold.ttf', 32)

score_X = 20
score_Y = 20

# Showing hints
hints = pg.font.Font('freesansbold.ttf', 24)
hint_X = 56
hint_Y = 550

# Winner
winner = pg.font.Font('freesansbold.ttf', 72)
winner_X = 100
winner_Y = 300

# Creating a ball to play
ball_Img = pg.image.load('ball.png')
ball_X = 384
ball_Y = 294
ball_changeX = -1
ball_changeY = 0


def player1(x, y):
    screen.blit(p1_Img, (x, y))


def player2(x, y):
    screen.blit(p2_Img, (x, y))


def ball(x, y):
    screen.blit(ball_Img, (x, y))


def show_score(x, y):
    score_value = score_font.render("Score A : " + str(score_1) + "  Score B : " + str(score_2), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def show_hints(x, y):
    show_hint = hints.render("Player A : W -> UP, S -> DOWN   Player B : I -> UP, K -> DOWN", True, (255, 255, 255))
    screen.blit(show_hint, (x, y))


def show_winner(x, y):
    global running
    if score_1 == 11:
        show_win = winner.render("Player A Won!!!", True, (255, 255, 255))
        screen.blit(show_win, (x, y))
        running = False
    elif score_2 == 11:
        show_win = winner.render("Player B Won!!!", True, (255, 255, 255))
        screen.blit(show_win, (x, y))
        running = False
    else:
        pass


def iscollision1(ball_X, ball_Y, p1_X, p1_Y):
    distance = math.sqrt(math.pow(ball_X - p1_X, 2) + math.pow(ball_Y - p1_Y, 2))
    if distance <= 50:
        return True
    else:
        return False


def iscollision2(ball_X, ball_Y, p2_X, p2_Y):
    distance = math.sqrt(math.pow(ball_X - p2_X, 2) + math.pow(ball_Y - p2_Y, 2))
    if distance <= 50:
        return True
    else:
        return False


# Infinite while loop
running = True
while running:
    # For background
    screen.fill((0, 0, 0))
    screen.blit(background, (10, 10))

    # Exiting the Game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Checking if any keystroke is pressed or not
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                p1_changeY = -2
            elif event.key == pg.K_s:
                p1_changeY = 2

            if event.key == pg.K_i:
                p2_changeY = -2
            elif event.key == pg.K_k:
                p2_changeY = 2

        # If keystroke is released
        if event.type == pg.KEYUP:
            if event.key == pg.K_w or event.key == pg.K_s or event.key == pg.K_i or event.key == pg.K_k:
                p1_changeY = 0
                p2_changeY = 0

    # Positioning and moving the players
    p1_Y += p1_changeY
    if p1_Y <= 60:
        p1_Y = 60
    elif p1_Y >= 500:
        p1_Y = 500
    player1(p1_X, p1_Y)

    p2_Y += p2_changeY
    if p2_Y <= 60:
        p2_Y = 60
    elif p2_Y >= 500:
        p2_Y = 500
    player2(p2_X, p2_Y)

    # Positioning the ball
    ball_X += ball_changeX
    ball_Y += ball_changeY
    ball(ball_X, ball_Y)

    # Counting the score
    if ball_X <= 10:
        ball_X = 384
        ball_Y = 294
        score_2 += 1
    elif ball_X >= 810:
        ball_X = 384
        ball_Y = 294
        score_1 += 1
    elif ball_Y <= 80:
        ball_changeY *= -1
    elif ball_Y >= 520:
        ball_changeY *= -1

    # Collision
    collision1 = iscollision1(ball_X, ball_Y, p1_X, p1_Y)
    if collision1:
        hit = mixer.Sound('hit.wav')
        hit.play()
        ball_changeX = 3
        ball_changeY = random.randint(-1, 1)

    collision2 = iscollision2(ball_X, ball_Y, p2_X, p2_Y)
    if collision2:
        hit = mixer.Sound('hit.wav')
        hit.play()
        ball_changeX = -3
        ball_changeY = random.randint(-1, 1)

    # Showing the score
    show_score(score_X, score_Y)
    show_hints(hint_X, hint_Y)
    show_winner(winner_X, winner_Y)

    # Updating the screen
    pg.display.update()
