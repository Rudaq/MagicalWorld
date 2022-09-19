import os
from pathlib import Path
import pygame as pygame

from game.quest_settings import DRUID_QUESTS
from npc.DarkWizard import DarkWizard
from npc.Druid import Druid
from npc.IceMonster import IceMonster
from npc.Mermaid import Mermaid
from npc.Orc import Orc
from os.path import dirname, realpath, join

current = os.path.dirname(os.path.realpath(__file__))
print("Current Directory", current)
path = Path(__file__).resolve().parent.parent
print(path)

MENU_WIDTH = 800
MENU_HEIGHT = 600

WIDTH_GAME = 1500
HEIGHT_GAME = 800
DIALOG_START = 100
TILES_SIZE = 64

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (24, 165, 88)
LIGHT_GREEN = (127, 255, 0)
YELLOW = (255, 234, 0)
HUD_YELLOW = (245, 245, 220)
ALMOND = (234, 221, 202)
CORAL = (248, 131, 121)

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SIGNS = [".", ",", "/", "!", ":", ";", "'", "-"]
LETTERS_NUMBERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9']

HERO_ANIMATIONS = {
    'Barbarian': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/barbarian_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/barbarian_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/barbarian_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/barbarian_small.png"))
    },
    'Dwarf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_small.png"))
    },
    'Wizard': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_small.png"))
    },
    'Elf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_small.png"))
    },
    'Faerie': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_small.png"))
    }
}

ELF_SPELLS = {
    'earth': pygame.image.load(os.path.join(path, "resources/graphics/particles", "earth.PNG")),
    'healing': pygame.image.load(os.path.join(path, "resources/graphics/particles", "healing_spell.PNG")),
    'arrow': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "arrow.PNG"))
}
FAERIE_SPELLS = {
    'fire': pygame.image.load(os.path.join(path, "resources/graphics/particles", "fire.PNG")),
    'flower': pygame.image.load(os.path.join(path, "resources/graphics/particles", "flowers.PNG")),
    'thrown': pygame.image.load(os.path.join(path, "resources/graphics/particles", "throw.PNG"))
}

BARBARIAN_ACTIONS = {
    'sword': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "sword.PNG"))
}

DWARVES_ACTIONS = {
    'braids': pygame.image.load(os.path.join(path, "resources/graphics/particles", "braids.PNG")),
    'axe': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "axe.PNG")),
    'sleep': pygame.image.load(os.path.join(path, "resources/graphics/particles", "sleep.PNG"))
}

WIZARD_SPELLS = {
    'wind': pygame.image.load(os.path.join(path, "resources/graphics/particles", "wind.PNG")),
    'magic_ball': pygame.image.load(os.path.join(path, "resources/graphics/particles", "magic_ball.PNG")),
    'healing': pygame.image.load(os.path.join(path, "resources/graphics/particles", "healing_spell.PNG")),
    'sparks': pygame.image.load(os.path.join(path, "resources/graphics/particles", "special_sparks.PNG"))
}

GUI_IMAGES = {
    'scroll_small': pygame.image.load(os.path.join(path, "resources/GUI", "scroll_small.png")),
    'scroll': pygame.image.load(os.path.join(path, "resources/GUI", "scroll.png")),
    'fight_button': pygame.image.load(os.path.join(path, "resources/GUI", "fight.png")),
    'talk_button': pygame.image.load(os.path.join(path, "resources/GUI", "talk.png")),
    'small_chest': pygame.image.load(os.path.join(path, "resources/GUI", "chest_small.png")),
    'small_chest_opened': pygame.image.load(os.path.join(path, "resources/GUI", "small_chest_opened.png")),
    'big_chest': pygame.image.load(os.path.join(path, "resources/GUI", "chest_big.png")),
    'swords':  pygame.image.load(os.path.join(path, "resources/GUI", "swords.png"))

}

MAP_IMAGES = {
    'ground_surf': pygame.image.load(os.path.join(path, "resources/graphics/tilemap", "floor.png"))
}
