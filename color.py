#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# Importation de la classe Vector à partir du module vector. Ici, la classe Color hérite des propriétés et méthodes de Vector.
from vector import Vector

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Color représente une couleur en utilisant des triplets RGB (Rouge, Vert, Bleu).
# Elle hérite de la classe Vector, car une couleur peut être vue comme un vecteur à trois dimensions.

class Color(Vector):
    """La classe Color stocke une couleur sous forme de triplets RGB. Il s'agit d'un alias pour la classe Vector."""

    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        # Cette méthode de classe permet de créer un objet Color à partir d'une chaîne hexadécimale.
        # L'argument hexcolor est une chaîne représentant une couleur au format hexadécimal, par défaut "#000000" (noir).
        x = int(hexcolor[1:3], 16) / 255.0  # Extraction et conversion de la composante rouge (R) de l'hexadécimal.
        y = int(hexcolor[3:5], 16) / 255.0  # Extraction et conversion de la composante verte (G) de l'hexadécimal.
        z = int(hexcolor[5:7], 16) / 255.0  # Extraction et conversion de la composante bleue (B) de l'hexadécimal.
        return cls(x, y, z)  # Retourne une instance de Color avec les valeurs RGB normalisées (entre 0 et 1).
