def set_fight_parameters(hero):
    if hero.in_fight_mode:
        hero.in_attack = not hero.in_attack
        if hero.performing_action:
            hero.performing_action = not hero.performing_action
            hero.attack_type = None
        else:
            hero.attack_type = None
            hero.performing_action = False
        if hero.mana == 0:
            hero.in_attack = False
            hero.attack_type = None
            hero.performing_action = False


# sey the settings of fight
def fight(hero, chosen_npc):
    if not chosen_npc.is_fighting:
        chosen_npc.is_fighting = True
        hero.in_fight_mode = True
        hero.performing_action = False
        hero.in_attack = False
        hero.attack_type = None
        print("FIGHT")


def stop_fight(hero, chosen_npc):
    chosen_npc.is_fighting = False
    hero.in_fight_mode = False
    hero.in_attack = False
    print("STOP FIGHT")
