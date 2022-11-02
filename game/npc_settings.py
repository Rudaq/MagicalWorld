import os
import pygame
from pathlib import Path

from npc.DarkWizard import DarkWizard
from npc.Druid import Druid
from npc.IceMonster import IceMonster
from npc.Mermaid import Mermaid
from npc.Orc import Orc
from npc.Elf import Elf
from npc.Treant import Treant
from npc.Donkey import Donkey
from npc.BlindRat import BlindRat
from npc.Smith import Smith
from npc.Farmer import Farmer
from npc.BigRaven import BigRaven
from npc.EscapingVegetable import EscapingVegetable
from npc.WheatMonster import WheatMonster
from npc.BigWolf import BigWolf
from npc.FriendlySnowman import FriendlySnowman
from npc.Crab import Crab
from npc.BigFish import BigFish
from npc.Panda import Panda
from npc.Lemur import Lemur
from npc.BigMonke import BigMonke
from npc.Unicorn import Unicorn
from npc.Faerie import Faerie
from npc.Leprechaun import Leprechaun
from npc.Amazon import Amazon
from npc.Snake import Snake
from npc.Tiger import Tiger
from npc.Spider import Spider
from npc.Vampire import Vampire
from npc.DarkElf import DarkElf
from npc.Dragon import Dragon
from npc.FireElemental import FireElemental
from npc.EarthElemental import EarthElemental


current = os.path.dirname(os.path.realpath(__file__))
print("Current Directory", current)
path = Path(__file__).resolve().parent.parent
print(path)

NPC_IMAGES = {
    'image_druid': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "druid_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "druid_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "druid_right.png"))
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "ice_monster_back.PNG")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "IceMonster.PNG")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "ice_monster_left.PNG")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "ice_monster_right.PNG"))
    },
    'image_orc': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "orc_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Orc.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "orc_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "orc_right.png"))
    },
    'image_smith': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "smith_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "smith_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "smith_right.png"))
    },
    'image_blind_rat': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BlindRat.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BlindRat.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BlindRat.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BlindRat.png"))
    },
    'image_escaping_vegetable': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Carrot.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Carrot.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Carrot.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Carrot.png"))
    },
    'image_crab': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png"))
    },
    'image_dark_elf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "dark_elf_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "dark_elf_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "dark_elf_right.png"))
    },
    'image_donkey': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "donkey_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "donkey_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "donkey_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "donkey_right.png"))
    },
    'image_dragon': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png"))
    },
    'image_earth_elemental': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "earth_elemental_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "earth_elemental_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "earth_elemental_right.png"))
    },
    'image_faerie': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "faeries_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Faeries.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "faeries_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "faeries_right.png"))
    },
    'image_farmer': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "farmer_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "farmer_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "farmer_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "farmer_right.png"))
    },
    'image_fire_elemental': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "fire_elemental_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "fire_elemental_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "fire_elemental_right.png"))
    },
    'image_big_monke': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "gorilla_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "gorilla_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "gorilla_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png"))
    },
    'image_leprechaun': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "leprechaun_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "leprechaun_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "leprechaun_right.png"))
    },
    'image_panda': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "panda_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "panda_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "panda_right.png"))
    },
    'image_snake': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snake_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snake_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snake_right.png"))
    },
    'image_spider': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png"))
    },
    'image_tiger': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "tiger_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "tiger_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "tiger_right.png"))
    },
    'image_treant': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "treant_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "treant_left2.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "treant_right2.png"))
    },
    'image_unicorn': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "unicorn_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "unicorn_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "unicorn_right.png"))
    },
    'image_vampire': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "vampire_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "vampire_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "vampire_right.png"))
    },
    'image_wheat_monster': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "WheatMonster.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "WheatMonster.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "WheatMonster.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "WheatMonster.png"))
    },
    'image_wolf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wolf.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wolf.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wolf.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Wolf.png"))
    },
    'image_elf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Elf.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Elf.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Elf.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Elf.png"))
    },
    'image_lemur': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "lemur_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "lemur_front.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "lemur_right.png"))
    },
    'image_big_raven': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png"))
    },
    'image_amazon': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "amazon_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "amazon_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "amazon_right.png"))
    },
    'image_big_fish': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png"))
    },
    'image_snowman': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_left.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_right.png"))
    },

    'image_snowman_nose': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_back.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_nose.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_left_nose.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "snowman_right_nose.png"))
    }
}

NPC_FIGHTS = {
    'ice': pygame.image.load(os.path.join(path, "resources/graphics/particles", "small_cube.PNG"))
}

# preferences -> name : side, artifacts, quests, x, y
# enchanted forest:
# X: 150 - 3350
# Y: 2300 - 4500
DRUIDS = {
    'Leaf': ["good", None, None, 1670, 3500]
}
ELVES = {
    'Manance': ["good", None, None, 2920, 2900]
}
TREANTS = {
    'Oak': ["good", None, None, 280, 4550],
    'Sequoia': ["good", None, None, 1770, 3900],
    'Bambus': ["good", None, None, 1170, 3520],
    'Maple': ["good", None, None, 2500, 2910]
}
# desolation of abdomination:
# X: 3450 - 6600
# Y: 250 - 1850

