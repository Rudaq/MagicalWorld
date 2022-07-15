import sys

import pygame
from pygame import QUIT
from pygame.locals import *

from game import game
from main import generate_text_about_character

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
pygame.display.set_caption("Menu")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def draw_text(text, x, w, size, color):
    font = pygame.font.SysFont('Verdana', size)
    img = font.render(text, True, color)
    screen.blit(img, (x, w))


def menu():
    while True:
        screen.fill(BLUE)
        button_start = pygame.Rect(250, 300, 300, 50)
        button_quit = pygame.Rect(250, 400, 300, 50)

        pygame.draw.rect(screen, BLACK, button_start)
        pygame.draw.rect(screen, BLACK, button_quit)
        draw_text("Start", 350, 300, 40, WHITE)
        draw_text("Quit", 350, 400, 40, WHITE)
        draw_text("Battle of the Realm", 200, 100, 40, WHITE)

        left, middle, right = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()

        if 250 < x < 550:
            if 300 < y < 350:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    break
            elif 400 < y < 450:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    pygame.quit()
                    sys.exit()
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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


def choose_character():

    eligible_characters_images = [pygame.image.load(r'./resources/Barbarian.png'),
                                  pygame.image.load(r'./resources/Dwarf2.PNG'),
                                  pygame.image.load(r'./resources/Wizard2.PNG'),
                                  pygame.image.load(r'./resources/Elf2.PNG'),
                                  pygame.image.load(r'./resources/Faerie.png')]

    eligible_small_images = [pygame.image.load(r'./resources/Barbarian.png'),
                                  pygame.image.load(r'./resources/Dwarf_small.png'),
                                  pygame.image.load(r'./resources/Wizard_small.png'),
                                  pygame.image.load(r'./resources/Elf_small.png'),
                                  pygame.image.load(r'./resources/Faerie.png')]

    names = ["Barbarian", "Dwarf", "Wizard", "Elf", "Faerie"]
    index = 0
    pressed = False
    prev = False
    good = True
    char_name = ""
    final_name = ""
    final_type = ""
    final_side = ""

    while True:
        screen.fill(BLACK)
        # screen.blit(eligible_characters_images[index], (400, 150))
        screen.blit(eligible_characters_images[index], (250, 0))

        draw_text("Character selection", 200, 50, 40, WHITE)

        pygame.draw.polygon(screen, WHITE, [(350, 250), (350, 350), (300, 300)])
        pygame.draw.polygon(screen, WHITE, [(SCREEN_WIDTH - 150, 250), (SCREEN_WIDTH - 150, 350), (SCREEN_WIDTH - 100, 300)])

        draw_text("Name: ", 75, 175, 20, WHITE)
        name = pygame.Rect(100, 200, 150, 40)
        pygame.draw.rect(screen, WHITE, name)
        draw_text(char_name, 100, 200, 20, BLACK)

        draw_text("Type: ", 75, 275, 20, WHITE)
        c_type = pygame.Rect(100, 300, 150, 40)
        pygame.draw.rect(screen, WHITE, c_type)
        draw_text(names[index], 100, 300, 20, BLACK)

        draw_text("Side: ", 75, 375, 20, WHITE)
        side = pygame.Rect(100, 400, 150, 40)
        pygame.draw.rect(screen, WHITE, side)
        pygame.draw.polygon(screen, WHITE, [(90, 410), (90, 430), (70, 420)])
        pygame.draw.polygon(screen, WHITE, [(260, 410), (260, 430), (280, 420)])

        if good:
            draw_text("Good", 100, 400, 20, BLACK)
        else:
            draw_text("Evil", 100, 400, 20, BLACK)

        button_next = pygame.Rect(600, 500, 200, 50)
        pygame.draw.rect(screen, WHITE, button_next)
        draw_text("Next", 650, 500, 40, BLACK)

        left, middle, right = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()

        if prev != left and left:
            pressed = True
        else:
            pressed = False

        if (70 <= x <= 90 and 410 <= y <= 430) or (260 <= x <= 280 and 410 <= y <= 430):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pressed:
                if good:
                    good = False
                else:
                    good = True
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if 600 < x < 850:
            if 500 < y < 550 and x >= 600:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if left:
                    final_type = names[index]
                    final_name = char_name
                    if good:
                        final_side = "good"
                    else:
                        final_side = "evil"

                    # pygame.quit()
                    # return final_name, final_type, final_side, eligible_characters_images[index]
                    return final_name, final_type, final_side, eligible_characters_images[index], eligible_small_images[index]
                    # break
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

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if len(char_name) < 15:
                    letters_numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                       'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                                       '8', '9']

                    if pygame.key.name(event.key) in letters_numbers:
                        if len(char_name) == 0:
                            char_name += pygame.key.name(event.key).upper()
                        else:
                            char_name += pygame.key.name(event.key)
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        char_name = char_name[:-1]

        prev = left
        pygame.display.update()
        clock.tick(60)


def divide(final_text):
    array = []
    sentence = ''
    i = 0
    for word in final_text:
        sentence += word
        if word == '\n':
            word = ' '
        if word == ' ':
            if i == 5:
                array.append(sentence)
                sentence = ''
                i = 0
            else:
                i += 1
    array.append(sentence)
    return array


def character_info(name, ch_type, side, image):
    sequence = "Welcome to our world " + name + ". You are a " + side + " " + ch_type + " that"
    final_text = generate_text_about_character(sequence)
    array_text = divide(final_text)
    while True:
        screen.fill(BLACK)

        button_play = pygame.Rect(250, 500, 300, 50)
        pygame.draw.rect(screen, WHITE, button_play)
        draw_text("Play", 350, 500, 40, BLACK)

        screen.blit(image, (350, 0))
        text_y = 100
        for sentence in array_text:
            draw_text(sentence, 50, text_y, 20, WHITE)
            text_y += 20

        # draw_text(final_text, 50, 100, 10, WHITE)

        left, middle, right = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()

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


menu()
chosen_name, chosen_type, chosen_side, image, image_small = choose_character()
character_info(chosen_name, chosen_type, chosen_side, image)
game(chosen_name, chosen_type, chosen_side, image_small)
