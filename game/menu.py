import csv
import sys

import pygame
from pygame.locals import *

from game_support import create_character
from menu_support import draw_text_on_menu, divide
from game_init import game
from NLP.description_generation.main import generate_text_about_character
from settings import BLACK, WHITE, BLUE, RED, MENU_WIDTH, MENU_HEIGHT, LETTERS_NUMBERS, GUI_IMAGES
import os
from pathlib import Path

full_path = os.getcwd()
path = str(Path(full_path).parents[0])
pygame.init()
pygame.display.set_caption("Menu")
screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(path, 'resources/graphics/tilemap/menu_background.png')).convert_alpha()
tutorial_background = pygame.image.load(os.path.join(path, 'resources/GUI/tutorial.png')).convert_alpha()
character_view = pygame.image.load(os.path.join(path, 'resources/graphics/tilemap/character_background.png')).convert_alpha()

'''
Menu for choosing character race and other characteristics and starting the game
'''

options = False
menu_state = 'main'
running = True


# Method displaying the start menu with options "Start" and "Quit"
def menu():
    # Loop displaying the screen
    global options
    global menu_state
    global running
    options = False
    menu_state = 'main'
    running = True

    while True:
        screen.blit(background, (0, 0))

        # Creating buttons - rectangles, texts
        button_start = pygame.Rect(250, 320, 300, 50)
        button_how_to = pygame.Rect(250, 420, 300, 50)
        button_quit = pygame.Rect(250, 520, 300, 50)

        pygame.draw.rect(screen, BLACK, button_start, 0, 3)
        pygame.draw.rect(screen, BLACK, button_how_to, 0, 3)
        pygame.draw.rect(screen, BLACK, button_quit, 0, 3)

        screen.blit(GUI_IMAGES['start'].convert_alpha(), (101, 202))
        screen.blit(GUI_IMAGES['how_to'].convert_alpha(), (250, 395))
        screen.blit(GUI_IMAGES['quit'].convert_alpha(), (103, 392))
        screen.blit(GUI_IMAGES['title'].convert_alpha(), (115, 20))

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()

        # Checking if the mouse position is within the buttons
        if 250 < x < 550:
            if 320 < y < 370:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    # "Start" clicked, loop ended, another menu function is called
                    running = False
                    return running
                    # break
            # How to play button
            elif 420 < y < 470:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    options = True
                    menu_state = 'options'
                    break

            elif 520 < y < 570:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    # "Quit" clicked, program ended
                    pygame.quit()
                    sys.exit()
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Checking if esc or "x" pressed -> ending program
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


def how_to_play():
    global options
    global menu_state

    screen.blit(background, (0, 0))
    screen.blit(tutorial_background, (0, 0))

    while True:
        button_back = pygame.Rect(560, 520, 200, 50)
        pygame.draw.rect(screen, BLACK, button_back, 0, 3)
        screen.blit(GUI_IMAGES['back_to'], (560, 520))

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()

        # Checking if the mouse position is within the buttons
        if 560 < x < 760:
            if 520 < y < 570:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    # "Start" clicked, loop ended, another menu function is called
                    options = False
                    menu_state = 'main'
                    return menu_state

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


