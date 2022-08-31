from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.settings import GUI_IMAGES, BLACK
import math


def show_quest_to_hero(screen, hero):
    multiplicator = 4
    distance = math.floor(screen.get_size()[0] / 6)
    screen.blit(GUI_IMAGES['scroll'], (multiplicator * distance, 100))
    text_list = wrap_text(hero.active_quest.description, 25, False)
    w = 200
    h = multiplicator * distance + 110
    for text in text_list:
        draw_text(text, h, w, 14, BLACK, screen)
        w += 20
        if h == 1170:
            h += 5
        else:
            h -= 5


# def show_quest_to_hero(screen, hero):
#     screen.blit(GUI_IMAGES['scroll'], (1100, 100))
#     text_list = wrap_text(hero.active_quest.description, 25, False)
#     w = 200
#     h = 1200
#     for text in text_list:
#         draw_text(text, h, w, 14, BLACK, screen)
#         w += 20
#         if h == 1170:
#             h += 5
#         else:
#             h -= 5
