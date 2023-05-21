# main game settings
import math

# screen resolution
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60


PLAYER_POS = 1.5, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# raycasting settings
# Field Of View for the player
FOV = math.pi/3
HALF_FOV = FOV/2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV/NUM_RAYS
MAX_DEPTH = 20

# place the player at correct distance from screen
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
# scaling factor
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE / 2
