import random
import pygame
from _csv import reader
from os import walk
import os
from pathlib import Path
from game.hero.Barbarian import Barbarian
from game.hero.Dwarf import Dwarf
from game.hero.Elf import Elf
from game.hero.Faerie import Faerie
from game.hero.Wizard import Wizard
from settings import NPCs, HERO_ANIMATIONS, GUI_IMAGES
from game.settings import BLACK
from game.dialog_support import talk
from game.fight_support import fight

path2 = os.path.dirname(os.path.realpath(__file__))
print("Current Directory", path2)
current_path = Path(__file__).resolve().parent.parent


class NPCTypeNotExistException(Exception):
    pass


def create_npc(npc_race, sprite_arrays, sprite_groups, collision_sprites, name=None):
    npc_dict_entry = NPCs.get(npc_race)
    if npc_dict_entry:
        if name is None:
            # rand choose one of the entities from its dict
            name, parameters = random.choice(list(npc_dict_entry['dict'].items()))  # "DRUIDS
        else:
            # specific entity
            parameters = npc_dict_entry['dict'][name]

        # creating npc object with its parameters
        entity = npc_dict_entry['class_name'](name=name, side=parameters[0], mana=npc_dict_entry['mana'],
                                              life=npc_dict_entry['life'], images=npc_dict_entry['images'],
                                              artifacts=parameters[1], quests=parameters[2], x=parameters[3],
                                              y=parameters[4], pos=(parameters[3], parameters[4]), groups=sprite_groups,
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
        hero = Elf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Elf'], None, (200, 200), (), (-10, -10), [])
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Faerie'], None, (200, 200), (), (-18, -18),
                      [])
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Wizard'], None, (200, 200), (), (-10, -10),
                      [])
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Dwarf'], None, (200, 200), (), (-30, -20), [])
    else:
        hero = Barbarian(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Barbarian'], None, (200, 200), (),
                         (-24, -30), [])

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
    surface_list = []
    for _, _, img_files in walk(path):
        for image in img_files:
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
    fight_button.rect.x = chosen_npc.rect.x - 40
    fight_button.rect.y = chosen_npc.rect.y - 50

    talk_button.rect.x = chosen_npc.rect.x + 40
    talk_button.rect.y = chosen_npc.rect.y - 50
    buttons.add(fight_button)
    buttons.add(talk_button)

    # check if buttons were clicked
    if talk_button.draw():
        talk(hero, chosen_npc)

    if fight_button.draw():
        fight(hero, chosen_npc)

    buttons.update()
    buttons.draw(screen)


# Function for displaying buttons above these NPC's that can only fight
def hero_only_in_fight(s, screen, fight_button, chosen_npc, hero):
    s.fill(BLACK)
    s.set_alpha(192)

    # create button 'Fight'
    buttons = pygame.sprite.Group()
    fight_button.rect.x = chosen_npc.rect.x
    fight_button.rect.y = chosen_npc.rect.y - 50
    buttons.add(fight_button)

    # check if buttons were clicked
    if fight_button.draw():
        fight(hero, chosen_npc)

    buttons.update()
    buttons.draw(screen)
