import os
import pygame
from pathlib import Path

from game.quest_settings import DRUID_QUESTS
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Druid.png"))
    },
    'image_dark_wizard': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkWizard.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkWizard.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkWizard.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkWizard.png"))
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
    },
    'image_amazon': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png"))
    },
    'image_big_fish': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png"))
    },
    'image_smith': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png"))
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png"))
    },
    'image_donkey': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png"))
    },
    'image_dragon': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png"))
    },
    'image_earth_elemental': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png"))
    },
    'image_faerie': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Faeries.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Faeries.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Faeries.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Faeries.png"))
    },
    'image_farmer': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png"))
    },
    'image_fire_elemental': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png"))
    },
    'image_big_monke': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png"))
    },
    'image_leprechaun': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png"))
    },
    'image_panda': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png"))
    },
    'image_snake': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png"))
    },
    'image_snowman': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png"))
    },
    'image_spider': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png"))
    },
    'image_tiger': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png"))
    },
    'image_treant': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png"))
    },
    'image_unicorn': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png"))
    },
    'image_vampire': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png"))
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png"))
    },
    'image_big_raven': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png"))
    },
    'image_amazon': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Amazon.png"))
    },
    'image_big_fish': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigFish.png"))
    },
    'image_smith': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Blacksmith.png"))
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "DarkElf.png"))
    },
    'image_donkey': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Donkey.png"))
    },
    'image_dragon': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Dragon.png"))
    },
    'image_earth_elemental': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "EarthElemental.png"))
    },
    # # which picture
    # 'image_faerie': {
    #     'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png")),
    #     'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png")),
    #     'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png")),
    #     'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Crab.png"))
    # },
    'image_farmer': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Farmer.png"))
    },
    'image_fire_elemental': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "FireElemental.png"))
    },
    'image_big_monke': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Gorilla.png"))
    },
    'image_leprechaun': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Leprechaun.png"))
    },
    'image_panda': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Panda.png"))
    },
    'image_snake': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snake.png"))
    },
    'image_snowman': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Snowman.png"))
    },
    'image_spider': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Spider.png"))
    },
    'image_tiger': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Tiger.png"))
    },
    'image_treant': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Treant.png"))
    },
    'image_unicorn': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Unicorn.png"))
    },
    'image_vampire': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Vampire.png"))
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "Lemur.png"))
    },
    'image_big_raven': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/npc", "BigRaven.png"))
    }
}

NPC_FIGHTS = {
    'ice': pygame.image.load(os.path.join(path, "resources/graphics/particles", "small_cube.PNG"))
}

# preferences -> name : side, artifacts, quests, x, y
# enchanted forest:
# x: 70 - 3870
# y: 3160 - 7100
DRUIDS = {
    'Leaf': ["good", None, None, 1670, 5700]
}
ELVES = {
    'Manance': ["good", None, None, 2920, 6800]
}
TREANTS = {
    'Oak': ["good", None, None, 170, 4550]
}
# desolation of abdomination:
# x: 3590 - 6710
# y: 140 - 1820
DARK_WIZARDS = {
    'Sarus': ["evil", None, None, 200, 400]
}
DRAGONS = {
    'Drogon': ["evil", None, None, 900, 800]
}
FIRE_ELEMENTALS = {
    'Firenzo': ["evil", None, None, 6100, 700]
}
EARTH_ELEMENTALS = {
    'Earthenzo': ["evil", None, None, 5200, 1000]
}
# FROZEN EMPIRE
# x: 70 - 3290
# y: 140 - 2960
ICE_MONSTERS = {
    'Icelius': ["evil", None, None, 2300, 1850]
}
BIG_WOLVES = {
    'Furry': ["evil", None, None, 120, 2500]
}
FRIENDLY_SNOWMEN = {
    'Olaf': ["good", None, None, 1200, 380]
}
# LAKE
# x: 9450 - 12850 (M:10050, BF: 9930)
# y: 7020 - 11000 (9720, 7360)
MERMAIDS = {
    'Arielle': ["good", None, None, 800, 700]
}
CRABS = {
    'Craberus': ["good", None, None, 11700, 10400]
}
BIG_FISHES = {
    'Gul': ["evil", None, None, 9930, 7360]
}
# SWAMP:
# x: 7070-10590
# y: 140-1900
ORCS = {
    'Stinker': ["evil", None, None, 8300, 950]
}

DONKEYS = {
    'Ponkey': ["good", None, None, 7900, 320]
}

BLIND_RATS = {
    'Mousey': ["evil", None, None, 9250, 1700]
}
# MEDIEVILLE:
# 8090 - 12850 (WM:8430 - 9350)
# 2400 - 6260 (WM:2760 - 3260)
SMITHS = {
    'Gavin': ["good", None, None, 700, 600]
}
FARMERS = {
    'Harwin': ["good", None, None, 700, 700]
}
BIG_RAVENS = {
    'Feather': ["evil", None, None, 700, 500]
}
ESCAPING_VEGETABLES = {
    'Parsley': ["evil", None, None, 10500, 3400]
}
WHEAT_MONSTERS = {
    'Wheater': ["evil", None, None, 9150, 2750]
}
# COAST:
# 10570 - 12850 (10730-12850)
# 140 - 4840 (140-4300)
PANDAS = {
    'Wanda': ["good", None, None, 11400, 2550]
}
LEMURS = {
    'Julian': ["good", None, None, 11510, 4340]
}
BIG_MONKES = {
    'Gorilla': ["evil", None, None, 850, 600]
}
# LOVEY DOVEY:
# 70 - 4890
# 7880 - 11000
UNICORNS = {
    'Pony': ["good", None, None, 200, 200]
}
FAERIES = {
    'Lovely': ["good", None, None, 300, 800]
}

LEPRECHAUNS = {
    'Goldey': ["evil", None, None, 4600, 9840]
}
# BUSH:
# x: 3470 - 5250 if higher ~ 7500
# y: 2900 - 6520
AMAZONS = {
    'Wilderina': ["good", None, None, 5900, 3750]
}
SNAKES = {
    'Anaconde': ["evil", None, None, 700, 900]
}
TIGERS = {
    'Lionel': ["evil", None, None, 700, 800]
}
# DREARY:
# x: 5690 - 9100
# y: 7720 - 11000
SPIDERS = {
    'Venom': ["evil", None, None, 600, 800]
}
VAMPIRES = {
    'Bloody': ["evil", None, None, 500, 400]
}
DARK_ELVES = {
    'Baldwin': ["evil", None, None, 500, 500]
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
        'dict': DRUIDS,
        # 'quests': DRUID_QUESTS
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