DRAGONS = {
    'Drogon': ["evil", None, None, 5700, 1000]
}
FIRE_ELEMENTALS = {
    'Firenzo': ["evil", None, None, 4400, 750],
    'Fireball': ["evil", None, None, 4950, 1350],
    'Damian': ["evil", None, None, 3705, 530]
}
EARTH_ELEMENTALS = {
    'Earthenzo': ["evil", None, None, 4600, 900],
    'Patrick': ["evil", None, None, 5820, 1500]
}
# FROZEN EMPIRE
# X: 50 - 3350
# Y: 200 - 2150
ICE_MONSTERS = {
    'Icelius': ["evil", None, None, 2300, 1650]
}
BIG_WOLVES = {
    'Furry': ["evil", None, None, 1170, 600],
    'Murry': ["evil", None, None, 290, 1600],
    'Durry': ["evil", None, None, 2270, 1500],
    'Bamburry': ["evil", None, None, 2870, 1200]
}
FRIENDLY_SNOWMEN = {
    'Olaf': ["good", None, None, 1100, 280],
    'Bodak': ["good", None, None, 2300, 990],
    'Benjamin': ["good", None, None, 250, 1480],
    'Dinerdo': ["good", None, None, 1200, 1880]
}
# LAKE
# X: 7400 - 11600
# Y: 4250 - 5600
MERMAIDS = {
    'Arielle': ["good", None, None, 10030, 9720]
}
CRABS = {
    'Craberus': ["good", None, None, 10700, 10400],
    'Crabemus': ["good", None, None, 8900, 10400],
    'Craperus': ["good", None, None, 9100, 10400]
}
BIG_FISHES = {
    'Gul': ["evil", None, None, 8930, 4860],
    'Bul': ["evil", None, None, 9930, 4660],
    'Dul': ["evil", None, None, 8230, 5160]
}
# SWAMP:
# X: 7100 - 10350
# Y: 250 - 1200
ORCS = {
    'Stinker': ["evil", None, None, 8300, 950]
}
DONKEYS = {
    'Ponkey': ["good", None, None, 8300, 320],
    'Conkey': ["good", None, None, 10000, 1000],
    'Donkey': ["good", None, None, 9830, 975],
}
BLIND_RATS = {
    'Mousey': ["evil", None, None, 9250, 390],
    'Wousey': ["evil", None, None, 8250, 1000],
    'Busy': ["evil", None, None, 7700, 870]
}
# MEDIEVILLE:
# X: 8400 - 11050
# Y: 2250 - 4350
SMITHS = {
    'Gavin': ["good", None, None, 8810, 2600]
}
FARMERS = {
    'Harwin': ["good", None, None, 9700, 3500]
}
BIG_RAVENS = {
    'Feather': ["evil", None, None, 10200, 3600],
    'Crow': ["evil", None, None, 8850, 2920],
    'Nights': ["evil", None, None, 8900, 3180],
}
ESCAPING_VEGETABLES = {
    'Parsley': ["evil", None, None, 10600, 4000],
    'Sage': ["evil", None, None, 9500, 3700],
    'Rosemary': ["evil", None, None, 10000, 2950],
    'Thyme': ["evil", None, None, 10200, 3100]
}
WHEAT_MONSTERS = {
    'Wheater': ["evil", None, None, 9150, 2750],
    'Skipper': ["evil", None, None, 9250, 3700],
    'Daphne': ["evil", None, None, 9400, 2950]
}
# COAST:
# X: 10350 - 12600
# Y: 250 - 4600
PANDAS = {
    'Wanda': ["good", None, None, 11400, 2550],
    'Banda': ["good", None, None, 12400, 900],
    'Bamboo': ["good", None, None, 10790, 1250]
}
LEMURS = {
    'Julian': ["good", None, None, 11550, 4340],
    'Moris': ["good", None, None, 12010, 2000],
}
BIG_MONKES = {
    'Gorilla': ["evil", None, None, 9700, 3500]
}
# LOVEY DOVEY:
# X: 150 - 3900
# Y: 4850 - 6400
UNICORNS = {
    'Pony': ["good", None, None, 400, 8600]
}
FAERIES = {
    'Lovely': ["good", None, None, 800, 6050],
    'Dovey': ["good", None, None, 2500, 5900],
    'Priscilla': ["good", None, None, 1290, 5600]
}
LEPRECHAUNS = {
    'Goldey': ["evil", None, None, 3250, 5840]
}
# BUSH:
# X: 3450 - 7400
# Y: 2400 - 3800
AMAZONS = {
    'Wilderina': ["good", None, None, 3800, 2700]
}
SNAKES = {
    'Anaconde': ["evil", None, None, 5600, 3300],
    'Bamboo': ["evil", None, None, 6200, 3150],
    'Snack': ["evil", None, None, 5750, 2750]
}
TIGERS = {
    'Lionel': ["evil", None, None, 4300, 2800]
}
# DREARY:
# X: 3600 - 5400 (im wyzej tym dalej)
# Y: 4500 - 6450

