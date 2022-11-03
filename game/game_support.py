import random

import pygame
from _csv import reader
from os import walk
import math
import os
from pathlib import Path

from hero.Barbarian import Barbarian
from hero.Dwarf import Dwarf
from hero.Elf import Elf
from hero.Faerie import Faerie
from hero.Wizard import Wizard
from settings import HERO_ANIMATIONS, GUI_IMAGES, TILES_SIZE, RED, SCALE
from npc_settings import NPCs
from settings import BLACK
from menu_support import draw_text_on_menu
from math import dist
from re import compile, split
from artifacts.Artifact import Artifact
from settings import MAP_IMAGES
from game.npc_settings import NPC_IMAGES

path2 = os.path.dirname(os.path.realpath(__file__))
current_path = Path(__file__).resolve().parent.parent


class NPCTypeNotExistException(Exception):
    pass


def create_npc(npc_race, sprite_arrays, sprite_groups, collision_sprites, name=None):
    npc_dict_entry = NPCs.get(npc_race)
    if npc_dict_entry:
        # for every object of type npc_dict_entry create a npc
        for item in npc_dict_entry['dict'].items():
            if name is None:
                name, parameters = item
                # print(parameters)
            else:
                # specific entity
                name, parameters = item

            # creating npc object with its parameters
            entity = npc_dict_entry['class_name'](name=name, side=parameters[0], mana=npc_dict_entry['mana'],
                                                  life=npc_dict_entry['life'], images=npc_dict_entry['images'],
                                                  artifacts=parameters[1], quests=parameters[2], x=parameters[3],
                                                  y=parameters[4], pos=(parameters[3], parameters[4]),
                                                  groups=sprite_groups,
                                                  inflation=(0, -10), collision_sprites=collision_sprites)

            for array in sprite_arrays:
                array.append(entity)
            for group in sprite_groups:
                group.add(entity)
    else:
        raise NPCTypeNotExistException

    return entity


def create_character(chosen_name, chosen_type, chosen_side):
    if chosen_type == "Elf":
        hero = Elf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Elf'], None, (200, 200), (), (0, 0), [])
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Faerie'], None, (200, 200), (), (0, 0),
                      [])
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Wizard'], None, (200, 200), (), (0, 0),
                      [])
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Dwarf'], None, (200, 200), (), (0, 0), [])
    else:
        hero = Barbarian(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Barbarian'], None, (200, 200), (),
                         (0, 0), [])

    return hero


def import_csv_layout(path):
    terrain_map = []

    with open(os.path.join(current_path, path)) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


# import all png graphics from one folder
# returns list of names of the images .png
# getting the whole path for each image
# folder name, subfolder, img_files
def import_folder(path):
    dre = compile(r'(\d+)')

    surface_list = []
    name_images = []
    for _, _, img_files in walk(path):
        for image in img_files:
            name_images.append(image)

    name_images.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in split(dre, l)])

    for image in name_images:
        full_path = path + '/' + image
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)

    return surface_list


# Function for displaying buttons above these NPC's that can talk and fight
def hero_in_dialog_or_talk(s, screen, fight_button, talk_button, chosen_npc, hero):
    s.fill(BLACK)
    s.set_alpha(192)

    # create buttons 'Fight' and 'Talk'
    buttons = pygame.sprite.Group()
    fight_button.image = pygame.transform.scale(GUI_IMAGES['fight_button'], (80, 40))
    fight_button.rect.x = chosen_npc.rect.x - 40
    fight_button.rect.y = chosen_npc.rect.y - 50

    talk_button.image = pygame.transform.scale(GUI_IMAGES['talk_button'], (80, 40))
    talk_button.rect.x = chosen_npc.rect.x + 40
    talk_button.rect.y = chosen_npc.rect.y - 50

    buttons.add(fight_button)
    buttons.add(talk_button)

    buttons.update()
    buttons.draw(screen)


# checking the distance between hero and chosen npc
def npc_in_interaction_range(chosen_npc, hero):
    distance = dist((chosen_npc.rect.x, chosen_npc.rect.y), (hero.rect.centerx, hero.rect.centery))
    # if the distance in straight line is smaller than 120 px then the interaction is possible
    if distance > 3 * TILES_SIZE:
        return False
    else:
        return True


