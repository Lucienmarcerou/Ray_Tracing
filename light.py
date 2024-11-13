#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# Importation de la classe Color à partir du module color. Elle est utilisée pour définir la couleur de la source lumineuse.
from color import Color

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Light représente une source de lumière ponctuelle dans la scène, ayant une position et une couleur.
# Les sources lumineuses sont essentielles pour éclairer les objets et calculer les ombres, reflets, etc.

class Light:
    """La classe Light représente une source de lumière ponctuelle d'une certaine couleur."""

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        # Constructeur de la classe Light. Prend en entrée un vecteur position, qui définit la position de la lumière
        # dans l'espace 3D, et une couleur, par défaut blanche.
        self.position = position  # Position de la source de lumière dans la scène.
        self.color = color  # Couleur de la lumière (blanche par défaut).
