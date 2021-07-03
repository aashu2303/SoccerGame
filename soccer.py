import time
import pygame
from pygame_widgets import *
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

# INITIALIZING PYGAME WINDOW
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


def plot_ball(win, color, centre, radius):
    pygame.draw.circle(win, color, centre, radius)


def plot_wall(win, color, specs):
    pygame.draw.rect(win, color, specs)


def ending(score_1, score_2, name1, name2, ball_c, wall_c):
    exit_game = False
    im = pygame.image.load("images/goal.jpg")
    im = pygame.transform.scale(im, (screen_width, screen_height))
    window.blit(im, (0, 0))
    text = TextBox(
        window, 525, 50, 465, 150,
        colour=yellow,
        borderColour=red,
        borderThickness=10,
        radius=5,
        textColour=(0, 10, 20),
        fontSize=100
    )
    text.setText("IT'S A GOAL")
    replay = Button(
        window, 500, 450, 200, 80,
        inactiveColour=(100, 150, 255),
        hoverColour=(255, 244, 122),
        onClick=lambda: gameloop(name1, name2, ball_c, wall_c),
        shadowDistance=10,
        shadowColour=(50, 50, 50),
        radius=10,
        text='REPLAY',
        fontSize=40,
    )
    exite = Button(
        window, 800, 450, 200, 80,
        inactiveColour=(100, 150, 255),
        hoverColour=(255, 244, 122),
        onClick=lambda: sys.exit(0),
        shadowDistance=10,
        shadowColour=(50, 50, 50),
        radius=10,
        text='EXIT GAME',
        fontSize=40,
    )
    while not exit_game:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
        text_screen(f"{name1}'S SCORE: {score_1 / 2}", black, 350, 300)
        text_screen(f"{name2}'S SCORE: {score_2 / 2}", black, 900, 300)
        if score_2 > score_1:
            text_screen(f"PLAYER-2 IS THE WINNER!", magenta, 520, 375)
        elif score_1 > score_2:
            text_screen(f"PLAYER-1 IS THE WINNER!", magenta, 520, 375)
        else:
            text_screen(f"Game has ended in a DRAW", magenta, 500, 375)
        text.draw()
        replay.listen(events)
        replay.draw()
        exite.listen(events)
        exite.draw()
        pygame.display.update()
        clock.tick(60)


