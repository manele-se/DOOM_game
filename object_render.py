import pygame as pg
from settings import *


class ObjectRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    # take texture from a specified path and return a scaled image
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):  # dictionary
        return{
            1: self.get_texture('resources/textures/black.jpg'),
            2: self.get_texture('resources/textures/bricks.jpg'),
            3: self.get_texture('resources/textures/bricks2.png'),
            4: self.get_texture('resources/textures/blood.png'),
            5: self.get_texture('resources/textures/blood2.png'),
            6: self.get_texture('resources/textures/stone.png'),

        }
