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

# Possible characters to be used as input
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = [".", ",", "/", "!", ":", ";", "'", "-"]

# Loading images of the npc
path = os.getcwd()
image_druid = pygame.image.load(os.path.join(path, "resources", "Druid.png"))
image_dark_wizard = pygame.image.load(os.path.join(path, "resources", "Wizard_dark.png"))
image_mermaid = pygame.image.load(os.path.join(path, "resources", "Mermaid.PNG"))
image_ice_monster = pygame.image.load(os.path.join(path, "resources", "IceMonster.PNG"))
image_orc = pygame.image.load(os.path.join(path, "resources", "Orc.png"))


# Function to limit the length of text input in the dialog and its formatting (moves text to the next line after 220
# characters and cutting it all together after 440) - hero text (this and the one for npc can be converted into one)
def check_text_length(text, screen, text_height_position, color):
    text_list = []
    if len(text) <= 220:
        text_list.append(text)
    else:
        text_list = wrap_text(text)

    for i in range(len(text_list)):
        draw_text(text_list[i], 50, text_height_position, 12, color, screen)
        text_height_position += 20


# Main game function
def game(chosen_name, chosen_type, chosen_side, image):
    # pygame initialization
    pygame.init()
    pygame.display.set_caption("Battle of the Realm")
    screen = pygame.display.set_mode((WIDTH_GAME, HEIGHT_GAME))
    clock = pygame.time.Clock()
    npcs = []

    # Creating hero of a class corresponding to a chosen race
    images = [image]
    if chosen_type == "Elf":
        hero = Elf(chosen_name, chosen_side, 300, 500, images, None, chosen_type)
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 400, 300, images, None, chosen_type)
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 500, 300, images, None, chosen_type)
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 200, 300, images, None, chosen_type)
    else:
        hero = Barbarian(chosen_name, chosen_side, 200, 400, images, None, chosen_type)

    # Creating npcs
    images_druid = [image_druid]
    druid = Druid("Leaf", "good", 300, 600, images_druid, "Druid", None, None, 700, 300)
    npcs.append(druid)
    images_dark_wizard = [image_dark_wizard]
    dark_wizard = DarkWizard("Sarus", "evil", 200, 400, images_dark_wizard,
                             "Wizard", None, None, 400, 500)
    npcs.append(dark_wizard)
    images_ice_monster = [image_ice_monster]
    ice_monster = IceMonster("Icelius", "evil", 200, 600, images_ice_monster,
                             "Ice Monster", None, None, 200, 700)
    npcs.append(ice_monster)
    images_mermaid = [image_mermaid]
    mermaid = Mermaid("Arielle", "good", 300, 100, images_mermaid,
                      "Mermaid", None, None, 400, 500)
    npcs.append(mermaid)
    images_orc = [image_orc]
    orc = Orc("Stinker", "evil", 700, 200, images_orc,
              "Orc", None, None, 800, 50)
    npcs.append(orc)

    # Adding created characters to group with all sprites
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
    npc_dialog_thread = None
    # npc_dialog_thread = NpcDialogThread(hero, screen, None)
    # npc_dialog_thread.start()

    s = pygame.Surface((WIDTH_GAME, 150), pygame.SRCALPHA)
    text_list = []

    # Main game loop
    while True:
        screen.fill(GREEN)
        # Updating and drawing sprites
        all_sprites_group.update()
        hero.update()
        all_sprites_group.draw(screen)
        # Drawing dialog elements if there is a dialog
        if hero.in_dialog:
            s.fill(BLACK)
            s.set_alpha(192) # 0 - 255
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

        # Getting the list of all pressed keys
        keys_pressed = pygame.key.get_pressed()

        # Event support - quiting, movement
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
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direct = "D"
                    dx = 0
                    dy = 5
                    moving = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direct = "R"
                    dx = 5
                    dy = 0
                    moving = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direct = "L"
                    dx = -5
                    dy = 0
                    moving = True

                # Event support for dialog
                if hero.in_dialog:
                    moving = False
                    # Checking if hero is now talking - possibility of keyboard interaction
                    # letters, digits, signs and space accepted (lists at the top)
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
                        # Deleting the last written letter
                        elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            hero.my_text = hero.my_text[:-1]
                        # Detecting enter, finishing the input, turn is changed to npc
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            hero.hero_turn = False

                        print(hero.my_text)

        # Moving hero
        if moving:
            hero.move(direct, dx, dy)

        # Random movement of npcs if not in dialog
        for npc in npcs:
            if not npc.is_talking and not npc.is_fighting:
                npc.move()

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()
        mouse_point = (x, y)

        # Checking if the value of left in the last iteration was different
        # Ensuring that one click only performs the action once
        if left and prev != left:
            pressed = True
        else:
            pressed = False

        # Checking if mouse pressed
        if pressed:
            for npc in npcs:
                # Checking mouse point collision with npc
                if npc.rect.collidepoint(mouse_point):
                    # (add condition that the hero needs to be in a certain proximity for it to work ?)

                    # Checking if the collided npc is talking
                    # if not - start the dialog, set variables, create thread
                    if not npc.is_talking:
                        npc.is_talking = True
                        hero.in_dialog = True
                        hero.hero_turn = False
                        hero.my_text = ">> "
                        npc_dialog_thread.set_npc(npc)
                        npc_dialog_thread = NpcDialogThread(hero, screen, npc)
                        npc_dialog_thread.start()
                        print("START TALKING!!")
                        break
                    # if yes - stop the dialog
                    else:
                        npc.is_talking = False
                        hero.in_dialog = False
                        hero.hero_turn = False
                        hero.my_text = ">> "
                        npc.text = ">> "
                        join_thread = True
                        print("STOP TALKING!!")
                        break

        # Set previous state of left mouse button
        prev = left

        # Join the thread
        if join_thread:
            npc_dialog_thread.join()

        clock.tick(60)
