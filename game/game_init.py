from game.game_support import create_npc, import_csv_layout, import_folder

import sys
import os
from datetime import datetime
from pygame.locals import *
from NLP.dialog_generation.ButtonClass import ButtonClass
from NLP.dialog_generation.NpcDialogThread import NpcDialogThread
from game.dialog_support import hero_in_dialog, update_positions_and_transparency, move_dialog_up, move_dialog_down, \
    stop_talk, talk
from game.game_support import hero_in_dialog_or_talk, npc_in_interaction_range, check_map_artifact
from game.fight_support import set_fight_parameters, stop_fight, remove_npc, fight
from game.game_support import create_npc, add_map_artifacts, show_map_to_hero, show_current_biome, \
    check_biome
from game.hud_component import update_hud
from game.map.CameraGroup import CameraGroup
from game.map.map_support import create_map
from game.quest_support import show_quest_to_hero, display_end_text
from game.equipment_support import show_chest_to_hero, show_equipment_name, time_measure, remove_artifact, \
    show_table_to_hero, give_artifact_to_npc
from settings import *
from npc_settings import *
import pygame
from shapely.geometry import Point
from pathlib import Path
from artifacts.MockNpc import MockNpc
from quest_support import create_quests

'''
Main game loop
'''

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent


# Main game function
def game(hero):
    # pygame initialization
    pygame.init()
    pygame.display.set_caption("Adventures in the Realm")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((WIDTH_GAME, HEIGHT_GAME))
    print("Screen size", screen.get_size()[0])
    # WIDTH_GAME = screen.get_size()[0]
    # HEIGHT_GAME = screen.get_size()[1]
    clock = pygame.time.Clock()

    music_path = os.path.join(path, "resources/music/background_sound.wav")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    hero.initialize_music(hero.sound1_path, hero.sound2_path, hero.sound3_path)

    npcs = []
    sprites_to_move_opposite = []
    all_sprites_group = CameraGroup()
    collision_sprites_hero = pygame.sprite.Group()

    collision_sprites_npc = pygame.sprite.Group()
    npc_boundaries = pygame.sprite.Group()

    all_artifacts = pygame.sprite.Group()
    all_sprites_group.add(all_artifacts)

    # Adding created characters to group with all sprites
    hero.collision_sprites = collision_sprites_hero
    hero.groups = all_sprites_group
    all_sprites_group.add(hero)

    moving = False

    dir_opposite = 'R'
    mov_x = 0
    mov_y = 0
    sign = 1
    movement = 'horizontal'

    pressed = False
    prev = False
    npc_dialog_thread = None
    npc_dialog_thread = NpcDialogThread(hero, screen, npcs)
    npc_dialog_thread.start()

    show_quest = False
    show_chest = False
    show_map = False
    chest_opened = False
    show_table = False
    show_message = False
    hero_active = True
    chosen_artifact = None
    restore_life = False
    restore_mana = False
    restore_life_time_passed = None
    restore_mana_time_passed = None
    restore = None
    option = 1
    npc_clicked = False
    chosen_npc = None
    counter = 0
    first_iteration = True

    s = pygame.Surface((screen.get_size()[0], 150), pygame.SRCALPHA)
    arrow_up = ButtonClass(25, 25, 'arrow_up')
    arrow_down = ButtonClass(25, 25, 'arrow_down')
    scroll_button = ButtonClass(30, 40, 'scroll_button')
    chest_button = ButtonClass(30, 40, 'chest_button')
    map_button = ButtonClass(230, 240, 'map_button')
    fight_button = ButtonClass(80, 40, 'fight_button')
    talk_button = ButtonClass(80, 40, 'talk_button')
    buttons = pygame.sprite.Group()

    equipment_buttons = pygame.sprite.Group()
    # equipment_buttons.update()
    # equipment_buttons.draw(screen)

    # artifacts that are placed on map and are needed for the quests (hero can collect them while clicking)
    map_artifacts = pygame.sprite.Group()
    add_map_artifacts(map_artifacts, all_artifacts)
    sprites_to_move_opposite.extend(map_artifacts)
    sprites_to_move_opposite.extend(all_artifacts)
    all_sprites_group.add(map_artifacts)
    collision_sprites_hero.add(map_artifacts)

    collision_sprites_npc.add(map_artifacts)
    collision_sprites_npc.add(npc_boundaries)
    collision_sprites_npc.add(hero)
    all_sprites_group.add(collision_sprites_npc)

    # list of NPC's from which hero can select to who give an artifact
    npcs_to_choose = pygame.sprite.Group()
    npcs_to_choose.update()
    npcs_to_choose.draw(screen)

    mock_npcs_to_choose = pygame.sprite.Group()
    mock_npcs_to_choose.update()
    mock_npcs_to_choose.draw(screen)


    # Creating npcs
    for npc_entity in NPCs:
        create_npc(npc_entity, [npcs, sprites_to_move_opposite], [all_sprites_group], collision_sprites_npc)

    for npc in npcs:
        npc.initialize_music(npc.sound_path)
        npc.start_centerx = npc.rect.centerx
        npc.start_centery = npc.rect.centery
        npc.set_start_centerx = False
        npc.set_start_centery = False

        mock_npc = MockNpc(npc)
        npcs_to_choose.add(mock_npc)
        mock_npcs_to_choose.add(mock_npc)
        sprites_to_move_opposite.extend(npc.artifacts)
        collision_sprites_hero.add(npc.artifacts)
        collision_sprites_npc.add(npc.artifacts)


        # npc_collision_with_npcs = pygame.sprite.Group()
        # for n in npcs:
        #     if npc != n:
        #         npc_collision_with_npcs.add(n)

        # all_sprites_group.add(npc_collision_with_npcs)
        # npc.collision_sprites = collision_sprites_npc
        # npc.collision_sprites_npc = npc_collision_with_npcs
        # npc.groups = all_sprites_group

        all_sprites_group.add(npc)
        collision_sprites_hero.add(npc)

    # collision_sprites_npc or npc_boundaries
    create_map(all_sprites_group, collision_sprites_hero, npc_boundaries, sprites_to_move_opposite)

    hero.collision_sprites = collision_sprites_hero

    print("Number of collision sprites: ", collision_sprites_npc)
    print("NPC boundaries no: ", npc_boundaries)
    print("Hero boundaries no: ", collision_sprites_hero)
    # collision_sprites_npc.add(npc_boundaries)

    for col_npc in collision_sprites_npc:
        npc_boundaries.add(col_npc)

    for npc in npcs:
        npc.collision_sprites = npc_boundaries
        npc.collision_sprites.remove(npc)

    hero.rect.centerx = screen.get_size()[0] / 2
    hero.rect.centery = screen.get_size()[1] / 2
    all_sprites_group.offset.x = 0
    all_sprites_group.offset.y = 0
    create_quests(hero)

    while True:
        # screen.blit(SEA, (0, 0))
        all_sprites_group.custom_draw(hero, npcs, screen)
        all_sprites_group.update()
        update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life, restore_mana,
                   restore_mana_time_passed,
                   restore_life_time_passed, hero.chosen_npc, chest_opened)

        all_artifacts.update()
        all_artifacts.draw(screen)

        map_artifacts.update()
        map_artifacts.draw(screen)

        # showing name of the biome
        actual_coordinates = Point(hero.rect.centerx + all_sprites_group.offset.x,
                                   hero.rect.centery + all_sprites_group.offset.y)
        show_current_biome(screen, check_biome(actual_coordinates))

        # Getting the list of all pressed keys
        keys_pressed = pygame.key.get_pressed()

        # Event support - quiting, movement
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_d or event.key == pygame.K_DOWN or event.key == pygame.K_s \
                        or event.key == pygame.K_UP or event.key == pygame.K_w:
                    moving = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    hero.direction = 'U'
                    movement = 'vertical'
                    moving = True
                    dir_opposite = 'D'
                    mov_x = 0
                    mov_y = HERO_SPEED
                    sign = (-1)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    hero.direction = 'D'
                    movement = 'vertical'
                    moving = True
                    dir_opposite = 'U'
                    mov_x = 0
                    mov_y = HERO_SPEED
                    sign = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    hero.direction = 'R'
                    movement = 'horizontal'
                    moving = True
                    dir_opposite = 'L'
                    mov_x = HERO_SPEED
                    mov_y = 0
                    sign = 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    hero.direction = 'L'
                    movement = 'horizontal'
                    moving = True
                    dir_opposite = 'R'
                    mov_x = HERO_SPEED
                    mov_y = 0
                    sign = (-1)
                elif event.key == pygame.K_1 and hero.in_fight_mode:
                    option = 1
                    set_fight_parameters(hero)
                elif event.key == pygame.K_2 and hero.in_fight_mode:
                    option = 2
                    set_fight_parameters(hero)
                elif event.key == pygame.K_3 and hero.in_fight_mode:
                    option = 3
                    set_fight_parameters(hero)

                # Event support for dialog
                if hero.in_dialog:
                    moving = False
                    # Checking if hero is now talking - possibility of keyboard interaction
                    # letters, digits, signs and space accepted (lists at the top)
                    if hero.hero_turn:
                        if pygame.key.name(event.key) in LETTERS:
                            if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                                hero.my_text += pygame.key.name(event.key).upper()
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text

                        elif pygame.key.name(event.key) in DIGITS:
                            if pygame.key.name(event.key) == '1' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '!'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        elif pygame.key.name(event.key) == 'space':
                            hero.my_text += ' '
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        elif pygame.key.name(event.key) in SIGNS:
                            if pygame.key.name(event.key) == '/' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '?'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        # Deleting the last written letter
                        elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            if hero.my_text != '>> ':
                                hero.my_text = hero.my_text[:-1]
                                hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        # Detecting enter, finishing the input, turn is changed to npc
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            hero.hero_turn = False
                            update_positions_and_transparency(hero.text_history)

        if moving:
            hero.move(movement, dir_opposite, mov_x, mov_y, sign, all_sprites_group,
                      sprites_to_move_opposite)

        # -----------------------------------------------------------------------------------------------
        # Random movement of npcs if not in dialog
        for npc in npcs:
            if not npc.is_talking and not npc.in_fight_mode:
                npc.move(all_sprites_group)

        if hero_active:
            if hero.active_quest is None:
                pygame.time.wait(120)
                hero_active = False
                show_message = True

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()
        mouse_point = (x, y)

        # Checking if the value of left in the last iteration was different
        # Ensuring that one click only performs the action once
        if left and prev != left:
            pressed = True
        else:
            pressed = False

        # Checking if mouse pressed
        if pressed:
            # check if hero have collected an artifact
            for artifact in all_artifacts:
                if artifact.rect.collidepoint(mouse_point):

                    update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life, restore_mana,
                               restore_mana_time_passed,
                               restore_life_time_passed, hero.chosen_npc, chest_opened)

                    # remove the artifact from the surface
                    if hero.collect_artifact(artifact, npcs):
                        # change the chest image in the hud to open chest
                        chest_opened = True
                        remove_artifact(all_sprites_group, collision_sprites_hero, collision_sprites_npc, all_artifacts,
                                        artifact, screen)
                        # time to chest icon to be opened
                        restore = datetime.now()
                    break

            for map_artifact in map_artifacts:
                if map_artifact.rect.collidepoint(mouse_point):
                    update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life, restore_mana,
                               restore_mana_time_passed,
                               restore_life_time_passed, hero.chosen_npc, chest_opened)
                    if hero.collect_map_artifact(map_artifact, equipment_buttons):
                        chest_opened = True
                        restore = datetime.now()
                        check_map_artifact(map_artifact)
                    break

            for npc in npcs:
                # Checking mouse point collision with npc
                if npc.rect.collidepoint(mouse_point):
                    # checking if hero is in npc's range in order to interact
                    if npc_in_interaction_range(npc, hero):
                        # check if NPC is clicked or / unclicked
                        if not hero.npc_clicked:
                            hero.chosen_npc = npc
                            hero.npc_clicked = True
                            # show NPC's life on hud
                            hero.chosen_npc.add_npc_to_hud = True
                            if hero.active_quest is None:
                                show_message = True
                            # if hero.active_quest is None:
                            #     update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life,
                            #                restore_mana,
                            #                restore_mana_time_passed,
                            #                restore_life_time_passed, hero.chosen_npc, chest_opened)
                            #     all_sprites_group.update()

                        else:
                            hero.npc_clicked = False
                            # remove NPC's life from hud
                            hero.chosen_npc.add_npc_to_hud = False
                            # Stop talking or fighting
                            if hero.chosen_npc.is_talking:
                                stop_talk(hero, hero.chosen_npc)

                            if hero.chosen_npc.in_fight_mode:
                                stop_fight(hero, hero.chosen_npc)

                            # update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life,
                            #            restore_mana,
                            #            restore_mana_time_passed,
                            #            restore_life_time_passed, hero.chosen_npc, chest_opened)
                            # all_sprites_group.update()
                    break

            if arrow_up.rect.collidepoint(mouse_point):
                move_dialog_up(hero.text_history)
            elif arrow_down.rect.collidepoint(mouse_point):
                move_dialog_down(hero.text_history)
            elif scroll_button.rect.collidepoint(mouse_point):
                show_quest = not show_quest
            elif chest_button.rect.collidepoint(mouse_point):
                show_chest = not show_chest
                if not show_chest:
                    show_table = False
            elif map_button.rect.collidepoint(mouse_point):
                show_map = not show_map
            elif fight_button.rect.collidepoint(mouse_point):
                fight(hero, hero.chosen_npc)
            elif talk_button.rect.collidepoint(mouse_point):
                talk(hero, hero.chosen_npc)

            if show_chest:
                for equipment in equipment_buttons:
                    if equipment.rect.collidepoint(mouse_point):
                        show_table = not show_table
                        if show_table:
                            hero.chosen_artifact = equipment


        # Set previous state of left mouse button
        prev = left
        # check the state of chest icon
        if restore is not None:
            if time_measure(restore, 1):
                chest_opened = False
                update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life, restore_mana,
                           restore_mana_time_passed,
                           restore_life_time_passed, hero.chosen_npc, chest_opened)

        # check if NPC is still alive
        for npc in npcs:
            if npc.life == 0 or npc.life < 0:
                if npc == hero.chosen_npc:
                    stop_fight(hero, npc)
                    stop_talk(hero, npc)
                    hero.npc_clicked = False
                npc.kill_npc(all_artifacts, screen)
                remove_npc(npc, npcs, all_sprites_group, npcs_to_choose, collision_sprites_hero, collision_sprites_npc,
                           screen)

        if hero.life == 0 or hero.life < 0:
            npc_clicked = False
            # remove NPC's life from hud
            chosen_npc.add_npc_to_hud = False
            # Stop talking or fighting
            if chosen_npc.is_talking:
                stop_talk(hero, chosen_npc)

            if chosen_npc.in_fight_mode:
                stop_fight(hero, chosen_npc)

            update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life,
                       restore_mana,
                       restore_mana_time_passed,
                       restore_life_time_passed, chosen_npc, chest_opened)
            all_sprites_group.update()

        if chosen_npc is not None:
            if chosen_npc.add_npc_to_hud:
                update_hud(screen, hero, scroll_button, chest_button, map_button, restore_life,
                           restore_mana,
                           restore_mana_time_passed,
                           restore_life_time_passed, hero.chosen_npc, chest_opened)
                all_sprites_group.update()

        if hero.in_attack and hero.mana > 0:
            hero.fight(screen, option, npcs)
            # all_sprites_group.update()

        if hero.chosen_npc is not None:
            if hero.chosen_npc.in_fight_mode:
                hero.chosen_npc.move_in_fight(hero, all_sprites_group)
                hero.chosen_npc.attack_type = None
                hero.chosen_npc.fight_npc(screen, hero, npcs)
                all_sprites_group.update()

        if hero.npc_clicked:
            if not hero.chosen_npc.is_talking and not hero.chosen_npc.in_fight_mode:
                # checking if talk or fight button are clicked
                value = hero_in_dialog_or_talk(screen, hero.chosen_npc)
                if value == 'fight':
                    fight(hero, hero.chosen_npc)
                elif value == 'talk':
                    talk(hero, hero.chosen_npc)
                all_sprites_group.update()

        if hero.in_dialog:
            hero_in_dialog(s, screen, arrow_up, arrow_down, hero)
            # all_sprites_group.update()

        if show_quest:
            if hero.active_quest.active_task is None and not hero.active_quest.is_opened:
                hero.active_quest.is_opened = True
            elif hero.active_quest.active_task is not None and not hero.active_quest.active_task.is_opened:
                hero.active_quest.active_task.is_opened = True
            show_quest_to_hero(screen, hero)

        if show_map:
            show_map_to_hero(screen, hero, all_sprites_group)

        # show the chest with the hero's equipment
        if show_chest:
            show_chest_to_hero(screen, hero, equipment_buttons)
            for equipment in equipment_buttons:
                if equipment.rect.collidepoint(mouse_point):
                    show_equipment_name(screen, equipment)

        # show the table with NPC's from which hero can choose while giving a gift
        if show_table:
            show_table_to_hero(screen, npcs_to_choose, mock_npcs_to_choose, hero)
            for mock_npc in mock_npcs_to_choose:
                if mock_npc.rect.collidepoint(mouse_point):
                    give_artifact_to_npc(hero, mock_npc, hero.chosen_artifact, equipment_buttons, npcs, screen)
                    show_table = False

        if show_message and (hero_active == False):
            if display_end_text(screen, hero) == 'continue':
                show_message = False
            elif display_end_text(screen, hero) == 'quit':
                pygame.quit()
                sys.exit()

        if hero.mana < 50 and not restore_mana:
            restore_mana = True
            restore_mana_time_passed = datetime.now()
        elif hero.mana >= 50:
            restore_mana = False

        if hero.life < 50 and not restore_life:
            restore_life = True
            restore_life_time_passed = datetime.now()
        elif hero.life >= 50:
            restore_life = False

        all_sprites_group.update()
        pygame.display.update()
        clock.tick(30)