def show_map_to_hero(screen, hero, all_sprites_group):
    map_top_right = 20
    screen.blit(GUI_IMAGES['map2'], (map_top_right, 100))

    x_position_scaled = (hero.rect.centerx + all_sprites_group.offset.x) * SCALE
    y_position_scaled = (hero.rect.centery + all_sprites_group.offset.y) * SCALE
    pygame.draw.rect(screen, RED, pygame.Rect(x_position_scaled + map_top_right, y_position_scaled + 100, 5, 5))

    # Position of the mouse
    x, y = pygame.mouse.get_pos()
    print(x)
    print(y)

    # Hover over the realm biomes
    if 27 < x < 190:
        if 111 < y < 205:
            draw_text_on_menu("Frozen Empire", x, y, 15, BLACK, screen)
        elif 233 < y < 330:
            draw_text_on_menu("Enchanted Forest", x, y, 15, BLACK, screen)
        elif 348 < y < 473:
            draw_text_on_menu("Lovey Dovey Land", x, y, 15, BLACK, screen)
    elif 208 < x < 379 and 112 < y < 198:
        draw_text_on_menu("Desolation of Abomination", x, y, 15, BLACK, screen)
    elif 208 < x < 420 and 234 < y < 303:
        draw_text_on_menu("Primeval Bush", x, y, 15, BLACK, screen)
    elif 478 < x < 634 and 221 < y < 320:
        draw_text_on_menu("Medieville", x, y, 15, BLACK, screen)
    elif 405 < x < 557 and 113 < y < 179:
        draw_text_on_menu("Misty Swamp", x, y, 15, BLACK, screen)
    elif 403 < x < 650 and 361 < y < 415:
        draw_text_on_menu("Specular Lakes", x, y, 15, BLACK, screen)
    elif (233 < x < 373 and 343 < y < 394) or (373 < x < 397 and 394 < y < 452):
        draw_text_on_menu("Dreary Forest", x, y, 15, BLACK, screen)
    elif 626 < x < 713 and 109 < y < 294:
        draw_text_on_menu("Coastline with Stormy Pier", x, y, 15, BLACK, screen)


def add_map_artifacts(map_artifacts, all_artifacts):
    rainbow = Artifact(MAP_IMAGES['rainbow'], 20, 'Rainbow', MAP_IMAGES['rainbow_small'])
    rainbow.rect.x = 900
    rainbow.rect.y = 5500

    enchanted_tree = Artifact(MAP_IMAGES['enchanted_tree'], 20, 'Enchanted Stick', MAP_IMAGES['stick'])
    enchanted_tree.rect.x = 480
    enchanted_tree.rect.y = 4050

    mud = Artifact(MAP_IMAGES['mud'], 20, 'Mud', MAP_IMAGES['mud'])
    mud.rect.x = 8300
    mud.rect.y = 950

    web = Artifact(MAP_IMAGES['spider_web'], 20, 'Spider web', MAP_IMAGES['spider_web'])
    web.rect.x = 4400
    web.rect.y = 5700

    ball = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "ball.PNG"))
    bamboo_tree = Artifact(MAP_IMAGES['bamboo_tree_ball'], 20, 'Ball', ball)
    bamboo_tree.rect.x = 11970
    bamboo_tree.rect.y = 4180

    flower = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "flower.PNG"))
    big_tree = Artifact(MAP_IMAGES['big_tree_flower'], 30, 'Immortality Flower', flower)
    big_tree.rect.x = 6050
    big_tree.rect.y = 4780

    skull = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "skull.PNG"))
    dig_ground = Artifact(MAP_IMAGES['dig_ground'], 30, 'Pandas Skull', skull)
    dig_ground.rect.x = big_tree.rect.x + 250
    dig_ground.rect.y = big_tree.rect.y + 150

    leaf = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "leaf.PNG"))
    leaves = Artifact(MAP_IMAGES['leaves'], 30, 'Leaves', leaf)
    leaves.rect.x = 3750
    leaves.rect.y = 2700

    snow_paper = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "snow_paper.PNG"))
    paper = Artifact(snow_paper, 20, 'Paper', MAP_IMAGES['paper'])
    paper.rect.x = 350
    paper.rect.y = 1200

    pot = Artifact(MAP_IMAGES['pot'], 20, 'Pot', None)
    pot.rect.x = rainbow.rect.x + 198
    pot.rect.y = rainbow.rect.y + 30

    water_on_map_image = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "water_on_map.PNG"))
    water_image = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "water.PNG"))
    water = Artifact(water_on_map_image, 20, 'Water', water_image)
    water.rect.x = 9200
    water.rect.y = 4950
    all_artifacts.add(paper, pot, water, leaves, mud, web)

    map_artifacts.add(rainbow, bamboo_tree, big_tree, dig_ground, enchanted_tree)


def check_map_artifact(map_artifact):
    if map_artifact.name == 'Ball':
        map_artifact.image = MAP_IMAGES['bamboo_tree']
    elif map_artifact.name == 'Immortality Flower':
        map_artifact.image = MAP_IMAGES['big_tree']
    map_artifact.small_image = None


def change_image(npc):
    npc.images = NPC_IMAGES['image_snowman_nose']
