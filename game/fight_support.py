
def set_fight_parameters(hero, use_spell):
    if hero.in_fight:
        use_spell = not use_spell
        if hero.casting_spell:
            hero.casting_spell = not hero.casting_spell
            hero.chosen_spell = None
        else:
            hero.chosen_spell = None
            hero.casting_spell = False
        if hero.mana == 0:
            use_spell = False
            hero.chosen_spell = None
            hero.casting_spell = False

    return use_spell
