import math
import random
import time

from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
shots = 0


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.time = 0



    def move(self):
        self.time += 1
        if self.time == 120:
            balls.pop(0)
        if self.x>=780:
            self.vx *= -0.6
            self.x = 780


        if self.y>=560:
            if abs(self.vy) < 3:
                self.vy = 0

            else:
                self.vy *= -0.6
                self.vx *= 0.6
                self.y =560
        else:
            self.vy += -1.5

        if abs(self.vx) <= 1:
            self.vx = 0
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        xt = obj.x
        yt = obj.y
        rt = obj.r
        if (xt - self.x)**2 + (yt - self.y)**2 <= (rt + self.r)**2:
            return True

        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global shots
        shots +=1
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, ko):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(screen, self.color, [20, 450], [20 +math.cos(self.an) *1.3* self.f2_power, 450 + math.sin(self.an) *1.3* self.f2_power], 10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen =screen
        self.points = 0
        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.r = random.uniform(10, 50)
        self.color = RED
        self.time = 0
        self.h=0
        global clock, shots


    # FIXME: don't work!!! How to call this functions when object is created?
        self.new_target()
    def disapear(self):
        self.x = 10000
        self.y = 10000
    def new_target(self):

        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.r = random.uniform(10, 50)
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += 1



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

        font1 = pygame.font.SysFont(None, 40)
        img1 = font1.render('%d' % self.points, True, BLUE)
        screen.blit(img1, (20, 20))
        


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
h =0
clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False
message_end_time = 0
time = 0
time0 = 0
k=0
while not finished:

    screen.fill(WHITE)

    gun.draw()
    target.draw()
    for b in balls:
        b.draw()


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and h==0:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and h==0:
            gun.fire2_end(event)

        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for b in balls:
        b.move()
        if b.hittest(target) and target.live and h==0:
            time0 = time
            h = 1
            k = 1

    if h==1:
        if k == 1:
            target.hit()
            k=0
        font1 = pygame.font.SysFont(None, 40)
        img1 = font1.render('Вы уничтожили цель за %d выстрелов' % shots, True, BLUE)
        screen.blit(img1, (200, 200))
        target.disapear()

        if time - time0>90:
            h=0
            time0=0
            time=0
            target.live = 0
            target.new_target()
            shots = 0
    time+=1
    pygame.display.update()


    gun.power_up()



pygame.quit()
