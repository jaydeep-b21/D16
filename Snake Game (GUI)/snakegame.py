import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Get the screen dimensions
dis_width = pygame.display.Info().current_w
dis_height = pygame.display.Info().current_h

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game In Python')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 25

# Use custom fonts
font_style = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 36)

def Your_score(score, speed):
    score_text = score_font.render("Your Score: " + str(score), True, yellow)
    speed_text = score_font.render("Snake Speed: " + str(speed), True, yellow)
    dis.blit(score_text, [20, 20])
    dis.blit(speed_text, [20, 60])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    global snake_speed  # Declare snake_speed as global

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block, snake_block))
    foody = round(random.randrange(0, dis_height - snake_block, snake_block))

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message(
                "You Lost! Press 'C' to Play Again or 'Q' To Quit The Game",
                red)
            Your_score(Length_of_snake - 1, snake_speed)  # Pass snake_speed
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0:
            game_close = True
        if y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - snake_block

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, snake_speed)  # Pass snake_speed

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(
                random.randrange(0, dis_width - snake_block, snake_block))
            foody = round(
                random.randrange(0, dis_height - snake_block, snake_block))
            Length_of_snake += 1
            snake_speed += 1  # Increase the snake's speed

        clock.tick(snake_speed)


    pygame.quit()
    quit()

gameLoop()
