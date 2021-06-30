import time
import pygame
from pygame_widgets import Button, TextBox
import sys

screen_width = 1500
screen_height = 700

#COLORS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SOCCER GAME')
icon = pygame.image.load("images/icon.jpg").convert()
pygame.display.set_icon(icon)
pygame.display.update()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])

def plot_ball(window, color, centre, radius):
    pygame.draw.circle(window, color, centre, radius)
def plot_wall(window, color, specs):
    pygame.draw.rect(window, color, specs)

def ending(SCORE_1, SCORE_2):
    exit_game = False
    while not exit_game:
        window.fill(black)
        im = pygame.image.load("images/goal.jpg")
        im = pygame.transform.scale(im, (screen_width, screen_height))
        window.blit(im, (0, 0))
        text = TextBox(
            window, 600, 50, 335, 150,
            colour=yellow,
            borderColour=red,
            borderThickness=15,
            textColour=(0, 10, 20),
            fontSize=100
        )
        text.setText("RESULT")
        replay = Button(
            window, 400, 450, 300, 100,
            inactiveColour=(100, 200, 255),
            hoverColour=(255, 244, 122),
            onClick=lambda: gameloop(),
            shadowDistance=10,
            shadowColour=(50, 50, 50),
            radius=10,
            text='REPLAY',
            fontSize=30,
        )
        exit = Button(
            window, 800, 450, 300, 100,
            inactiveColour=(100, 200, 255),
            hoverColour=(255, 244, 122),
            onClick=lambda: sys.exit(0),
            shadowDistance=10,
            shadowColour=(50, 50, 50),
            radius=10,
            text='EXIT GAME',
            fontSize=30,
        )
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
        text_screen(f"PLAYER-1 SCORE: {SCORE_1 / 2}", black, 400, 300)
        text_screen(f"PLAYER-2 SCORE: {SCORE_2 / 2}", black, 800, 300)
        if SCORE_2 > SCORE_1:
            text_screen(f"PLAYER-2 IS THE WINNER!", magenta, 520, 375)
        elif SCORE_1 > SCORE_2:
            text_screen(f"PLAYER-1 IS THE WINNER!", magenta, 520, 375)
        else:
            text_screen(f"Game has ended in a DRAW", magenta, 500, 375)
        text.draw()
        replay.listen(events)
        replay.draw()
        exit.listen(events)
        exit.draw()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    time.sleep(0.5)
    exit_game = False
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
    SCORE_1 = 0
    SCORE_2 = 0
    border_color = green
    FPS = 60
    clock = pygame.time.Clock()

    while not exit_game:
        window.fill(black)
        img = pygame.image.load("images/cross.jpg").convert()
        img = pygame.transform.scale(img, (80, 80))
        bg = pygame.image.load("images/stadium.jpg").convert()
        bg = pygame.transform.scale(bg, (screen_width, screen_height))
        window.blit(bg, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ending(SCORE_1, SCORE_2)
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
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()
        if ball_x + ball_radius >= screen_width - 5:
            ball_vel_x = -ball_vel_x
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()
        if ball_y - ball_radius <= 165:
            ball_vel_y = -ball_vel_y
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()
        if ball_y + ball_radius >= screen_height - 5:
            ball_vel_y = -ball_vel_y
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()
        if ball_x - ball_radius == wall_x1 + wall_breadth + 5 and wall_y1 - ball_radius <= ball_y <= wall_y1 + wall_length + ball_radius:
            ball_vel_x = -ball_vel_x
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()
        if ball_x + ball_radius == wall_x2 - 5 and wall_y2 - ball_radius <= ball_y <= wall_y2 + wall_length + ball_radius:
            ball_vel_x = -ball_vel_x
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()

        if wall_y2 >= screen_height - wall_length - 5 or wall_y2 <= 165:
            wall_vel_2 = -wall_vel_2

        if wall_y1 >= screen_height - wall_length - 5 or wall_y1 <= 165:
            wall_vel_1 = -wall_vel_1

        ball_x += ball_vel_x
        ball_y += ball_vel_y
        wall_y1 += wall_vel_1
        wall_y2 += wall_vel_2

        if ball_x == wall_x1:
            SCORE_2 += 1
        if ball_x == wall_x2 + 10:
            SCORE_1 += 1
        close = Button(
            window, 650, 45, 80, 80,
            inactiveColour=red,
            hoverColour=(255, 244, 122),
            onClick=lambda: ending(SCORE_1, SCORE_2),
            shadowColour=(50, 50, 50),
            radius=10,
            # text='X',
            image=img,
            # imageHAlign=20,
            # imageVAlign=20,
            fontSize=60
        )
        text_screen(f'PLAYER-1 SCORE: {SCORE_1 / 2}', yellow, 225, 50)
        text_screen(f"PLAYER-2 SCORE: {SCORE_2 / 2}", yellow, 975, 50)
        pygame.draw.rect(window, border_color, [0, 150, screen_width, 10])
        pygame.draw.rect(window, border_color, [screen_width / 2 - 5, 0, 10, 700])
        pygame.draw.rect(window, border_color, [0, 0, 10, screen_height])
        pygame.draw.rect(window, border_color, [0, 0, screen_width, 10])
        pygame.draw.rect(window, border_color, [0, screen_height - 10, screen_width, 10])
        pygame.draw.rect(window, border_color, [screen_width - 10, 0, 10, screen_height])
        plot_ball(window, ball_color, [ball_x, ball_y], ball_radius)
        plot_wall(window, wall_color, [wall_x1, wall_y1, wall_breadth, wall_length])
        plot_wall(window, wall_color, [wall_x2, wall_y2, wall_breadth, wall_length])
        close.listen(events)
        close.draw()
        pygame.display.update()
        clock.tick(FPS)

def welcome():
    exit_game = False
    while not exit_game:
        window.fill(black)
        image = pygame.image.load("images/bg2.jpg")
        image = pygame.transform.scale(image, (screen_width, screen_height))
        window.blit(image, (40, 100))
        text = TextBox(
            window, 375, 50, 750, 150,
            colour=yellow,
            borderColour=red,
            borderThickness=15,
            textColour=(0, 10, 20),
            fontSize=100
        )
        text.setText("THE SOCCER GAME")
        button = Button(
            window, 600, 250, 300, 100,
            inactiveColour=(100, 200, 255),
            hoverColour=(255, 244, 122),
            onClick=lambda: gameloop(),
            shadowDistance=10,
            shadowColour=(50, 50, 50),
            radius=10,
            text='START',
            fontSize=30,
        )
        button1 = Button(
            window, 600, 450, 300, 100,
            inactiveColour=(100, 200, 255),
            hoverColour=(255, 244, 122),
            onClick=lambda: sys.exit(0),
            shadowDistance=10,
            shadowColour=(50, 50, 50),
            radius=10,
            text='EXIT',
            fontSize=30,
        )

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit_game = True

        button.listen(events)
        button.draw()
        button1.listen(events)
        button1.draw()
        text.draw()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    welcome()


