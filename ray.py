#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# (Pas d'importations supplémentaires nécessaires pour cette partie du code)

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Ray représente un rayon, un élément clé dans le ray tracing. Un rayon est défini par une origine et une direction normalisée.
# Les rayons sont utilisés pour interroger la scène et déterminer les intersections avec les objets 3D.

class Ray:
    """La classe Ray représente une demi-droite avec une origine et une direction normalisée."""

    def __init__(self, origin, direction):
        # Constructeur de la classe Ray. Prend en entrée un vecteur origine (origin), qui représente le point de départ du rayon,
        # et un vecteur direction (direction) qui est automatiquement normalisé pour garantir une longueur unitaire.
        self.origin = origin  # Point d'origine du rayon.
        self.direction = direction.normalize()  # Direction normalisée du rayon pour assurer la précision des calculs.
