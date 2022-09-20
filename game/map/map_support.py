from game.game_support import import_folder, import_csv_layout
from game.map.Tile import Tile
from game.settings import TILE_SIZE


def create_map(all_sprites_group, collision_sprites, npc_boundaries, sprites_to_move_opposite):
    layouts = {
        'boundary_hero': import_csv_layout('resources/map/tilesets/constraints_hero.csv'),
        'boundary_npc': import_csv_layout('resources/map/tilesets/constraints_npc.csv'),
        'nature_object': import_csv_layout('resources/map/tilesets/trees_rocks_positions.csv'),
        'harvest_object': import_csv_layout('resources/map/tilesets/harvest_positions.csv'),
    }
    graphics = {
        'trees_rocks': import_folder('../resources/graphics/objects/trees'),
        'harvest_tiles': import_folder('../resources/graphics/objects/harvest')
    }

    # bound = pygame.image.load(os.path.join(path, 'resources/graphics/tilemap/npc_blocker.png'))

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

                    if style == 'nature_object':
                        surf = graphics['trees_rocks'][int(tile)]
                        Tile((x, y), [sprites_to_move_opposite], (all_sprites_group, collision_sprites, npc_boundaries),
                             'object', (0,0), surf)

                    if style == 'harvest_object':
                        surf = graphics['harvest_tiles'][int(tile)]
                        Tile((x, y), [sprites_to_move_opposite], (all_sprites_group, collision_sprites, npc_boundaries),
                             'object', (0,0), surf)