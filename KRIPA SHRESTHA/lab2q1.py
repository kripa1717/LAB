
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 0, 0)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm

def draw_line_dda(x1, y1, x2, y2):
    dx=abs(int(x2-x1))
    dy=abs(int(y2-y1))
    x=x1
    y=y1
    if abs(x2)>abs(x1): 
        lx=1
    else: 
      lx=-1
    if abs(y2)>(y1):
        ly=1
    else:
        ly=-1 
    if abs(dx)>(dy):
            p=2*dy-dx
            while(not(x==x2)):
                if p<0:
                    x=x+lx
                    p=p+2*dy
                else:
                    x=x+lx
                    y=y+ly
                    p=p+2*dy-2*dx
                screen.set_at((round(x), round(y)), WHITE)
    else:
        p=2*dx-dy
        while(not(y==y2)):
            if p<0:
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((round(x), round(y)), WHITE)

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
        draw_line_dda(100,200 , 200, 100)
        draw_line_dda(200,100 , 300, 200)
        draw_line_dda(300,200 , 100, 200)
        draw_line_dda(100,200 , 100, 500)
        draw_line_dda(300,500 , 300, 200)
        draw_line_dda(300,500 , 500, 500)
        draw_line_dda(500,500 , 500, 200)
        draw_line_dda(500,200 , 700, 200)
        draw_line_dda(700,200 , 700, 500)
        draw_line_dda(500,200 , 600, 100)
        draw_line_dda(600,100 , 700, 200)
        draw_line_dda(100,500 , 700, 500)
        draw_line_dda(300,350 , 500, 350)
        draw_line_dda(350,500 , 350, 400)
        draw_line_dda(350,400 , 450, 400)
        draw_line_dda(450,400 , 450, 500)
        draw_line_dda(400,200 , 500, 350)
        draw_line_dda(300,350 , 400, 200)


        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()