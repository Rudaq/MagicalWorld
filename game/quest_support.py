from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.settings import GUI_IMAGES, BLACK
import math
from quest_settings import QUESTS
from settings import BLACK
from quest.Quest import Quest
from quest.Task import Task


class NPCTypeNotExistException(Exception):
    pass


def create_quests(hero):
    if hero.race == 'Faerie':
        quests_dict_entry = QUESTS.get(hero.race)
    if quests_dict_entry:
        if hero.side == 'evil':
            parameters = quests_dict_entry.get('evil')
            for p in parameters:
                tasks = []
                for t in parameters[p][3]:
                    task = Task(t[0], t[1], t[2], t[3], t[4], t[5], t[6],t[7], hero, False)
                    tasks.append(task)

                quest = Quest(parameters[p][0], parameters[p][1], parameters[p][2], tasks, hero, False)
                # quest = quests_dict_entry[p](name=p[0], side=parameters[0], mana=npc_dict_entry['mana'],
                #                                       life=npc_dict_entry['life'], images=npc_dict_entry['images'],
                #                                       artifacts=parameters[1], quests=parameters[2], x=parameters[3],
                #                                       y=parameters[4], pos=(parameters[3], parameters[4]), groups=sprite_groups,
                #                                       inflation=(0, -10), collision_sprites=collision_sprites)

                hero.quests.append(quest)
            hero.set_active_quest()
    else:
        raise NPCTypeNotExistException

    #
