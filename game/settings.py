import os
from pathlib import Path
import pygame as pygame
from shapely.geometry import Polygon

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent

MENU_WIDTH = 800
MENU_HEIGHT = 600

TILE_SIZE = 64
DEFAULT_IMAGE_SIZE = (50, 50)

WIDTH_GAME = 1200
HEIGHT_GAME = 600
DIALOG_START = 100
TILES_SIZE = 64
SCALE = 700 / 12928

SEA = pygame.image.load(os.path.join(path, "resources/graphics/tilemap/ocean.png"))

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

# Biomes surfaces
FrozenEmpireSurface = Polygon([(50, 200), (150, 1900), (800, 2100), (1500, 2250), (3250, 2250),
                               (3350, 1800), (3450, 1300), (3300, 850), (3400, 200)])
EnchantedSurface = Polygon([(750, 2000), (750, 2100), (1000, 2350), (1450, 2350), (1750, 2450),
                            (2500, 2350), (3300, 2600), (3350, 3700), (3350, 4150), (2950, 4600),
                            (2500, 4800), (1250, 4800), (800, 4750), (100, 4500)])
LoveyDoveySurface = Polygon([(100, 4600), (450, 4750), (750, 4800), (1150, 4850), (1150, 4850), (1500, 4870),
                             (1900, 4870), (2500, 4900), (3000, 4650), (3400, 4350), (3600, 4900),
                             (3750, 5400), (3750, 5700), (3900, 5700), (3900, 5700), (3900, 5900),
                             (3050, 6600), (3050, 6650), (1350, 6650), (600, 6550), (100, 6550)])
DesolationSurface = Polygon([(3400, 200), (3450, 900), (3500, 1200), (3450, 1650), (3350, 2350),
                             (3750, 1950), (4150, 2050), (4600, 2050), (4850, 1950), (5250, 1900),
                             (5700, 1800), (6150, 1800), (6650, 1850), (6700, 1550), (6820, 1100),
                             (6820, 650), (7000, 200)])
BushSurface = Polygon([(3450, 4250), (3500, 4300), (3700, 4300), (3800, 4375), (4150, 4375), (4350, 4350),
                       (4450, 4325), (4850, 4325), (5100, 4350), (5250, 4300), (5500, 4200), (6000, 3900),
                       (6250, 3900), (6450, 3870), (6950, 3870), (7300, 3900), (7400, 3850), (7500, 3700),
                       (7600, 3650), (7650, 3600), (7650, 3500), (7750, 3500), (7750, 3400), (8000, 2900),
                       (8000, 2600), (8000, 2450), (7500, 2250), (7450, 2200), (7250, 2150), (7150, 2100),
                       (7100, 2050), (6650, 2000), (5950, 1850), (5750, 1850), (5250, 2000), (4650, 2100),
                       (4150, 2100), (3850, 2050), (3400, 2450), (3350, 2550), (3350, 2950), (3400, 3600),
                       (3400, 3700), (3400, 4150)])
MedievilleSurface = Polygon([(8150, 2350), (8050, 2650), (8050, 2950), (7850, 3400), (7800, 3450), (7700, 3650),
                             (7700, 3650), (7650, 3650), (7600, 3700), (7500, 4000), (7700, 4200), (7800, 4250),
                             (7850, 4300), (7900, 4300), (8050, 4400), (8250, 4500), (9000, 4650), (9550, 4650),
                             (10050, 4550), (10700, 4500), (10900, 4400), (11050, 4400), (11050, 4300), (11200, 4300),
                             (11200, 4300), (11200, 4250), (11250, 4250), (11350, 4150), (11600, 3900), (11600, 3700),
                             (11350, 3450), (11250, 3250), (11200, 3100), (11100, 3050), (11100, 2900), (11050, 2850),
                             (11000, 2900), (11050, 2850), (11000, 2800), (10950, 2650), (10900, 2450),
                             (10850, 2350), (10650, 1850), (10500, 1350), (10000, 1500), (9800, 1700),
                             (9400, 1950), (8950, 2000), (8500, 2200), (8100, 2350), (8000, 2950)])
