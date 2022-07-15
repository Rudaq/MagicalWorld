import os
import sys

import pygame
from pygame.locals import *

from hero.Barbarian import Barbarian
from hero.Dwarf import Dwarf
from hero.Elf import Elf
from hero.Faerie import Faerie
from hero.Wizard import Wizard
from npc.Druid import Druid

WIDTH_GAME = 1500
HEIGHT_GAME = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (24, 165, 88)


path = os.getcwd()
image_elf = pygame.image.load(os.path.join(path, "resources", "Elf.png"))
image_faerie = pygame.image.load(os.path.join(path, "resources", "Faerie.png"))
image_dwarf = pygame.image.load(os.path.join(path, "resources", "Dwarf.png"))
image_wizard = pygame.image.load(os.path.join(path, "resources", "Wizard.png"))
image_barbarian = pygame.image.load(os.path.join(path, "resources", "Barbarian.png"))
image_druid = pygame.image.load(os.path.join(path, "resources", "Druid.png"))


def game(chosen_name, chosen_type, chosen_side, image):
    pygame.init()
    pygame.display.set_caption("Battle of the Realm")
    screen = pygame.display.set_mode((WIDTH_GAME, HEIGHT_GAME))
    clock = pygame.time.Clock()
    npcs = []

    if chosen_type == "Elf":
        hero = Elf(chosen_name, chosen_side, 300, 500, image, image_elf, image_elf, None, chosen_type)
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 400, 300, image, image_faerie, image_faerie, None, chosen_type)
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 500, 300, image, image_wizard, image_wizard, None, chosen_type)
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 200, 300, image, image_dwarf, image_dwarf, None, chosen_type)
    else:
        hero = Barbarian(chosen_name, chosen_side, 200, 400, image, image_barbarian, image_barbarian, None, chosen_type)

    druid = Druid("Leaf", "good", 300, 600, image_druid, image_druid, image_druid, "Druid", None, None, 700, 300)
    npcs.append(druid)

    all_sprites_group = pygame.sprite.Group()
    all_sprites_group.add(hero)
    all_sprites_group.add(druid)

    dx = 0
    dy = 0
    direct = "U"
    moving = False
    dialog = False
    pressed = False
    prev = False

    while True:
        screen.fill(GREEN)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_d or event.key == pygame.K_DOWN or event.key == pygame.K_s \
                        or event.key == pygame.K_UP or event.key == pygame.K_w:
                    moving = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direct = "U"
                    dx = 0
                    dy = -5
                    moving = True
                    # hero.move("U", 0, -5)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direct = "D"
                    dx = 0
                    dy = 5
                    moving = True
                    # hero.move("D", 0, 5)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direct = "R"
                    dx = 5
                    dy = 0
                    moving = True
                    # hero.move("R", 5, 0)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direct = "L"
                    dx = -5
                    dy = 0
                    moving = True
                    # hero.move("L", -5, 0)

        # Moving hero and random movement of npcs
        if moving:
            hero.move(direct, dx, dy)

        for npc in npcs:
            if not npc.is_talking and not npc.is_fighting:
                npc.move()

        # Clicking on npc to start dialog
        left, middle, right = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        mouse_point = (x, y)

        if left and prev != left:
            pressed = True
        else:
            pressed = False

        if pressed:
            for npc in npcs:
                if npc.rect.collidepoint(mouse_point):
                    # add condition that the hero needs to be in a certain proximity for it to work ?
                    if not npc.is_talking:
                        npc.is_talking = True
                        dialog = True
                        print("START TALKING!!")
                        break
                    else:
                        npc.is_talking = False
                        dialog = False
                        print("STOP TALKING!!")
                        break

        prev = left
        all_sprites_group.update()
        hero.update()
        all_sprites_group.draw(screen)
        if dialog:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH_GAME, 150))
        pygame.display.update()
        clock.tick(60)
