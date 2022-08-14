import os
import sys
from copy import copy
from datetime import datetime, time

import pygame
from pygame.locals import *
from sklearn import clone

from dialog.ButtonClass import ButtonClass
from dialog.DialogLine import DialogLine
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
from quest.Quest import Quest

WIDTH_GAME = 1500
HEIGHT_GAME = 800
DIALOG_START = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (24, 165, 88)
LIGHT_GREEN = (127, 255, 0)
YELLOW = (255, 234, 0)
HUD_YELLOW = (245, 245, 220)
ALMOND = (234, 221, 202)
CORAL = (248, 131, 121)

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
scroll_small = pygame.image.load(os.path.join(path, "resources", "scroll_small.png"))
scroll = pygame.image.load(os.path.join(path, "resources", "scroll.png"))


# Function to limit the length of text input in the dialog and its formatting (moves text to the next line after 220
# characters and cutting it all together after 440) - hero text (this and the one for npc can be converted into one)
def check_text_length(text, screen, text_height_position, color):
    text_list = []
    if len(text) <= 220:
        text_list.append(text)
    else:
        text_list = wrap_text(text, 220, True)

    for i in range(len(text_list)):
        draw_text(text_list[i], 50, text_height_position, 12, color, screen)
        text_height_position += 20


# Function that checks if the text is in available position to be displayed
def check_transparency(text):
    if text.position == DIALOG_START + 25 or text.position == DIALOG_START + 100:
        text.transparent = True
    else:
        text.transparent = False


# Move text to make place for another
def update_positions_and_transparency(text_history):
    for text in text_history:
        text.position -= 150
        if text.position == DIALOG_START + 25 or text.position == DIALOG_START + 100:
            text.transparent = True
        else:
            text.transparent = False


# Function to move dialog up to see previous messages
def move_dialog_up(text_history):
    i = 0

    for text in text_history:
        check_transparency(text)
        if i == 0 and text.position == DIALOG_START + 25:
            break
        text.position += 75
        i += 1


# Function to move dialog down to see next messages
def move_dialog_down(text_history):
    reversed_text = text_history[::-1]
    for i in range(len(reversed_text)):
        check_transparency(reversed_text[i])
        if i == 0 and reversed_text[i].position == DIALOG_START + 100 and reversed_text[i+1].position == DIALOG_START + 25:
            print("HERE")
            break
        reversed_text[i].position -= 75


def time_to_restore(screen, restore_life_time_passed, x):
    time_diff = datetime.now() - restore_life_time_passed
    time_sec = time_diff.total_seconds()
    # print("time_start", restore_life_time_passed)

    time_to_display = 120 - time_sec
    minutes = int(time_to_display / 60)
    seconds = int(time_to_display % 60)
    draw_text(str(minutes) + ':', x, 50, 12, BLACK, screen)
    if seconds < 10:
        draw_text('0' + str(seconds), x + 20, 50, 12, BLACK, screen)
    else:
        draw_text(str(seconds), x + 20, 50, 12, BLACK, screen)
    if time_to_display <= 0:
        return 0
    else:
        return 1


# Function to update hud and displayed there components
def update_hud(screen, hero, scroll_button, restore_life, restore_mana, restore_mana_time_passed, restore_life_time_passed):
    hud = pygame.Rect(0, 0, WIDTH_GAME, 100)
    pygame.draw.rect(screen, HUD_YELLOW, hud, 0, 1)

    border = pygame.Rect(0, 0, WIDTH_GAME, 100)
    pygame.draw.rect(screen, ALMOND, border, 5, 2)

    draw_text("Life ", 100, 25, 12, BLACK, screen)

    life = pygame.Rect(150, 50, hero.life, 25)
    pygame.draw.rect(screen, LIGHT_GREEN, life, 0, 2)
    border = pygame.Rect(150, 50, 100, 25)
    pygame.draw.rect(screen, BLACK, border, 2, 2)

    draw_text("Mana ", 400, 25, 12, BLACK, screen)

    mana = pygame.Rect(450, 50, hero.mana, 25)
    pygame.draw.rect(screen, BLUE, mana, 0, 2)
    border = pygame.Rect(450, 50, 100, 25)
    pygame.draw.rect(screen, BLACK, border, 2, 2)

    draw_text("Points ", 1100, 25, 12, BLACK, screen)
    draw_text(str(hero.points), 1150, 50, 12, BLACK, screen)
    scroll_surface = pygame.Surface((30, 30))

    draw_text("Quest ", 1300, 25, 12, BLACK, screen)
    screen.blit(scroll_small, (1350, 50))
    scroll_button.image = scroll_small
    scroll_button.rect.x = 1350
    scroll_button.rect.y = 50
    scroll_surface.blit(scroll_button.image, (scroll_button.rect.x, scroll_button.rect.y))

    if restore_life:
        time_left = time_to_restore(screen, restore_life_time_passed, 300)
        if time_left == 0:
            hero.life = 100

    if restore_mana:
        time_left = time_to_restore(screen, restore_mana_time_passed, 600)
        if time_left == 0:
            hero.mana = 100


