#=================================================================================================================
# PARTIE 1: APPELS DES FICHERS ET LIBRARIES EXTERNE (IMPORT)
#=================================================================================================================

from color import Color
from light import Light
from material import *
from point import Point
from sphere import Sphere
from vector import Vector


# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================
# ==============================================================================
WIDTH = 920
HEIGHT = 620
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    # Ground Plane
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#FFFFFF"),
            color2=Color.from_hex("#000000"),
            ambient=0.2,
            reflection=0.2,
        ),
    ),
    #ball 1
    Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#d900ff"))),
    #ball 2
    Sphere(Point(-0.75, -1.4, 3.25), 0.6, Material(Color.from_hex("#C0C0C0"))),
]
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
]