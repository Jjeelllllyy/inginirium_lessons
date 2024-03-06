import pygame

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

class Circle:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def say_hello_to(self):
           print('Hello,', name_to)

    def tell_about_yourself(self):
           print('Hello, my name is', self.color)
           print('I am', self.color, 'y o')


krug = Circle((255,0,0), 250, 300, 30)

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))

    pygame.draw.circle(win, (255, 0, 0), (x, y), 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1

    pygame.display.update()
    pygame.time.delay(10)