DARK_WIZARDS = {
    'Sarus': ["evil", None, None, 5300, 5700]
}

SPIDERS = {
    'Venom': ["evil", None, None, 4500, 5600],
    'Bradley': ["evil", None, None, 5570, 5970],
    'Duncan': ["evil", None, None, 3900, 4920]
}
VAMPIRES = {
    'Bloody': ["evil", None, None, 4800, 6080]
}
DARK_ELVES = {
    'Baldwin': ["evil", None, None, 5000, 5050]
}

RANDOM_ANSWERS = {
    1: "Crr..",
    2: "Ugh..",
    3: "Arr..",
    4: "Grrr..",
    5: "Ohhh.."
}

# constants -> name, mana, life, images[]
NPCs = {
    'druid': {
        'class_name': Druid,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_druid'],
        'dict': DRUIDS
    },
    'dark_wizard': {
        'class_name': DarkWizard,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_dark_wizard'],
        'dict': DARK_WIZARDS
    },
    'ice_monster': {
        'class_name': IceMonster,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_ice_monster'],
        'dict': ICE_MONSTERS
    },
    'mermaid': {
        'class_name': Mermaid,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_mermaid'],
        'dict': MERMAIDS
    },
    'orc': {
        'class_name': Orc,
        'mana': 700,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_orc'],
        'dict': ORCS
    },
    'elf': {
        'class_name': Elf,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_elf'],
        'dict': ELVES
    },
    'treant': {
        'class_name': Treant,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_treant'],
        'dict': TREANTS
    },
    'donkey': {
        'class_name': Donkey,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_donkey'],
        'dict': DONKEYS
    },
    'blind_rat': {
        'class_name': BlindRat,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_blind_rat'],
        'dict': BLIND_RATS
    },
    'smith': {
        'class_name': Smith,
        'mana': 700,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_smith'],
        'dict': SMITHS
    },
    'farmer': {
        'class_name': Farmer,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_farmer'],
        'dict': FARMERS
    },
    'big_raven': {
        'class_name': BigRaven,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_big_raven'],
        'dict': BIG_RAVENS
    },
    'escaping_vegetable': {
        'class_name': EscapingVegetable,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_escaping_vegetable'],
        'dict': ESCAPING_VEGETABLES
    },
    'wheat_monster': {
        'class_name': WheatMonster,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_wheat_monster'],
        'dict': WHEAT_MONSTERS
    },
    'friendly_snowman': {
        'class_name': FriendlySnowman,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_snowman'],
        'dict': FRIENDLY_SNOWMEN
    },
    'crab': {
        'class_name': Crab,
        'mana': 700,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_crab'],
        'dict': CRABS
    },
    'big_fish': {
        'class_name': BigFish,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_big_fish'],
        'dict': BIG_FISHES
    },
    'panda': {
        'class_name': Panda,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_panda'],
        'dict': PANDAS
    },
    'lemur': {
        'class_name': Lemur,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_lemur'],
        'dict': LEMURS
    },
    'big_monke': {
        'class_name': BigMonke,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_big_monke'],
        'dict': BIG_MONKES
    },
    'unicorn': {
        'class_name': Unicorn,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_unicorn'],
        'dict': UNICORNS
    },
    'faerie': {
        'class_name': Faerie,
        'mana': 700,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_faerie'],
        'dict': FAERIES
    },
    'leprechaun': {
        'class_name': Leprechaun,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_leprechaun'],
        'dict': LEPRECHAUNS
    },
    'amazon': {
        'class_name': Amazon,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_amazon'],
        'dict': AMAZONS
    },
    'snake': {
        'class_name': Snake,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_snake'],
        'dict': SNAKES
    },
    'tiger': {
        'class_name': Tiger,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_tiger'],
        'dict': TIGERS
    },
    'spider': {
        'class_name': Spider,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_spider'],
        'dict': SPIDERS
    },
    'vampire': {
        'class_name': Vampire,
        'mana': 700,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_vampire'],
        'dict': VAMPIRES
    },
    'dark_elf': {
        'class_name': DarkElf,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_dark_elf'],
        'dict': DARK_ELVES
    },
    'dragon': {
        'class_name': Dragon,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_dragon'],
        'dict': DRAGONS
    },
    'fire_elemental': {
        'class_name': FireElemental,
        'mana': 200,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_fire_elemental'],
        'dict': FIRE_ELEMENTALS
    },
    'earth_elemental': {
        'class_name': EarthElemental,
        'mana': 300,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_earth_elemental'],
        'dict': EARTH_ELEMENTALS
    },
    'big_wolf': {
        'class_name': BigWolf,
        'mana': 700,
        'life': 100,
        'inflate': (-10, -10),
        'images': NPC_IMAGES['image_wolf'],
        'dict': BIG_WOLVES
    }
}