# def create_quest(NPC, quest_name):
#     if NPC.race == "Dark Wizard":
#         quest = Quest(DARK_WIZARDS_QUESTS[quest_name][0], DARK_WIZARDS_QUESTS[quest_name][1],
#                       DARK_WIZARDS_QUESTS[quest_name][2], DARK_WIZARDS_QUESTS[quest_name][3],
#                       DARK_WIZARDS_QUESTS[quest_name][4], DARK_WIZARDS_QUESTS[quest_name][5],
#                       DARK_WIZARDS_QUESTS[quest_name][6], DARK_WIZARDS_QUESTS[quest_name][7])
#     elif NPC.race == "Mermaid":
#         quest = Quest(MERMAIDS_QUESTS[quest_name][0], MERMAIDS_QUESTS[quest_name][1], MERMAIDS_QUESTS[quest_name][2],
#                       MERMAIDS_QUESTS[quest_name][3], MERMAIDS_QUESTS[quest_name][4], MERMAIDS_QUESTS[quest_name][5],
#                       MERMAIDS_QUESTS[quest_name][6], MERMAIDS_QUESTS[quest_name][7])
#     elif NPC.race == "Orc":
#         quest = Quest(ORCS_QUESTS[quest_name][0], ORCS_QUESTS[quest_name][1], ORCS_QUESTS[quest_name][2],
#                       ORCS_QUESTS[quest_name][3], ORCS_QUESTS[quest_name][4], ORCS_QUESTS[quest_name][5],
#                       ORCS_QUESTS[quest_name][6], ORCS_QUESTS[quest_name][7])
#     elif NPC.race == "Vampire":
#         quest = Quest(VAMPIRE_QUESTS[quest_name][0], VAMPIRE_QUESTS[quest_name][1], VAMPIRE_QUESTS[quest_name][2],
#                       VAMPIRE_QUESTS[quest_name][3], VAMPIRE_QUESTS[quest_name][4], VAMPIRE_QUESTS[quest_name][5],
#                       VAMPIRE_QUESTS[quest_name][6], VAMPIRE_QUESTS[quest_name][7])
#     elif NPC.race == "Pandas":
#         quest = Quest(PANDAS_QUESTS[quest_name][0], PANDAS_QUESTS[quest_name][1], PANDAS_QUESTS[quest_name][2],
#                       PANDAS_QUESTS[quest_name][3], PANDAS_QUESTS[quest_name][4], PANDAS_QUESTS[quest_name][5],
#                       PANDAS_QUESTS[quest_name][6], PANDAS_QUESTS[quest_name][7])
#     elif NPC.race == "Faeries":
#         quest = Quest(FAERIES_QUESTS[quest_name][0], FAERIES_QUESTS[quest_name][1], FAERIES_QUESTS[quest_name][2],
#                       FAERIES_QUESTS[quest_name][3], FAERIES_QUESTS[quest_name][4], FAERIES_QUESTS[quest_name][5],
#                       FAERIES_QUESTS[quest_name][6], FAERIES_QUESTS[quest_name][7])
#     elif NPC.race == "Earth Elemental":
#         quest = Quest(EARTH_ELEMENTAL_QUESTS[quest_name][0], EARTH_ELEMENTAL_QUESTS[quest_name][1],
#                       EARTH_ELEMENTAL_QUESTS[quest_name][2],
#                       EARTH_ELEMENTAL_QUESTS[quest_name][3], EARTH_ELEMENTAL_QUESTS[quest_name][4],
#                       EARTH_ELEMENTAL_QUESTS[quest_name][5],
#                       EARTH_ELEMENTAL_QUESTS[quest_name][6], EARTH_ELEMENTAL_QUESTS[quest_name][7])
#     elif NPC.race == "Dark Elf":
#         quest = Quest(DARK_ELVES_QUESTS[quest_name][0], DARK_ELVES_QUESTS[quest_name][1],
#                       DARK_ELVES_QUESTS[quest_name][2],
#                       DARK_ELVES_QUESTS[quest_name][3], DARK_ELVES_QUESTS[quest_name][4],
#                       DARK_ELVES_QUESTS[quest_name][5],
#                       DARK_ELVES_QUESTS[quest_name][6], DARK_ELVES_QUESTS[quest_name][7])
#     elif NPC.race == "Elf":
#         quest = Quest(ELVES_QUESTS[quest_name][0], ELVES_QUESTS[quest_name][1], ELVES_QUESTS[quest_name][2],
#                       ELVES_QUESTS[quest_name][3], ELVES_QUESTS[quest_name][4], ELVES_QUESTS[quest_name][5],
#                       ELVES_QUESTS[quest_name][6], ELVES_QUESTS[quest_name][7])
#     elif NPC.race == "Smith":
#         quest = Quest(SMITHS_QUESTS[quest_name][0], SMITHS_QUESTS[quest_name][1], SMITHS_QUESTS[quest_name][2],
#                       SMITHS_QUESTS[quest_name][3], SMITHS_QUESTS[quest_name][4], SMITHS_QUESTS[quest_name][5],
#                       SMITHS_QUESTS[quest_name][6], SMITHS_QUESTS[quest_name][7])
#     elif NPC.race == "Unicorn":
#         quest = Quest(UNICORN_QUESTS[quest_name][0], UNICORN_QUESTS[quest_name][1], UNICORN_QUESTS[quest_name][2],
#                       UNICORN_QUESTS[quest_name][3], UNICORN_QUESTS[quest_name][4], UNICORN_QUESTS[quest_name][5],
#                       UNICORN_QUESTS[quest_name][6], UNICORN_QUESTS[quest_name][7])
#     elif NPC.race == "Blind Rats":
#         quest = Quest(BLIND_RATS_QUESTS[quest_name][0], BLIND_RATS_QUESTS[quest_name][1],
#                       BLIND_RATS_QUESTS[quest_name][2],
#                       BLIND_RATS_QUESTS[quest_name][3], BLIND_RATS_QUESTS[quest_name][4],
#                       BLIND_RATS_QUESTS[quest_name][5],
#                       BLIND_RATS_QUESTS[quest_name][6], BLIND_RATS_QUESTS[quest_name][7])
#     elif NPC.race == "Treant":
#         quest = Quest(TREANTS_QUESTS[quest_name][0], TREANTS_QUESTS[quest_name][1], TREANTS_QUESTS[quest_name][2],
#                       TREANTS_QUESTS[quest_name][3], TREANTS_QUESTS[quest_name][4], TREANTS_QUESTS[quest_name][5],
#                       TREANTS_QUESTS[quest_name][6], TREANTS_QUESTS[quest_name][7])
#     elif NPC.race == "Amazon":
#         quest = Quest(AMAZONS_QUESTS[quest_name][0], AMAZONS_QUESTS[quest_name][1], AMAZONS_QUESTS[quest_name][2],
#                       AMAZONS_QUESTS[quest_name][3], AMAZONS_QUESTS[quest_name][4], AMAZONS_QUESTS[quest_name][5],
#                       AMAZONS_QUESTS[quest_name][6], AMAZONS_QUESTS[quest_name][7])
#     elif NPC.race == "Farmer":
#         quest = Quest(FARMERS_QUESTS[quest_name][0], FARMERS_QUESTS[quest_name][1], FARMERS_QUESTS[quest_name][2],
#                       FARMERS_QUESTS[quest_name][3], FARMERS_QUESTS[quest_name][4], FARMERS_QUESTS[quest_name][5],
#                       FARMERS_QUESTS[quest_name][6], FARMERS_QUESTS[quest_name][7])
#     elif NPC.race == "Big Monke":
#         quest = Quest(BIG_MONKE_QUESTS[quest_name][0], BIG_MONKE_QUESTS[quest_name][1], BIG_MONKE_QUESTS[quest_name][2],
#                       BIG_MONKE_QUESTS[quest_name][3], BIG_MONKE_QUESTS[quest_name][4], BIG_MONKE_QUESTS[quest_name][5],
#                       BIG_MONKE_QUESTS[quest_name][6], BIG_MONKE_QUESTS[quest_name][7])
#     elif NPC.race == "Spirit":
#         quest = Quest(SPIRIT_QUESTS[quest_name][0], SPIRIT_QUESTS[quest_name][1], SPIRIT_QUESTS[quest_name][2],
#                       SPIRIT_QUESTS[quest_name][3], SPIRIT_QUESTS[quest_name][4], SPIRIT_QUESTS[quest_name][5],
#                       SPIRIT_QUESTS[quest_name][6], SPIRIT_QUESTS[quest_name][7])
#     elif NPC.race == "Snowman":
#         quest = Quest(SNOWMAN_QUESTS[quest_name][0], SNOWMAN_QUESTS[quest_name][1], SNOWMAN_QUESTS[quest_name][2],
#                       SNOWMAN_QUESTS[quest_name][3], SNOWMAN_QUESTS[quest_name][4], SNOWMAN_QUESTS[quest_name][5],
#                       SNOWMAN_QUESTS[quest_name][6], SNOWMAN_QUESTS[quest_name][7])
#     elif NPC.race == "Leprechaun":
#         quest = Quest(LEPRECHAUN_QUESTS[quest_name][0], LEPRECHAUN_QUESTS[quest_name][1],
#                       LEPRECHAUN_QUESTS[quest_name][2],
#                       LEPRECHAUN_QUESTS[quest_name][3], LEPRECHAUN_QUESTS[quest_name][4],
#                       LEPRECHAUN_QUESTS[quest_name][5],
#                       LEPRECHAUN_QUESTS[quest_name][6], LEPRECHAUN_QUESTS[quest_name][7])
#     elif NPC.race == "Big Wolves":
#         quest = Quest(BIG_WOLVES_QUESTS[quest_name][0], BIG_WOLVES_QUESTS[quest_name][1],
#                       BIG_WOLVES_QUESTS[quest_name][2],
#                       BIG_WOLVES_QUESTS[quest_name][3], BIG_WOLVES_QUESTS[quest_name][4],
#                       BIG_WOLVES_QUESTS[quest_name][5],
#                       BIG_WOLVES_QUESTS[quest_name][6], BIG_WOLVES_QUESTS[quest_name][7])
#
#     else:
#         quest = Quest(DRUID_QUESTS[quest_name][0], DRUID_QUESTS[quest_name][1],
#                       DRUID_QUESTS[quest_name][2], DRUID_QUESTS[quest_name][3],
#                       DRUID_QUESTS[quest_name][4], DRUID_QUESTS[quest_name][5],
#                       DRUID_QUESTS[quest_name][6], DRUID_QUESTS[quest_name][7])
#
#     return quest