def gameloop(name1, name2, ball_c, wall_c):
    time.sleep(0.5)
    exit_game = False
    ball_x = 750
    ball_y = 350
    ball_radius = 25
    ball_vel_x = 10
    ball_vel_y = 10
    ball_color = ball_c
    wall_length = 150
    wall_breadth = 10
    wall_x1 = 100
    wall_y1 = 330
    wall_x2 = screen_width - wall_x1
    wall_y2 = 330
    wall_vel_1 = 0
    wall_vel_2 = 0
    wall_color = wall_c
    player1 = name1
    player2 = name2
    SCORE_1 = 0
    SCORE_2 = 0
    border_color = green
    clock = pygame.time.Clock()
    imag = pygame.image.load("images/cross.jpg").convert()
    imag = pygame.transform.scale(imag, (80, 80))
    ws_img = pygame.image.load("images/ws.jpg")
    ws_img = pygame.transform.scale(ws_img, (80, 100))
    updown_img = pygame.image.load("images/updown.jpg")
    updown_img = pygame.transform.scale(updown_img, (80, 100))
    bg = pygame.image.load("images/stadium.jpg").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    close = Button(
        window, 710, 40, 80, 80,
        onClick=lambda: ending(SCORE_1, SCORE_2, name1, name2, ball_c, wall_c),
        image=imag
    )
    ws = Button(
        window, 40, 30, 80, 100,
        image=ws_img
    )
    updown = Button(
        window, 1370, 30, 80, 100,
        image=updown_img
    )
    while not exit_game:
        window.blit(bg, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ending(SCORE_1, SCORE_2, name1, name2, ball_c, wall_c)
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
        if ball_x - ball_radius == wall_x1 + wall_breadth + 5 and wall_y1 - ball_radius <= ball_y <= wall_y1 + \
                wall_length + ball_radius:
            ball_vel_x = -ball_vel_x
            pygame.mixer.music.load('hit_sound.wav')
            pygame.mixer.music.play()
        if ball_x + ball_radius == wall_x2 - 5 and wall_y2 - ball_radius <= ball_y <= wall_y2 + wall_length + \
                ball_radius:
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
        text_screen(f"{player1}'S SCORE: {SCORE_1 / 2}", yellow, 175, 50)
        text_screen(f"{player2}'S SCORE: {SCORE_2 / 2}", yellow, 925, 50)
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
        ws.draw()
        updown.draw()
        pygame.display.update()
        clock.tick(60)


def settings():
    time.sleep(0.5)
    exit_game = False
    image = pygame.image.load("images/bg2.jpg").convert()
    image = pygame.transform.scale(image, (screen_width, screen_height))
    text = TextBox(
        window, 600, 50, 290, 100,
        colour=yellow,
        radius=5,
        borderColour=red,
        borderThickness=10,
        textColour=(0, 10, 20),
        fontSize=70
    )
    text.setText("SETTINGS")
# PLAYER NAMES
    player1_name = TextBox(
        window, 625, 200, 250, 60,
        fontSize=40,
        radius=5,
        borderColour=cyan,
        borderThickness=5,
        placeholderText="Enter Player-1 Name"
    )
    player2_name = TextBox(
        window, 625, 300, 250, 60,
        fontSize=40,
        radius=5,
        borderThickness=5,
        borderColour=cyan,
        placeholderText="Enter Player-2 Name"
    )
    player1_name.setText("PLAYER-1")
    player2_name.setText("PLAYER-2")
    ball_name = TextBox(
        window, 80, 80, 230, 60,
        fontSize=40,
        radius=5,
        borderColour=cyan,
        borderThickness=5
    )
    ball_name.setText("BALL COLOUR")
    wall_name = TextBox(
        window, 1200, 80, 230, 60,
        fontSize=40,
        radius=5,
        borderColour=cyan,
        borderThickness=5
    )
    wall_name.setText("WALL COLOUR")
# BALL COLORS
    ball_r = Slider(
        window, 300, 400, 200, 30,
        min=0,
        max=255,
        step=1,
        handleColour=yellow
    )
    ball_g = Slider(
        window, 650, 400, 200, 30,
        min=0,
        max=255,
        step=1,
        handleColour=yellow
    )
    ball_b = Slider(
        window, 1000, 400, 200, 30,
        min=0,
        max=255,
        step=1,
        handleColour=yellow
    )

    ball_r_disp = TextBox(
        window, 530, 400, 30, 30,
        borderColour=white
    )
    ball_g_disp = TextBox(
        window, 880, 400, 30, 30,
        borderColour=white
    )
    ball_b_disp = TextBox(
        window, 1230, 400, 30, 30,
        borderColour=white
    )

# WALL COLOURS
    wall_r = Slider(
        window, 300, 500, 200, 30,
        min=0,
        max=255,
        step=1,
        handleColour=yellow
    )
    wall_g = Slider(
        window, 650, 500, 200, 30,
        min=0,
        max=255,
        step=1,
        handleColour=yellow
    )
    wall_b = Slider(
        window, 1000, 500, 200, 30,
        min=0,
        max=255,
        step=1,
        handleColour=yellow
    )
    wall_r_disp = TextBox(
        window, 530, 500, 30, 30,
        borderColour=white
    )
    wall_g_disp = TextBox(
        window, 880, 500, 30, 30,
        borderColour=white
    )
    wall_b_disp = TextBox(
        window, 1230, 500, 30, 30,
        borderColour=white
    )

# NAVIGATION BUTTONS
    but = Button(
        window, 850, 550, 150, 80,
        inactiveColour=(100, 150, 255),
        hoverColour=(255, 244, 122),
        onClick=lambda: gameloop(player1_name.getText().upper(), player2_name.getText().upper(), ball_color, wall_color),
        shadowDistance=10,
        shadowColour=(50, 50, 50),
        radius=10,
        text='PLAY',
        fontSize=40,
    )
    back = Button(
        window, 550, 550, 150, 80,
        inactiveColour=(100, 150, 255),
        hoverColour=(255, 244, 122),
        onClick=lambda: welcome(),
        shadowDistance=10,
        shadowColour=(50, 50, 50),
        radius=10,
        text='BACK',
        fontSize=40,
    )
    while not exit_game:
        window.fill(black)
        window.blit(image, (40, 80))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)

        text.draw()
        ball_name.draw()
        wall_name.draw()
        but.listen(events)
        but.draw()
        back.listen(events)
        back.draw()
        player1_name.listen(events)
        player1_name.draw()
        player2_name.listen(events)
        player2_name.draw()
        ball_r.listen(events)
        ball_r.draw()
        ball_g.listen(events)
        ball_g.draw()
        ball_b.listen(events)
        ball_b.draw()
        ball_r_disp.colour = (ball_r.getValue(), 0, 0)
        ball_r_disp.draw()
        ball_g_disp.colour = (0, ball_g.getValue(), 0)
        ball_g_disp.draw()
        ball_b_disp.colour = (0, 0, ball_b.getValue())
        ball_b_disp.draw()
        ball_color = (ball_r.getValue(), ball_g.getValue(), ball_b.getValue())
        plot_ball(window, ball_color, (200, 270), 100)

        wall_r.listen(events)
        wall_r.draw()
        wall_g.listen(events)
        wall_g.draw()
        wall_b.listen(events)
        wall_b.draw()
        wall_r_disp.colour = (wall_r.getValue(), 0, 0)
        wall_r_disp.draw()
        wall_g_disp.colour = (0, wall_g.getValue(), 0)
        wall_g_disp.draw()
        wall_b_disp.colour = (0, 0, wall_b.getValue())
        wall_b_disp.draw()
        wall_color = (wall_r.getValue(), wall_g.getValue(), wall_b.getValue())
        plot_wall(window, wall_color, [1320, 170, 20, 350])

        pygame.display.update()
        clock.tick(60)


def welcome():
    exit_game = False
    image = pygame.image.load("images/bg2.jpg")
    image = pygame.transform.scale(image, (screen_width, screen_height))
    window.blit(image, (40, 80))
    text = TextBox(
        window, 375, 50, 740, 150,
        colour=yellow,
        radius=5,
        borderColour=red,
        borderThickness=10,
        textColour=(0, 10, 20),
        fontSize=100
    )
    text.setText("THE SOCCER GAME")
    button = Button(
        window, 600, 300, 300, 100,
        inactiveColour=(100, 150, 255),
        hoverColour=(255, 244, 122),
        onClick=lambda: settings(),
        shadowDistance=10,
        shadowColour=(50, 50, 50),
        radius=10,
        text='START',
        fontSize=50,
    )
    button1 = Button(
        window, 600, 450, 300, 100,
        inactiveColour=(100, 150, 255),
        hoverColour=(255, 244, 122),
        onClick=lambda: sys.exit(0),
        shadowDistance=10,
        shadowColour=(50, 50, 50),
        radius=10,
        text='EXIT',
        fontSize=50,
    )
    while not exit_game:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)

        button.listen(events)
        button.draw()
        button1.listen(events)
        button1.draw()
        text.draw()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    welcome()


