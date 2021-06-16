import pygame
import random

screen_width = 1500
screen_height = 700

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
# pygame.mixer.init()
# pygame.mixer.music.load()
# pygame.mixer.music.play()
clock = pygame.time.Clock()
soccer = pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MINI-SOCCER')
pygame.display.update()


#Required Functions
def plot_ball(window, color, centre, radius):
    pygame.draw.circle(window, color, centre, radius)


def plot_wall(window, color, specs):
    pygame.draw.rect(window, color, specs)


def score_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])

def gameloop():
    # Game variables
    exit_game = False
    game_over = False
    clock = pygame.time.Clock()
    FPS = 60
    ball_x = 750
    ball_y = 350
    ball_radius = 25
    ball_vel_x = 10
    ball_vel_y = 10
    ball_color = blue
    wall_length = 150
    wall_breadth = 10
    wall_x1 = 100
    wall_y1 = 330
    wall_x2 = screen_width - wall_x1
    wall_y2 = 330
    wall_vel_1 = 0
    wall_vel_2 = 0
    wall_color = red
    font = pygame.font.SysFont(None, 50)
    border_color = magenta
    SCORE_1 = 0
    SCORE_2 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                wall_vel_2 = 5
            if event.key == pygame.K_UP:
                wall_vel_2 = -5
            if event.key == pygame.K_w:
                wall_vel_1 = -5
            if event.key == pygame.K_s:
                wall_vel_1 = 5
    if ball_x - ball_radius <= 5:
        ball_vel_x = -ball_vel_x
    if ball_x + ball_radius >= screen_width - 5:
        ball_vel_x = -ball_vel_x
    if ball_y - ball_radius <= 165:
        ball_vel_y = -ball_vel_y
    if ball_y + ball_radius >= screen_height - 5:
        ball_vel_y = -ball_vel_y
    if ball_x - ball_radius == wall_x1 + wall_breadth + 5 and wall_y1 <= ball_y <= wall_y1 + wall_length:
        ball_vel_x = -ball_vel_x
    if ball_x + ball_radius == wall_x2 - 5 and wall_y2 <= ball_y <= wall_y2 + wall_length:
        ball_vel_x = -ball_vel_x

    if wall_y2 >= screen_height - wall_length - 5 or wall_y2 <= 165:
        wall_vel_2 = -wall_vel_2
    elif wall_y1 >= screen_height - wall_length - 5 or wall_y1 <= 165:
        wall_vel_1 = -wall_vel_1

    ball_x += ball_vel_x
    ball_y += ball_vel_y
    wall_y1 += wall_vel_1
    wall_y2 += wall_vel_2

    if ball_x == wall_x1:
        SCORE_2 += 1
    if ball_x == wall_x2 + 10:
        SCORE_1 += 1

    window.fill(black)
    score_screen(f'PLAYER-1 SCORE: {SCORE_1 / 2}', yellow, 225, 50)
    score_screen(f"PLAYER-2 SCORE: {SCORE_2 / 2}", yellow, 975, 50)
    pygame.draw.rect(window, border_color, [0, 150, screen_width, 10])
    pygame.draw.rect(window, border_color, [screen_width / 2 - 5, 0, 10, 700])
    pygame.draw.rect(window, border_color, [0, 0, 10, screen_height])
    pygame.draw.rect(window, border_color, [0, 0, screen_width, 10])
    pygame.draw.rect(window, border_color, [0, screen_height - 10, screen_width, 10])
    pygame.draw.rect(window, border_color, [screen_width - 10, 0, 10, screen_height])
    plot_ball(window, ball_color, [ball_x, ball_y], ball_radius)
    plot_wall(window, wall_color, [wall_x1, wall_y1, wall_breadth, wall_length])
    plot_wall(window, wall_color, [wall_x2, wall_y2, wall_breadth, wall_length])
    clock.tick(FPS)
    pygame.display.update()


    pygame.quit()
    quit()

while not exit_game:
    window.fill("black")
    score_screen('Press the SPACE key to start the game', red, 250, 320)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameloop()
        pygame.display.update()
        clock.tick(60)



# gameloop()
