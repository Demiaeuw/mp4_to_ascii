from PIL import Image
import os
import time

# Paramètres
WIDTH = 100
ASCII_CHARS = "@%#*+=-:. "
OUTPUT_DIR = "frames_ascii"

def resize_image(image, new_width=WIDTH):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel//32] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path):
    image = Image.open(image_path)
    image = resize_image(image)
    image = grayscale_image(image)
    ascii_str = pixel_to_ascii(image)
    
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i+img_width] for i in range(0, ascii_str_len, img_width)])
    
    return ascii_img

# Créer le dossier frames_ascii s'il n'existe pas
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Boucle pour traiter toutes les images
for i in range(1, 270):  # Boucle de 1 à 269 inclus
    image_filename = f"frames/frame_{i:04d}.png"  # Génère des noms comme frame_0001.png, frame_0002.png, ...
    if os.path.exists(image_filename):  # Vérifie que le fichier existe
        ascii_art = image_to_ascii(image_filename)
        
        # Sauvegarde de l'art ASCII dans un fichier texte
        output_filename = f"{OUTPUT_DIR}/ascii_frame_{i:04d}.txt"
        with open(output_filename, "w") as f:
            f.write(ascii_art)
        
        # Affiche l'art ASCII dans le terminal
        os.system("clear")  # Efface le terminal
        print(ascii_art)
        time.sleep(0.04)  # Pause entre les frames pour simuler l'animation
    else:
        print(f"Fichier {image_filename} non trouvé.")

