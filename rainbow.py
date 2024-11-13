#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORTATION)
#=================================================================================================================

from color import Color
from light import Light
from material import *
from point import Point
from sphere import Sphere
from vector import Vector
import random


# ==============================================================================
# PARTIE 2: DÉFINITION DES CONSTANTES ET FONCTIONS
# ==============================================================================

WIDTH = 920
HEIGHT = 620
CAMERA = Vector(0, -0.35, -1)

# Liste des objets de la scène
OBJECTS = [
    # Grand sol pour placer les petites balles
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#FFFFFF"),
            color2=Color.from_hex("#05d1f5"),
            ambient=0.2,
            reflection=0.2,
        ),
    ),
    # Grande balle blanche (réfléchissante)
    Sphere(Point(0, -0.4, 2), 1.0, Material(Color.from_hex("#FFFFFF"), reflection=0.5)),
]

# Génération de nombreuses petites balles autour de la grande balle, toutes sur le sol
NUM_SMALL_BALLS = 5  # Nombre de petites balles
RADIUS_SMALL_BALL = 0.2  # Taille des petites balles
SPACING_X = 1.5  # Distance maximale en x autour de la grande balle
SPACING_Z_FRONT = 0.5  # Distance maximale devant la grande balle

for _ in range(NUM_SMALL_BALLS):
    # Génère des positions aléatoires autour de la grande balle, mais devant la grande balle
    x = random.uniform(-SPACING_X, SPACING_X)
    z = random.uniform(0.5, 1.9)  # Limite Z pour que les balles soient devant la grande balle
    y = 0.0 # Place les petites balles sur le sol (ajusté pour être sur la surface)

    # Ajout d'une petite balle à la liste d'objets
    OBJECTS.append(
        Sphere(
            Point(x, y, z),
            RADIUS_SMALL_BALL,
            Material(
                Color(random.random(), random.random(), random.random()),  # Couleur aléatoire
                reflection=0.3  # Propriété réfléchissante
            )
        )
    )

# Liste des lumières
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
]
