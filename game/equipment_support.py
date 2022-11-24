from NLP.dialog_generation.GenerateNpcDialog import draw_text
from game.settings import GUI_IMAGES, BLACK
import pygame
import math
from artifacts.Artifact import Artifact
from datetime import datetime
from game_support import npc_in_interaction_range


def show_equipment_name(screen, equipment):
    draw_text(equipment.name, equipment.rect.x - 2, equipment.rect.y, 12, BLACK, screen)


def show_chest_to_hero(screen, hero, equipment_buttons):
    distance = math.floor(screen.get_size()[0] / 5)
    pos = 2 * distance
    screen.blit(GUI_IMAGES['big_chest'].convert_alpha(), (pos, 100))
    x = pos + 40
    y = 220
    counter = 0
    # equipment_buttons.update()
    # equipment_buttons.draw(screen)
    for eq in hero.equipment:
        image = pygame.transform.scale(eq.image, (60, 60))
        eq.image = image
        eq.rect.x = x
        eq.rect.y = y
        screen.blit(image.convert_alpha(), (eq.rect.x, eq.rect.y))
        equipment_buttons.add(eq)
        equipment_buttons.update()
        equipment_buttons.draw(screen)
        if counter == 2:
            y += 65
            x = pos - 30
            counter = -1
        x += 70
        counter += 1


# function that shows NPC's while giving a gift
def show_table_to_hero(screen, npcs_to_choose, mock_npc_to_choose, hero):
    distance = math.floor(screen.get_size()[0] / 5)
    chest_pos = 2 * distance
    pos = chest_pos - 400

    x = pos + 20
    y = 150
    counter = 0
    check = 0
    image = GUI_IMAGES['table'].convert_alpha()

    for npc in npcs_to_choose:
        if npc_in_interaction_range(npc.npc, hero):
            if npc not in mock_npc_to_choose:
                mock_npc_to_choose.add(npc)
        else:
            mock_npc_to_choose.remove(npc)

    for mock_npc in mock_npc_to_choose:
        if mock_npc not in npcs_to_choose:
            mock_npc_to_choose.remove(mock_npc)

    if len(mock_npc_to_choose) > 0:
        for mock_npc in mock_npc_to_choose:
            image = pygame.transform.scale(image, (400, 150 + check * 60))
            screen.blit(image.convert_alpha(), (pos, 100))

            text = 'Choose NPC to which you wanna give a gift:'
            draw_text(text, pos + 10, 110, 13, BLACK, screen)

            mock_npc.rect.x = x
            mock_npc.rect.y = y
            mock_npc_to_choose.update()
            mock_npc_to_choose.draw(screen)

            if counter == 6:
                y += 65
                x = pos - 35
                counter = -1
                check += 1

            x += 55
            counter += 1
    else:
        image = pygame.transform.scale(image, (400, 50))
        screen.blit(image, (pos, 100))
        text = 'You have to get closer to the NPC to give him a gift ...'
        draw_text(text, pos + 10, 110, 13, BLACK, screen)


def give_artifact_to_npc(hero, mock_npc, artifact, equipment_buttons, npcs, screen):
    npc = mock_npc.npc

    for e in hero.equipment:
        if e.name == artifact.name:
            hero.equipment.remove(e)
    equipment_buttons.remove(artifact)
    if npc.take_gift(hero, artifact, npcs, screen):
        return True
    return False


def time_measure(restore_time_passed, seconds):
    time_diff = datetime.now() - restore_time_passed
    time_sec = time_diff.total_seconds()

    time_to_display = seconds - time_sec
    if time_to_display <= 0:
        return True
    else:
        return False


def remove_artifact(all_sprites_group, collision_sprites_hero, collision_sprites_npc, all_artifacts, artifact, screen):
    all_sprites_group.remove(artifact)
    collision_sprites_hero.remove(artifact)
    collision_sprites_npc.remove(artifact)
    all_artifacts.remove(artifact)
    # all_artifacts.update()
    # all_sprites_group.update()
    # collision_sprites_hero.update()
    # collision_sprites_npc.update()
    # all_artifacts.draw(screen)


def collect_map_artifact(hero, map_artifact, npcs):
    artifact = Artifact(map_artifact.small_image, map_artifact.points, map_artifact.name, None)
    hero.collect_artifact(artifact, npcs)
