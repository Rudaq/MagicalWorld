from NLP.dialog_generation.ButtonClass import ButtonClass
from NLP.dialog_generation.GenerateNpcDialog import draw_text
from game.settings import GUI_IMAGES, BLACK
import pygame


def show_equipment_name(screen, equipment):
    draw_text(equipment.name, equipment.rect.x - 2, equipment.rect.y, 12, BLACK, screen)


def show_chest_to_hero(screen, hero, equipment_buttons):
    screen.blit(GUI_IMAGES['big_chest'], (800, 100))
    x = 840
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
            x = 770
            counter = -1
        x += 70
        counter += 1
