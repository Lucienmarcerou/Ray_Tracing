#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# Importation de la classe Vector à partir du module vector. Cette classe est utilisée pour représenter
# des points ou des directions dans l'espace 3D.
from vector import Vector

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Point est un alias de la classe Vector. Elle représente des points dans un espace 3D,
# en utilisant les mêmes attributs et méthodes que la classe Vector.

class Point(Vector):
    """La classe Point stocke les coordonnées 3D. Il s'agit d'un alias pour la classe Vector."""

    # Aucun changement n'est apporté aux fonctionnalités de la classe Vector.
    # Point hérite de toutes les méthodes et attributs de Vector.
    pass