#
# def create_quest(NPC, hero):
#     quest = None
#     if NPC.race == "Dark Wizard":
#         for q in DARK_WIZARDS_QUESTS:
#             if DARK_WIZARDS_QUESTS[q][3] == hero.race:
#                 quest = Task(DARK_WIZARDS_QUESTS[q][0], DARK_WIZARDS_QUESTS[q][1],
#                              DARK_WIZARDS_QUESTS[q][2], DARK_WIZARDS_QUESTS[q][3],
#                              DARK_WIZARDS_QUESTS[q][4], DARK_WIZARDS_QUESTS[q][5],
#                              DARK_WIZARDS_QUESTS[q][6], DARK_WIZARDS_QUESTS[q][7])
#     elif NPC.race == "Mermaid":
#         for q in MERMAIDS_QUESTS:
#             if MERMAIDS_QUESTS[q][3] == hero.race:
#                 quest = Task(MERMAIDS_QUESTS[q][0], MERMAIDS_QUESTS[q][1], MERMAIDS_QUESTS[q][2],
#                              MERMAIDS_QUESTS[q][3], MERMAIDS_QUESTS[q][4], MERMAIDS_QUESTS[q][5],
#                              MERMAIDS_QUESTS[q][6], MERMAIDS_QUESTS[q][7])
#                 break;
#     elif NPC.race == "Orc":
#         for q in ORCS_QUESTS:
#             if ORCS_QUESTS[q][3] == hero.race:
#                 quest = Task(ORCS_QUESTS[q][0], ORCS_QUESTS[q][1], ORCS_QUESTS[q][2],
#                              ORCS_QUESTS[q][3], ORCS_QUESTS[q][4], ORCS_QUESTS[q][5],
#                              ORCS_QUESTS[q][6], ORCS_QUESTS[q][7])
#     elif NPC.race == "Vampire":
#         for q in ORCS_QUESTS:
#             if ORCS_QUESTS[q][3] == hero.race:
#                 quest = Task(VAMPIRE_QUESTS[q][0], VAMPIRE_QUESTS[q][1], VAMPIRE_QUESTS[q][2],
#                              VAMPIRE_QUESTS[q][3], VAMPIRE_QUESTS[q][4], VAMPIRE_QUESTS[q][5],
#                              VAMPIRE_QUESTS[q][6], VAMPIRE_QUESTS[q][7])
#     elif NPC.race == "Pandas":
#         for q in PANDAS_QUESTS:
#             if PANDAS_QUESTS[q][3] == hero.race:
#                 quest = Task(PANDAS_QUESTS[q][0], PANDAS_QUESTS[q][1], PANDAS_QUESTS[q][2],
#                              PANDAS_QUESTS[q][3], PANDAS_QUESTS[q][4], PANDAS_QUESTS[q][5],
#                              PANDAS_QUESTS[q][6], PANDAS_QUESTS[q][7])
#     elif NPC.race == "Faeries":
#         for q in FAERIES_QUESTS:
#             if FAERIES_QUESTS[q][3] == hero.race:
#                 quest = Task(FAERIES_QUESTS[q][0], FAERIES_QUESTS[q][1], FAERIES_QUESTS[q][2],
#                              FAERIES_QUESTS[q][3], FAERIES_QUESTS[q][4], FAERIES_QUESTS[q][5],
#                              FAERIES_QUESTS[q][6], FAERIES_QUESTS[q][7])
#     elif NPC.race == "Earth Elemental":
#         for q in EARTH_ELEMENTAL_QUESTS:
#             if EARTH_ELEMENTAL_QUESTS[q][3] == hero.race:
#                 quest = Task(EARTH_ELEMENTAL_QUESTS[q][0], EARTH_ELEMENTAL_QUESTS[q][1],
#                              EARTH_ELEMENTAL_QUESTS[q][2],
#                              EARTH_ELEMENTAL_QUESTS[q][3], EARTH_ELEMENTAL_QUESTS[q][4],
#                              EARTH_ELEMENTAL_QUESTS[q][5],
#                              EARTH_ELEMENTAL_QUESTS[q][6], EARTH_ELEMENTAL_QUESTS[q][7])
#
#     elif NPC.race == "Dark Elf":
#         for q in DARK_ELVES_QUESTS:
#             if DARK_ELVES_QUESTS[q][3] == hero.race:
#                 quest = Task(DARK_ELVES_QUESTS[q][0], DARK_ELVES_QUESTS[q][1],
#                              DARK_ELVES_QUESTS[q][2],
#                              DARK_ELVES_QUESTS[q][3], DARK_ELVES_QUESTS[q][4],
#                              DARK_ELVES_QUESTS[q][5],
#                              DARK_ELVES_QUESTS[q][6], DARK_ELVES_QUESTS[q][7])
#     elif NPC.race == "Elf":
#         for q in ELVES_QUESTS:
#             if ELVES_QUESTS[q][3] == hero.race:
#                 quest = Task(ELVES_QUESTS[q][0], ELVES_QUESTS[q][1], ELVES_QUESTS[q][2],
#                              ELVES_QUESTS[q][3], ELVES_QUESTS[q][4], ELVES_QUESTS[q][5],
#                              ELVES_QUESTS[q][6], ELVES_QUESTS[q][7])
#     elif NPC.race == "Smith":
#         for q in SMITHS_QUESTS:
#             if SMITHS_QUESTS[q][3] == hero.race:
#                 quest = Task(SMITHS_QUESTS[q][0], SMITHS_QUESTS[q][1], SMITHS_QUESTS[q][2],
#                              SMITHS_QUESTS[q][3], SMITHS_QUESTS[q][4], SMITHS_QUESTS[q][5],
#                              SMITHS_QUESTS[q][6], SMITHS_QUESTS[q][7])
#     elif NPC.race == "Unicorn":
#         for q in UNICORN_QUESTS:
#             if UNICORN_QUESTS[q][3] == hero.race:
#                 quest = Task(UNICORN_QUESTS[q][0], UNICORN_QUESTS[q][1], UNICORN_QUESTS[q][2],
#                              UNICORN_QUESTS[q][3], UNICORN_QUESTS[q][4], UNICORN_QUESTS[q][5],
#                              UNICORN_QUESTS[q][6], UNICORN_QUESTS[q][7])
#     elif NPC.race == "Blind Rats":
#         for q in BLIND_RATS_QUESTS:
#             if BLIND_RATS_QUESTS[q][3] == hero.race:
#                 quest = Task(BLIND_RATS_QUESTS[q][0], BLIND_RATS_QUESTS[q][1],
#                              BLIND_RATS_QUESTS[q][2],
#                              BLIND_RATS_QUESTS[q][3], BLIND_RATS_QUESTS[q][4],
#                              BLIND_RATS_QUESTS[q][5],
#                              BLIND_RATS_QUESTS[q][6], BLIND_RATS_QUESTS[q][7])
#     elif NPC.race == "Treant":
#         for q in TREANTS_QUESTS:
#             if TREANTS_QUESTS[q][3] == hero.race:
#                 quest = Task(TREANTS_QUESTS[q][0], TREANTS_QUESTS[q][1], TREANTS_QUESTS[q][2],
#                              TREANTS_QUESTS[q][3], TREANTS_QUESTS[q][4], TREANTS_QUESTS[q][5],
#                              TREANTS_QUESTS[q][6], TREANTS_QUESTS[q][7])
#     elif NPC.race == "Amazon":
#         for q in AMAZONS_QUESTS:
#             if AMAZONS_QUESTS[q][3] == hero.race:
#                 quest = Task(AMAZONS_QUESTS[q][0], AMAZONS_QUESTS[q][1], AMAZONS_QUESTS[q][2],
#                              AMAZONS_QUESTS[q][3], AMAZONS_QUESTS[q][4], AMAZONS_QUESTS[q][5],
#                              AMAZONS_QUESTS[q][6], AMAZONS_QUESTS[q][7])
#     elif NPC.race == "Farmer":
#         for q in FARMERS_QUESTS:
#             if FARMERS_QUESTS[q][3] == hero.race:
#                 quest = Task(FARMERS_QUESTS[q][0], FARMERS_QUESTS[q][1], FARMERS_QUESTS[q][2],
#                              FARMERS_QUESTS[q][3], FARMERS_QUESTS[q][4], FARMERS_QUESTS[q][5],
#                              FARMERS_QUESTS[q][6], FARMERS_QUESTS[q][7])
#     elif NPC.race == "Big Monke":
#         for q in BIG_MONKE_QUESTS:
#             if BIG_MONKE_QUESTS[q][3] == hero.race:
#                 quest = Task(BIG_MONKE_QUESTS[q][0], BIG_MONKE_QUESTS[q][1], BIG_MONKE_QUESTS[q][2],
#                              BIG_MONKE_QUESTS[q][3], BIG_MONKE_QUESTS[q][4], BIG_MONKE_QUESTS[q][5],
#                              BIG_MONKE_QUESTS[q][6], BIG_MONKE_QUESTS[q][7])
#     elif NPC.race == "Spirit":
#         for q in SPIRIT_QUESTS:
#             if SPIRIT_QUESTS[q][3] == hero.race:
#                 quest = Task(SPIRIT_QUESTS[q][0], SPIRIT_QUESTS[q][1], SPIRIT_QUESTS[q][2],
#                              SPIRIT_QUESTS[q][3], SPIRIT_QUESTS[q][4], SPIRIT_QUESTS[q][5],
#                              SPIRIT_QUESTS[q][6], SPIRIT_QUESTS[q][7])
#     elif NPC.race == "Snowman":
#         for q in SNOWMAN_QUESTS:
#             if SNOWMAN_QUESTS[q][3] == hero.race:
#                 quest = Task(SNOWMAN_QUESTS[q][0], SNOWMAN_QUESTS[q][1], SNOWMAN_QUESTS[q][2],
#                              SNOWMAN_QUESTS[q][3], SNOWMAN_QUESTS[q][4], SNOWMAN_QUESTS[q][5],
#                              SNOWMAN_QUESTS[q][6], SNOWMAN_QUESTS[q][7])
#     elif NPC.race == "Leprechaun":
#         for q in LEPRECHAUN_QUESTS:
#             if LEPRECHAUN_QUESTS[q][3] == hero.race:
#                 quest = Task(LEPRECHAUN_QUESTS[q][0], LEPRECHAUN_QUESTS[q][1],
#                              LEPRECHAUN_QUESTS[q][2],
#                              LEPRECHAUN_QUESTS[q][3], LEPRECHAUN_QUESTS[q][4],
#                              LEPRECHAUN_QUESTS[q][5],
#                              LEPRECHAUN_QUESTS[q][6], LEPRECHAUN_QUESTS[q][7])
#     elif NPC.race == "Big Wolves":
#         for q in BIG_WOLVES_QUESTS:
#             if BIG_WOLVES_QUESTS[q][3] == hero.race:
#                 quest = Task(BIG_WOLVES_QUESTS[q][0], BIG_WOLVES_QUESTS[q][1],
#                              BIG_WOLVES_QUESTS[q][2],
#                              BIG_WOLVES_QUESTS[q][3], BIG_WOLVES_QUESTS[q][4],
#                              BIG_WOLVES_QUESTS[q][5],
#                              BIG_WOLVES_QUESTS[q][6], BIG_WOLVES_QUESTS[q][7])
#
#     else:
#         for q in DRUID_QUESTS:
#             if DRUID_QUESTS[q][3] == hero.race:
#                 quest = Task(DRUID_QUESTS[q][0], DRUID_QUESTS[q][1],
#                              DRUID_QUESTS[q][2], DRUID_QUESTS[q][3],
#                              DRUID_QUESTS[q][4], DRUID_QUESTS[q][5],
#                              DRUID_QUESTS[q][6], DRUID_QUESTS[q][7])
#
#     if quest is not None:
#         hero.active_quest = quest

