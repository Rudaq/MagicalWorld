from NLP.dialog_generation.ButtonClass import ButtonClass
from NLP.dialog_generation.GenerateNpcDialog import draw_text
from game.settings import GUI_IMAGES, BLACK
import pygame
import math
from artifacts.NpcRepresent import NpcRepresent
from datetime import datetime
import copy


def show_equipment_name(screen, equipment):
    draw_text(equipment.name, equipment.rect.x - 2, equipment.rect.y, 12, BLACK, screen)


def show_chest_to_hero(screen, hero, equipment_buttons):
    distance = math.floor(screen.get_size()[0] / 5)
    pos = 2 * distance
    screen.blit(GUI_IMAGES['big_chest'], (pos, 100))
    x = pos + 40
    y = 220
    counter = 0

    for eq in hero.equipment:
       # eq = ButtonClass(60, 60, i.name)
        image = pygame.transform.scale(eq.image, (60, 60))
        eq.image = image
        eq.rect.x = x
        eq.rect.y = y
        screen.blit(image, (eq.rect.x, eq.rect.y))
        equipment_buttons.add(eq)
        equipment_buttons.update()
        equipment_buttons.draw(screen)
        if counter == 2:
            y += 65
            x = pos - 30
            counter = -1
        x += 70
        counter += 1


def show_table_to_hero(screen, hero, npcs, equipment_buttons, npcs_to_choose):
    distance = math.floor(screen.get_size()[0] / 5)
    chest_pos = 2 * distance
    pos = chest_pos - 400
    # chest jest 300 x 300
    # table 400 X 200
    screen.blit(GUI_IMAGES['table'], (pos, 100))
    text = 'Choose NPC to which you wanna give an artifact:'
    draw_text(text, pos + 10, 110, 13, BLACK, screen)

    x = pos + 20
    y = 150
    counter = 0

    for npc in npcs:
        npc_represent = NpcRepresent(npc)
        # image = pygame.transform.scale(npc.image, (60, 60))
        # copy_npc.image = image
        npc_represent.rect.x = x
        npc_represent.rect.y = y
        screen.blit(npc_represent.image, (npc_represent.rect.x, npc_represent.rect.y))
        npcs_to_choose.add(npc_represent)
        npcs_to_choose.update()
        npcs_to_choose.draw(screen)
        if counter == 6:
            y += 65
            x = pos - 30
            counter = -1
        x += 55
        counter += 1


def time_to_chest_be_opened(restore_time_passed):
    time_diff = datetime.now() - restore_time_passed
    time_sec = time_diff.total_seconds()
    # print("time_start", restore_life_time_passed)

    time_to_display = 1 - time_sec
    if time_to_display <= 0:
        return True
    else:
        return False


def remove_artifact(hero, all_artifacts, artifact, screen):
    if hero.collect_artifact(artifact):
        all_artifacts.remove(artifact)
        all_artifacts.update()
        all_artifacts.draw(screen)
