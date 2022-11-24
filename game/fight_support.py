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
    if hero.life > 0:
        chosen_npc.in_attack = False
        chosen_npc.attack_type = None
        chosen_npc.in_fight_mode = True
        chosen_npc.performing_action = False

        hero.in_fight_mode = True
        hero.performing_action = False
        hero.in_attack = False
        hero.attack_type = None
        print("FIGHT")


def stop_fight(hero, chosen_npc):
    chosen_npc.in_attack = False
    chosen_npc.in_fight_mode = False
    hero.in_fight_mode = False
    hero.in_attack = False
    print("STOP FIGHT")


def remove_npc(npc, npcs, all_sprites_group, npcs_to_choose, collision_sprites_hero, collision_sprites_npc, screen):
    npcs.remove(npc)
    for mock in npcs_to_choose:
        if mock.npc == npc:
            npcs_to_choose.remove(mock)
            npcs_to_choose.update()
    for n in npcs:
        if n != npc:
            n.collision_sprites_npc.remove(npc)
    all_sprites_group.remove(npc)
    collision_sprites_hero.remove(npc)
    collision_sprites_npc.remove(npc)
    npc.kill()
    collision_sprites_hero.update()
    collision_sprites_npc.update()
    all_sprites_group.update()
    all_sprites_group.draw(screen)
