# ==============================================================================
# PARTIE 1: DÉFINITION DES FONCTIONS
# ==============================================================================

# La classe Image représente une image 2D avec une largeur et une hauteur, et elle permet de manipuler les pixels.
# Cette classe est utilisée pour créer et stocker l'image produite par le moteur de ray tracing.
# L'image est ensuite sauvegardée au format PPM (un format simple pour stocker des images en couleur).

class Image:
    def __init__(self, width, height):
        # Constructeur de la classe Image. Initialise une image de dimensions données (width, height),
        # et crée une matrice de pixels où chaque pixel est initialisé à None.
        self.width = width  # Largeur de l'image en pixels.
        self.height = height  # Hauteur de l'image en pixels.
        self.pixels = [[None for _ in range(width)] for _ in range(height)]  # Matrice de pixels.

    def set_pixel(self, x, y, col):
        # Définit la couleur d'un pixel à la position (x, y).
        # 'col' est un objet Color représentant la couleur à assigner au pixel.
        self.pixels[y][x] = col

    def write_ppm(self, img_file):
        # Sauvegarde l'image dans un fichier au format PPM.
        # 'img_file' est un objet fichier ouvert en mode écriture.

        def to_byte(c):
            # Convertit une composante de couleur (entre 0 et 1) en une valeur comprise entre 0 et 255.
            return round(max(min(c * 255, 255), 0))

        # Écriture de l'en-tête du fichier PPM, incluant le format P3, la largeur, la hauteur et la valeur maximale des couleurs (255).
        img_file.write("P3 {} {}\n255\n".format(self.width, self.height))

        # Écriture des couleurs des pixels ligne par ligne. Chaque couleur est représentée par ses composantes RGB (Rouge, Vert, Bleu).
        for row in self.pixels:
            for color in row:
                img_file.write(
                    "{} {} {} ".format(
                        to_byte(color.x), to_byte(color.y), to_byte(color.z)
                    )
                )
            img_file.write("\n")  # Saut de ligne après chaque rangée de pixels.
