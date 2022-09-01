import os
from pathlib import Path
import pygame as pygame
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
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/Barbarian_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/Barbarian_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/Barbarian_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/Barbarian_small.png"))
    },
    'Dwarf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/Dwarf_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/Dwarf_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/Dwarf_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/Dwarf_small.png"))
    },
    'Wizard': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/Wizard_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/Wizard_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/Wizard_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/Wizard_small.png"))
    },
    'Elf': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/Elf_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/Elf_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/Elf_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/Elf_small.png"))
    },
    'Faerie': {
        'up': pygame.image.load(os.path.join(path, "resources/graphics/characters/Faerie_small.png")),
        'down': pygame.image.load(os.path.join(path, "resources/graphics/characters/Faerie_small.png")),
        'left': pygame.image.load(os.path.join(path, "resources/graphics/characters/Faerie_small.png")),
        'right': pygame.image.load(os.path.join(path, "resources/graphics/characters/Faerie_small.png"))
    }
}

ELF_SPELLS = {
    'earth': pygame.image.load(os.path.join(path, "resources/graphics/particles", "earth2.PNG")),
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
    'scroll': pygame.image.load(os.path.join(path, "resources/GUI", "scroll.png")),
    'fight_button': pygame.image.load(os.path.join(path, "resources/GUI", "fight.png")),
    'talk_button': pygame.image.load(os.path.join(path, "resources/GUI", "talk.png")),
    'small_chest': pygame.image.load(os.path.join(path, "resources/GUI", "chest_small.png")),
    'small_chest_opened': pygame.image.load(os.path.join(path, "resources/GUI", "small_chest_opened.png")),
    'big_chest': pygame.image.load(os.path.join(path, "resources/GUI", "chest_big.png")),
    'swords':  pygame.image.load(os.path.join(path, "resources/GUI", "swords.png"))

}

DWARVES_ACTIONS = {
    # TO DO DRAW NICER BRAIDS :(
    'braids': pygame.image.load(os.path.join(path, "resources/graphics/particles", "braids.PNG")),
    'axe': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "axe.PNG")),
    'axe_throw': pygame.image.load(os.path.join(path, "resources/graphics/weapon", "axe.PNG")),
    'sleep': pygame.image.load(os.path.join(path, "resources/graphics/particles", "sleep.PNG"))
}

WIZARD_SPELLS = {
    'wind': pygame.image.load(os.path.join(path, "resources/graphics/particles", "wind.PNG")),
    'magic_ball': pygame.image.load(os.path.join(path, "resources/graphics/particles", "magic_ball.PNG")),
    'healing': pygame.image.load(os.path.join(path, "resources/graphics/particles", "healing_spell.PNG")),
    'sparks': pygame.image.load(os.path.join(path, "resources/graphics/particles", "special_sparks.PNG"))
}

NPC_FIGHTS = {
    'ice': pygame.image.load(os.path.join(path, "resources/graphics/particles", "small_cube.PNG"))
}
MAP_IMAGES = {
    'ground_surf': pygame.image.load(os.path.join(path, "resources/graphics/tilemap", "floor.png"))
}
# preferences -> name : side, artifacts, quests, x, y
DRUIDS = {
    'Leaf': ["good", None, None, 700, 300]
}
DRUID_QUESTS = {
    'snake_sacrifice_berserker': ["Make the sacrifice to receive the Berserker's blessing", 100, "dead snake",
                                  "Barbarian", "evil", False, 1],
    'long_lost_treasure': ["find the Greatest Gem of the Dwarven Empire", 100, "the Greatest Gem of the Dwarven Empire",
                           "Dwarf", "good", False, 1],
    'become_the_thief': ["find and steal the Greatest Gem of the Dwarven Empire", 100,
                         "the Greatest Gem of the Dwarven Empire", "Dwarf", "evil", False, 1],
    'learn_and_heal': ["create and learn a new spell that enables you to heal yourself when harmed", 100,
                       "spell", "Wizard", "good", False, 1]
}


