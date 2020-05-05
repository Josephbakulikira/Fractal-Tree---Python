import pygame, math
import os

os.environ["SDL_VIDEO_CENTERED"]='1'

white, black, purple, blue = (255, 255, 255), (0, 0 ,0), (100, 0, 100), (21, 71, 200)
width, height = 1000, 1000

pygame.init()
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

speed = 0.01

def FractalTree(position, angle, z_value, n_value, direction,color=black, depth=0):
    branch_ratio = 0.30
    branch = z_value * branch_ratio
    angle_x = branch * math.cos(direction)
    angle_y = branch * math.sin(direction)
    (x, y) = n_value
    next_position = (x + angle_x, y + angle_y)
    pygame.draw.line(screen, color, n_value, next_position)

    if position > 0:
        if depth == 0:
            color2 = blue
            color1 = purple
        else:
            color1 = color
            color2 = color

        new = z_value * (1 - branch_ratio)
        FractalTree(position-1, angle, new, next_position, direction-angle, color1, depth+1)
        FractalTree(position-1, angle, new, next_position, direction+angle, color1, depth+1)


def main():
    angle = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        angle += speed
        screen.fill(white)
        FractalTree(9, angle, height * 0.9, (width//2, width-50), -math.pi/2)
        pygame.display.update()
if __name__=='__main__':
    main()
    pygame.quit()
