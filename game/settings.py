import os
import pygame as pygame
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
LETTERS_NUMBERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9']

HERO_ANIMATIONS = {
    'Barbarian': {
        'up': pygame.image.load(r'resources/graphics/characters/barbarian.png'),
        'down': pygame.image.load(r'resources/graphics/characters/barbarian.png'),
        'left': pygame.image.load(r'resources/graphics/characters/barbarian.png'),
        'right': pygame.image.load(r'resources/graphics/characters/barbarian.png')
    },
    'Dwarf': {
        'up': pygame.image.load(r'resources/graphics/characters/Dwarf_small.png'),
        'down': pygame.image.load(r'resources/graphics/characters/Dwarf_small.png'),
        'left': pygame.image.load(r'resources/graphics/characters/Dwarf_small.png'),
        'right': pygame.image.load(r'resources/graphics/characters/Dwarf_small.png')
    },
    'Wizard': {
        'up': pygame.image.load(r'resources/graphics/characters/Wizard_small.png'),
        'down': pygame.image.load(r'resources/graphics/characters/Wizard_small.png'),
        'left': pygame.image.load(r'resources/graphics/characters/Wizard_small.png'),
        'right': pygame.image.load(r'resources/graphics/characters/Wizard_small.png')
    },
    'Elf': {
        'up': pygame.image.load(r'resources/graphics/characters/Elf_small.png'),
        'down': pygame.image.load(r'resources/graphics/characters/Elf_small.png'),
        'left': pygame.image.load(r'resources/graphics/characters/Elf_small.png'),
        'right': pygame.image.load(r'resources/graphics/characters/Elf_small.png')
    },
    'Faerie': {
        'up': pygame.image.load(r'resources/graphics/characters/Faerie_small.png'),
        'down': pygame.image.load(r'resources/graphics/characters/Faerie_small.png'),
        'left': pygame.image.load(r'resources/graphics/characters/Faerie_small.png'),
        'right': pygame.image.load(r'resources/graphics/characters/Faerie_small.png')
    }
}

ELF_SPELLS = {
    'earth': pygame.image.load(os.path.join(path, "resources/graphics/particles", "earth2.PNG")),
    'healing': pygame.image.load(os.path.join(path, "resources/graphics/particles", "healing_spell.PNG")),
    'arrow': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "arrow.PNG"))
}

NPC_IMAGES = {
    'image_druid': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png"))
    },
    'image_dark_wizard': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wizard_dark.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wizard_dark.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wizard_dark.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wizard_dark.png"))
    },
    'image_mermaid': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Mermaid.PNG")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Mermaid.PNG")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Mermaid.PNG")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Mermaid.PNG"))
    },
    'image_ice_monster': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "IceMonster.PNG")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "IceMonster.PNG")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "IceMonster.PNG")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "IceMonster.PNG"))
    },
    'image_orc': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Orc.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Orc.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Orc.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Orc.png"))
    }
}
GUI_IMAGES = {
    'scroll_small': pygame.image.load(os.path.join(path, "resources/GUI", "scroll_small.png")),
    'scroll': pygame.image.load(os.path.join(path, "resources/GUI", "scroll.png"))
}

# preferences -> name : side, artifacts, quests, x, y
DRUIDS = {
    'Leaf': ["good", None, None, 700, 300]
}
DRUID_QUESTS = {
    'quest1': ["bnlablabla"]
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
        'images': NPC_IMAGES['image_druid'],
        'dict': DRUIDS,
        'quests': DRUID_QUESTS
    },
    'dark_wizard': {
        'class_name': DarkWizard,
        'mana': 200,
        'life': 400,
        'images': NPC_IMAGES['image_dark_wizard'],
        'dict': DARK_WIZARDS
    },
    'ice_monster': {
        'class_name': IceMonster,
        'mana': 200,
        'life': 600,
        'images': NPC_IMAGES['image_ice_monster'],
        'dict': ICE_MONSTERS
    },
    'mermaid': {
        'class_name': Mermaid,
        'mana': 300,
        'life': 100,
        'images': NPC_IMAGES['image_mermaid'],
        'dict': MERMAIDS
    },
    'orc': {
        'class_name': Orc,
        'mana': 700,
        'life': 200,
        'images': NPC_IMAGES['image_orc'],
        'dict': ORCS
    }
}
