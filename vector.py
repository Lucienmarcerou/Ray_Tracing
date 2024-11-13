#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORT)
#=================================================================================================================
# Nous commençons par importer la bibliothèque mathématique standard de Python,
# qui sera utilisée pour certaines opérations mathématiques, comme la racine carrée.
import math


#=================================================================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
#=================================================================================================================

# La classe Vector définit un vecteur à trois dimensions, souvent utilisé dans les graphiques 3D
# et les simulations physiques pour représenter des points ou des directions dans l'espace 3D.

class Vector:
    """Un vecteur à trois dimensions"""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        # Constructeur de la classe, initialise un vecteur avec des coordonnées x, y et z.
        # Par défaut, le vecteur est initialisé avec les valeurs (0.0, 0.0, 0.0).
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        # Redéfinition de la méthode __str__ pour permettre l'affichage du vecteur
        # dans un format lisible sous la forme (x, y, z).
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def dot_product(self, other):
        # Méthode pour calculer le produit scalaire entre deux vecteurs.
        # Le produit scalaire est la somme des produits des composants correspondants.
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        # Méthode pour calculer la magnitude (ou longueur) du vecteur.
        # La magnitude est la racine carrée du produit scalaire du vecteur avec lui-même.
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        # Méthode pour normaliser le vecteur, c'est-à-dire pour obtenir un vecteur
        # de même direction mais de longueur unitaire (magnitude égale à 1).
        return self / self.magnitude()

    def __add__(self, other):
        # Redéfinition de l'opérateur d'addition pour ajouter deux vecteurs composante par composante.
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # Redéfinition de l'opérateur de soustraction pour soustraire deux vecteurs composante par composante.
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        # Redéfinition de l'opérateur de multiplication pour multiplier chaque composante du vecteur
        # par un scalaire (nombre). Notez qu'il n'est pas possible de multiplier deux vecteurs entre eux.
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        # Méthode spéciale permettant d'assurer que la multiplication soit commutative,
        # c'est-à-dire que le produit scalaire fonctionne dans les deux sens (scalaire * vecteur).
        return self.__mul__(other)

    def __truediv__(self, other):
        # Redéfinition de l'opérateur de division pour diviser chaque composante du vecteur
        # par un scalaire. La division de deux vecteurs n'est pas autorisée.
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)
