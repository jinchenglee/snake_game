"""
 Snake game
 
 Sample Python/Pygame Programs
 http://programarcadegames.com/
 
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
size = [400, 400]
frame_width = 20 
block_size = 10
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snake Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 250
rect_y = 50
 
# Snake list
snake = [(rect_x, rect_y)]

# Default direction of movement
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
cur_dir = 3

# Count clock ticks
cnt = 120

eaten = False

# Initial food block location
food_block = (random.randrange(1,(size[0]-1)//block_size)*block_size, random.randrange(1,(size[0]-1)//block_size)*block_size)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cur_dir = LEFT
            elif event.key == pygame.K_RIGHT:
                cur_dir = RIGHT
            elif event.key == pygame.K_UP:
                cur_dir = UP
            elif event.key == pygame.K_DOWN:
                cur_dir = DOWN
 
    if cnt == 0:
        # Food block
        food_block = (random.randrange(1,(size[0]-1)//block_size)*block_size, random.randrange(1,(size[0]-1)//block_size)*block_size)
        # Regenerate food block
        while food_block in snake:
            food_block = (random.randrange(1,(size[0]-1)//block_size)*block_size, random.randrange(1,(size[0]-1)//block_size)*block_size)
        # Count reset
        cnt = 120
        eaten = False

    if cnt % 3 == 0:
        # Move the snake head starting point
        if cur_dir == LEFT:
            new_block = (snake[0][0]-block_size,snake[0][1])
        elif cur_dir == RIGHT:
            new_block = (snake[0][0]+block_size,snake[0][1])
        elif cur_dir == UP:
            new_block = (snake[0][0],snake[0][1]-block_size)
        elif cur_dir == DOWN:
            new_block = (snake[0][0],snake[0][1]+block_size)
     
        # Insert new block at the front of snake list
        snake.insert(0,new_block)
        if food_block != new_block:
            snake.pop()
    
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        pygame.draw.line(screen, GREEN, [0, 0], [size[0]-1,0], frame_width)
        pygame.draw.line(screen, GREEN, [0, 0], [0,size[1]-1], frame_width)
        pygame.draw.line(screen, GREEN, [size[0]-1, 0], [size[0]-1,size[1]-1], frame_width)
        pygame.draw.line(screen, GREEN, [0, size[1]-1], [size[0]-1,size[1]-1], frame_width)
     
        # Draw the rectangle
        for row in range(39):
            for column in range(39):
                tmp_block = (row*block_size,column*block_size)
                if tmp_block in snake:
                    pygame.draw.rect(screen, WHITE, [tmp_block[0], tmp_block[1], block_size, block_size])
        if (food_block != new_block) and (not eaten):
            pygame.draw.rect(screen, RED, [food_block[0], food_block[1], block_size, block_size])
        elif (not eaten):
            pygame.draw.rect(screen, WHITE, [food_block[0], food_block[1], block_size, block_size])
            eaten = True
     
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # --- Wrap-up
    # Limit to n frames per second
    # If set to low value, key input response feels slow!
    clock.tick(20)
    cnt-=1

    if cnt % 3 == 0:
        # Snake hit the walls, quit the loop
        if new_block[1] > size[1]-block_size or new_block[1] < block_size:
            break
        if new_block[0] > size[0]-block_size or new_block[0] < block_size:
            break
        # Hit snake body, game over.
        if new_block in snake[2:]:
            break

# Game over
font = pygame.font.SysFont('Calibri',25, True, False)
text = font.render("Game Over!", True, RED)
screen.blit(text,[160,160])
pygame.display.flip()

# Close everything down
pygame.quit()
