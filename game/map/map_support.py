import pygame

from game.game_support import import_csv_layout
from game.map.Tile import Tile
from game.settings import TILE_SIZE


def create_map(all_sprites_group, collision_sprites, npc_boundaries, sprites_to_move_opposite):
    layouts = {
        'boundary_hero': import_csv_layout('resources/map/tilesets/_constraints_hero.csv'),
        'boundary_npc': import_csv_layout('resources/map/tilesets/_constraints_npc.csv')
    }

    # for testing
    # bound = pygame.image.load("../resources/graphics/tilemap/npc_blocker.png")

    for style, layout in layouts.items():
        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                if tile != '-1':
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE

                    if style == 'boundary_hero':
                        Tile((x, y), [sprites_to_move_opposite], [collision_sprites], 'invisible')

                    if style == 'boundary_npc':
                        Tile((x, y), [sprites_to_move_opposite], [npc_boundaries], 'invisible')
