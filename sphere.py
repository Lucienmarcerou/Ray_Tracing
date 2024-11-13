#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# Importation de la fonction sqrt (racine carrée) depuis la bibliothèque mathématique pour
# les calculs d'intersection de rayons avec des sphères.
from math import sqrt

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Sphere représente une sphère en 3D, qui est un des objets de base dans le ray tracing.
# Chaque sphère est définie par son centre, son rayon, et son matériau.

class Sphere:
    """La classe Sphere est la seule forme 3D implémentée dans ce projet. Elle possède un centre, un rayon et un matériau."""

    def __init__(self, center, radius, material):
        # Constructeur de la classe Sphere. Prend en entrée un vecteur center (qui définit la position de la sphère dans l'espace 3D),
        # un radius (rayon de la sphère) et un material (matériau de la sphère, utilisé pour définir son apparence lors du rendu).
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """Vérifie si un rayon donné intersecte la sphère. Retourne la distance à l'intersection ou None s'il n'y a pas d'intersection."""
        # Calcule le vecteur entre l'origine du rayon et le centre de la sphère.
        sphere_to_ray = ray.origin - self.center
        # Les coefficients pour l'équation quadratique: ici a = 1.
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        # Si le discriminant est supérieur ou égal à 0, cela signifie qu'il y a une intersection possible.
        if discriminant >= 0:
            # Calcul de la distance à l'intersection la plus proche (la plus petite racine positive).
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        # Si aucune intersection n'est trouvée, retourne None.
        return None

    def normal(self, surface_point):
        """Retourne la normale de la surface à un point donné sur la surface de la sphère."""
        # La normale est obtenue en soustrayant le centre de la sphère au point sur la surface et en normalisant le résultat.
        return (surface_point - self.center).normalize()
