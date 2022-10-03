from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.settings import GUI_IMAGES, BLACK
import math
from quest_settings import QUESTS
from settings import BLACK
from quest.Quest import Quest
from quest.Task import Task


class QuestTypeNotExistException(Exception):
    pass


def create_quests(hero):
    if hero.race == 'Faerie':
        quests_dict_entry = QUESTS.get(hero.race)
    elif hero.race == 'Elf':
        quests_dict_entry = QUESTS.get(hero.race)
    if quests_dict_entry:
        if hero.side == 'good':
            parameters = quests_dict_entry.get('good')
            index = 0
            keys = list(parameters.keys())
            for p in parameters:
                tasks = []
                print(list(parameters.keys())[index])
                for t in parameters[p]['tasks']:
                    task = Task(t['name'], t['description'], t['artefact'], t['points'], t['npc_give_task '], t['npc_take_artifact '], t['next_npc '], t['gift'], hero, False)
                    tasks.append(task)

                quest = Quest(keys[index], parameters[p]['description'], parameters[p]['points'], tasks, hero, False)

                hero.quests.append(quest)
                index += 1
            hero.set_active_quest()
    else:
        raise QuestTypeNotExistException


def show_quest_to_hero(screen, hero):
    screen_width = math.floor(screen.get_size()[0])
    quest_top_right = screen_width - 400
    screen.blit(GUI_IMAGES['scroll'], (quest_top_right, 100))
    w = 200
    h = quest_top_right + 110
    if hero.active_quest is not None:
        if hero.active_quest.active_task is not None:
            text = hero.active_quest.active_task.description
        else:
            text = hero.active_quest.description
    else:
        text = "You mission is completed! Congratulation!!! <3"

    text_list = wrap_text(text, 25, False)
    for text in text_list:
        draw_text(text, h, w, 14, BLACK, screen)
        w += 20
        if h == 1170:
            h += 5
        else:
            h -= 5
