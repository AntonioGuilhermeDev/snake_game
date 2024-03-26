
import pygame
import random

pygame.init()
pygame.display.set_caption('Jogo Snake Python')
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#CORES
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

#Parametros
square_size = 10 
snake_speed = 15


def generate_food():
       food_x = round(random.randrange(0 , width - square_size) / float(square_size)) * float(square_size)
       food_y = round(random.randrange(0, height - square_size) / float(square_size)) * float(square_size)
       return food_x, food_y

def draw_food(size, food_x, food_y):
     pygame.draw.rect(screen, green, [food_x, food_y, size, size])

def draw_snake(size, snake_pixels):
     for pixel in snake_pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])

def draw_score(score):
     font = pygame.font.SysFont('Helvetica', 25)
     text = font.render(f'Score: {score}', True, red)
     screen.blit(text, [1, 1])

def select_speed(key):
     if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
     if key == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
     elif key == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0
     elif key == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
     return speed_x, speed_y

def run_game():   
    game_over = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    snake_pixels = []
    food_x, food_y = generate_food()
    

    while not game_over:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                 speed_x, speed_y = select_speed(event.key)
        
        
        draw_food(square_size, food_x, food_y)
        
        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True
        x += speed_x
        y += speed_y
     
        snake_pixels.append([x, y])
        if len(snake_pixels) > snake_size:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
             if pixel == [x, y]:
                  game_over = True
        
        
        draw_snake(square_size, snake_pixels)
        draw_score(snake_size - 1)



        pygame.display.update()

        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = generate_food()

        clock.tick(snake_speed)

run_game()
 










