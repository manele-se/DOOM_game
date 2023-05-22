import pygame as pg
from settings import *


class ObjectRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

        # take texture from a specified path and return a scaled image

        @staticmethod
        def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
            texture = pg.image.load(path).convert_alpha()
            return pg.transform.scale(texture, res)

        def load_wall_textures(self):  # dictionary
            return{
                1: self.get_texture('resources/textures/black.jpg'),
                2: self.get_texture('resources/textures/bricks.jpg'),
                3: self.get_texture('resources/textures/bricks2.jpg'),
                4: self.get_texture('resources/textures/blood.jpg'),
                5: self.get_texture('resources/textures/blood2.jpg'),

            }
