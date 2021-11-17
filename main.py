import pygame
import math

pygame.init()
pygame.display.set_caption('Rolling')
size = (700, 500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
LIGHTGRAY = (200, 200, 200)
DARKGRAY = (75, 75, 75)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (0, 255, 255)
stat_ball_radius = 0
font = pygame.font.SysFont("comicsansms", 24)
points = []

stat_ball_radius = 120

class Button(object):
    def __init__(self, x1, y1, x2, y2, text):
        self.text = text
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)
        self.color = GRAY
        self.padding_x = self.p1[0]+5
        self.padding_y = self.p1[1]
        self.shadow = (self.p1[0], self.p2[1]+self.p1[1]-2,
                       self.p2[0]+self.p1[0], self.p2[1]+self.p1[1]-2)
        self.lhigh = (self.p1[0], self.p1[1], self.p1[0],
                      self.p2[1]+self.p1[1]-2)
        self.rhigh = (self.p2[0]+self.p1[0], self.p1[1],
                      self.p2[0]+self.p1[0], self.p2[1]+self.p1[1]-2)
        self.light = (self.p1[0], self.p1[1],
                      self.p2[0]+self.p1[0], self.p1[1])
        self.run = 1

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         (self.p1[0], self.p1[1], self.p2[0], self.p2[1]))
        pygame.draw.line(
            screen, DARKGRAY, (self.shadow[0], self.shadow[1]), (self.shadow[2], self.shadow[3]), 3)
        pygame.draw.line(
            screen, LIGHTGRAY, (self.lhigh[0], self.lhigh[1]), (self.lhigh[2], self.lhigh[3]), 3)
        pygame.draw.line(
            screen, DARKGRAY, (self.rhigh[0], self.rhigh[1]), (self.rhigh[2], self.rhigh[3]), 3)
        pygame.draw.line(
            screen, WHITE, (self.light[0], self.light[1]), (self.light[2], self.light[3]), 3)
        img = font.render(self.text, True, RED)
        screen.blit(img, (self.padding_x, self.padding_y))

    def click(self):
        if(self.text == "Start"):
            self.text = "Stop"
            self.run = 1
            stat.radius=int(menu[1].value)
            dyn.radius=int(menu[2].value)
            global stat_ball_radius
            stat_ball_radius=int(menu[1].value)
        elif(self.text=="Stop"):
            self.text = "Start"
            self.run = 0
        else:
            global points
            points=[]

class InputBox(object):
    def __init__(self, x1, y1, x2, y2, text,value):
        self.text=text
        self.value = value
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)
        self.color = WHITE
        self.padding_x = self.p1[0]+20
        self.padding_y = self.p1[1]
        self.padding_x2=self.p1[0]-100
        self.shadow = (self.p1[0], self.p2[1]+self.p1[1]-2,
                       self.p2[0]+self.p1[0], self.p2[1]+self.p1[1]-2)
        self.lhigh = (self.p1[0], self.p1[1], self.p1[0],
                      self.p2[1]+self.p1[1]-2)
        self.rhigh = (self.p2[0]+self.p1[0], self.p1[1],
                      self.p2[0]+self.p1[0], self.p2[1]+self.p1[1]-2)
        self.light = (self.p1[0], self.p1[1],
                      self.p2[0]+self.p1[0], self.p1[1])
        self.run = 1

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         (self.p1[0], self.p1[1], self.p2[0], self.p2[1]))
        pygame.draw.line(
            screen, WHITE, (self.shadow[0], self.shadow[1]), (self.shadow[2], self.shadow[3]), 3)
        pygame.draw.line(
            screen, DARKGRAY, (self.lhigh[0], self.lhigh[1]), (self.lhigh[2], self.lhigh[3]), 3)
        pygame.draw.line(
            screen, LIGHTGRAY, (self.rhigh[0], self.rhigh[1]), (self.rhigh[2], self.rhigh[3]), 3)
        pygame.draw.line(
            screen, DARKGRAY, (self.light[0], self.light[1]), (self.light[2], self.light[3]), 3)
        img = font.render(self.value, True, RED)
        screen.blit(img, (self.padding_x, self.padding_y))
        img = font.render(self.text, True, WHITE)
        screen.blit(img, (self.padding_x2, self.padding_y))

    def click(self):
        return self


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.roll = 0
        self.line = 2

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, self.line)

    def rolling(self, second):
        self.x = round((self.radius+second.radius-2)
                       * math.cos(self.roll))+second.x
        self.y = round((self.radius+second.radius-2)
                       * math.sin(self.roll))+second.y
        self.roll = self.roll+math.pi/180

    def radius_draw(self, second):
        pygame.draw.line(screen, GREEN, (self.x, self.y),
                         (second.x, second.y), 3)

    def trace(self, second):
        self.x = round((self.radius+second.radius-4)
                       * math.cos(self.roll))+second.x
        self.y = round((self.radius+second.radius-4)
                       * math.sin(self.roll))+second.y
        self.roll = self.roll+(stat_ball_radius/second.radius+1)*math.pi/180
        return (self.x, self.y)

stat = ball(round(size[0]/2), round(size[1]/2), stat_ball_radius, WHITE)
dyn = ball(round(size[0]/2)-stat.radius*2, round(size[1]/2), 40, WHITE)
pointer = ball(round(size[0]/2)-stat.radius*2, round(size[1]/2), 3, RED)
menu = [Button(20, 20, 70, 35, "Stop"), InputBox(400, 20, 100, 35, "Static", str(stat_ball_radius)),InputBox(200, 20, 100, 35, "Dynamic",str(40)), Button(20, 70, 150, 35, "Reset Trace")]
active_value = menu[1]
menu[1].padding_x2=menu[1].padding_x2+25

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in menu:
                if(pos[0] > i.p1[0] and pos[0] < (i.p2[0]+i.p1[0]) and pos[1] > i.p1[1] and pos[1] < (i.p2[1]+i.p1[1])):
                    if(isinstance(i,InputBox)):
                        active_value=i.click()
                    else:
                        i.click()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                active_value.value = str(int(active_value.value)*10)
            elif event.key == pygame.K_1:
                active_value.value = str(int(active_value.value)*10+1)
            elif event.key == pygame.K_2:
                active_value.value = str(int(active_value.value)*10+2)
            elif event.key == pygame.K_3:
                active_value.value = str(int(active_value.value)*10+3)
            elif event.key == pygame.K_4:
                active_value.value = str(int(active_value.value)*10+4)
            elif event.key == pygame.K_5:
                active_value.value = str(int(active_value.value)*10+5)
            elif event.key == pygame.K_6:
                active_value.value = str(int(active_value.value)*10+6)
            elif event.key == pygame.K_7:
                active_value.value = str(int(active_value.value)*10+7)
            elif event.key == pygame.K_8:
                active_value.value = str(int(active_value.value)*10+8)
            elif event.key == pygame.K_9:
                active_value.value = str(int(active_value.value)*10+9)
            elif event.key == pygame.K_DELETE:
                active_value.value = str(0)

    screen.fill(BLACK)

    if(menu[0].run):
        dyn.rolling(stat)
        points.append(pointer.trace(dyn))
    stat.draw()
    dyn.draw()
    pointer.draw()
    pointer.radius_draw(dyn)
    for i in menu:
        i.draw()
    for i in points:
        pygame.draw.line(screen, YELLOW, i, i)
    pygame.display.flip()
    clock.tick(70)

pygame.quit()
