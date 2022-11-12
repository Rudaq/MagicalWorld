import sys

import pygame
from shapely.geometry import Point, Polygon
from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.settings import GUI_IMAGES, BLACK, HEIGHT_GAME, END_TEXT, continue_button, quit_button
import math
from quest_settings import QUESTS
from settings import BLACK
from quest.Quest import Quest
from quest.Task import Task


class QuestTypeNotExistException(Exception):
    pass


def create_quests(hero):
    quests_dict_entry = QUESTS.get(hero.race)
    if quests_dict_entry:
        if hero.side == 'evil':
            parameters = quests_dict_entry.get('evil')
        else:
            parameters = quests_dict_entry.get('good')
        for p in parameters:
            tasks = []
            task_parameters = parameters[p].get('tasks')
            for t in task_parameters:
                task = Task(t.get('name'), t.get('description'), t.get('artefact'), t.get('points'),
                            t.get('npc_give_task'), t.get('npc_take_artifact'), t.get('next_npc'), t.get('gift'), hero,
                            False)
                tasks.append(task)

            quest = Quest(parameters[p].get('name'), parameters[p].get('description'), parameters[p].get('points'),
                          tasks, hero, False)
            hero.quests.append(quest)
        hero.set_active_quest()
    else:
        raise QuestTypeNotExistException


def show_quest_to_hero(screen, hero):
    screen_width = math.floor(screen.get_size()[0])
    quest_top_right = screen_width - 400
    screen.blit(GUI_IMAGES['scroll'], (quest_top_right, 100))
    w = 150
    h = quest_top_right + 110
    if hero.active_quest is not None:
        if hero.active_quest.active_task is not None:
            text = hero.active_quest.active_task.description
        elif hero.active_quest.active_task is None \
                and hero.active_quest.is_started:
            text = "Find a correct character to get a next task!"
        else:
            text = hero.active_quest.description
    else:
        text = "Your missions are completed!"

    text_list = wrap_text(text, 25, False)
    for text in text_list:
        draw_text(text, h, w, 14, BLACK, screen)
        w += 20
        if h == 1170:
            h += 5
        else:
            h -= 5


def display_end_text(screen, hero):
    screen_width = math.floor(screen.get_size()[0])
    top_right = (screen_width - 500) / 2
    screen.blit(GUI_IMAGES['end_frame'], (top_right, (HEIGHT_GAME - 480) / 2))
    w = top_right - 230
    h = HEIGHT_GAME / 2 + 140

    text_list = wrap_text(END_TEXT[hero.race].replace("+name+", hero.name), 50, False)

    for text in text_list:
        draw_text(text, h, w, 16, BLACK, screen)
        w += 27

    x, y = pygame.mouse.get_pos()
    mouse_position = Point(x, y)
    left, middle, right = pygame.mouse.get_pressed()
    value = ''
    if left:
        if quit_button.contains(mouse_position):
            value = 'quit'
        elif continue_button.contains(mouse_position):
            value = 'continue'

    return value