DrearyForestSurface = Polygon([(3500, 4400), (3650, 4750), (3770, 5200), (3800, 5400), (3800, 5640),
                               (3950, 5650), (3950, 5650), (3950, 5650), (3950, 5900), (4000, 5900),
                               (4050, 6450), (5400, 6450), (5650, 6100), (5850, 5900), (5900, 5850),
                               (5950, 5730), (5910, 5770), (6000, 5730), (6050, 5650), (6100, 5600), (7100, 4550),
                               (7200, 4500), (7250, 4450), (7300, 4400), (7350, 4350), (7350, 4300),
                               (7300, 3950), (6950, 3900), (6450, 3900), (6300, 3950), (6000, 4050),
                               (5500, 4350), (5200, 4400), (4850, 4400), (4850, 4350),
                               (4400, 4350), (4350, 4400), (4150, 4400), (3800, 4400)])
SpecularLakesSurface = Polygon([(7400, 4100), (7350, 4450), (7250, 4500), (7150, 4600), (6100, 5100),
                                (5800, 5950), (5500, 5950), (5500, 6450), (6000, 5800), (6000, 6600), (7800, 6600),
                                (11350, 5900), (12100, 5000), (11700, 4650), (11500, 4500), (11350, 4200),
                                (10900, 4500), (9850, 4650), (8950, 4650), (7950, 4400), (7700, 4350)])
CoastSurface = Polygon([(10350, 200), (10400, 450), (10450, 500), (10450, 500), (10450, 500), (10450, 800),
                        (10500, 1350), (10750, 1800), (10950, 2400), (11000, 2600), (11050, 2800),
                        (11150, 2850), (11150, 3050), (11300, 3100), (11650, 3650), (11700, 3850),
                        (11450, 4350), (11550, 4500), (11650, 2550), (11750, 4650), (12150, 4950),
                        (12850, 4650), (12950, 200)])
SwampSurface = Polygon([(7100, 200), (6870, 650), (6870, 1150), (6800, 1650), (6800, 1900), (7150, 2000),
                        (7200, 2100), (7320, 2100), (7320, 2150), (7500, 2150), (7500, 2250), (7900, 2250),
                        (8050, 2200), (8450, 2050), (8550, 2100), (8650, 2100), (8650, 2020), (8800, 2020),
                        (8850, 1950), (9000, 1950), (9200, 1900), (9600, 1750), (9800, 1600), (9850, 1550),
                        (9900, 1550), (9950, 1500), (10000, 1450), (10500, 1200), (10450, 850), (10400, 800),
                        (10400, 500), (10250, 450), (10250, 200)])

# mini map biomes surfaces
MiniFrozenEmpire = Polygon([(24, 111), (24, 200), (82, 219), (191, 223), (201, 111)])
MiniEnchantedForest = Polygon([(23, 208), (25, 342), (110, 358), (198, 332), (194, 235), (26, 207)])
MiniLoveyDoveyLand = Polygon([(29, 361), (26, 524), (141, 493), (231, 450), (201, 337), (158, 366), (28, 352)])
MiniDrearyForest = Polygon([(218, 346), (242, 445), (307, 445), (409, 322), (341, 324), (290, 343), (214, 342)])
MiniPrimevalBush = Polygon([(204, 234), (206, 327), (304, 330), (362, 309), (416, 303), (450, 232), (385, 207),
                            (278, 213), (239, 216), (227, 211)])
MiniDesolationOfAbomination = Polygon(
    [(206, 114), (208, 186), (201, 225), (227, 201), (331, 195), (377, 196), (389, 112)])
MiniMistySwamp = Polygon([(404, 114), (395, 137), (387, 195), (451, 220), (585, 164), (570, 112)])
MiniMedieville = Polygon(
    [(461, 233), (451, 277), (428, 314), (488, 346), (617, 332), (644, 305), (583, 176), (529, 208)])
MiniStormyPier = Polygon([(586, 114), (653, 302), (646, 338), (682, 362), (715, 330), (715, 116)])
MiniSpecularLakes = Polygon([(427, 336), (325, 447), (504, 439), (671, 372), (636, 336), (532, 357), (459, 348)])

