# =================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET LIBRAIRIES EXTERNES (IMPORTATION)
# =================================================================================================================
# Moteur de ray tracing réalisé en Python

import importlib  # Module pour importer dynamiquement d'autres modules
import os  # Module pour les opérations sur le système de fichiers
from engine import RenderEngine  # Importation du moteur de rendu
from scene import Scene  # Importation de la classe qui définit la scène


# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

def main():
    """
    Fonction principale du programme :
    - Initialise la scène et le moteur de rendu.
    - Génère l'image et la sauvegarde dans un fichier PPM.
    """
    # Définition du chemin vers le module de la scène (sans extension .py)
    scene_module = "rainbow"

    # Chargement dynamique du module de scène
    mod = importlib.import_module(scene_module)

    # Configuration de la scène et du moteur de rendu
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)  # Génération de l'image par le moteur de rendu

    # Chemin du fichier où l'image sera sauvegardée (format PPM)
    output_file = "/Users/e/PycharmProjects/pythonProject/Projects/Ray tracing/output.ppm"

    # Change le répertoire courant pour correspondre à l'emplacement du fichier de scène
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))

    # Ouverture du fichier en mode écriture et sauvegarde de l'image
    with open(output_file, "w") as img_file:
        image.write_ppm(img_file)  # Écriture de l'image en format PPM dans le fichier


# ==============================================================================
# PARTIE 3: CORPS PRINCIPAL DU SCRIPT (MAIN)
# ==============================================================================

main()
