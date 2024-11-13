#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# (Pas d'importations supplémentaires nécessaires pour cette partie du code)

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Scene contient toutes les informations nécessaires pour exécuter l'algorithme de ray tracing.
# Cela inclut la caméra, les objets à rendre, les sources de lumière, ainsi que les dimensions de l'image finale.

class Scene:
    """La classe Scene contient toutes les informations nécessaires pour le moteur de rendu par ray tracing."""

    def __init__(self, camera, objects, lights, width, height):
        # Constructeur de la scène. Prend en entrée une caméra (camera), une liste d'objets (objects),
        # une liste de sources lumineuses (lights), ainsi que la largeur (width) et la hauteur (height)
        # de l'image à produire.
        self.camera = camera  # Position et orientation de la caméra dans la scène.
        self.objects = objects  # Liste des objets présents dans la scène (comme des sphères, des plans, etc.).
        self.lights = lights  # Liste des sources de lumière qui éclairent la scène.
        self.width = width  # Largeur de l'image finale (en pixels).
        self.height = height  # Hauteur de l'image finale (en pixels).
