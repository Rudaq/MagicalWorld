from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.settings import GUI_IMAGES, BLACK
import math


def show_quest_to_hero(screen, hero):
    screen_width = math.floor(screen.get_size()[0])
    quest_top_right = screen_width - 400
    screen.blit(GUI_IMAGES['scroll'], (quest_top_right, 100))
    w = 200
    h = quest_top_right + 110
    if hero.active_quest is not None:
        text_list = wrap_text(hero.active_quest.description, 25, False)
        for text in text_list:
            draw_text(text, h, w, 14, BLACK, screen)
            w += 20
            if h == 1170:
                h += 5
            else:
                h -= 5
    else:
        text = "You have no active quest!"
        draw_text(text, h, w, 14, BLACK, screen)


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
