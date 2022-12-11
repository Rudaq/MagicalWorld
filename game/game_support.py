import random

import pygame
from _csv import reader
from os import walk
import math
import os
from pathlib import Path
from shapely.geometry import Point, Polygon

from hero.Barbarian import Barbarian
from hero.Dwarf import Dwarf
from hero.Elf import Elf
from hero.Faerie import Faerie
from hero.Wizard import Wizard
from settings import HERO_ANIMATIONS, GUI_IMAGES, TILES_SIZE, RED, SCALE, WHITE, WIDTH_GAME, HEIGHT_GAME, \
    FrozenEmpireSurface, EnchantedSurface, LoveyDoveySurface, BushSurface, SpecularLakesSurface, DrearyForestSurface, \
    MedievilleSurface, CoastSurface, DesolationSurface, SwampSurface, MiniFrozenEmpire, MiniEnchantedForest, \
    MiniLoveyDoveyLand, MiniPrimevalBush, MiniSpecularLakes, MiniDrearyForest, MiniMedieville, MiniStormyPier, \
    MiniDesolationOfAbomination, MiniMistySwamp
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
                                                  y=parameters[4], pos=(parameters[3], parameters[4]), groups=sprite_groups,
                                                  collision_sprites=collision_sprites)

            for array in sprite_arrays:
                array.append(entity)
            for group in sprite_groups:
                group.add(entity)
    else:
        raise NPCTypeNotExistException

    return entity