# buttons for ending the game
continue_button = Polygon([(558, 539), (557, 609), (722, 609), (722, 539)])
quit_button = Polygon([(769, 539), (769, 609), (931, 609), (931, 539)])

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
    'swords': pygame.image.load(os.path.join(path, "resources/GUI", "swords.png")),
    'map_icon': pygame.image.load(os.path.join(path, "resources/GUI", "mapIcon.png")),
    'frozen_empire': pygame.image.load(os.path.join(path, "resources/GUI", "FrozenEmpire.png")),
    'enchanted_forest': pygame.image.load(os.path.join(path, "resources/GUI", "EnchantedForest.png")),
    'lovey_dovey_land': pygame.image.load(os.path.join(path, "resources/GUI", "LoveyDoveyLand.png")),
    'primeval_bush': pygame.image.load(os.path.join(path, "resources/GUI", "PrimevalBush.png")),
    'desolation_of_abomination': pygame.image.load(os.path.join(path, "resources/GUI", "DesolationOfAbomination.png")),
    'dreary_forest': pygame.image.load(os.path.join(path, "resources/GUI", "DrearyForest.png")),
    'stormy_pier': pygame.image.load(os.path.join(path, "resources/GUI", "StormyPier.png")),
    'specular_lakes': pygame.image.load(os.path.join(path, "resources/GUI", "SpecularLakes.png")),
    'medieville': pygame.image.load(os.path.join(path, "resources/GUI", "Medieville.png")),
    'misty_swamp': pygame.image.load(os.path.join(path, "resources/GUI", "MistySwamp.png")),
    'end_frame': pygame.image.load(os.path.join(path, "resources/GUI", "endFrame.png")),
    'name': pygame.image.load(os.path.join(path, "resources/GUI", "name.png")),
    'side': pygame.image.load(os.path.join(path, "resources/GUI", "side.png")),
    'type': pygame.image.load(os.path.join(path, "resources/GUI", "type.png"))
    # 'cross': pygame.image.load(os.path.join(path, "resources/GUI", "crossButton.png"))
}

MAP_IMAGES = {
    'bamboo_tree': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "bamboo_tree.png")),
    'bamboo_tree_ball': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "bamboo_tree_ball.png")),
    'rainbow': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "rainbow.png")),
    'rainbow_small': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "rainbow_part.png")),
    'paper': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "paper.png")),
    'big_tree': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "big_tree.png")),
    'big_tree_flower': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "big_tree_flower.png")),
    'dig_ground': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "ground.png")),
    'pot': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "pot_of_gold.png")),
    'leaves': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "leaf.png")),
    'stick': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "Stick.png")),
    'enchanted_tree': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "EnchantedTree.png")),
    'mud': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "Mud.png")),
    'spider_web': pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "spiderweb.png"))
}

END_TEXT = {
    'Barbarian': 'Congratulations +name+! Your eagerness to complete all of the tasks that were a part of your trial '
                 'was outstanding. The adrenaline running through your veins could have been sensed throughout the '
                 'whole game. Your adventures in the Realm may be coming to an end but do not worry... You can still '
                 'wander through the lands and explore! What do you think?',
    'Dwarf': 'Congratulations +name+! You have solved one of the greatest mysteries in our Realm and your axe is '
             'dripping blood of your dead enemies! You are one, proud dwarf... Your adventures in the Realm may be '
             'coming to an end but do not worry... You can still wander through the lands and explore! What do you '
             'think?',
    'Elf': 'Congratulations +name+! It has been a pleasure seeing you saving the realm from being destroyed by the '
           'gods and spirits. Runes, spirits, powers... Outstanding. Other elves would be proud. Your adventures '
           'in the Realm may be coming to an end but do not worry... You can still wander through the lands and '
           'explore! What do you think?',
    'Faerie': 'Congratulations +name+! You have used the power of Magical Flower in the best possible way! Another '
              'mystery of the Realm solved... A reason to certainly be proud of. Your adventures in the Realm may be '
              'coming to an end but do not worry... You can still wander through the lands and explore! What do you '
              'think?',
    'Wizard': 'Congratulations +name+! What a scientific and magical ride it was. You have broadened wizards '
              'knowledge and power, thus this grasp will be mentioned for a long time. The Realm will be way too '
              'tranquil after you leave... Your adventures may be approaching the end but you can still explore and '
              'wander through the lands. What do you think? '
}
