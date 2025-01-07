
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_line_dda(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy): 
        step=abs(dx)
    else: 
        step=abs(dy)
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    screen.set_at((round(x), round(y)), WHITE)
    for i in range(step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x), round(y)), WHITE)
