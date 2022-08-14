import os
import pygame

from game.npc.DarkWizard import DarkWizard
from game.npc.Druid import Druid
from game.npc.IceMonster import IceMonster
from game.npc.Mermaid import Mermaid
from game.npc.Orc import Orc

path = os.getcwd()
print(path)

MENU_WIDTH = 800
MENU_HEIGHT = 600

WIDTH_GAME = 1500
HEIGHT_GAME = 800
DIALOG_START = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
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

NPC_IMAGES = {
    'image_druid': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
    'image_dark_wizard': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wizard_dark.png")),
    'image_mermaid': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Mermaid.PNG")),
    'image_ice_monster': pygame.image.load(os.path.join(path, "resources/graphics/npc", "IceMonster.PNG")),
    'image_orc': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Orc.png"))
}
GUI_IMAGES = {
    'scroll_small': pygame.image.load(os.path.join(path, "resources/GUI", "scroll_small.png")),
    'scroll': pygame.image.load(os.path.join(path, "resources/GUI", "scroll.png"))
}

# preferences -> name : side, artifacts, quests, x, y
DRUIDS = {
    'Leaf': ["good", None, None, 700, 300]
}
DARK_WIZARDS = {
    'Sarus': ["evil", None, None, 400, 500]
}
ICE_MONSTERS = {
    'Icelius': ["evil", None, None, 200, 700]
}
MERMAIDS = {
    'Arielle': ["good", None, None, 400, 500]
}
ORCS = {
    'Stinker': ["evil", None, None, 800, 50]
}

# constants -> name, mana, life, images[]
NPCs = {
    'druid': {
        'class_name': Druid,
        'mana': 300,
        'life': 600,
        'images': [NPC_IMAGES['image_druid']],
        'dict': DRUIDS
    },
    'dark_wizard': {
        'class_name': DarkWizard,
        'mana': 200,
        'life': 400,
        'images': [NPC_IMAGES['image_dark_wizard']],
        'dict': DARK_WIZARDS
    },
    'ice_monster': {
        'class_name': IceMonster,
        'mana': 200,
        'life': 600,
        'images': [NPC_IMAGES['image_ice_monster']],
        'dict': ICE_MONSTERS
    },
    'mermaid': {
        'class_name': Mermaid,
        'mana': 300,
        'life': 100,
        'images': [NPC_IMAGES['image_mermaid']],
        'dict': MERMAIDS
    },
    'orc': {
        'class_name': Orc,
        'mana': 700,
        'life': 200,
        'images': [NPC_IMAGES['image_orc']],
        'dict': ORCS
    }
}