DARK_WIZARDS = {
    'Sarus': ["evil", None, None, 400, 500]
}
DARK_WIZARDS_QUESTS = {
    'true_in_blood': ["prove the Dark Wizard that you are of their kind", 100, "vampire's tear", "Wizard", "evil",
                      False, 1],
    'kill_unicorn': ["Kill the unicorn and bring back its horn ", 100, "unicorn's horn", "Fearie", "evil", False, 1],
    'get_sacred_fire': ["Look for druid and if you find them, drink the Liar’s potion and ask them kindly for some of "
                        "their sacred fire.", 100, "fire", "Elf", "evil", False, 1],
    'fearies_magic_dust': ["Find the little Fairies and ask them for the magic dust from them and return to get "
                           "healing potion.", 100, "magic dust", "Elf", "good", False, 2],
    'wheat_from_monsters': ["Prove you worth by fighting the dragon. Bring back dragon eyeballs.", 100,
                            "dragon eyeballs", "Elf", "good", False, 3],
    'fight_the_dragon': ["Prove you worth by fighting the dragon. Bring back dragon eyeballs.", 100, "fire", "Elf",
                         "good", False, 4],
    'gold_leprechaun_fight': ["Fight the leprechaun for the gold", 100, "pot of gold", "Elf", "good", False, 5],
    'kill_dragon': ["Prove your strength to the Dark Wizard", 100, "dragon’s fang", "Barbarian", "good", False, 1],
    'steal_leprechaun_gold': ["Steal gold from the Leprechaun", 100, "pot of gold", "Barbarian", "good", False, 1],
    'artisanal_skill': ["learn a new artisanal skill - find a smith that is crafting a metal/gem and ask him/her to "
                        "teach you.", 100, "gem", "Dwarf", "good", False, 1],
    'deadly_avalanche': ["cause an avalanche that will kill the inhabitants of the mountain of the Frozen Empire.", 100,
                         "axe", "Dwarf", "evil", False, 1]
}
ICE_MONSTERS = {
    'Icelius': ["evil", None, None, 200, 700]
}
MERMAIDS = {
    'Arielle': ["good", None, None, 400, 500]
}
MERMAIDS_QUESTS = {
    'find_pandas_ball': ["Get to the bamboo island and help the panda find a ball that is stuck somewhere in a bamboo "
                         "tree", 100, "ball", "Fearie", "good", False, 1]
}
ORCS = {
    'Stinker': ["evil", None, None, 800, 50]
}
ORCS_QUESTS = {
    'clean_feet': ["clean the orcs feet using mud from the swamp (learn a spell that will enable you to change the "
                   "mud into water", 100, "water", "Wizard", "evil", False, 1],
    'expel_the_blind': ["expel blind rats from the Misty Swamp (lead them out of the swamp so that they can’t find "
                        "their way back).", 100, "nth", "Wizard", "good", False, 1],
    'kill_tiger': ["Deprive the good barbarians of their strength", 100, "tiger's fur", "Barbarian", "evil", False, 1]
}
VAMPIRE_QUESTS = {
    'kill_the_raven': ["Kill the big Raven to collect its blood", 100, "raven's blood", "Elf", "evil", False, 7],
    'sage_from_forest': ["Go to the Forest and find someone who has sage (Amazon).", 100, "sage", "Elf", "evil", False,
                         6],
    'liar_potion_wizard': ["Ask Dark Wizard for Liar’s potion.", 100, "Liar’s potion", "Elf", "evil", False, 5],
    'voice_of_mermaid': ["Steal the voice of a mermaid", 100, "Mermaid’s necklace", "Elf", "evil", False, 4],
    'get_the_incantation': ["Ask Dark Elf for the scroll with the incantation.", 100, "scroll", "Elf", "evil", False,
                            3],
    'summon_the_god': ["Go to the place where you found the stone, pour raven blood over it, burn the sage in the "
                       " sacred fire, release mermaid’s voice and say the incantation to summon the god", 100, "god",
                       "Elf", "evil", False, 2],
    'eat_unicorn_heart': ["Eat unicorn’s heart to gain extra power, more mana and raster regeneration.", 100,
                          "unicorn's heart", "Elf", "evil", False, 1],
    'mermaid_blood': ["Bring back the Mermaid blood", 100, "blood", "Fearie", "evil", False, 1]
}
PANDAS_QUESTS = {
    'spiders_gone': ["Beat the spiders that pandas are scared of", 100, "nth", "Wizard", "evil", False, 1]
}

FEARIES_QUESTS = {
    'kill_spiders': ["Save faeries from ugly, evil spiders!", 100, "spider's fang", "Barbarian", "good", False, 1],
    'the_thief': ["find and beat the thief of the Greatest Gem of the Dwarven Empire", 100,
                  "the Greatest Gem of the Dwarven Empire", "Dwarf", "good", False, 1],
    'kill_the_gorilla': ["Kill the gorilla that hunts the fairies and get the magic dust from them", 100, "magic dust",
                         "Elf", "good", False, 1],
    'find_immortality_flower': ["Find the lost Flower of Immortality that was stolen by the Dwarf", 100,
                                "a magical flower and piece of paper", "Fearie", "good", False, 1],
    'mud_swimming': ["swim in a swamp to regain all your magical power", 100, "mud", "Wizard", "good", False, 1]
}

AMAZONS_QUESTS = {
    'deadly_dragon_fangs': ["Kill the dragon and bring its fang back", 100, "dragon's fang", "Dwarf", "good", False, 1],
    'amazons_feed_tiger': ["Help the Amazons feed the wild tiger", 100, "tiger's meat", "Barbarian", "good", False, 1]
}

