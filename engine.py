#=================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORTATION)
#=================================================================================================================

from color import Color  # Importation de la classe Color pour gérer les couleurs
from image import Image  # Importation de la classe Image pour gérer la création d'images
from point import Point  # Importation de la classe Point pour représenter les points 3D
from ray import Ray  # Importation de la classe Ray pour représenter les rayons utilisés dans le ray tracing

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

class RenderEngine:
    """Moteur de rendu pour convertir des objets 3D en images 2D en utilisant le ray tracing"""

    MAX_DEPTH = 5  # Profondeur maximale de récursion pour le ray tracing
    MIN_DISPLACE = 0.0001  # Déplacement minimum pour éviter les artefacts de calculs

    def render(self, scene):
        """Rend la scène en utilisant le ray tracing et retourne une image 2D"""
        width = scene.width  # Largeur de la scène
        height = scene.height  # Hauteur de la scène
        aspect_ratio = float(width) / height  # Calcul du rapport d'aspect (largeur/hauteur)
        x0 = -1.0  # Coordonnée X initiale de la caméra
        x1 = +1.0  # Coordonnée X finale de la caméra
        xstep = (x1 - x0) / (width - 1)  # Incrément en X par pixel
        y0 = -1.0 / aspect_ratio  # Coordonnée Y initiale ajustée par le rapport d'aspect
        y1 = +1.0 / aspect_ratio  # Coordonnée Y finale ajustée par le rapport d'aspect
        ystep = (y1 - y0) / (height - 1)  # Incrément en Y par pixel

        camera = scene.camera  # Position de la caméra dans la scène
        pixels = Image(width, height)  # Création d'une image vide avec la largeur et la hauteur données

        # Parcours de chaque pixel de l'image
        for j in range(height):
            y = y0 + j * ystep  # Calcul de la coordonnée Y du pixel
            for i in range(width):
                x = x0 + i * xstep  # Calcul de la coordonnée X du pixel
                ray = Ray(camera, Point(x, y) - camera)  # Création d'un rayon partant de la caméra vers le point (x, y)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))  # Calcul de la couleur du pixel à la position (i, j)
            print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")  # Affichage de la progression en pourcentage
        return pixels  # Retourne l'image finale

    def ray_trace(self, ray, scene, depth=0):
        """Trace un rayon et calcule la couleur en fonction des objets rencontrés dans la scène"""
        color = Color(0, 0, 0)  # Couleur de base (noir)
        # Recherche de l'objet le plus proche touché par le rayon
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color  # Si aucun objet n'est touché, retourne la couleur de fond (noir)
        hit_pos = ray.origin + ray.direction * dist_hit  # Position de l'impact sur l'objet
        hit_normal = obj_hit.normal(hit_pos)  # Normale de l'objet au point d'impact
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)  # Ajoute la couleur de l'objet au point d'impact
        if depth < self.MAX_DEPTH:
            new_ray_pos = hit_pos + hit_normal * self.MIN_DISPLACE  # Nouveau point de départ du rayon réfléchi
            new_ray_dir = ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal  # Calcul de la direction du rayon réfléchi
            new_ray = Ray(new_ray_pos, new_ray_dir)  # Création du rayon réfléchi
            # Atténuation du rayon réfléchi en fonction du coefficient de réflexion de l'objet
            color += self.ray_trace(new_ray, scene, depth + 1) * obj_hit.material.reflection
        return color  # Retourne la couleur calculée

    def find_nearest(self, ray, scene):
        """Trouve l'objet le plus proche touché par le rayon"""
        dist_min = None  # Distance minimale de l'impact
        obj_hit = None  # Objet touché le plus proche
        for obj in scene.objects:  # Parcours de tous les objets de la scène
            dist = obj.intersects(ray)  # Calcul de la distance d'intersection avec le rayon
            if dist is not None and (obj_hit is None or dist < dist_min):  # Vérification de l'objet le plus proche
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)  # Retourne la distance minimale et l'objet touché

    def color_at(self, obj_hit, hit_pos, normal, scene):
        """Calcule la couleur de l'objet à la position d'impact"""
        material = obj_hit.material  # Matériau de l'objet touché
        obj_color = material.color_at(hit_pos)  # Couleur de l'objet au point d'impact
        to_cam = scene.camera - hit_pos  # Direction vers la caméra
        specular_k = 50  # Coefficient de spécularité
        color = material.ambient * Color.from_hex("#000000")  # Calcul de la composante ambiante (couleur d'ombre)

        # Calcul de l'éclairage
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)  # Rayon vers la source de lumière
            # Éclairage diffus (modèle Lambert)
            color += obj_color * material.diffuse * max(normal.dot_product(to_light.direction), 0)
            # Éclairage spéculaire (modèle Blinn-Phong)
            half_vector = (to_light.direction + to_cam).normalize()  # Vecteur demi-angle entre la lumière et la caméra
            color += light.color * material.specular * max(normal.dot_product(half_vector), 0) ** specular_k
        return color  # Retourne la couleur finale calculée
