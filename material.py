#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# Importation de la classe Color à partir du module color. Elle est utilisée pour gérer les couleurs des matériaux.
from color import Color

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Material représente un matériau avec des propriétés physiques qui définissent comment il réagit à la lumière,
# telles que la couleur, l'ambiance, la diffusion, la réflectivité et la brillance.

class Material:
    """La classe Material possède une couleur et des propriétés qui définissent comment il réagit à la lumière."""

    def __init__(
        self,
        color=Color.from_hex("#FFFFFF"),  # Couleur par défaut en blanc.
        ambient=0.05,  # Intensité de la lumière ambiante (faible par défaut).
        diffuse=1.0,  # Propriété de diffusion de la lumière (répartie sur toute la surface).
        specular=1.0,  # Propriété de brillance (réflexion spéculaire).
        reflection=0.5,  # Propriété de réflexion (mi-réfléchissant par défaut).
    ):
        # Initialisation des propriétés du matériau.
        self.color = color  # Couleur du matériau.
        self.ambient = ambient  # Composante de lumière ambiante.
        self.diffuse = diffuse  # Composante de diffusion de la lumière.
        self.specular = specular  # Brillance du matériau.
        self.reflection = reflection  # Réflexion du matériau.

    def color_at(self, position):
        # Retourne la couleur du matériau à une position donnée. Ici, la couleur est uniforme sur toute la surface.
        return self.color

# La classe ChequeredMaterial définit un matériau avec un motif en damier. Il est constitué de deux couleurs alternées
# en fonction de la position dans l'espace, ce qui crée un effet de grille.

class ChequeredMaterial:
    """La classe ChequeredMaterial représente un matériau avec un motif de damier basé sur deux couleurs."""

    def __init__(
        self,
        color1=Color.from_hex("#FFFFFF"),  # Première couleur du damier (blanc par défaut).
        color2=Color.from_hex("#000000"),  # Deuxième couleur du damier (noir par défaut).
        ambient=0.05,  # Intensité de la lumière ambiante.
        diffuse=1.0,  # Propriété de diffusion de la lumière.
        specular=1.0,  # Propriété de brillance.
        reflection=0.5,  # Propriété de réflexion.
    ):
        # Initialisation des propriétés du matériau en damier.
        self.color1 = color1  # Première couleur du damier.
        self.color2 = color2  # Deuxième couleur du damier.
        self.ambient = ambient  # Composante de lumière ambiante.
        self.diffuse = diffuse  # Composante de diffusion de la lumière.
        self.specular = specular  # Brillance du matériau.
        self.reflection = reflection  # Réflexion du matériau.

    def color_at(self, position):
        # Détermine la couleur à une position donnée en fonction du motif en damier.
        # Alternance des couleurs en fonction des coordonnées de la position dans l'espace.
        if int((position.x + 5.0) * 3.0) % 2 == int(position.z * 3.0) % 2:
            return self.color1  # Retourne la première couleur du damier.
        else:
            return self.color2  # Retourne la deuxième couleur du damier.
