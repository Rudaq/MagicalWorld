from game.settings import GUI_IMAGES

def set_fight_parameters(hero):
    if hero.in_fight:
        hero.in_spell = not hero.in_spell
        if hero.casting_spell:
            hero.casting_spell = not hero.casting_spell
            hero.chosen_spell = None
        else:
            hero.chosen_spell = None
            hero.casting_spell = False
        if hero.mana == 0:
            hero.in_spell = False
            hero.chosen_spell = None
            hero.casting_spell = False


def fight(hero, chosen_npc, fight_button, talk_button):
    if not chosen_npc.is_fighting:
        chosen_npc.is_fighting = True
        hero.in_fight = True
        hero.casting_spell = False
        hero.in_spell = False
        hero.chosen_spell = None
        print("FIGHT")
        fight_button.change_image(GUI_IMAGES['clicked_fight_button'], 0.8)
        talk_button.change_image(GUI_IMAGES['talk_button'], 0.8)

    else:
        chosen_npc.is_fighting = False
        hero.in_fight = False
        print("STOP FIGHT")
        fight_button.change_image(GUI_IMAGES['fight_button'], 0.8)