# Method displaying the menu for choosing the character race
def choose_character():
    # images to be displayed in the menu - (big, small)
    eligible_characters_images = [(pygame.image.load(os.path.join(path, "resources/graphics/characters/Barbarian.png")).convert_alpha(),
                                   pygame.image.load(
                                       os.path.join(path, "resources/graphics/characters/barbarian_small.png")).convert_alpha()),
                                  (pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf2.png")).convert_alpha(),
                                   pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf.png")).convert_alpha()),
                                  (pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard.png")).convert_alpha(),
                                   pygame.image.load(
                                       os.path.join(path, "resources/graphics/characters/wizard_small.png")).convert_alpha()),
                                  (pygame.image.load(os.path.join(path, "resources/graphics/characters/elf.png")).convert_alpha(),
                                   pygame.image.load(
                                       os.path.join(path, "resources/graphics/characters/elf_small.png")).convert_alpha()),
                                  (pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie.png")).convert_alpha(),
                                   pygame.image.load(
                                       os.path.join(path, "resources/graphics/characters/faerie_small.png")).convert_alpha())]

    names = ["Barbarian", "Dwarf", "Wizard", "Elf", "Faerie"]
    index = 0
    pressed = False
    prev = False
    good = True
    char_name = ""
    final_name = ""
    final_type = ""
    final_side = ""

    # Menu displaying loop
    while True:
        screen.blit(character_view, (0, 0))
        # screen.blit(eligible_characters_images[index], (400, 150))
        screen.blit(eligible_characters_images[index][0], (250, 0))

        # draw_text_on_menu("Character selection", 200, 50, 40, WHITE, screen)
        screen.blit(GUI_IMAGES['selection'].convert_alpha(), (105, 30))

        # Drawing arrows for character selection
        pygame.draw.polygon(screen, WHITE, [(350, 250), (350, 350), (300, 300)], 5)
        pygame.draw.polygon(screen, WHITE,
                            [(MENU_WIDTH - 150, 250), (MENU_WIDTH - 150, 350), (MENU_WIDTH - 100, 300)], 5)

        # Field for entering name
        #draw_text_on_menu("Name: ", 75, 175, 20, WHITE, screen)
        screen.blit(GUI_IMAGES['name'].convert_alpha(), (135, 163))
        name = pygame.Rect(100, 200, 150, 40)
        pygame.draw.rect(screen, WHITE, name, 0, 3)
        draw_text_on_menu(char_name, 100, 200, 20, BLACK, screen)

        # Field for displaying race
        #draw_text_on_menu("Type: ", 75, 275, 20, WHITE, screen)
        screen.blit(GUI_IMAGES['type'].convert_alpha(), (132, 263))
        c_type = pygame.Rect(100, 300, 150, 40)
        pygame.draw.rect(screen, WHITE, c_type, 0, 3)
        draw_text_on_menu(names[index], 100, 300, 20, BLACK, screen)

        # Field for choosing side - good or evil
        #draw_text_on_menu("Side: ", 75, 375, 20, WHITE, screen)
        screen.blit(GUI_IMAGES['side'].convert_alpha(), (137, 363))
        side = pygame.Rect(100, 400, 150, 40)
        pygame.draw.rect(screen, WHITE, side, 0, 3)
        pygame.draw.polygon(screen, WHITE, [(90, 410), (90, 430), (70, 420)], 2)
        pygame.draw.polygon(screen, WHITE, [(260, 410), (260, 430), (280, 420)], 2)

        if good:
            draw_text_on_menu("Good", 100, 400, 20, BLACK, screen)
        else:
            draw_text_on_menu("Evil", 100, 400, 20, BLACK, screen)

        # Button for the next menu screen - "Next"
        button_next = pygame.Rect(600, 500, 200, 50)
        pygame.draw.rect(screen, WHITE, button_next, 0, 3)
        screen.blit(GUI_IMAGES['next'], (624, 502))

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()

        # Checking if the value of left in the last iteration was different
        # Ensuring that one click only moves the characteristics by one
        if prev != left and left:
            pressed = True
        else:
            pressed = False

        # Choosing the good or evil side, by clicking the arrows
        if (70 <= x <= 90 and 410 <= y <= 430) or (260 <= x <= 280 and 410 <= y <= 430):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pressed:
                if good:
                    good = False
                else:
                    good = True
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Arrows for choosing the character race
        if 600 < x < 850:
            if 500 < y < 550 and x >= 600:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                # return character's details only if the name is inserted
                if left and len(char_name) > 0:
                    final_type = names[index]
                    final_name = char_name
                    if good:
                        final_side = "good"
                    else:
                        final_side = "evil"

                    return final_name, final_type, final_side, eligible_characters_images[index][0], \
                           eligible_characters_images[index][1]
                elif len(char_name) == 0:
                    pygame.draw.rect(screen, RED, ((MENU_WIDTH-400)/2, (MENU_HEIGHT-80)/2, 400, 80), 0, 3)
                    pygame.draw.rect(screen, BLACK, ((MENU_WIDTH - 400) / 2, (MENU_HEIGHT - 80) / 2, 400, 80), 1, 5)
                    draw_text_on_menu("Do not forget to insert the name", (MENU_WIDTH - 330) / 2,
                                      (MENU_HEIGHT - 50) / 2, 20, BLACK, screen)
                    draw_text_on_menu("of your character!", (MENU_WIDTH - 190) / 2,
                                      MENU_HEIGHT / 2, 20, BLACK, screen)
            elif 250 < y < 350 and 650 < x <= 700:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if pressed:
                    if index < (len(eligible_characters_images) - 1):
                        index += 1
                    else:
                        index = 0
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif 300 < x < 350:
            if 250 < y < 350:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if pressed:
                    if index > 0:
                        index -= 1
                    else:
                        index = len(eligible_characters_images) - 1

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Event support - catching user input for character name
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Setting name size limit and possible characters
                if len(char_name) < 15:
                    if pygame.key.name(event.key) in LETTERS_NUMBERS:
                        # Changing first letter to be big
                        if len(char_name) == 0:
                            char_name += pygame.key.name(event.key).upper()
                        else:
                            char_name += pygame.key.name(event.key)
                    # Deleting last letter
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        char_name = char_name[:-1]

        prev = left
        pygame.display.update()
        clock.tick(60)

from csv import writer
# Method for last menu screen, displaying the final generated text and character image
def character_info(name, ch_type, side, image):
    sequence = "Welcome to our world " + name + ". You are a " + side + " " + ch_type + " that"
    final_text = generate_text_about_character(sequence)
    array_text = divide(final_text)
    # if len(final_text.split(' a ', 1))>0:
    #     final_text_to_write = '"'+final_text.split(' a ', 1)[1]+'"'
    #     print(final_text_to_write)
    #     with open('C:\\Inżynierka\\MagicalWorld\\NLP\\description_generation\\descriptions_new.csv', 'a') as f:
    #         write = csv.writer(f)
    #         write.writerow([final_text_to_write])

    # Main loop for this menu
    while True:
        screen.fill(BLACK)

        # Creating button "Play" tp exit menu and start the game
        button_play = pygame.Rect(250, 500, 300, 50)
        pygame.draw.rect(screen, WHITE, button_play, 0, 3)
        draw_text_on_menu("Play", 350, 500, 40, BLACK, screen)

        # Displaying image and text
        screen.blit(image, (350, 0))
        text_y = 100
        for sentence in array_text:
            draw_text_on_menu(sentence, 50, text_y, 20, WHITE, screen)
            text_y += 20

        # draw_text(final_text, 50, 100, 10, WHITE)

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()

        # Checking in mouse cursor on the button and if clicked- performing action
        if 350 < x < 550:
            if 500 < y < 550:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    pygame.quit()
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Event supporting exiting from program
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(30)


# Calling menus in the right order
while running:
    menu()
    if menu_state == 'options':
        state = how_to_play()
        if state == 'main':
            continue

chosen_name, chosen_type, chosen_side, image, image_small = choose_character()

character_info(chosen_name, chosen_type, chosen_side, image)
main_character = create_character(chosen_name, chosen_type, chosen_side)

# Calling main game function with hero parameter
game(main_character)