def create_character(chosen_name, chosen_type, chosen_side):
    if chosen_type == "Elf":
        hero = Elf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Elf'], None, (200, 200), (), [])
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Faerie'], None, (200, 200), (), [])
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Wizard'], None, (200, 200), (), [])
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Dwarf'], None, (200, 200), (), [])
    else:
        hero = Barbarian(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Barbarian'], None, (200, 200), (), [])

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
def hero_in_dialog_or_talk(screen, chosen_npc):

    fight_image = pygame.transform.scale(GUI_IMAGES['fight_button'], (80, 40))
    talk_image = pygame.transform.scale(GUI_IMAGES['talk_button'], (80, 40))
    screen.blit(fight_image.convert_alpha(), (chosen_npc.rect.x - 40, chosen_npc.rect.y - 50))
    screen.blit(talk_image.convert_alpha(), (chosen_npc.rect.x + 40, chosen_npc.rect.y - 50))

    fight_polygon = Polygon([(chosen_npc.rect.x - 40, chosen_npc.rect.y - 50), (
        chosen_npc.rect.x - 40, chosen_npc.rect.y - 10), (chosen_npc.rect.x + 40, chosen_npc.rect.y - 10), (
                                 chosen_npc.rect.x + 40, chosen_npc.rect.y - 50)])
    talk_polygon = Polygon([(chosen_npc.rect.x + 40, chosen_npc.rect.y - 50), (
        chosen_npc.rect.x + 40, chosen_npc.rect.y - 10), (chosen_npc.rect.x + 120, chosen_npc.rect.y - 10), (
                                 chosen_npc.rect.x + 120, chosen_npc.rect.y - 50)])

    x, y = pygame.mouse.get_pos()
    mouse_position = Point(x, y)
    left, middle, right = pygame.mouse.get_pressed()
    value = ''

    if left:
        if fight_polygon.contains(mouse_position):
            value = 'fight'
        elif talk_polygon.contains(mouse_position):
            value = 'talk'

    return value


# checking the distance between hero and chosen npc
def npc_in_interaction_range(chosen_npc, hero):
    distance = dist((chosen_npc.rect.x, chosen_npc.rect.y), (hero.rect.centerx, hero.rect.centery))
    # if the distance in straight line is smaller than 120 px then the interaction is possible
    if distance > 4 * TILES_SIZE:
        return False
    else:
        return True


def show_map_to_hero(screen, hero, all_sprites_group):
    map_top_right = 20
    screen.blit(GUI_IMAGES['map2'].convert_alpha(), (map_top_right, 100))

    x_position_scaled = (hero.rect.centerx + all_sprites_group.offset.x) * SCALE
    y_position_scaled = (hero.rect.centery + all_sprites_group.offset.y) * SCALE
    pygame.draw.rect(screen, RED, pygame.Rect(x_position_scaled + map_top_right, y_position_scaled + 100, 5, 5))

    # Position of the mouse
    x, y = pygame.mouse.get_pos()
    coords = Point(x, y)
    x_show = x + 5
    y_show = y - 15

    # Hover over the realm biomes
    if MiniFrozenEmpire.contains(coords):
        draw_text_on_menu("Frozen Empire", x_show, y_show, 15, BLACK, screen)
    elif MiniEnchantedForest.contains(coords):
        draw_text_on_menu("Enchanted Forest", x_show, y_show, 15, BLACK, screen)
    elif MiniLoveyDoveyLand.contains(coords):
        draw_text_on_menu("Lovey Dovey Land", x_show, y_show, 15, BLACK, screen)
    elif MiniPrimevalBush.contains(coords):
        draw_text_on_menu("Primeval Bush", x_show, y_show, 15, BLACK, screen)
    elif MiniSpecularLakes.contains(coords):
        draw_text_on_menu("Specular Lakes", x_show, y_show, 15, BLACK, screen)
    elif MiniDrearyForest.contains(coords):
        draw_text_on_menu("Dreary Forest", x_show, y_show, 15, BLACK, screen)
    elif MiniMedieville.contains(coords):
        draw_text_on_menu("Medieville", x_show, y_show, 15, BLACK, screen)
    elif MiniStormyPier.contains(coords):
        draw_text_on_menu("Coastline with Stormy Pier", x_show, y_show, 15, BLACK, screen)
    elif MiniDesolationOfAbomination.contains(coords):
        draw_text_on_menu("Desolation of Abomination", x_show, y_show, 15, BLACK, screen)
    elif MiniMistySwamp.contains(coords):
        draw_text_on_menu("Misty Swamp", x_show, y_show, 15, BLACK, screen)


def check_biome(coords):
    global image

    if FrozenEmpireSurface.contains(coords):
        image = GUI_IMAGES['frozen_empire']
    elif EnchantedSurface.contains(coords):
        image = GUI_IMAGES['enchanted_forest']
    elif LoveyDoveySurface.contains(coords):
        image = GUI_IMAGES['lovey_dovey_land']
    elif BushSurface.contains(coords):
        image = GUI_IMAGES['primeval_bush']
    elif SpecularLakesSurface.contains(coords):
        image = GUI_IMAGES['specular_lakes']
    elif DrearyForestSurface.contains(coords):
        image = GUI_IMAGES['dreary_forest']
    elif MedievilleSurface.contains(coords):
        image = GUI_IMAGES['medieville']
    elif CoastSurface.contains(coords):
        image = GUI_IMAGES['stormy_pier']
    elif DesolationSurface.contains(coords):
        image = GUI_IMAGES['desolation_of_abomination']
    elif SwampSurface.contains(coords):
        image = GUI_IMAGES['misty_swamp']

    return image


def show_current_biome(screen, image):
    WIDTH_GAME_TMP = screen.get_size()[0]
    HEIGHT_GAME_TMP = screen.get_size()[1]
    coordinates = (WIDTH_GAME_TMP - 350, HEIGHT_GAME_TMP - 50)
    screen.blit(image.convert_alpha(), coordinates)


def add_map_artifacts(map_artifacts, all_artifacts):
    rainbow = Artifact(MAP_IMAGES['rainbow'].convert_alpha(), 20, 'Rainbow',
                       MAP_IMAGES['rainbow_small'].convert_alpha())
    rainbow.rect.x = 900
    rainbow.rect.y = 5500

    enchanted_tree = Artifact(MAP_IMAGES['enchanted_tree'].convert_alpha(), 20, 'Enchanted Stick',
                              MAP_IMAGES['stick'].convert_alpha())
    enchanted_tree.rect.x = 480
    enchanted_tree.rect.y = 4050

    mud = Artifact(MAP_IMAGES['mud'].convert_alpha(), 20, 'Mud', MAP_IMAGES['mud'].convert_alpha())
    mud.rect.x = 8300
    mud.rect.y = 950

    web = Artifact(MAP_IMAGES['spider_web'].convert_alpha(), 20, 'Spider web', MAP_IMAGES['spider_web'].convert_alpha())
    web.rect.x = 4400
    web.rect.y = 5700

    ball = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "ball.PNG")).convert_alpha()
    bamboo_tree = Artifact(MAP_IMAGES['bamboo_tree_ball'].convert_alpha(), 20, 'Ball', ball)
    bamboo_tree.rect.x = 11970
    bamboo_tree.rect.y = 4180

    flower = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "flower.PNG")).convert_alpha()
    big_tree = Artifact(MAP_IMAGES['big_tree_flower'].convert_alpha(), 30, 'Immortality Flower', flower)
    big_tree.rect.x = 6050
    big_tree.rect.y = 4780

    skull = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "skull.PNG")).convert_alpha()
    dig_ground = Artifact(MAP_IMAGES['dig_ground'].convert_alpha(), 30, 'Pandas Skull', skull)
    dig_ground.rect.x = big_tree.rect.x + 250
    dig_ground.rect.y = big_tree.rect.y + 150

    leaf = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "leaf.PNG")).convert_alpha()
    leaves = Artifact(MAP_IMAGES['leaves'].convert_alpha(), 30, 'Leaves', leaf)
    leaves.rect.x = 3750
    leaves.rect.y = 2700

    snow_paper = pygame.image.load(
        os.path.join(current_path, "resources/graphics/artifacts", "snow_paper.PNG")).convert_alpha()
    paper = Artifact(snow_paper, 20, 'Paper', MAP_IMAGES['paper'].convert_alpha())
    paper.rect.x = 350
    paper.rect.y = 1200

    pot = Artifact(MAP_IMAGES['pot'].convert_alpha(), 20, 'Pot', None)
    pot.rect.x = rainbow.rect.x + 198
    pot.rect.y = rainbow.rect.y + 30

    water_on_map_image = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "water_on_map.PNG")).convert_alpha()
    water_image = pygame.image.load(os.path.join(current_path, "resources/graphics/artifacts", "water.PNG")).convert_alpha()
    water = Artifact(water_on_map_image, 20, 'Water', water_image)
    water.rect.x = 9200
    water.rect.y = 4950
    all_artifacts.add(paper, pot, water, leaves, mud, web)

    map_artifacts.add(rainbow, bamboo_tree, big_tree, dig_ground, enchanted_tree)


def check_map_artifact(map_artifact):
    if map_artifact.name == 'Ball':
        map_artifact.image = MAP_IMAGES['bamboo_tree'].convert_alpha()
    elif map_artifact.name == 'Immortality Flower':
        map_artifact.image = MAP_IMAGES['big_tree'].convert_alpha()
    map_artifact.small_image = None


def change_image(npc):
    npc.images = NPC_IMAGES['image_snowman_nose']
