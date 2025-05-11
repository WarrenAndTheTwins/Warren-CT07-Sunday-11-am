print("Hello from lesson 14_15_16")
import pygame
pygame.init()

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
ball_dx = 0.5
ball_dy = 0.5
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pong Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 1
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += 1

    if keys[pygame.K_UP] and paddle1_y > 0:
        paddle1_y -= 1
    if keys[pygame.K_DOWN] and paddle1_y < screen_height - paddle_height:
        paddle1_y += 1
    ball_x += ball_dx
    ball_y += ball_dy

    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
pygame.quit