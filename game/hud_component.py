# Function to update hud and displayed there components
import math
from datetime import datetime
from PIL import Image
import pygame

from NLP.dialog_generation.GenerateNpcDialog import draw_text
from game.settings import WIDTH_GAME, HEIGHT_GAME, HUD_YELLOW, ALMOND, BLACK, LIGHT_GREEN, BLUE, GUI_IMAGES, RED


def time_to_restore(screen, restore_life_time_passed, x):
    time_diff = datetime.now() - restore_life_time_passed
    time_sec = time_diff.total_seconds()
    # print("time_start", restore_life_time_passed)

    time_to_display = 60 - time_sec
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


def update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life, restore_mana, restore_mana_time_passed,
               restore_life_time_passed, chosen_npc, chest_opened):
    hud = pygame.Rect(0, 0, screen.get_size()[0], 100)
    pygame.draw.rect(screen, HUD_YELLOW, hud, 0, 1)

    border = pygame.Rect(0, 0, screen.get_size()[0], 100)
    pygame.draw.rect(screen, ALMOND, border, 5, 2)

    distance = math.floor(screen.get_size()[0] / 6)
    multiplicator = 0

    draw_text("Life ", multiplicator * distance + 50, 25, 12, BLACK, screen)

    life = pygame.Rect(multiplicator * distance + 100, 50, hero.life, 25)
    pygame.draw.rect(screen, LIGHT_GREEN, life, 0, 2)
    border = pygame.Rect(multiplicator * distance + 100, 50, 100, 25)
    pygame.draw.rect(screen, BLACK, border, 2, 2)
    multiplicator += 1

    draw_text("Mana ", multiplicator * distance + 50, 25, 12, BLACK, screen)

    mana = pygame.Rect(multiplicator * distance + 100, 50, hero.mana, 25)
    pygame.draw.rect(screen, BLUE, mana, 0, 2)
    border = pygame.Rect(multiplicator * distance + 100, 50, 100, 25)
    pygame.draw.rect(screen, BLACK, border, 2, 2)
    multiplicator += 1

    if restore_life:
        time_left = time_to_restore(screen, restore_life_time_passed, life.x + 150)
        if time_left == 0:
            hero.life = 100

    if restore_mana:
        time_left = time_to_restore(screen, restore_mana_time_passed, mana.x + 150)
        if time_left == 0:
            hero.mana = 100

    if chosen_npc is not None and chosen_npc.add_npc_to_hud:
        text = chosen_npc.race + "'s Life"

        draw_text(text, multiplicator * distance + 50, 25, 12, BLACK, screen)
        life = pygame.Rect(multiplicator * distance + 100, 50, chosen_npc.life, 25)
        pygame.draw.rect(screen, RED, life, 0, 2)
        border = pygame.Rect(multiplicator * distance + 100, 50, 100, 25)
        pygame.draw.rect(screen, BLACK, border, 2, 2)
    multiplicator += 1

    if chosen_npc is not None and chosen_npc.in_fight_mode:
        swords = GUI_IMAGES['swords']
        screen.blit(swords, (3, 8))

    draw_text("Equipment ", multiplicator * distance + 50, 25, 12, BLACK, screen)
    chest_surface = pygame.Surface((30, 30))
    if chest_opened:
        chest_image = GUI_IMAGES['small_chest_opened']
    else:
        chest_image = GUI_IMAGES['small_chest']
    screen.blit(chest_image, (multiplicator * distance + 125, 25))
    chest_button.image = chest_image
    chest_button.rect.x = multiplicator * distance + 125
    chest_button.rect.y = 40
    chest_surface.blit(chest_button.image, (chest_button.rect.x, chest_button.rect.y))
    multiplicator += 1

    # MAPA IKONA
    map_surface = pygame.Surface((20, 6 / 8 * HEIGHT_GAME))
    map_image = GUI_IMAGES['map_icon']
    screen.blit(map_image, (20, 6 / 8 * HEIGHT_GAME))
    map_button.image = map_image
    map_button.rect.x = 20
    map_button.rect.y = 6 / 8 * HEIGHT_GAME
    map_surface.blit(map_button.image, (map_button.rect.x, map_button.rect.y))

    draw_text("Points ", multiplicator * distance + 50, 25, 12, BLACK, screen)
    draw_text(str(hero.points), multiplicator * distance + 100, 50, 12, BLACK, screen)
    scroll_surface = pygame.Surface((30, 30))
    multiplicator += 1

    draw_text("Quest ", multiplicator * distance + 50, 25, 12, BLACK, screen)
    if (hero.active_quest is not None
           and hero.active_quest.active_task is not None
        and not hero.active_quest.active_task.is_opened) or \
            (hero.active_quest is not None and
             hero.active_quest.active_task is None and
             not hero.active_quest.is_opened):
        screen.blit(GUI_IMAGES['new_task_scroll'], (multiplicator * distance + 100, 50))
        scroll_button.image = GUI_IMAGES['new_task_scroll']
    else:
        screen.blit(GUI_IMAGES['scroll_small'], (multiplicator * distance + 100, 50))
        scroll_button.image = GUI_IMAGES['scroll_small']
    scroll_button.rect.x = multiplicator * distance + 100
    scroll_button.rect.y = 50
    scroll_surface.blit(scroll_button.image, (scroll_button.rect.x, scroll_button.rect.y))
