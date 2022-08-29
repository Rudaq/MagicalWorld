# Function to update hud and displayed there components
from datetime import datetime
from PIL import Image
import pygame

from NLP.dialog_generation.GenerateNpcDialog import draw_text
from game.settings import WIDTH_GAME, HUD_YELLOW, ALMOND, BLACK, LIGHT_GREEN, BLUE, GUI_IMAGES, RED


def time_to_restore(screen, restore_life_time_passed, x):
    time_diff = datetime.now() - restore_life_time_passed
    time_sec = time_diff.total_seconds()
    # print("time_start", restore_life_time_passed)

    time_to_display = 120 - time_sec
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


def update_hud(screen, hero, scroll_button, chest_button, restore_life, restore_mana, restore_mana_time_passed,
               restore_life_time_passed, chosen_npc):
    hud = pygame.Rect(0, 0, screen.get_size()[0], 100)
    pygame.draw.rect(screen, HUD_YELLOW, hud, 0, 1)

    border = pygame.Rect(0, 0, screen.get_size()[0], 100)
    pygame.draw.rect(screen, ALMOND, border, 5, 2)

    draw_text("Life ", 50, 25, 12, BLACK, screen)

    life = pygame.Rect(100, 50, hero.life, 25)
    pygame.draw.rect(screen, LIGHT_GREEN, life, 0, 2)
    border = pygame.Rect(100, 50, 100, 25)
    pygame.draw.rect(screen, BLACK, border, 2, 2)

    draw_text("Mana ", 250, 25, 12, BLACK, screen)

    mana = pygame.Rect(300, 50, hero.mana, 25)
    pygame.draw.rect(screen, BLUE, mana, 0, 2)
    border = pygame.Rect(300, 50, 100, 25)
    pygame.draw.rect(screen, BLACK, border, 2, 2)

    draw_text("Equipment ", 850, 25, 12, BLACK, screen)
    chest_surface = pygame.Surface((30, 30))
    screen.blit(GUI_IMAGES['small_chest'], (900, 50))
    chest_button.image = GUI_IMAGES['small_chest']
    chest_button.rect.x = 900
    chest_button.rect.y = 50
    chest_surface.blit(chest_button.image, (chest_button.rect.x, chest_button.rect.y))

    draw_text("Points ", 1100, 25, 12, BLACK, screen)
    draw_text(str(hero.points), 1150, 50, 12, BLACK, screen)
    scroll_surface = pygame.Surface((30, 30))

    draw_text("Quest ", 1300, 25, 12, BLACK, screen)
    screen.blit(GUI_IMAGES['scroll_small'], (1350, 50))
    scroll_button.image = GUI_IMAGES['scroll_small']
    scroll_button.rect.x = 1350
    scroll_button.rect.y = 50
    scroll_surface.blit(scroll_button.image, (scroll_button.rect.x, scroll_button.rect.y))

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

        draw_text(text, 500, 25, 12, BLACK, screen)
        life = pygame.Rect(600, 50, chosen_npc.life, 25)
        pygame.draw.rect(screen, RED, life, 0, 2)
        border = pygame.Rect(600, 50, 100, 25)
        pygame.draw.rect(screen, BLACK, border, 2, 2)

    if chosen_npc is not None and chosen_npc.is_fighting:
        swords = GUI_IMAGES['swords']
        screen.blit(swords, (3, 8))
