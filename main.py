import pygame as pg
import sys
import random
import time
from paddle import Paddle

# Initialising the pg
pg.init()

# frames per second
c = pg.time.Clock()

# Dimensions for window
width = 900
height = 600

# creating game window
screen = pg.display.set_mode((width, height))

# Title and icon
pg.display.set_caption("Ping Pong Game")

# Game variables
ball_speedx = 6 * random.choice((1, -1))
ball_speedy = 6 * random.choice((1, -1))

# Game rectangle
ball = pg.Rect(width / 2 - 15, height / 2 - 15, 30, 30, )
player1 = Paddle(screen, width - 20, 0, 0)
player2 = Paddle(screen, 10, 6, 0)

# Function for ball to move
def ball_movement():
    global ball_speedx, ball_speedy, player1_score, player2_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    # Bouncing the ball
    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        player1.increase_score()
        ball_restart()
    if ball.right >= width:
        player2.increase_score()
        ball_restart()

    if ball.colliderect(player1.graphic) or ball.colliderect(player2.graphic):
        ball_speedx *= -1


# Function to reset the ball position
def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (width / 2, height / 2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))

def game_over(winner: int):
    player1.reset_score()
    player2.reset_score()
    print(f"Player {winner} wins!")
    time.sleep(2)

# Font variable
font = pg.font.SysFont("calibri", 25)

# Game Loop
while True:
    # checking for winner
    if player1.score >= 5:
        game_over(1)
    elif player2.score >= 5:
        game_over(2)

    for event in pg.event.get():
        # Checking for quit event
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # checking for key pressed event
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                player1.accelerate(8)
            if event.key == pg.K_UP:
                player1.accelerate(-8)
        # checking for key released event
        if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                player1.accelerate(-8)
            if event.key == pg.K_UP:
                player1.accelerate(8)

    # calling the movement methods
    ball_movement()
    player1.move()
    player2.bot_move(ball)

    # setting the score condition
    if ball.x < 0:
        player1.increase_score()
    elif ball.x > width:
        player2.increase_score()

    # Visuals
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (220, 220, 220), player1.graphic)
    pg.draw.rect(screen, (220, 220, 220), player2.graphic)
    pg.draw.ellipse(screen, (220, 220, 220), ball)
    pg.draw.aaline(screen, (220, 220, 220), (width / 2, 0), (width / 2, height))

    # To draw score font
    player1_text = font.render("Score:" + str(player1.score), False, (255, 255, 255))
    screen.blit(player1_text, [600, 50])
    player2_text = font.render("Score:" + str(player2.score), False, (255, 255, 255))
    screen.blit(player2_text, [300, 50])

    # Updating the game window
    pg.display.update()

    # 60 frames per second
    c.tick(60)