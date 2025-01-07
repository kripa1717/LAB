
import pygame
import sys
from math import *

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformation (rotation)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x1=int(input("enter x-coordinate"))
y1=int(input("enter y-coordinate"))
x2=int(input("enter x-coordinate"))
y2=int(input("enter y-coordinate"))
a=int(input("enter angle to be rotated"))
the=a*(3.14/180)

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
x3=int(((x1*cos(the))-(y1*sin(the))))
y3=int(((x1*sin(the))+(y1*cos(the))))
x4=int(((x2*cos(the))-(y2*sin(the))))
y4=int(((x2*sin(the))+(y2*cos(the))))
        

# Main loop
  

      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_dda(x1,y1,x2,y2)
        draw_line_dda(x3,y3,x4,y4)



        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

