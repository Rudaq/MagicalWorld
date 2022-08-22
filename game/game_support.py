import random
import pygame

from game.hero.Barbarian import Barbarian
from game.hero.Dwarf import Dwarf
from game.hero.Elf import Elf
from game.hero.Faerie import Faerie
from game.hero.Wizard import Wizard
from settings import NPCs, HERO_ANIMATIONS, GUI_IMAGES
from game.settings import BLACK
from game.dialog_support import talk
from game.fight_support import fight


class NPCTypeNotExistException(Exception):
    pass


def create_npc(npc_race, sprite_arrays, sprite_groups, name=None):
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
                                              y=parameters[4])

        for array in sprite_arrays:
            array.append(entity)
        for group in sprite_groups:
            group.add(entity)
    else:
        raise NPCTypeNotExistException

    return entity


def create_character(chosen_name, chosen_type, chosen_side):
    if chosen_type == "Elf":
        hero = Elf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Elf'], None)
    elif chosen_type == "Faerie":
        hero = Faerie(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Faerie'], None)
    elif chosen_type == "Wizard":
        hero = Wizard(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Wizard'], None)
    elif chosen_type == "Dwarf":
        hero = Dwarf(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Dwarf'], None)
    else:
        hero = Barbarian(chosen_name, chosen_side, 100, 100, HERO_ANIMATIONS['Barbarian'], None)

    return hero


def hero_in_dialog_or_talk(s, screen, fight_button, talk_button, chosen_npc, hero):
    s.fill(BLACK)
    s.set_alpha(192)

    buttons = pygame.sprite.Group()
    fight_button.rect.x = chosen_npc.rect.x - 40
    fight_button.rect.y = chosen_npc.rect.y - 70

    talk_button.rect.x = chosen_npc.rect.x + 40
    talk_button.rect.y = chosen_npc.rect.y - 70
    buttons.add(fight_button)
    buttons.add(talk_button)

    if talk_button.draw():
        talk(hero, chosen_npc, talk_button, fight_button)

    if fight_button.draw():
        fight(hero, chosen_npc, fight_button, talk_button)

    buttons.update()
    buttons.draw(screen)
