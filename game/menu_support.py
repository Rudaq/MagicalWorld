# Method to draw text on the screen given its position, color and size
import sys

import pygame


# Method to draw text on the screen given its position, color and size
def draw_text_on_menu(text, x, w, size, color, screen, font_type='Verdana'):
    font = pygame.font.SysFont(font_type, size)
    img = font.render(text, True, color)
    screen.blit(img, (x, w))


# Format final generated text about character to be displayed in a few lines next to the image
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


