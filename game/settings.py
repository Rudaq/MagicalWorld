import os
from pathlib import Path
import pygame as pygame

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent

MENU_WIDTH = 800
MENU_HEIGHT = 600

TILE_SIZE = 64
DEFAULT_IMAGE_SIZE = (50, 50)

WIDTH_GAME = 1500
HEIGHT_GAME = 800
DIALOG_START = 100
TILES_SIZE = 64
SCALE = 700/12928

HERO_SPEED = 25

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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/BarbarianBackSmall.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/barbarian_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/BarbarianLeft.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/BarbarianRight.png"))
    },
    'Dwarf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/dwarf_right.png"))
    },
    'Wizard': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/wizard_right.png"))
    },
    'Elf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/elf_right.png"))
    },
    'Faerie': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/faerie_right.png"))
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
    'sword': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "sword.PNG")),
    'fury': pygame.image.load(os.path.join(path, "resources/graphics/particles", "fury_2.PNG")),
    'fury_flames': [pygame.image.load(os.path.join(path, "resources/graphics/particles", "flame_1.PNG")),
                    pygame.image.load(os.path.join(path, "resources/graphics/particles", "flame_2.PNG")),
                    pygame.image.load(os.path.join(path, "resources/graphics/particles", "flame_3.PNG")),
                    pygame.image.load(os.path.join(path, "resources/graphics/particles", "flame_4.PNG"))],
    'resistance': pygame.image.load(os.path.join(path, "resources/graphics/particles", "claws.PNG"))
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
    'new_task_scroll': pygame.image.load(os.path.join(path, "resources/GUI", "new_task_scroll.png")),
    'fight_button': pygame.image.load(os.path.join(path, "resources/GUI", "fight.png")),
    'talk_button': pygame.image.load(os.path.join(path, "resources/GUI", "talk.png")),
    'small_chest': pygame.image.load(os.path.join(path, "resources/GUI", "chest_small.png")),
    'small_chest_opened': pygame.image.load(os.path.join(path, "resources/GUI", "small_chest_opened.png")),
    'big_chest': pygame.image.load(os.path.join(path, "resources/GUI", "chest_big.png")),
    'table': pygame.image.load(os.path.join(path, "resources/GUI", "table.png")),
    'map2': pygame.image.load(os.path.join(path, "resources/GUI", "map2.png")),
    'title': pygame.image.load(os.path.join(path, "resources/GUI", "AdventuresInTheRealm.png")),
    'start': pygame.image.load(os.path.join(path, "resources/GUI", "Start.png")),
    'how_to': pygame.image.load(os.path.join(path, "resources/GUI", "how_to_play.png")),
    'back_to': pygame.image.load(os.path.join(path, "resources/GUI", "back_white.png")),
    'quit': pygame.image.load(os.path.join(path, "resources/GUI", "Quit.png")),
    'next': pygame.image.load(os.path.join(path, "resources/GUI", "Next.png")),
    'selection': pygame.image.load(os.path.join(path, "resources/GUI", "CharacterSelection.png")),
    'swords':  pygame.image.load(os.path.join(path, "resources/GUI", "swords.png")),
    'map_icon': pygame.image.load(os.path.join(path, "resources/GUI", "mapIcon.png"))

}

MAP_IMAGES = {
    # 'ground_surf': pygame.image.load(os.path.join(path, "resources/graphics/tilemap", "floor.png")),
    'bamboo_tree': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "bamboo_tree.png")),
    'bamboo_tree_ball': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "bamboo_tree_ball.png")),
    'rainbow': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "rainbow.png")),
    'rainbow_small': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "rainbow_part.png")),
    'paper': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "paper.png")),
    'big_tree': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "big_tree.png")),
    'big_tree_flower': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "big_tree_flower.png")),
    'dig_ground': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "ground.png")),
    'pot': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "pot_of_gold.png"))

}
