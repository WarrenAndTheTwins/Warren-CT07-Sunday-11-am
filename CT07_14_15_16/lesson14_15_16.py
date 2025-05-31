print("Hello from lesson 14_15_16")
import pygame
from pygame.transform import rotate
pygame.init()

background_image = pygame.image.load("/workspaces/Warren-CT07-Sunday-11-am/CT07_14_15_16/Grass Court.jpg")
tennis_ball_image = pygame.image.load("/workspaces/Warren-CT07-Sunday-11-am/CT07_14_15_16/Tennis Ball.png")
tennis_racket_image = pygame.image.load("/workspaces/Warren-CT07-Sunday-11-am/CT07_14_15_16/Tennis Racket.png")
screen_width = 800
screen_height = 600
paddle_width = 20
paddle_height = 100
paddle1_x = 10
paddle1_y = screen_height // 2 - paddle_height // 2
paddle2_x = screen_width - paddle_width - 10
paddle2_y = screen_height // 2 - paddle_height // 2
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
white = (255, 255, 255)
ball_dx = 7
ball_dy = 7
player1_score = 0
player2_score = 0
screen = pygame.display.set_mode((screen_width, screen_height))
score_font = pygame.font.Font(None, 32)

pygame.display.set_caption("Pong Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    screen.blit(background_image,(0,0)) #this set the color back black 
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 1
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += 1

    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 1
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += 1
    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= screen_height:
        ball_dy *= -1
    # if ball_x <= 0 or ball_x >= screen_width:
    #     ball_dx *= -1
    if ball_x >= screen_width:
        ball_dx *= -1
        player1_score += 1
        print("Player 1 score: " + str(player1_score))
    if ball_x <= 0:
        ball_dx *= -1
        player2_score += 1
        print("Player 2 score: " + str(player2_score))
    paddle1_box = pygame.Rect(paddle1_x, paddle1_y, paddle_width, paddle_height)
    paddle2_box = pygame.Rect(paddle2_x, paddle2_y, paddle_width, paddle_height)

    if ball_x <= paddle1_box.right + ball_radius and ball_y >= paddle1_box.top and ball_y <= paddle1_box.bottom:
        ball_dx *= -1
    if ball_x >= paddle2_box.left - ball_radius and ball_y >= paddle2_box.top and ball_y <= paddle2_box.bottom:
        ball_dx *= -1           

    screen.blit(tennis_racket_image,(paddle1_x, paddle1_y, paddle_width, paddle_height))
    screen.blit(rotate(tennis_racket_image, 180),(paddle2_x, paddle2_y, paddle_width, paddle_height))
    screen.blit(tennis_ball_image, (ball_x - ball_radius, ball_y - ball_radius))
    player1_score_text = score_font.render("Player 1 : " + str(player1_score), True, (0, 0, 0))
    player2_score_text = score_font.render("Player 2 : " + str(player2_score), True, (0, 0, 0))
    screen.blit(player1_score_text, (10, 10))
    screen.blit(player2_score_text, (screen_width - player1_score_text.get_width()-10, 10))

    pygame.display.flip()
pygame.quit()