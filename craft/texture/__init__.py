"""
    Texture
"""

import os.path

TEXTURE_DIR = 'craft/texture'


# pylint: disable=invalid-name
def coord(x, y, n=4):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m
tex_coord = coord


def coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = coord(*top)
    bottom = coord(*bottom)
    side = coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result
tex_coords = coords
# pylint: enable=invalid-name


TEXTURE_PATH = os.path.join(TEXTURE_DIR, 'texture.png')

GRASS = coords((1, 0), (0, 1), (0, 0))
SAND = coords((1, 1), (1, 1), (1, 1))
BRICK = coords((2, 0), (2, 0), (2, 0))
STONE = coords((2, 1), (2, 1), (2, 1))

FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]
