
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformation (translation)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x1=int(input("enter x-coordinate"))
y1=int(input("enter y-coordinate"))
x2=int(input("enter x-coordinate"))
y2=int(input("enter y-coordinate"))
tx=int(input("enter translation vector of x coordinate"))
ty=int(input("enter translation vector of y coordinate"))
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
        draw_line_dda(x1+tx,y1+ty,x2+tx,y2+ty)



        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

