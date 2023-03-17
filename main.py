import random
import pygame
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

background = pygame.image.load("images/background.png")

menu = True
Menu_image = pygame.image.load("images/menu.png")
Menu_image.set_colorkey((255, 255, 255))
menu_y = 150
jumpcout = 10

class Clicker():
    possition = [50, 100]
    image = [pygame.image.load("images/c2.png"),
             pygame.image.load("images/c3.png"),
             pygame.image.load("images/c4.png"),
             pygame.image.load("images/c5.png"),
             pygame.image.load("images/c6.png"),
             pygame.image.load("images/c7.png"),
             pygame.image.load("images/c8.png"),
             pygame.image.load("images/c9.png")]
    animcout = 0
    angle = 0

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

scet = 0

pygame.mixer.music.load("music2.mp3")
pygame.mixer.music.play(-1)
hrust = pygame.mixer.Sound("3309-hrusta-rtom-suhogo-pechenja.mp3")

done = True
while done:
    if Clicker.animcout == 7:
        Clicker.animcout = 0

    f1 = pygame.font.Font(None, 36)
    schet_number = f1.render(str(scet), True, (255, 255, 255))
    schet_text = f1.render("Счет: ", True, (255, 122, 87))

    Clicker.angle += 1.5

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            menu = False
            if not(menu):
                crateballs(CST_group)
                hrust.play()
                scet += 1
                Clicker.animcout += 1
            pygame.display.flip()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = False

    window.fill((0, 0, 0))
    window.blit(pygame.transform.rotate(background, 90), (0, 0))

    if menu:
        window.blit(Menu_image, (5, menu_y))

    if not(menu):
        Clicker.image[Clicker.animcout].set_colorkey((255, 255, 255))
        window.blit(pygame.transform.rotate(Clicker.image[Clicker.animcout], Clicker.angle), Clicker.possition)

        CST_group.draw(window)

        #window.blit(pygame.transform.scale(CST.image_chastiza, (40, 40)), CST.rect)
        window.blit(schet_number, (100, 30))
        window.blit(schet_text, (30, 30))

        CST_group.update(600)
    pygame.display.update()
    clock.tick(60)

pygame.quit()