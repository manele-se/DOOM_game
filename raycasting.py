import pygame as pg
import math
from settings import *

# raycast is a projection of a given number of rays from the view of the player. For each ray we need to determine the intersection point with the wall.
# Because the map is a grid we need to find the intersection with vertical and horizontal lines (2 cases)


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001  # avoid division by zero

        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # calculate intersection with horizontal lines, check if possible to extract a method
            if sin_a > 0:
                y_hor = y_map + 1
                dy = 1
            else:
                y_hor = y_map - 1e-6
                dy = -1

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # calculate intersection with vertical lines
            if cos_a > 0:
                x_vert = x_map + 1
                dx = 1
            else:
                x_vert = x_map - 1e-6
                dx = -1

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # remove fishbowl effect due to the cartesian system.
            depth *= math.cos(self.game.player.angle - ray_angle)

            # projection 3D
            proj_height = SCREEN_DIST / \
                (depth + 0.00001)  # avoid division by 0

            # create a gradient effect where walls closer to the player are brighter and walls farther away are darker.
            color = [220 / (1 + depth ** 5 * 0.0002), 150 / (1 +
                                                             depth ** 5 * 0.0002), 200 / (1 + depth ** 5 * 0.0002)]

            pg.draw.rect(self.game.screen, color, (ray * SCALE,
                                                   HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