def set_fight_parameters(hero, use_spell):
    if hero.in_fight:
        use_spell = not use_spell
        if hero.casting_spell:
            hero.casting_spell = not hero.casting_spell
            hero.chosen_spell = None
        else:
            hero.chosen_spell = None
            hero.casting_spell = False
        if hero.mana == 0:
            use_spell = False
            hero.chosen_spell = None
            hero.casting_spell = False

    return use_spell


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
        hero = Elf(chosen_name, chosen_side, 100, 100, images, None, chosen_type)
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 100, 100, images, None, chosen_type)
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 100, 100, images, None, chosen_type)
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 100, 100, images, None, chosen_type)
    else:
        hero = Barbarian(chosen_name, chosen_side, 100, 100, images, None, chosen_type)

    # Test quest
    quest = Quest("Go to the place where you found the stone, pour raven blood over it, burn the sage in the sacred fire, release mermaid’s voice and say the incantation to summon the god.", 50, [], [])
    hero.active_quest = quest

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
    npc_dialog_thread = NpcDialogThread(hero, screen, npcs)
    npc_dialog_thread.start()
    show_quest = False
    use_spell = False
    restore_life = False
    restore_mana = False
    restore_life_time_passed = None
    restore_mana_time_passed = None
    option = 1

    s = pygame.Surface((WIDTH_GAME, 150), pygame.SRCALPHA)
    arrow_up = ButtonClass(25, 25)
    arrow_down = ButtonClass(25, 25)
    scroll_button = ButtonClass(30, 40)

    # Main game loop
    while True:
        screen.fill(GREEN)
        # Updating and drawing sprites
        all_sprites_group.update()
        hero.update()
        all_sprites_group.draw(screen)

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
                elif event.key == pygame.K_0:
                    hero.in_fight = not hero.in_fight
                    hero.casting_spell = False
                    use_spell = False
                    hero.chosen_spell = None
                elif event.key == pygame.K_1:
                    option = 1
                    use_spell = set_fight_parameters(hero, use_spell)
                elif event.key == pygame.K_2:
                    option = 2
                    use_spell = set_fight_parameters(hero, use_spell)
                elif event.key == pygame.K_3:
                    option = 3
                    use_spell = set_fight_parameters(hero, use_spell)

                # Event support for dialog
                if hero.in_dialog:
                    moving = False
                    # Checking if hero is now talking - possibility of keyboard interaction
                    # letters, digits, signs and space accepted (lists at the top)
                    if hero.hero_turn:
                        if pygame.key.name(event.key) in letters:
                            if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                                hero.my_text += pygame.key.name(event.key).upper()
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history)-1].text = hero.my_text

                        elif pygame.key.name(event.key) in digits:
                            if pygame.key.name(event.key) == '1' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '!'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history)-1].text = hero.my_text
                        elif pygame.key.name(event.key) == 'space':
                            # print("SPACE")
                            hero.my_text += ' '
                            hero.text_history[len(hero.text_history)-1].text = hero.my_text
                        elif pygame.key.name(event.key) in signs:
                            if pygame.key.name(event.key) == '/' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '?'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history)-1].text = hero.my_text
                        # Deleting the last written letter
                        elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            hero.my_text = hero.my_text[:-1]
                            hero.text_history[len(hero.text_history)-1].text = hero.my_text
                        # Detecting enter, finishing the input, turn is changed to npc
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            hero.hero_turn = False
                            update_positions_and_transparency(hero.text_history)

        # Moving hero
        if moving:
            hero.move(direct, dx, dy)

        if use_spell:
            hero.fight(screen, option)

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
                        print("START TALKING!!")
                        break
                    # if yes - stop the dialog
                    else:
                        npc.is_talking = False
                        hero.in_dialog = False
                        hero.hero_turn = False
                        hero.my_text = ">> "
                        hero.text_history = []
                        npc.text_history = []
                        npc.text = ">> "
                        print("STOP TALKING!!")
                        break

            if arrow_up.rect.collidepoint(mouse_point):
                move_dialog_up(hero.text_history)
            elif arrow_down.rect.collidepoint(mouse_point):
                move_dialog_down(hero.text_history)
            elif scroll_button.rect.collidepoint(mouse_point):
                show_quest = not show_quest

        # Set previous state of left mouse button
        prev = left

        if hero.in_dialog:
            s.fill(BLACK)
            s.set_alpha(192)  # 0 - 255
            screen.blit(s, (0, DIALOG_START))

            arrows = pygame.sprite.Group()
            arrow_up.rect.x = WIDTH_GAME - 50
            arrow_up.rect.y = DIALOG_START + 25
            arrow_down.rect.x = WIDTH_GAME - 50
            arrow_down.rect.y = DIALOG_START + 100

            arrows.add(arrow_up)
            arrows.add(arrow_down)

            for text in hero.text_history:
                check_transparency(text)
                if text.transparent:
                    check_text_length(text.text, screen, text.position, text.color)

            arrows.update()
            arrows.draw(screen)
            pygame.draw.polygon(screen, BLACK, [(WIDTH_GAME - 45, 140), (WIDTH_GAME - 38, 130), (WIDTH_GAME - 30, 140)], 2)
            pygame.draw.polygon(screen, BLACK, [(WIDTH_GAME - 45, 210), (WIDTH_GAME - 38, 220), (WIDTH_GAME - 30, 210)],
                                2)

            border = pygame.Rect(0, DIALOG_START, WIDTH_GAME, 150)
            pygame.draw.rect(screen, WHITE, border, 2, 3)

        update_hud(screen, hero, scroll_button, restore_life, restore_mana, restore_mana_time_passed, restore_life_time_passed)
        if show_quest:
            screen.blit(scroll, (1100, 100))
            text_list = wrap_text(hero.active_quest.description, 25, False)
            w = 200
            h = 1200
            for text in text_list:
                draw_text(text, h, w, 14, BLACK, screen)
                w += 20
                if h == 1170:
                    h += 5
                else:
                    h -= 5

        if hero.mana == 0 and not restore_mana:
            restore_mana = True
            # print("TEST")
            restore_mana_time_passed = datetime.now()
        elif hero.mana > 0:
            restore_mana = False

        if hero.life == 0 and not restore_life:
            restore_life = True
            restore_life_time_passed = datetime.now()
        elif hero.mana > 0:
            restore_life = False

        pygame.display.update()
        clock.tick(60)