FARMERS_QUESTS = {
    'spirit_animal': ["Prove your connection to your spirit animal", 100, "magic necklace", "Barbarian", "good", False,
                      2],
    'harvest_ravens': ["Save the villagers’ harvest from the Big Ravens", 100, "raven’s feathers", "Barbarian", "good",
                       False, 1],
    'saved_crops': ["Kill the big raven that is haunting the Medieville’s rural areas and get food in return", 100,
                    "food", "Dwarf", "good", False, 1],
    'make_vegetables_grow': ["Fly to the cloud and bring back a piece of the cloud and take it to the dry part of "
                             "Medieville so that the rain can fall and the vegetables will start to grow ", 100,
                             "cloud",
                             "Fearie", "good", False, 1]
}

SMITHS_QUESTS = {
    'smith_needs_gold': ["Go to the Leprechaun and convince him to give you a gold bar and bring it back", 100,
                         "gold bar",
                         "Fearie", "good", False, 1],
    'home_stones_smith': ["Save villagers from dying from a lack of home", 100, "miniature stone", "Barbarian", "good",
                          False, 2],
    'update_weapon': ["Update your weapon", 100, "weapon", "Barbarian", "good", False, 1],
    'mace_for_gold': ["Exchange the Orc’s mace for gold at the Blacksmith’s place", 100, "orc's mace", "Barbarian",
                      "evil",
                      False, 1]
}

UNICORN_QUESTS = {
    'safe_comeback': ["Climb the highest mountain of the Frozen Empire and help a creature that is living there", 100,
                      "rope", "Dwarf", "good", False, 1],
    'kill_the_god': ["Kill the god you summoned and take control over the demons he controlled.", 100, "nth", "Elf",
                     "evil",
                     False, 1]
}

BLIND_RATS_QUESTS = {
    'bring_eyesight_back': ["learn a spell that will regain blind rats eyesight", 100, "spell", "Wizard", "evil", False,
                            1]
}

EARTH_ELEMENTAL_QUESTS = {
    'magic_oak_bloom': ["Help the oak bloom with your earth magic", 100, "nth", "Elf", "good", False, 1]
}

TREANTS_QUESTS = {
    'secret_of_orcs': ["Acquire the secret of the Orcs", 100, "nth", "Wizard", "evil", False, 1],
    'make_a_wand': ["find a big old oak and take a piece of wood (trunk) so you could gain a wand", 100, "wand",
                    "Wizard",
                    "good", False, 1],
    'pour_potion_oak': ["Pour the potion over the roots of the sacred oak.", 100, "nth", "Elf", "good", False, 1],
    'find_potion_wizard': ["Find the Dark Wizard and ask him for the healing potion paying with gold.", 100,
                           "healing potion", "Elf", "good", 2]
}

DARK_ELVES_QUESTS = {
    'heart_of_unicorn': ["Get the heart of a unicorn", 100, "heart of unicorn", "Elf", "evil", False, 1],
    'bring_tools': ["Kill the blacksmith and take his tools", 100, "blacksmith's tools", "Fearie", "evil", False, 1],
    'donkey_the_companion': ["convince the chosen donkey to travel the world with you", 100, "stoned donkey", "Wizard",
                             "good", False, 1]
}

ELVES_QUESTS = {
    'bring_tigers_fur': ["Bring the tiger’s fur", 100, "tiger's fur", "Fearie", "evil", False, 1],
    'kill_Yeti': ["Kill the ice monster that is attacking the poor snowman", 100, "nth", "Fearie", "good", False, 1]
}

BIG_MONKE_QUESTS = {
    'find_panda_skull': ["Bring the buried panda skull", 100, "panda's skull", "Fearie", "evil", False, 1]
}

SPIRIT_QUESTS = {
    'ask_freedom_dark': ["Healing of the oak brings the god to thanks you granting you a wish. You ask for freeing "
                         "all dark elves from the demons under the rebelious god control.", 100, "wish", "Elf", "good",
                         False, 1]
}

SNOWMAN_QUESTS = {
    'running_carrots': ["Kill the escaping vegetable monster (form the Medieville) and bring the carrot to the "
                        "snowman so that he could use his smell again", 100, "carrot", "Dwarf", "good", False, 1],
    'icey_weapon': ["Make a weapon out of ice and beat the Yeti with it", 100, "ice weapon", "Dwarf", "evil", False, 1]
}

LEPRECHAUN_QUESTS = {
    'snowman_the_thief': ["find a Snowman and make him steal the treasure of the dwarves for you", 100, "gem", "Dwarf",
                          "evil", False, 1]
}

BIG_WOLVES_QUESTS = {
    'sacrifice': ["Sacrifice one of your belongings in order to get through the pack of wolves", 100, "nth", "Dwarf",
                  "evil", False, 1]
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
        'quests': DRUID_QUESTS
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
    }
}