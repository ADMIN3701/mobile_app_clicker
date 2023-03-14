import random
import pygame
pygame.init()
pygame.font.init()

scet = "aaa"
f1 = pygame.font.Font(None, 36)
text1 = f1.render(scet, True, (255, 255, 255))

clock = pygame.time.Clock()

background = pygame.image.load("images/background.png")

menu = True
Menu_image = pygame.image.load("images/menu.png")
Menu_image.set_colorkey((255, 255, 255))
menu_y = 150
jumpcout = 10

class Clicker():
    possition = [50, 100]
    image = pygame.image.load("images/cookie.png")
    image.set_colorkey((255, 255, 255))
    angle = 0
    rect = pygame.Rect(possition[0], possition[1], image.get_height(), image.get_width())

class Chastiza(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group, Random, Random_way):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(surf, (40, 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, 150))
        self.speed = speed
        self.add(group)
        self.Random = Random
        self.Random_way = Random_way


    jumpcout = 15

    def update(self, *args):
        if self.Random == 0 and self.rect.x > 50:
            self.rect.x -= self.Random_way
        elif self.Random == 1 and self.rect.x < 450:
            self.rect.x += self.Random_way

        if self.jumpcout >= -10:
            if self.jumpcout < 0:
                self.rect.y += (self.jumpcout ** 2) / 6
            else:
                self.rect.y -= (self.jumpcout ** 2) / 6
            self.jumpcout -= 1

        if self.rect.y < args[0]:
            self.rect.y += (self.jumpcout ** 2) / 10
        else:
            self.kill()

def crateballs(group):
    x = 200
    speed = 5
    image = pygame.transform.scale(pygame.image.load("images/cookie.png"), (40, 40))
    Random = random.randint(0, 1)
    Random_way = random.randint(2, 5)
    return Chastiza(x, speed, image, group, Random, Random_way)

CST_group = pygame.sprite.Group()

window = pygame.display.set_mode((400, 600))
pygame.display.set_caption(("Mobile App"))

#crateballs(CST_group)

done = True
while done:

    Clicker.angle += 1.5

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            menu = False
            if not(menu):
                crateballs(CST_group)
                pygame.mixer.music.load("3309-hrusta-rtom-suhogo-pechenja.mp3")
                pygame.mixer.music.play()
                scet += "1"
            pygame.display.flip()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = False

    window.fill((0, 0, 0))
    window.blit(pygame.transform.rotate(background, 90), (0, 0))

    if menu:
        window.blit(Menu_image, (5, menu_y))

    if not(menu):
        window.blit(pygame.transform.rotate(Clicker.image, Clicker.angle), Clicker.possition)

        CST_group.draw(window)

        #window.blit(pygame.transform.scale(CST.image_chastiza, (40, 40)), CST.rect)
        window.blit(text1, (200, 0))
        CST_group.update(600)
    pygame.display.update()
    clock.tick(60)

pygame.quit()