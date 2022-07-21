import os
import sys

import pygame
from pygame.locals import *

from dialog.GenerateNpcDialog import draw_text, wrap_text
from dialog.NpcDialogThread import NpcDialogThread
from hero.Barbarian import Barbarian
from hero.Dwarf import Dwarf
from hero.Elf import Elf
from hero.Faerie import Faerie
from hero.Wizard import Wizard
from npc.DarkWizard import DarkWizard
from npc.Druid import Druid
from npc.IceMonster import IceMonster
from npc.Mermaid import Mermaid
from npc.Orc import Orc

# Main game loop

WIDTH_GAME = 1500
HEIGHT_GAME = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (24, 165, 88)
YELLOW = (255, 234, 0)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = [".", ",", "/", "!", ":", ";", "'", "-"]


path = os.getcwd()
image_elf = pygame.image.load(os.path.join(path, "resources", "Elf.png"))
image_faerie = pygame.image.load(os.path.join(path, "resources", "Faerie.png"))
image_dwarf = pygame.image.load(os.path.join(path, "resources", "Dwarf.png"))
image_wizard = pygame.image.load(os.path.join(path, "resources", "Wizard.png"))
image_barbarian = pygame.image.load(os.path.join(path, "resources", "Barbarian.png"))
image_druid = pygame.image.load(os.path.join(path, "resources", "Druid.png"))
image_dark_wizard = pygame.image.load(os.path.join(path, "resources", "Wizard_dark.png"))
image_mermaid = pygame.image.load(os.path.join(path, "resources", "Mermaid.PNG"))
image_ice_monster = pygame.image.load(os.path.join(path, "resources", "IceMonster.PNG"))
image_orc = pygame.image.load(os.path.join(path, "resources", "Orc.png"))


def check_text_length(text, screen, text_height_position, color):
    text_list = []
    if len(text) <= 220:
        text_list.append(text)
    else:
        text_list = wrap_text(text)

    for i in range(len(text_list)):
        draw_text(text_list[i], 50, text_height_position, 12, color, screen)
        text_height_position += 20


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
    dark_wizard = DarkWizard("Sarus", "evil", 200, 400, image_dark_wizard, image_dark_wizard, image_dark_wizard,
                             "Wizard", None, None, 400, 500)
    npcs.append(dark_wizard)
    ice_monster = IceMonster("Icelius", "evil", 200, 600, image_ice_monster, image_ice_monster, image_ice_monster,
                             "Ice Monster", None, None, 200, 700)
    npcs.append(ice_monster)
    mermaid = Mermaid("Arielle", "good", 300, 100, image_mermaid, image_mermaid, image_mermaid,
                      "Mermaid", None, None, 400, 500)
    npcs.append(mermaid)
    orc = Orc("Stinker", "evil", 700, 200, image_orc, image_orc, image_orc,
              "Orc", None, None, 800, 50)
    npcs.append(orc)

    all_sprites_group = pygame.sprite.Group()
    all_sprites_group.add(hero)
    all_sprites_group.add(druid)
    all_sprites_group.add(dark_wizard)
    all_sprites_group.add(ice_monster)
    all_sprites_group.add(mermaid)
    all_sprites_group.add(orc)

    dx = 0
    dy = 0
    direct = "U"
    moving = False
    pressed = False
    prev = False
    npc_dialog_thread = NpcDialogThread(hero, screen, None)
    s = pygame.Surface((WIDTH_GAME, 150), pygame.SRCALPHA)
    text_list = []

    while True:
        screen.fill(GREEN)
        all_sprites_group.update()
        hero.update()
        all_sprites_group.draw(screen)
        if hero.in_dialog:
            s.fill(BLACK)
            s.set_alpha(192)
            screen.blit(s, (0, 0))
            border = pygame.Rect(0, 0, WIDTH_GAME, 150)
            pygame.draw.rect(screen, WHITE, border, 2, 3)

            check_text_length(hero.my_text, screen, 100, WHITE)

            for npc in npcs:
                if npc.is_talking:
                    check_text_length(npc.text, screen, 25, YELLOW)
                    break

        pygame.display.update()

        join_thread = False

        keys_pressed = pygame.key.get_pressed()

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
                if hero.in_dialog:
                    moving = False
                    if hero.hero_turn:
                        print("Event: ", pygame.key.name(event.key))
                        if pygame.key.name(event.key) in letters:
                            if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                                hero.my_text += pygame.key.name(event.key).upper()
                            else:
                                hero.my_text += pygame.key.name(event.key)
                        elif pygame.key.name(event.key) in digits:
                            if pygame.key.name(event.key) == '1' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '!'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                        elif pygame.key.name(event.key) == 'space':
                            print("SPACE")
                            hero.my_text += ' '
                        elif pygame.key.name(event.key) in signs:
                            if pygame.key.name(event.key) == '/' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '?'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                        elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            hero.my_text = hero.my_text[:-1]
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            hero.hero_turn = False

                        print(hero.my_text)

                    # else:
                    #     # NPC generates text
                    #     pass

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
                        hero.in_dialog = True
                        # hero.hero_turn = True
                        hero.my_text = ">> "
                        npc_dialog_thread = NpcDialogThread(hero, screen, npc)
                        npc_dialog_thread.start()
                        print("START TALKING!!")
                        break
                    else:
                        npc.is_talking = False
                        hero.in_dialog = False
                        hero.hero_turn = False
                        hero.my_text = ">> "
                        npc.text = ">> "
                        join_thread = True
                        print("STOP TALKING!!")
                        break

        prev = left

        if join_thread:
            npc_dialog_thread.join()

        # all_sprites_group.update()
        # hero.update()
        # all_sprites_group.draw(screen)
        # if dialog:
        #     pygame.draw.rect(screen, BLACK, (0, 0, WIDTH_GAME, 150))
        #     draw_text(hero.my_text, 50, 25, 12, WHITE, screen)
        # pygame.display.update()
        clock.tick(60)
