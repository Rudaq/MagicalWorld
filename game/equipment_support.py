from NLP.dialog_generation.ButtonClass import ButtonClass
from NLP.dialog_generation.GenerateNpcDialog import draw_text
from game.settings import GUI_IMAGES, BLACK
import pygame
import math
from datetime import datetime


def show_equipment_name(screen, equipment):
    draw_text(equipment.name, equipment.rect.x - 2, equipment.rect.y, 12, BLACK, screen)


def show_chest_to_hero(screen, hero, equipment_buttons):
    distance = math.floor(screen.get_size()[0] / 5)
    pos = 2 * distance
    screen.blit(GUI_IMAGES['big_chest'], (pos, 100))
    x = pos + 40
    y = 220
    counter = 0

    for i in hero.equipment:
        eq = ButtonClass(60, 60, i.name)
        image = pygame.transform.scale(i.image, (60, 60))
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
