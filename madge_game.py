import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

player = pygame.Rect(400, 300, 50, 50)
enemy_x = random.randint(0,WIDTH - 50)
enemy_y = 0
enemy = pygame.Rect(enemy_x - 25,enemy_y - 25,50,50)
player_speed = 0.9
enemy_speed = 0.1

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Madge Game")

running = True
game_over = False
while running:
    
    enemy.x = enemy_x -25
    enemy.y = enemy_y -25 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x += player_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.y += player_speed

    screen.fill((30,30,40))

    pygame.draw.rect(screen, (0,0,0), player)
    pygame.draw.circle(screen,(255,0,0),(enemy_x,enemy_y),25)
 
    if enemy.colliderect(player):
          game_over = True


    if enemy_y > HEIGHT:
          enemy_y = 0
          enemy_x = random.randint(0,WIDTH - 50)

    if game_over:
          keys = pygame.key.get_pressed()
          if keys[pygame.K_r]:
                player_x = 400
                player_y = 300
                enemy_x = random.randint(0,WIDTH - 50)
                enemy_y = 0
                game_over = False
                

    if game_over:
          screen.fill((255, 255, 255))
          font = pygame.font.Font(None,80)
          text = font.render("GAME OVER",True,(0,0,0))
          screen.blit(text,(250,250))

    if not game_over:
        enemy_y += enemy_speed
     
    pygame.display.flip()

pygame.quit()



    

