import random
import pygame
from _csv import reader
from os import walk
import os
from pathlib import Path
from hero.Barbarian import Barbarian
from hero.Dwarf import Dwarf
from hero.Elf import Elf
from hero.Faerie import Faerie
from hero.Wizard import Wizard
from settings import NPCs, HERO_ANIMATIONS, GUI_IMAGES, TILES_SIZE
from settings import BLACK, DARK_WIZARDS_QUESTS, MERMAIDS_QUESTS, ORCS_QUESTS, VAMPIRE_QUESTS, PANDAS_QUESTS, \
    FEARIES_QUESTS, AMAZONS_QUESTS, FARMERS_QUESTS, SMITHS_QUESTS, UNICORN_QUESTS, BLIND_RATS_QUESTS, EARTH_ELEMENTAL_QUESTS, \
    TREANTS_QUESTS, DARK_ELVES_QUESTS, ELVES_QUESTS, BIG_MONKE_QUESTS, SPIRIT_QUESTS, SNOWMAN_QUESTS, LEPRECHAUN_QUESTS, BIG_WOLVES_QUESTS, DRUID_QUESTS
from math import dist
from quest.Quest import Quest

from dialog_support import talk
from fight_support import fight

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


def create_quest(NPC, quest_name):
    if NPC.race == "Dark Wizard":
        quest = Quest(DARK_WIZARDS_QUESTS[quest_name[0]], DARK_WIZARDS_QUESTS[quest_name[1]], DARK_WIZARDS_QUESTS[quest_name[2]], DARK_WIZARDS_QUESTS[quest_name[3]], DARK_WIZARDS_QUESTS[quest_name[4]], DARK_WIZARDS_QUESTS[quest_name[5]], DARK_WIZARDS_QUESTS[quest_name[6]])
    elif NPC.race == "Mermaid":
        quest = Quest(MERMAIDS_QUESTS[quest_name[0]], MERMAIDS_QUESTS[quest_name[1]], MERMAIDS_QUESTS[quest_name[2]], MERMAIDS_QUESTS[quest_name[3]], MERMAIDS_QUESTS[quest_name[4]], MERMAIDS_QUESTS[quest_name[5]], MERMAIDS_QUESTS[quest_name[6]])
    elif NPC.race == "Orc":
        quest = Quest(ORCS_QUESTS[quest_name[0]], ORCS_QUESTS[quest_name[1]], ORCS_QUESTS[quest_name[2]], ORCS_QUESTS[quest_name[3]], ORCS_QUESTS[quest_name[4]], ORCS_QUESTS[quest_name[5]], ORCS_QUESTS[quest_name[6]])
    elif NPC.race == "Vampire":
        quest = Quest(VAMPIRE_QUESTS[quest_name[0]], VAMPIRE_QUESTS[quest_name[1]], VAMPIRE_QUESTS[quest_name[2]], VAMPIRE_QUESTS[quest_name[3]], VAMPIRE_QUESTS[quest_name[4]], VAMPIRE_QUESTS[quest_name[5]], VAMPIRE_QUESTS[quest_name[6]])
    elif NPC.race == "Panda":
        quest = Quest(PANDAS_QUESTS[quest_name[0]], PANDAS_QUESTS[quest_name[1]], PANDAS_QUESTS[quest_name[2]],
                      PANDAS_QUESTS[quest_name[3]], PANDAS_QUESTS[quest_name[4]], PANDAS_QUESTS[quest_name[5]],
                      PANDAS_QUESTS[quest_name[6]])
    elif NPC.race == "Faerie":
        quest = Quest(FEARIES_QUESTS[quest_name[0]], FEARIES_QUESTS[quest_name[1]], FEARIES_QUESTS[quest_name[2]],
                      FEARIES_QUESTS[quest_name[3]], FEARIES_QUESTS[quest_name[4]], FEARIES_QUESTS[quest_name[5]],
                      FEARIES_QUESTS[quest_name[6]])
    elif NPC.race == "Earth Elemental":
        quest = Quest(EARTH_ELEMENTAL_QUESTS[quest_name[0]], EARTH_ELEMENTAL_QUESTS[quest_name[1]], EARTH_ELEMENTAL_QUESTS[quest_name[2]],
                      EARTH_ELEMENTAL_QUESTS[quest_name[3]], EARTH_ELEMENTAL_QUESTS[quest_name[4]], EARTH_ELEMENTAL_QUESTS[quest_name[5]],
                      EARTH_ELEMENTAL_QUESTS[quest_name[6]])
    elif NPC.race == "Dark Elf":
        quest = Quest(DARK_ELVES_QUESTS[quest_name[0]], DARK_ELVES_QUESTS[quest_name[1]], DARK_ELVES_QUESTS[quest_name[2]],
                      DARK_ELVES_QUESTS[quest_name[3]], DARK_ELVES_QUESTS[quest_name[4]], DARK_ELVES_QUESTS[quest_name[5]],
                      DARK_ELVES_QUESTS[quest_name[6]])
    elif NPC.race == "Elf":
        quest = Quest(ELVES_QUESTS[quest_name[0]], ELVES_QUESTS[quest_name[1]], ELVES_QUESTS[quest_name[2]],
                      ELVES_QUESTS[quest_name[3]], ELVES_QUESTS[quest_name[4]], ELVES_QUESTS[quest_name[5]],
                      ELVES_QUESTS[quest_name[6]])
    elif NPC.race == "Smith":
        quest = Quest(SMITHS_QUESTS[quest_name[0]], SMITHS_QUESTS[quest_name[1]], SMITHS_QUESTS[quest_name[2]],
                      SMITHS_QUESTS[quest_name[3]], SMITHS_QUESTS[quest_name[4]], SMITHS_QUESTS[quest_name[5]],
                      SMITHS_QUESTS[quest_name[6]])
    elif NPC.race == "Unicorn":
        quest = Quest(UNICORN_QUESTS[quest_name[0]], UNICORN_QUESTS[quest_name[1]], UNICORN_QUESTS[quest_name[2]],
                      UNICORN_QUESTS[quest_name[3]], UNICORN_QUESTS[quest_name[4]], UNICORN_QUESTS[quest_name[5]],
                      UNICORN_QUESTS[quest_name[6]])
    elif NPC.race == "Blind Rats":
        quest = Quest(BLIND_RATS_QUESTS[quest_name[0]], BLIND_RATS_QUESTS[quest_name[1]], BLIND_RATS_QUESTS[quest_name[2]],
                      BLIND_RATS_QUESTS[quest_name[3]], BLIND_RATS_QUESTS[quest_name[4]], BLIND_RATS_QUESTS[quest_name[5]],
                      BLIND_RATS_QUESTS[quest_name[6]])
    elif NPC.race == "Treant":
        quest = Quest(TREANTS_QUESTS[quest_name[0]], TREANTS_QUESTS[quest_name[1]], TREANTS_QUESTS[quest_name[2]],
                      TREANTS_QUESTS[quest_name[3]], TREANTS_QUESTS[quest_name[4]], TREANTS_QUESTS[quest_name[5]],
                      TREANTS_QUESTS[quest_name[6]])
    elif NPC.rac == "Amazon":
        quest = Quest(AMAZONS_QUESTS[quest_name[0]], AMAZONS_QUESTS[quest_name[1]], AMAZONS_QUESTS[quest_name[2]],
                      AMAZONS_QUESTS[quest_name[3]], AMAZONS_QUESTS[quest_name[4]], AMAZONS_QUESTS[quest_name[5]],
                      AMAZONS_QUESTS[quest_name[6]])
    elif NPC.race == "Farmer":
        quest = Quest(FARMERS_QUESTS[quest_name[0]], FARMERS_QUESTS[quest_name[1]], FARMERS_QUESTS[quest_name[2]],
                      FARMERS_QUESTS[quest_name[3]], FARMERS_QUESTS[quest_name[4]], FARMERS_QUESTS[quest_name[5]],
                      FARMERS_QUESTS[quest_name[6]])
    elif NPC.race == "Big Monke":
        quest = Quest(BIG_MONKE_QUESTS[quest_name[0]], BIG_MONKE_QUESTS[quest_name[1]], BIG_MONKE_QUESTS[quest_name[2]],
                      BIG_MONKE_QUESTS[quest_name[3]], BIG_MONKE_QUESTS[quest_name[4]], BIG_MONKE_QUESTS[quest_name[5]],
                      BIG_MONKE_QUESTS[quest_name[6]])
    elif NPC.race == "Spirit":
        quest = Quest(SPIRIT_QUESTS[quest_name[0]], SPIRIT_QUESTS[quest_name[1]], SPIRIT_QUESTS[quest_name[2]],
                      SPIRIT_QUESTS[quest_name[3]], SPIRIT_QUESTS[quest_name[4]], SPIRIT_QUESTS[quest_name[5]],
                      SPIRIT_QUESTS[quest_name[6]])
    elif NPC.race == "Snowman":
        quest = Quest(SNOWMAN_QUESTS[quest_name[0]], SNOWMAN_QUESTS[quest_name[1]], SNOWMAN_QUESTS[quest_name[2]],
                      SNOWMAN_QUESTS[quest_name[3]], SNOWMAN_QUESTS[quest_name[4]], SNOWMAN_QUESTS[quest_name[5]],
                      SNOWMAN_QUESTS[quest_name[6]])
    elif NPC.race == "Leprechaun":
        quest = Quest(LEPRECHAUN_QUESTS[quest_name[0]], LEPRECHAUN_QUESTS[quest_name[1]], LEPRECHAUN_QUESTS[quest_name[2]],
                      LEPRECHAUN_QUESTS[quest_name[3]], LEPRECHAUN_QUESTS[quest_name[4]], LEPRECHAUN_QUESTS[quest_name[5]],
                      LEPRECHAUN_QUESTS[quest_name[6]])
    elif NPC.race == "Big Wolves":
        quest = Quest(BIG_WOLVES_QUESTS[quest_name[0]], BIG_WOLVES_QUESTS[quest_name[1]], BIG_WOLVES_QUESTS[quest_name[2]],
                      BIG_WOLVES_QUESTS[quest_name[3]], BIG_WOLVES_QUESTS[quest_name[4]], BIG_WOLVES_QUESTS[quest_name[5]],
                      BIG_WOLVES_QUESTS[quest_name[6]])

    else:
        quest = Quest(DRUID_QUESTS[quest_name[0]], DRUID_QUESTS[quest_name[1]],
                      DRUID_QUESTS[quest_name[2]], DRUID_QUESTS[quest_name[3]],
                      DRUID_QUESTS[quest_name[4]], DRUID_QUESTS[quest_name[5]],
                      DRUID_QUESTS[quest_name[6]])

    return quest

def test_quest(npc, hero):
    if npc.race == "DarkWizard":
        quest_name = "true_in_blood"
    elif npc.race == "Mermaid":
        quest_name = "find_pandas_ball"
    elif npc.race == "Druid":
        quest_name = "snake_sacrifice_berserker"
    elif npc.race == "Orc":
        quest_name = "clean_feet"
    else:
        quest_name = "0"

    if quest_name == "0":
        print("No quest")
    else:
        npc.give_quest(hero, quest_name)
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