# def test_quest(npc, hero):
#     quest_name = None
#     if npc.race == "DarkWizard":
#         for q in DARK_WIZARDS_QUESTS:
#             if DARK_WIZARDS_QUESTS[q][3] == hero.race:
#                 quest_name = DARK_WIZARDS_QUESTS[q]
#     elif npc.race == "Mermaid":
#         for q in MERMAIDS_QUESTS:
#             if MERMAIDS_QUESTS[q][3] == hero.race:
#                 quest_name = MERMAIDS_QUESTS[q]
#                 print(quest_name)
#     elif npc.race == "Druid":
#         for i in len(DRUID_QUESTS) - 1:
#             if DRUID_QUESTS[i][3] == hero.race:
#                 quest_name = DRUID_QUESTS[i]
#     elif npc.race == "Orc":
#         for i in len(ORCS_QUESTS) - 1:
#             if ORCS_QUESTS[i][3] == hero.race:
#                 quest_name = ORCS_QUESTS[i]
#
#     if quest_name is None:
#         print("No quest")
#     else:
#         quest = create_quest(npc, quest_name)
#         hero.active_quest = quest


def show_quest_to_hero(screen, hero):
    screen_width = math.floor(screen.get_size()[0])
    quest_top_right = screen_width - 400
    screen.blit(GUI_IMAGES['scroll'], (quest_top_right, 100))
    w = 200
    h = quest_top_right + 110
    if hero.active_quest is not None:
        if hero.active_quest.active_task is not None:
            text_list = wrap_text(hero.active_quest.active_task.description, 25, False)
        else:
            text_list = wrap_text(hero.active_quest.description, 25, False)
        for text in text_list:
            draw_text(text, h, w, 14, BLACK, screen)
            w += 20
            if h == 1170:
                h += 5
            else:
                h -= 5
    else:
        text = "You mission is completed! Congratulation!!! <3"
        draw_text(text, h, w, 14, BLACK, screen)

